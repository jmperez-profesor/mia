#!/usr/bin/env python3
"""Normaliza las portadas de unidad a un ratio comun sin recortar contenido.

    python3 scripts/normalizar_portadas.py [--aplicar]

Sin --aplicar solo informa. Las seis portadas existentes son ilustraciones, logos o fotos de
producto sobre fondo plano y claro, asi que en vez de recortar al ratio comun se RELLENA hasta el
con el color del propio borde: no se pierde nada y la costura no se ve.

Ratio objetivo 4:3, que es la mediana de las seis. Se rellena en resolucion nativa (cero
reescalado) y solo se reduce lo que pase de ANCHO_MAX. La portada de UD00 no existe y se compone
del banner de marca del sitio mas el logotipo de Docker Desktop de la propia unidad.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
RATIO = 4 / 3
ANCHO_MAX = 1200
UNIDADES = ["UD01", "UD02", "UD03", "UD04", "UD05", "UD06"]


def color_borde(im: Image.Image) -> tuple:
    """Color dominante del borde. Es el relleno que hace invisible la costura."""
    px = im.load()
    w, h = im.size
    muestras = []
    for x in range(0, w, max(1, w // 80)):
        muestras += [px[x, 0], px[x, h - 1]]
    for y in range(0, h, max(1, h // 80)):
        muestras += [px[0, y], px[w - 1, y]]
    opacas = [c for c in muestras if len(c) < 4 or c[3] > 250]
    if not opacas:
        return (255, 255, 255)
    # La moda va bien con fondos planos; con ruido (UD03) la media del borde no deja escalon.
    from collections import Counter
    dom, n = Counter(opacas).most_common(1)[0]
    if n / len(opacas) >= 0.5:
        return dom[:3]
    return tuple(sum(c[i] for c in opacas) // len(opacas) for i in range(3))


def normalizar(origen: Path) -> Image.Image:
    im = Image.open(origen)
    fondo = color_borde(im.convert("RGBA"))
    if im.mode in ("RGBA", "LA", "P"):
        plano = Image.new("RGB", im.size, fondo)
        im = im.convert("RGBA")
        plano.paste(im, (0, 0), im)
        im = plano
    else:
        im = im.convert("RGB")

    w, h = im.size
    if w / h > RATIO:
        nw, nh = w, round(w / RATIO)
    else:
        nw, nh = round(h * RATIO), h
    lienzo = Image.new("RGB", (nw, nh), fondo)
    lienzo.paste(im, ((nw - w) // 2, (nh - h) // 2))
    if nw > ANCHO_MAX:
        lienzo = lienzo.resize((ANCHO_MAX, round(ANCHO_MAX / RATIO)), Image.LANCZOS)
    return lienzo


def portada_ud00() -> Image.Image:
    """UD00 no tiene portada: se compone con los logotipos de lo que ensena la unidad.

    Docker y Jupyter, que es exactamente de lo que va UD00. Los SVG son los oficiales de
    simple-icons, copiados del tema Material a docs/UD00/assets/ para que esto sea reproducible
    sin depender del venv. Son glifos de un solo trazo, asi que se les inyecta el color de marca.
    """
    ancho = ANCHO_MAX
    alto = round(ancho / RATIO)
    lienzo = Image.new("RGB", (ancho, alto), (255, 255, 255))

    LOGOS = [("logo-docker.svg", "#2496ED"), ("logo-jupyter.svg", "#F37626")]
    lado = round(alto * 0.42)          # los dos glifos son cuadrados (viewBox 24x24)
    hueco = round(ancho * 0.10)
    piezas = []
    for nombre, color in LOGOS:
        svg = (DOCS / "UD00" / "assets" / nombre).read_text()
        svg = svg.replace("<svg ", f'<svg fill="{color}" ', 1)
        tmp_svg = Path(f"/tmp/_{nombre}")
        tmp_png = Path(f"/tmp/_{nombre}.png")
        tmp_svg.write_text(svg)
        try:
            subprocess.run(["convert", "-background", "none", "-density", "600",
                            "-resize", f"{lado}x{lado}", str(tmp_svg), str(tmp_png)],
                           check=True, capture_output=True)
            piezas.append(Image.open(tmp_png).convert("RGBA"))
        except Exception as e:                                    # noqa: BLE001
            print(f"  aviso: no se pudo rasterizar {nombre} ({e})")

    if not piezas:
        return lienzo
    total = sum(p.width for p in piezas) + hueco * (len(piezas) - 1)
    x = (ancho - total) // 2
    for pieza in piezas:
        lienzo.paste(pieza, (x, (alto - pieza.height) // 2), pieza)
        x += pieza.width + hueco
    return lienzo


def main() -> int:
    aplicar = "--aplicar" in sys.argv
    print(f"Ratio objetivo {RATIO:.3f} (4:3) · ancho maximo {ANCHO_MAX} px"
          f"{'' if aplicar else '  [simulacion, usa --aplicar]'}\n")
    for ud in UNIDADES:
        origen = DOCS / ud / "assets" / "cover.png"
        if not origen.exists():
            print(f"{ud}: no existe {origen}")
            continue
        antes = Image.open(origen)
        salida = normalizar(origen)
        print(f"{ud}: {antes.format:5} {antes.width}x{antes.height} (ratio {antes.width/antes.height:.3f})"
              f"  ->  PNG {salida.width}x{salida.height} (4:3), relleno {color_borde(antes.convert('RGBA'))}")
        if aplicar:
            salida.save(origen, "PNG", optimize=True)

    destino = DOCS / "UD00" / "assets" / "cover.png"
    salida = portada_ud00()
    print(f"UD00: compuesta  ->  PNG {salida.width}x{salida.height} (4:3)")
    if aplicar:
        destino.parent.mkdir(parents=True, exist_ok=True)
        salida.save(destino, "PNG", optimize=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
