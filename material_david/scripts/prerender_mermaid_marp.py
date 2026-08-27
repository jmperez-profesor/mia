#!/usr/bin/env python3
"""Pre-renderiza los bloques mermaid de un guion Marp a PNG y devuelve una copia lista para marp.

Marp no renderiza mermaid: los bloques ```mermaid llegan a la diapositiva como texto plano. Se
resuelve igual que en el libro PDF (ver hooks.py): se rasteriza cada diagrama con mmdc y se
sustituye el bloque por la imagen. El guion original NO se toca -sigue siendo la fuente de verdad
con el codigo mermaid editable-; la sustitucion ocurre en una copia temporal que es la que consume
marp, escrita en el mismo directorio para que las rutas relativas (../assets, img/) sigan validas.

Uso:  prerender_mermaid_marp.py <guion.md>
Imprime en stdout la ruta de la copia procesada (o la del original si no hay mermaid).
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

# Caja util de una diapositiva 16:9 de marp (1280x720) dejando margen para titulo y pie.
MAX_ANCHO = 1000
MAX_ALTO = 330

BLOQUE_MERMAID = re.compile(r'^```mermaid[^\n]*\n(.*?)^```[ \t]*$', re.DOTALL | re.MULTILINE)


def chrome_path() -> str | None:
    from os import environ
    if environ.get('CHROME_PATH'):
        return environ['CHROME_PATH']
    for c in Path.home().glob('.cache/ms-playwright/chromium-*/chrome-linux64/chrome'):
        return str(c)
    return None


def render(codigo: str, destino: Path) -> bool:
    if destino.exists():
        return True
    with tempfile.TemporaryDirectory() as tmp:
        mmd = Path(tmp) / 'd.mmd'
        mmd.write_text(codigo, encoding='utf-8')
        args = ['npx', '--yes', '@mermaid-js/mermaid-cli@latest',
                '-i', str(mmd), '-o', str(destino), '-b', 'transparent', '-s', '2']
        chrome = chrome_path()
        if chrome:
            cfg = Path(tmp) / 'p.json'
            cfg.write_text(json.dumps({
                'executablePath': chrome,
                'args': ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
            }), encoding='utf-8')
            args += ['-p', str(cfg)]
        r = subprocess.run(args, capture_output=True, text=True, timeout=180)
        if r.returncode != 0 or not destino.exists():
            print(f'  [mermaid] fallo al renderizar: {r.stderr.strip()[:300]}', file=sys.stderr)
            return False
    return True


def altura(png: Path) -> int:
    with Image.open(png) as img:
        w, h = img.size
    return max(1, min(MAX_ALTO, round(MAX_ANCHO * h / w)))


def main() -> int:
    guion = Path(sys.argv[1]).resolve()
    texto = guion.read_text(encoding='utf-8')
    if '```mermaid' not in texto:
        print(guion)
        return 0

    img_dir = guion.parent / 'img'
    img_dir.mkdir(parents=True, exist_ok=True)
    fallos = 0

    def sustituir(m: re.Match) -> str:
        nonlocal fallos
        codigo = m.group(1)
        clave = hashlib.sha256(codigo.encode('utf-8')).hexdigest()[:12]
        png = img_dir / f'mermaid-{clave}.png'
        if not render(codigo, png):
            fallos += 1
            return m.group(0)
        return f'![center h:{altura(png)}](img/{png.name})'

    procesado, n = BLOQUE_MERMAID.subn(sustituir, texto)
    hechos = n - fallos
    print(f'  [mermaid] {hechos}/{n} diagrama(s) rasterizado(s)', file=sys.stderr)
    if fallos:
        print(f'  [mermaid] {fallos} sin renderizar, se quedan como texto', file=sys.stderr)

    salida = guion.with_name(f'.{guion.stem}.marp.md')
    salida.write_text(procesado, encoding='utf-8')
    print(salida)
    return 0


if __name__ == '__main__':
    sys.exit(main())
