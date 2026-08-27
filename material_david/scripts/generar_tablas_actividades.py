#!/usr/bin/env python3
"""Genera el cuerpo de las paginas de Practica y Entregas de cada unidad.

    python3 scripts/generar_tablas_actividades.py            # escribe
    python3 scripts/generar_tablas_actividades.py --check    # solo avisa si estan desfasadas

Rellena los bloques  <!-- AUTO:notebooks inicio --> ... <!-- AUTO:notebooks fin -->  con:

  1. la admonicion de cabecera, con la misma forma en las trece paginas;
  2. una tabla de cuatro columnas: la actividad, que es, la descarga y el badge de Colab;
  3. un apartado por actividad con su resumen, sus materiales de apoyo y que se entrega.

Cubre TODAS las actividades, no solo los notebooks: los talleres y los debates son paginas y
tambien se entregan. Para ellos no hay `.ipynb` que descargar ni Colab que abrir.

Por que existe: este cuerpo se escribio a mano varias veces y se desalineo todas (codigos viejos,
actividades sin badge, apartados que faltaban o estaban en la pagina del regimen equivocado,
encabezados absorbidos por la tabla de arriba). De donde sale cada cosa:

  - `mkdocs.yml` decide QUE actividades hay en cada grupo y EN QUE ORDEN.
  - El titulo H1 del propio notebook o de la propia pagina da su nombre.
  - `datos/actividades.yml` guarda solo lo que no se puede deducir del fichero: la columna «que es»,
    el resumen, que se entrega y los materiales de apoyo.
"""
import json
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
RAW = "https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs"
COLAB = "https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs"
INICIO, FIN = "<!-- AUTO:notebooks inicio -->", "<!-- AUTO:notebooks fin -->"
CODIGO = re.compile(r"UD0\d_([NTD]\d+)_")


def _titulo_de(texto: str, defecto: str) -> str:
    for linea in texto.split("\n"):
        if linea.startswith("# "):
            return linea.split("—")[-1].strip() if "—" in linea else linea[2:].strip()
    return defecto


def titulo(ruta: Path) -> str:
    """Nombre de la actividad, del H1 de su notebook o de su pagina."""
    if ruta.suffix == ".ipynb":
        nb = json.loads(ruta.read_text(encoding="utf-8"))
        md = "\n\n".join("".join(c.get("source", ""))
                         for c in nb.get("cells", []) if c.get("cell_type") == "markdown")
        return _titulo_de(md, ruta.stem)
    return _titulo_de(ruta.read_text(encoding="utf-8"), ruta.stem)


def actividades_del_nav() -> dict[tuple[str, str], list[str]]:
    """Por (unidad, grupo), la lista ORDENADA de ficheros que el nav coloca ahi."""
    texto = (RAIZ / "mkdocs.yml").read_text(encoding="utf-8")
    resto = texto[texto.index("\nnav:") + 1:].split("\n")
    nav = [resto[0]]
    for linea in resto[1:]:
        if linea and not linea.startswith(" "):
            break
        nav.append(linea)

    fuera: dict[tuple[str, str], list[str]] = {}
    grupo = None
    for linea in nav:
        m = re.match(r"^    - (Práctica|Practica|Entregas):", linea)
        if m:
            grupo = "entregas" if m.group(1) == "Entregas" else "practica"
            continue
        if re.match(r"^    - \w", linea):
            grupo = None
            continue
        if grupo is None:
            continue
        m = re.search(r"(UD0\d)/(?:notebooks/)?(\S+\.(?:ipynb|md))\s*$", linea)
        if m and CODIGO.match(m.group(2)):
            fuera.setdefault((m.group(1), grupo), []).append(m.group(2))
    return fuera


def practica_de(ud: str, entregas: set[str], nav: dict) -> list[str]:
    """Actividades de practica de una unidad, en orden.

    El nav lista las entregas una a una, pero NO los notebooks de practica: se alcanzan desde su
    pagina, no desde el menu (esa fue la decision al reorganizar). Asi que la practica se deduce:
    todo notebook de la unidad que no sea entrega, mas cualquier pagina que el nav si coloque bajo
    «Practica» —un taller que no se entrega, por ejemplo—.
    """
    paginas = [n for n in nav.get((ud, "practica"), []) if n.endswith(".md")]
    notebooks = sorted(x.name for x in (DOCS / ud / "notebooks").glob(f"{ud}_N*.ipynb")
                       if x.name not in entregas)
    return notebooks + paginas


def tabla(fichas: list[dict], ud: str) -> str:
    filas = ["| Actividad | Qué es | Descargar | Abrir en Colab |", "|---|---|---|---|"]
    for f in fichas:
        nb, cod = f["fichero"], f["codigo"]
        if f["es_notebook"]:
            enlace = f"[`{cod}` · {f['titulo']}](notebooks/{nb})"
            descarga = ("[![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)]"
                        f"({RAW}/{ud}/notebooks/{nb})" + '{:target="_blank"}')
            colab = ("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
                     f"({COLAB}/{ud}/notebooks/{nb})" + '{:target="_blank"}')
        else:
            # Los talleres y los debates son paginas: no hay .ipynb ni Colab.
            enlace, descarga, colab = f"[`{cod}` · {f['titulo']}]({nb})", "—", "—"
        filas.append(f"| {enlace} | {f['que_es']} | {descarga} | {colab} |")
    return "\n".join(filas)


def galeria(g: dict) -> str:
    """Rejilla de miniaturas, cada una enlazada a la imagen a tamaño completo.

    Usa la clase `grid` de Material y `<figure markdown="span">`, que ya funcionan con las
    extensiones `attr_list` y `md_in_html` que el sitio tiene activas: sin plugins nuevos.
    """
    ancho = g.get("ancho", 200)
    fuera = [f"\n**{g['titulo']}.** Pulsa la miniatura para verla a tamaño completo.\n",
             '<div class="grid" markdown>']
    for im in g["imagenes"]:
        src, pie = im["src"], im.get("pie", "")
        crudo = f"{RAW}/{g['ud']}/{src}"
        fuera.append('<figure markdown="span">')
        fuera.append(f"  [![{pie}]({src}){{ width=\"{ancho}\" }}]({src})")
        pie_txt = f"{pie} · " if pie else ""
        fuera.append(f'  <figcaption>{pie_txt}<a href="{crudo}" download>descargar</a></figcaption>')
        fuera.append("</figure>")
    fuera.append("</div>")
    return "\n".join(fuera)


def apartados(fichas: list[dict], grupo: str) -> str:
    """Un apartado por actividad: titulo, resumen, materiales y que se entrega."""
    fuera = []
    for f in fichas:
        fuera.append(f"## `{f['codigo']}` · {f['titulo']}\n")
        fuera.append(f["resumen"])
        if f.get("materiales"):
            fuera.append("\n| Recurso | Enlace |\n|---|---|\n" + "\n".join(f["materiales"]))
        if f.get("galeria"):
            fuera.append(galeria(f["galeria"]))
        if f.get("se_entrega"):
            etiqueta = "Se entrega" if grupo == "entregas" else "Qué tienes que tener al terminar"
            fuera.append(f"\n**{etiqueta}**: {f['se_entrega']}")
        fuera.append("")
    return "\n".join(fuera).strip()


def admonicion(grupo: str, n: int, ra: str | None, ud: str, extra: str | None,
               sin_rubrica: bool, hay_practica: bool) -> str:
    """La misma cabecera en las trece paginas, con lo que cambia entre unidades parametrizado."""
    if grupo == "practica":
        plural = "s" if n != 1 else ""
        cuerpo = (f'!!! info "Práctica: se hace, no se entrega"\n'
                  f"    {n} actividad{'es' if n != 1 else ''} que se trabaja{'n' if n != 1 else ''} "
                  f"**en clase**, con el profesor. **No se\n"
                  f"    entrega{plural} ni puntúa{plural}**: prepara{plural} las "
                  f"[entregas de la unidad]({ud}_Entregas.md) y "
                  f"{'la prueba escrita del ' + ra if ra else 'el resto del módulo'}.")
    else:
        cola = (f" La [práctica de la unidad]({ud}_ActividadesGuiadas.md) no se\n    entrega ni puntúa."
                if hay_practica else
                f" Los [ejercicios de autoevaluación]({ud}_Ejercicios.md) son\n    práctica y no se entregan.")
        if sin_rubrica:
            medio = ("    Se entregan en Moodle y **no llevan rúbrica**: se marcan como hechas o no "
                     "hechas." + cola)
        else:
            medio = ("    Cada una se corrige con **su rúbrica**, que puedes leer antes de empezar en la "
                     "propia\n    tarea de Moodle. El **peso** de cada entrega está en el libro de "
                     "calificaciones de\n    Moodle, no aquí." + cola)
        titulo_adm = f"{n} entrega{'s' if n != 1 else ''}" + (f" en el {ra}" if ra else "")
        cuerpo = f'!!! important "{titulo_adm}"\n{medio}'
    if extra:
        cuerpo += "\n\n" + "\n".join(f"    {l}" if l.strip() else "" for l in extra.strip().split("\n"))
    return cuerpo


# ---------------------------------------------------------------- comprobaciones

def etiquetas_descuadradas() -> list[str]:
    """Enlaces cuya etiqueta cita un codigo distinto de la actividad a la que apuntan."""
    patron = re.compile(r"\[([^\]\n]*?)\]\(([^)\s]*?UD0\d_([NTD]\d+)_[^)\s]*?\.(?:ipynb|md))\)")
    mal = []
    for f in sorted(DOCS.rglob("*.md")):
        if "Presentacion" in str(f):
            continue
        for m in patron.finditer(f.read_text(encoding="utf-8")):
            codigos = re.findall(r"\b[NTD]\d+\b", m.group(1))
            if codigos and m.group(3) not in codigos:
                mal.append(f"{f.relative_to(RAIZ)}: «{m.group(1)[:55]}» apunta al {m.group(3)}")
    return mal


def apartados_mal_colocados(datos: dict, nav: dict) -> list[str]:
    """Apartados que estan en la pagina del regimen equivocado."""
    mal = []
    for ud, d in datos.items():
        for clave, grupo in (("_pagina_practica", "practica"), ("_pagina_entregas", "entregas")):
            pagina = d.get(clave)
            if not pagina:
                continue
            entregas_ud = set(nav.get((ud, "entregas"), []))
            listas = {"entregas": sorted(entregas_ud),
                      "practica": practica_de(ud, entregas_ud, nav)}
            propios = {CODIGO.match(n).group(1) for n in listas[grupo]}
            otro = "entregas" if grupo == "practica" else "practica"
            ajenos = {CODIGO.match(n).group(1) for n in listas[otro]}
            texto = (DOCS / ud / pagina).read_text(encoding="utf-8")
            for m in re.finditer(r"(?m)^## `?([NTD]\d+)`?", texto):
                if m.group(1) in ajenos and m.group(1) not in propios:
                    mal.append(f"{ud}/{pagina}: «{m.group(1)}» es {otro}, está en {grupo}")
    return mal


def actividades_sin_resumen(datos: dict, nav: dict) -> list[str]:
    """Actividades que no tienen ficha con resumen en actividades.yml."""
    faltan = []
    todo = {}
    for ud in datos:
        entregas_ud = set(nav.get((ud, "entregas"), []))
        todo[(ud, "practica")] = practica_de(ud, entregas_ud, nav)
        todo[(ud, "entregas")] = sorted(entregas_ud)
    for (ud, grupo), lista in sorted(todo.items()):
        for nombre in lista:
            ficha = datos.get(ud, {}).get(nombre)
            if not isinstance(ficha, dict) or not ficha.get("resumen"):
                faltan.append(f"{ud}/{nombre} ({grupo}): sin resumen en datos/actividades.yml")
    return faltan


def defectos_de_markdown() -> list[str]:
    """Lineas pegadas a una fila de tabla o al separador del pie: Markdown se las traga."""
    mal = []
    for f in sorted(DOCS.rglob("*.md")):
        if "Presentacion" in str(f):
            continue
        lineas = f.read_text(encoding="utf-8").split("\n")
        dentro = False
        for i in range(len(lineas) - 1):
            if lineas[i].strip().startswith("```"):
                dentro = not dentro
            if dentro:
                continue
            a, b = lineas[i].strip(), lineas[i + 1].strip()
            if a.startswith("|") and a.endswith("|") and b and not b.startswith(("|", "<!--")):
                mal.append(f"{f.relative_to(RAIZ)}:{i + 2} → «{b[:50]}» dentro de la tabla")
            if b == "---" and a and not a.startswith("<!--"):
                mal.append(f"{f.relative_to(RAIZ)}:{i + 2} → «---» pegado a «{a[:40]}»")
    return mal


def recursos_redundantes() -> list[str]:
    """Filas de «Recurso | Enlace» que repiten lo que ya da la tabla generada."""
    redundante = re.compile(r"^\|\s*(Notebook|Ejecutar en Colab|Colab|Abrir en Colab|Descargar)\s*\|", re.I)
    mal = []
    for f in sorted(DOCS.rglob("*.md")):
        if "Presentacion" in str(f):
            continue
        for m in re.finditer(r"\| Recurso \| Enlace \|\n\|---\|---\|\n((?:\|[^\n]*\|\n)+)",
                             f.read_text(encoding="utf-8")):
            for fila in m.group(1).strip().split("\n"):
                if redundante.match(fila.strip()):
                    mal.append(f"{f.relative_to(RAIZ)}: «{fila.split('|')[1].strip()}» ya está en la tabla")
    return mal


def main() -> int:
    check = "--check" in sys.argv
    datos = yaml.safe_load((RAIZ / "datos" / "actividades.yml").read_text(encoding="utf-8"))
    nav = actividades_del_nav()
    desfasados = []

    for ud in sorted(datos):
        fichas = {"practica": [], "entregas": []}
        entregas_ud = set(nav.get((ud, "entregas"), []))
        listas = {"practica": practica_de(ud, entregas_ud, nav),
                  "entregas": nav.get((ud, "entregas"), [])}
        for grupo in ("practica", "entregas"):
            for nombre in listas[grupo]:
                es_nb = nombre.endswith(".ipynb")
                ruta = DOCS / ud / (f"notebooks/{nombre}" if es_nb else nombre)
                ficha = datos[ud].get(nombre)
                ficha = ficha if isinstance(ficha, dict) else {}
                fichas[grupo].append({
                    "fichero": nombre, "codigo": CODIGO.match(nombre).group(1),
                    "es_notebook": es_nb, "titulo": titulo(ruta),
                    "que_es": ficha.get("que_es", "—"), "resumen": ficha.get("resumen", ""),
                    "se_entrega": ficha.get("se_entrega", ""),
                    "materiales": ficha.get("materiales", []),
                    "galeria": (dict(ficha["galeria"], ud=ud) if ficha.get("galeria") else None),
                })

        for clave, grupo in (("_pagina_practica", "practica"), ("_pagina_entregas", "entregas")):
            pagina = datos[ud].get(clave)
            if not pagina:
                continue
            p = DOCS / ud / pagina
            texto = p.read_text(encoding="utf-8")
            if INICIO not in texto:
                print(f"  {ud}/{pagina}: sin bloque AUTO:notebooks")
                continue
            i, j = texto.index(INICIO) + len(INICIO), texto.index(FIN)
            nuevo = "\n" + admonicion(grupo, len(fichas[grupo]), datos[ud].get("_ra"), ud,
                                      datos[ud].get(f"_nota_{grupo}"),
                                      datos[ud].get("_sin_rubrica", False),
                                      bool(datos[ud].get("_pagina_practica"))) + "\n"
            if fichas[grupo]:
                nuevo += ("\n" + tabla(fichas[grupo], ud) + "\n\n"
                          + apartados(fichas[grupo], grupo) + "\n")
            if texto[i:j] == nuevo:
                print(f"  al día: {ud}/{pagina} [{grupo}]")
                continue
            desfasados.append(f"{ud}/{pagina} [{grupo}]")
            if not check:
                p.write_text(texto[:i] + nuevo + texto[j:], encoding="utf-8")
                print(f"  actualizado: {ud}/{pagina} [{grupo}] · {len(fichas[grupo])} actividades")

    problemas = {
        "ACTIVIDADES SIN RESUMEN": actividades_sin_resumen(datos, nav),
        "APARTADOS EN LA PÁGINA EQUIVOCADA": apartados_mal_colocados(datos, nav),
        "ETIQUETAS DESCUADRADAS": etiquetas_descuadradas(),
        "DEFECTOS DE MARKDOWN": defectos_de_markdown(),
        "RECURSOS REPETIDOS": recursos_redundantes(),
    }
    for titulo_p, lista in problemas.items():
        if lista:
            print(f"\n  {titulo_p}:")
            for x in lista:
                print(f"    {x}")

    if check and (desfasados or any(problemas.values())):
        if desfasados:
            print("\n  DESFASADAS: " + ", ".join(desfasados))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
