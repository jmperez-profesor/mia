#!/usr/bin/env python3
"""Genera las tablas curriculares desde datos/curriculo.yml.

Cada tabla se escribe entre marcadores en el fichero destino:

    <!-- AUTO:unidades inicio -->
    ...tabla generada...
    <!-- AUTO:unidades fin -->

Así una sola edición de datos/curriculo.yml actualiza todas las páginas y no vuelven
a divergir horas, semanas o pesos entre index.md, PLAN.md y la programación.

Uso:
  scripts/generar_tablas.py            # reescribe los bloques marcados
  scripts/generar_tablas.py --check    # solo comprueba que están al día (para el QA)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos" / "curriculo.yml"

# tabla -> ficheros destino
# En ModelosIA (sitio maestro) las tablas viven en la portada. La de RA lleva
# incorporados los pesos y la nota mínima (decisión del profesor, 2026-08-21).
DESTINOS = {
    "unidades": ["docs/index.md"],
    "ra_pesos": ["docs/index.md"],
}


def semanas(u: dict) -> str:
    a, b = u["semana_inicio"], u["semana_fin"]
    return str(a) if a == b else f"{a}-{b}"


MESES = ["ene", "feb", "mar", "abr", "may", "jun",
         "jul", "ago", "sep", "oct", "nov", "dic"]


def fechas(u: dict) -> str:
    """Rango de fechas reales de la unidad, en formato «13 oct – 6 nov»."""
    a, b = u.get("fecha_inicio"), u.get("fecha_fin")
    if not a or not b:
        return "—"
    return f"{a.day} {MESES[a.month - 1]} – {b.day} {MESES[b.month - 1]}"


def pagina_unidad(u: dict) -> str | None:
    """Ruta relativa a la página de teoría de la unidad, o None si no tiene entrada en el sitio
    (UD07 es el proyecto integrador, placeholder deliberado; Cierre no es una unidad)."""
    if u["id"] in ("UD07", "Cierre"):
        return None
    return f"{u['id']}/{u['id']}_ES.md"


def tabla_unidades(d: dict) -> str:
    filas = ["| UD | Título | RA | Horas | Semanas | Fechas |",
             "|---|---|---|---|---|---|"]
    for u in d["unidades"]:
        ra = u["ra"] or "—"
        titulo = u["titulo"]
        if u["id"] == "UD07":
            titulo = f"**{titulo}**"
        pagina = pagina_unidad(u)
        ud_celda = f"[{u['id']}]({pagina})" if pagina else u["id"]
        titulo_celda = f"[{titulo}]({pagina})" if pagina else titulo
        filas.append(
            f"| {ud_celda} | {titulo_celda} | {ra} | {u['horas']} | {semanas(u)} | {fechas(u)} |"
        )
    total = sum(u["horas"] for u in d["unidades"])
    cal = d.get("calendario", {})
    con_clase = cal.get("semanas_con_clase")
    nota = f"**{d['modulo']['semanas']}** nominales"
    if con_clase:
        nota += f"<br/>{con_clase} con clase"
    filas.append(f"| | **Total** | | **{total}** | {nota} | |")
    return "\n".join(filas)


def tabla_ra(d: dict) -> str:
    filas = ["| RA | CE | Enunciado |", "|---|---|---|"]
    for r in d["resultados_aprendizaje"]:
        enunciado = " ".join(r["enunciado"].split())
        filas.append(f"| **{r['id']}** | {r['ce']} | {enunciado} |")
    return "\n".join(filas)


def tabla_pesos(d: dict) -> str:
    ev = d["evaluacion"]
    filas = ["| RA | Peso en la nota del módulo |", "|---|---|"]
    for ra, peso in ev["pesos_ra"].items():
        txt = f"{peso:g}".replace(".", ",")
        filas.append(f"| {ra} | {txt} % |")
    filas.append("| | **100 %** |")
    filas.append("")
    filas.append(f"Cada RA se califica ({ev['escala_calificacion']}) = "
                 f"**{ev['peso_actividades']} %** tareas, talleres y "
                 f"ejercicios + **{ev['peso_prueba_escrita']} %** prueba escrita. "
                 f"Para superar el módulo hace falta **≥{ev['nota_minima_por_ra']} en cada RA**.")
    return "\n".join(filas)


def tabla_ra_pesos(d: dict) -> str:
    """RA + CE + enunciado + nota mínima + peso, en una sola tabla."""
    ev = d["evaluacion"]
    pesos = ev["pesos_ra"]
    minima = ev["nota_minima_por_ra"]
    filas = ["| RA | CE | Descripción | Nota mínima | Peso |", "|---|---|---|---|---|"]
    for r in d["resultados_aprendizaje"]:
        enunciado = " ".join(r["enunciado"].split())
        peso = f"{pesos.get(r['id'], 0):g}".replace(".", ",")
        filas.append(f"| **{r['id']}** | {r['ce']} | {enunciado} | **{minima}** | **{peso} %** |")
    filas.append("| | | | | **100 %** |")
    filas.append("")
    filas.append(f"Cada RA se califica **{ev['escala_calificacion']}** "
                 f"(Orden 8/2025, art. 5.1): **{ev['peso_actividades']} %** las entregas de la "
                 f"unidad + **{ev['peso_prueba_escrita']} %** la prueba escrita. Para superar el "
                 f"módulo hace falta **{minima} o más en cada RA**. Los ejercicios de "
                 f"autoevaluación y los notebooks guiados son práctica: no se entregan ni "
                 f"puntúan. El peso de cada entrega está en el libro de calificaciones de Moodle.")
    return "\n".join(filas)

GENERADORES = {"unidades": tabla_unidades, "ra": tabla_ra,
               "pesos": tabla_pesos, "ra_pesos": tabla_ra_pesos}


def aplicar(texto: str, nombre: str, contenido: str) -> tuple[str, bool]:
    patron = re.compile(
        rf"<!-- AUTO:{nombre} inicio -->.*?<!-- AUTO:{nombre} fin -->",
        re.DOTALL,
    )
    if not patron.search(texto):
        return texto, False
    bloque = (f"<!-- AUTO:{nombre} inicio -->\n{contenido}\n"
              f"<!-- AUTO:{nombre} fin -->")
    return patron.sub(lambda _: bloque, texto), True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true", help="no escribe; falla si hay algo desactualizado")
    args = p.parse_args()

    datos = yaml.safe_load(DATOS.read_text(encoding="utf-8"))
    desactualizados, sin_marcador = [], []

    for nombre, ficheros in DESTINOS.items():
        contenido = GENERADORES[nombre](datos)
        for rel in ficheros:
            ruta = RAIZ / rel
            texto = ruta.read_text(encoding="utf-8")
            nuevo, encontrado = aplicar(texto, nombre, contenido)
            if not encontrado:
                sin_marcador.append(f"{rel} (falta <!-- AUTO:{nombre} inicio/fin -->)")
                continue
            if nuevo == texto:
                print(f"  al día: {rel} [{nombre}]")
            elif args.check:
                desactualizados.append(f"{rel} [{nombre}]")
            else:
                ruta.write_text(nuevo, encoding="utf-8")
                print(f"  actualizado: {rel} [{nombre}]")

    for aviso in sin_marcador:
        print(f"  AVISO: {aviso}")

    if desactualizados:
        print("\nDesactualizados respecto a datos/curriculo.yml:")
        for d in desactualizados:
            print(f"  - {d}")
        print("Ejecuta scripts/generar_tablas.py para regenerarlos.")
        return 1

    total = sum(u["horas"] for u in datos["unidades"])
    if total != datos["modulo"]["horas"]:
        print(f"\nERROR: las horas de las unidades suman {total} y el módulo declara "
              f"{datos['modulo']['horas']}.")
        return 1

    return 1 if sin_marcador else 0


if __name__ == "__main__":
    sys.exit(main())
