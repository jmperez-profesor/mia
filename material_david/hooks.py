import gzip
import hashlib
import io
import logging
import os
import posixpath
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
from PIL import Image

PRERENDER = os.environ.get('PRERENDER_MERMAID', '0') == '1'
PUPPETEER_CONFIG = Path(__file__).parent / 'puppeteer-config.json'


class _SkipWithPdfDisabledWarning(logging.Filter):
    # with-pdf solo genera PDF si PRERENDER_MERMAID=1 (enabled_if_env en mkdocs.yml):
    # el build web (sin la variable) avisa de que no genera PDF, y --strict lo convertiría
    # en fallo aunque sea el comportamiento esperado.
    def filter(self, record):
        return 'without generate PDF' not in record.getMessage()


logging.getLogger('mkdocs.with-pdf').addFilter(_SkipWithPdfDisabledWarning())

_cache = {}

_current_page = ''
_site_dir = ''


def _mermaid_asset_dir() -> Path:
    d = Path(_site_dir) / 'assets' / 'mermaid'
    d.mkdir(parents=True, exist_ok=True)
    return d


def _relative_asset_path(page_url: str, filename: str) -> str:
    """Path to the shared mermaid asset dir, relative to the current page."""
    page_dir = posixpath.dirname(page_url)
    target = posixpath.join('assets', 'mermaid', filename)
    if not page_dir:
        return target
    return posixpath.relpath(target, start=page_dir)


def _mmdc_render(code: str, mmd_path: str, png_path: str) -> bool:
    args = [
        'mmdc', '-i', mmd_path, '-o', png_path,
        '-b', 'transparent', '-s', '1',
    ]
    if PUPPETEER_CONFIG.exists():
        args.extend(['-p', str(PUPPETEER_CONFIG)])
    result = subprocess.run(args, capture_output=True, text=True, timeout=30)
    return result.returncode == 0


_PNG_MAGIC = b'\x89PNG\r\n\x1a\n'
_PNG_MAX_DIMENSION = 2000  # px; una imagen mas alta o ancha que esto rompe la paginacion en el PDF


def _valid_png(data: bytes) -> bool:
    """Descarta PNG corruptos, vacios o desproporcionados antes de insertarlos en el HTML.

    Anadido el 2026-08-24 como defensa general: "returncode == 0" de mmdc no garantiza "imagen
    valida", asi que si el PNG esta corrupto, vacio o tiene un tamano fuera de lo razonable para
    un diagrama, se descarta aqui y el diagrama cae al texto plano de respaldo (siempre seguro).

    OJO: esto NO es el arreglo del corte de docs/Libro.pdf en produccion (sigue sin explicar,
    ver HISTORIAL.md 2026-08-24). Esta funcion solo protegeria contra un PNG de mmdc realmente
    corrupto o desproporcionado; los PNG que genera mmdc en la CI son validos, asi que este
    filtro no rechaza nada en la practica y no cambia el resultado del PDF truncado.
    """
    if len(data) < 100 or not data.startswith(_PNG_MAGIC):
        return False
    if len(data) < 33:
        return False
    width = int.from_bytes(data[16:20], 'big')
    height = int.from_bytes(data[20:24], 'big')
    if width <= 0 or height <= 0:
        return False
    if width > _PNG_MAX_DIMENSION or height > _PNG_MAX_DIMENSION:
        return False
    return True


_TALL_HEIGHT_LIMIT = 900  # px; por encima de esto, un diagrama mermaid vertical rompe el PDF


def _shrink_if_tall(data: bytes) -> bytes:
    """Reduce diagramas mermaid excesivamente altos y estrechos antes de insertarlos en el PDF.

    Hallazgo 2026-08-24, contrastado con el mismo problema en el repositorio hermano
    1DAMProgramacion: WeasyPrint 62.3 tiene un fallo de paginacion, sin excepcion ni aviso en el
    log, que se dispara al maquetar una imagen concreta con dimensiones nativas grandes y de
    aspecto muy vertical (alto/ancho alto) -confirmado alli con un diagrama de 486x1114 px al subir
    la escala de mmdc de -s 1 a -s 2-, y trunca el resto del documento sin dejar rastro. El
    diagrama `flowchart TD` con mas nodos encadenados de este sitio genera 567x1495 px incluso a
    escala 1 (la escala minima), justo en la unidad donde el PDF de producción se corta. El
    `style="max-height"` en CSS no evita el fallo porque este ocurre al decodificar/maquetar el
    PNG por sus dimensiones nativas, antes de que WeasyPrint aplique ningun estilo. Se reescala
    aqui con Pillow a una altura maxima segura, conservando el aspecto; con eso basta para que el
    PNG que llega a WeasyPrint tenga las dimensiones de cualquier otro diagrama del sitio que ya
    se sabe que renderiza bien.
    """
    with Image.open(io.BytesIO(data)) as img:
        width, height = img.size
        if height <= _TALL_HEIGHT_LIMIT:
            return data
        scale = _TALL_HEIGHT_LIMIT / height
        new_size = (max(1, round(width * scale)), _TALL_HEIGHT_LIMIT)
        resized = img.resize(new_size, Image.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format='PNG')
        return buf.getvalue()


def _quote_labels(code: str) -> str:
    """Wrap unquoted labels in quotes to handle special characters."""
    def _wrap(m):
        inner = m.group(1)
        if inner.startswith('"') and inner.endswith('"'):
            return m.group(0)
        esc = inner.replace('\\', '\\\\').replace('"', '\\"')
        return f'["{esc}"]'
    return re.sub(r'\[([^\[\]]*)\]', _wrap, code)


def _render_mermaid_png(code: str, index: int) -> str | None:
    key = hashlib.sha256(code.encode()).hexdigest()
    if key in _cache:
        return _cache[key]

    result_png = b''

    def _attempt(mmd_text: str) -> bool:
        nonlocal result_png
        with tempfile.NamedTemporaryFile(suffix='.mmd', delete=False, mode='w') as f_in:
            f_in.write(mmd_text)
            mmd_path = f_in.name
        png_path = mmd_path.replace('.mmd', '.png')
        ok = _mmdc_render(mmd_text, mmd_path, png_path)
        if ok:
            data = Path(png_path).read_bytes()
            ok = _valid_png(data)
            if ok:
                result_png = _shrink_if_tall(data)
        for p in [mmd_path, png_path]:
            Path(p).unlink(missing_ok=True)
        return ok

    strategies = [
        ('original', code),
        ('quoted labels', _quote_labels(code)),
    ]

    for name, text in strategies:
        try:
            if _attempt(text):
                filename = f'{key}.png'
                out_path = _mermaid_asset_dir() / filename
                if not out_path.exists():
                    out_path.write_bytes(result_png)
                rel_path = _relative_asset_path(_current_page, filename)
                _cache[key] = rel_path
                return rel_path
        except Exception as e:
            print(f'  [hooks] mmdc {name} exception ({_current_page}, idx {index}): {e}')

    print(f'  [hooks] mmdc all strategies failed ({_current_page}, idx {index})')
    _cache[key] = None
    return None


MERMAID_RE = re.compile(
    r'<pre class="mermaid"[^>]*><code[^>]*>(.*?)</code></pre>',
    re.DOTALL,
)

# Hallazgo 2026-08-24, aislado por biseccion exhaustiva contra la CI real (no reproducible en
# local): una admonicion `!!!` justo despues de una tabla, sin ningun elemento de bloque entre
# medias, corrompe la paginacion de WeasyPrint 62.3 en el runner de GitHub Actions -sin excepcion
# ni aviso en ningun log-, y trunca en seco el resto del PDF combinado a partir de ahi. Confirmado
# en aislamiento total: cambiar el texto de la admonicion no lo arregla; un simple margen CSS
# tampoco; intercalar un parrafo real de contenido si. El patron aparece en ~70 paginas del sitio
# (tabla seguida de un aviso sobre ella es una forma de escribir muy natural), asi que en vez de
# reescribir el contenido en cada sitio se inserta aqui, por hook, un parrafo separador real
# entre cualquier `</table>` y la admonicion que la siga inmediatamente.
TABLE_ADMONITION_RE = re.compile(r'(</table>)\s*(<div class="admonition)')
TABLE_ADMONITION_SPACER = '<p class="pdf-spacer">Nota sobre la tabla anterior.</p>'

# Hallazgo 2026-08-25: mkdocs-with-pdf convierte CUALQUIER href relativo en un ancla interna del
# PDF combinado (`get_combined` en su preprocessor: site-packages/mkdocs_with_pdf/preprocessor/
# __init__.py), sin comprobar si el destino es una pagina excluida por `exclude_pages` (notebooks/,
# Presentacion/...) ni si es directamente un fichero que no genera pagina (.ipynb, .zip, .mp4,
# .wav servidos como asset estatico, enlazados desde el propio Markdown). Cuando esa pagina o esa
# ancla no existen, WeasyPrint avisa "No anchor ... for internal URI reference" en cada build -no
# rompe el PDF, pero ensucia el log y deja el enlace muerto dentro del libro-. `get_combined` solo
# se salta los href que ya sean absolutos, así que aquí se convierten a absolutos esos enlaces
# antes de que el plugin los procese: los trata entonces como externos (los deja intactos) y en
# el PDF quedan clicables hacia la web en vez de ser un ancla muerta.
ANCHOR_HREF_RE = re.compile(r'(<a\s[^>]*\bhref=")(?!\w+:|#)([^"#]+)(")')


def _pdf_exclude_patterns(config):
    """Los mismos patrones que usa mkdocs-with-pdf (Generator.__init__) para decidir que
    paginas quedan fuera del PDF combinado, leidos de su propia config en vez de duplicar la
    lista de mkdocs.yml aqui."""
    plugin = config.get('plugins', {}).get('with-pdf')
    if plugin is None:
        return []
    raw = (getattr(plugin, 'config', None) or {}).get('exclude_pages') or []
    return [re.compile(p if p.startswith('^') else f'^{p}') for p in raw]


def _fix_dead_pdf_links(html: str, page_url: str, site_url: str, exclude_patterns) -> tuple[str, int]:
    if not site_url or '<a ' not in html:
        return html, 0

    base = site_url.rstrip('/')
    count = 0

    def _replace(m):
        nonlocal count
        href = m.group(2)
        abs_path = posixpath.normpath(posixpath.join(posixpath.dirname(page_url), href))
        es_asset = not abs_path.endswith('.html')
        es_pagina_excluida = any(p.match(abs_path) for p in exclude_patterns)
        if not (es_asset or es_pagina_excluida):
            return m.group(0)
        count += 1
        return f'{m.group(1)}{base}/{abs_path.lstrip("/")}{m.group(3)}'

    result = ANCHOR_HREF_RE.sub(_replace, html)
    return result, count


def _absolutize_notebook_links(html: str, page_url: str, site_url: str) -> tuple[str, int]:
    if '/notebooks/' not in html or not site_url:
        return html, 0

    base = site_url.rstrip('/')
    count = 0

    def _replace(m):
        nonlocal count
        href = m.group(2)
        abs_path = posixpath.normpath(posixpath.join(posixpath.dirname(page_url), href))
        count += 1
        return f'{m.group(1)}{base}/{abs_path.lstrip("/")}{m.group(3)}'

    result = NOTEBOOK_HREF_RE.sub(_replace, html)
    return result, count


def _fix_tabbed_for_print(html: str) -> tuple[str, int]:
    """Reconstruye las pestañas (`=== "..."`) como bloques lineales para impresion.

    pymdownx.tabbed genera todas las <label> juntas dentro de .tabbed-labels y, aparte,
    todos los .tabbed-block juntos dentro de un unico .tabbed-content -el emparejamiento
    label<->contenido lo hace en pantalla la seleccion CSS `:checked ~ .tabbed-content`,
    no el orden del DOM. Forzar `display:block` (como se hacia antes) linealiza el DOM tal
    cual: todas las etiquetas primero, todo el contenido despues, sin relacion visible entre
    ambos en el PDF. Aqui se reconstruye, solo para impresion, una copia con cada etiqueta
    seguida de su bloque, insertada como hermana del `.tabbed-set` original.

    El `.tabbed-set` original se deja tal cual (forzado a `display:block`, igual que antes)
    y solo se oculta su `.tabbed-labels` (docs/css/extra.css), ya redundante porque cada
    etiqueta se repite como cabecera en la copia. Probado y descartado: ocultar por completo
    el `.tabbed-set` original con `display:none` -en vez de solo su `.tabbed-labels`- corrompe
    de nuevo la paginacion de WeasyPrint en todo el libro a partir de ahi (mismo sintoma que
    TABLE_ADMONITION_RE mas arriba, sin excepcion ni aviso), aun reproducible en local. La
    reconstruccion del DOM en si (mover los `.tabbed-block` a la copia) no es la causa -aislado
    por bisección: con el `.tabbed-set` visible y forzado a bloque, la copia convive sin
    problema-; el disparador es concretamente el `display:none` sobre un contenedor cuyo
    `.tabbed-content` interno lleva `display:contents` en el CSS de Material, aunque ese
    descendiente nunca deberia pintarse al estar oculto el antecesor.
    """
    if 'tabbed-set' not in html:
        return html, 0

    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    for tabbed_set in soup.find_all('div', class_='tabbed-set'):
        labels_div = tabbed_set.find('div', class_='tabbed-labels', recursive=False)
        content_div = tabbed_set.find('div', class_='tabbed-content', recursive=False)
        if not labels_div or not content_div:
            continue
        labels = labels_div.find_all('label', recursive=False)
        blocks = content_div.find_all('div', class_='tabbed-block', recursive=False)
        if not labels or len(labels) != len(blocks):
            continue

        print_div = soup.new_tag('div')
        print_div['class'] = ['tabbed-print']
        for label, block in zip(labels, blocks):
            heading = soup.new_tag('p')
            heading['class'] = ['tabbed-print-label']
            strong = soup.new_tag('strong')
            strong.string = label.get_text()
            heading.append(strong)
            print_div.append(heading)
            print_div.append(block.extract())

        tabbed_set.insert_after(print_div)
        count += 1

    return str(soup), count


def on_page_markdown(markdown, page, config, files):
    site_url = config.get('site_url', '').rstrip('/')
    return markdown.replace('{{ site_url }}', site_url)


def on_page_content(html, page, config, files):
    exclude_patterns = _pdf_exclude_patterns(config)
    result, n_dead_links = _fix_dead_pdf_links(
        html, page.url, config.get('site_url', ''), exclude_patterns)
    if n_dead_links > 0:
        print(f'  [hooks] {n_dead_links} enlace(s) a paginas/assets fuera del PDF '
              f'convertido(s) a absoluto en {page.url} (evita anclas muertas de with-pdf)')

    if not PRERENDER:
        return result

    _cache.clear()
    rendered = [0]
    global _current_page, _site_dir
    _current_page = page.url
    _site_dir = config['site_dir']

    def _replace(match):
        code = match.group(1)
        code = code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        code = code.replace('&quot;', '"').replace('&#39;', "'")

        rel_path = _render_mermaid_png(code, rendered[0])
        rendered[0] += 1

        if rel_path:
            return f'<p><img class="mermaid-rendered" src="{rel_path}" alt="Mermaid diagram" style="max-width:70%;height:auto;max-height:350px;" /></p>'
        return match.group(0)

    result = MERMAID_RE.sub(_replace, result)

    if rendered[0] > 0:
        print(f'  [hooks] Pre-rendered {rendered[0]} Mermaid diagram(s) on {page.url}')

    result, n_spacers = TABLE_ADMONITION_RE.subn(
        lambda m: m.group(1) + TABLE_ADMONITION_SPACER + m.group(2), result)
    if n_spacers > 0:
        print(f'  [hooks] Inserted {n_spacers} table->admonition spacer(s) on {page.url}')

    result, n_tabbed = _fix_tabbed_for_print(result)
    if n_tabbed > 0:
        print(f'  [hooks] Rebuilt {n_tabbed} tabbed-set(s) for print on {page.url}')

    return result


SITEMAP_NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


def _git_last_commit_date(path: Path) -> str | None:
    """Fecha (YYYY-MM-DD) del último commit que tocó `path`, o None si no está en git."""
    try:
        out = subprocess.run(
            ['git', 'log', '-1', '--format=%cd', '--date=short', '--', path.name],
            cwd=path.parent, capture_output=True, text=True, timeout=5,
        )
    except Exception:
        return None
    date = out.stdout.strip()
    return date or None


def _source_for_sitemap_url(loc: str, docs_dir: Path, base_path: str) -> Path | None:
    """De una <loc> del sitemap, encuentra el .md o .ipynb de docs/ que la genera."""
    rel = urlsplit(loc).path.lstrip('/')
    if base_path and rel.startswith(base_path + '/'):
        rel = rel[len(base_path) + 1:]
    if rel.endswith('.html'):
        rel = rel[:-len('.html')]
    if not rel:
        return None
    for suffix in ('.md', '.ipynb'):
        candidate = docs_dir / f'{rel}{suffix}'
        if candidate.exists():
            return candidate
    return None


def _relative_pdf_path(dest_path: str) -> str:
    start_dir = posixpath.split(dest_path)[0]
    return posixpath.join(posixpath.relpath('docs', start_dir), 'Libro.pdf')


_PDF_ICON_SVG = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2'
    'm-9.5 8.5c0 .8-.7 1.5-1.5 1.5H7v2H5.5V9H8c.8 0 1.5.7 1.5 1.5zm5 2c0 .8-.7 1.5-1.5 1.5'
    'h-2.5V9H13c.8 0 1.5.7 1.5 1.5zm4-3H17v1h1.5V13H17v2h-1.5V9h3zm-6.5 0h1v3h-1zm-5 0h1v1H7z"/>'
    '</svg>'
)


def on_post_page(output, page, config):
    """Añade el icono de descarga del PDF en la cabecera, a la derecha de la lupa.

    with-pdf solo corre con PRERENDER_MERMAID=1 (enabled_if_env en mkdocs.yml, ver
    _fix_dead_pdf_links): el build web normal ya no lo activa, así que perdía también
    su único efecto útil sobre el sitio, el acceso al PDF completo desde cada página.
    Se añade como un `.md-header__button` más, junto a los que ya pone el propio tema
    Material (paleta, búsqueda, repositorio). Se inserta al final de la cabecera, tras
    el enlace al repositorio (`.md-header__source`, oculto en móvil por CSS): así en
    escritorio queda a la derecha de GitHub y en móvil, donde ese enlace no ocupa
    espacio, queda pegado a la derecha de la lupa.
    """
    if PRERENDER:
        return output
    soup = BeautifulSoup(output, 'html.parser')
    header = soup.select_one('.md-header__inner')
    if not header:
        return output
    a = soup.new_tag('a', href=_relative_pdf_path(page.file.dest_path), title='Descargar el PDF del libro completo',
                      **{'class': 'md-header__button md-icon'})
    a.append(BeautifulSoup(_PDF_ICON_SVG, 'html.parser'))
    source = header.select_one('.md-header__source')
    if source:
        source.insert_after(a)
    else:
        header.append(a)
    return str(soup)


def on_post_build(config):
    """Reescribe <lastmod> del sitemap con la fecha real de git de cada fichero.

    MkDocs pone la misma fecha de build en todas las URLs del sitemap; con eso Google
    no puede distinguir una página que cambió hoy de una que no se toca hace meses.
    """
    site_dir = Path(config['site_dir'])
    docs_dir = Path(config['docs_dir'])
    sitemap_path = site_dir / 'sitemap.xml'
    if not sitemap_path.exists():
        return

    base_path = urlsplit(config.get('site_url', '')).path.strip('/')

    ET.register_namespace('', SITEMAP_NS.strip('{}'))
    try:
        tree = ET.parse(sitemap_path)
    except ET.ParseError as e:
        print(f'  [hooks] sitemap.xml: no se pudo parsear ({e}), lastmod sin tocar')
        return

    root = tree.getroot()
    updated = 0
    for url_el in root.findall(f'{SITEMAP_NS}url'):
        loc_el = url_el.find(f'{SITEMAP_NS}loc')
        lastmod_el = url_el.find(f'{SITEMAP_NS}lastmod')
        if loc_el is None or lastmod_el is None or not loc_el.text:
            continue

        source = _source_for_sitemap_url(loc_el.text, docs_dir, base_path)
        if source is None:
            continue  # página generada sin fichero fuente propio (p. ej. una plantilla)

        date = _git_last_commit_date(source)
        if date:
            lastmod_el.text = date
            updated += 1

    if not updated:
        return

    tree.write(sitemap_path, encoding='UTF-8', xml_declaration=True)

    gz_path = site_dir / 'sitemap.xml.gz'
    with open(sitemap_path, 'rb') as f:
        content = f.read()
    with gzip.GzipFile(gz_path, 'wb', mtime=0) as gz:
        gz.write(content)

    print(f'  [hooks] sitemap.xml: lastmod real de git aplicado en {updated} URLs')
