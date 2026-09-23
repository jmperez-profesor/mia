#!/usr/bin/env bash
# nbl2assets.sh — convierte y optimiza artefactos de NotebookLM para el sitio MkDocs.
#
# Uso:
#   ./scripts/nbl2assets.sh <BLOQUE> <fichero> [--tipo image|pdf|audio]
#
#   <BLOQUE>   Etiqueta usada en el nombre (p. ej. B01, B04, B05).
#   <fichero>  PDF, PNG/JPG, PPTX o WAV/MP3 descargado de NotebookLM.
#   --tipo     (opcional) fuerza el tratamiento. Por defecto:
#                - PDF/PNG/JPG -> image (genera imagen optimizada en docs/assets/nbl/)
#                - PPTX        -> pdf   (convierte y guarda en docs/assets/pdf/)
#                - WAV/MP3     -> audio (convierte a mp3 en docs/assets/audio/)
#
# Requiere: pdftoppm, libreoffice, ffmpeg y Python con Pillow (ya disponibles).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NBL="$ROOT/docs/assets/nbl"
PDFDIR="$ROOT/docs/assets/pdf"
AUDIO="$ROOT/docs/assets/audio"
mkdir -p "$NBL" "$PDFDIR" "$AUDIO"

# Python con Pillow: preferimos el venv del proyecto.
PYBIN="${MIA_PYTHON:-python3}"
if [ -x "$HOME/virtual-envs/mia-mkdocs/bin/python" ]; then
  PYBIN="$HOME/virtual-envs/mia-mkdocs/bin/python"
fi

if [ $# -lt 2 ]; then
  echo "Uso: $0 <BLOQUE> <fichero> [--tipo image|pdf|audio]" >&2
  exit 1
fi

BLOQUE="$1"; FILE="$2"; TIPO="${4:-}"
[ -f "$FILE" ] || { echo "No existe: $FILE" >&2; exit 1; }
BASE="$(basename "$FILE")"; EXT="${BASE##*.}"; EXT="$(echo "$EXT" | tr '[:upper:]' '[:lower:]')"
NAME="$(echo "${BASE%.*}" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')"
SLUG="${BLOQUE,,}_${NAME}"

# Tipo por defecto
if [ -z "$TIPO" ]; then
  case "$EXT" in
    pdf|png|jpg|jpeg) TIPO="image" ;;
    pptx)             TIPO="pdf" ;;
    wav|mp3|m4a)      TIPO="audio" ;;
    *) echo "Extensión no reconocida: $EXT" >&2; exit 1 ;;
  esac
fi

optimize_img() {  # $1=entrada $2=salida
  "$PYBIN" - "$1" "$2" <<'PY'
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src)
if im.width > 1400:
    im = im.resize((1400, int(im.height*1400/im.width)))
im.convert("RGB").save(dst, "JPEG", quality=85)
PY
}

case "$TIPO" in
  image)
    if [ "$EXT" = "pdf" ]; then
      pdftoppm -png -r 150 "$FILE" "$NBL/${SLUG}"
      for p in "$NBL/${SLUG}"-*.png; do
        optimize_img "$p" "${p%.png}.jpg"; rm -f "$p"
      done
      echo "Imágenes generadas en docs/assets/nbl/:"
      ls -1 "$NBL/${SLUG}"-*.jpg
      echo
      echo "Pega esto en el .md (ajusta la ruta relativa y el texto):"
      echo "----------------------------------------------------------------"
      echo '<figure markdown>'
      echo "  ![Descripción](../assets/nbl/${SLUG}-1.jpg){ width=\"700\" }"
      echo "  <figcaption>Descripción · elaborado con NotebookLM</figcaption>"
      echo '</figure>'
    else
      optimize_img "$FILE" "$NBL/${SLUG}.jpg"
      echo "Imagen optimizada: docs/assets/nbl/${SLUG}.jpg"
      echo
      echo "Pega esto en el .md:"
      echo "----------------------------------------------------------------"
      echo '<figure markdown>'
      echo "  ![Descripción](../assets/nbl/${SLUG}.jpg){ width=\"700\" }"
      echo "  <figcaption>Descripción · elaborado con NotebookLM</figcaption>"
      echo '</figure>'
    fi
    ;;
  pdf)
    if [ "$EXT" = "pptx" ]; then
      libreoffice --headless --convert-to pdf "$FILE" --outdir "$PDFDIR" >/dev/null
      OUT="$PDFDIR/$NAME.pdf"
    else
      cp "$FILE" "$PDFDIR/${SLUG}.pdf"; OUT="$PDFDIR/${SLUG}.pdf"
    fi
    echo "PDF guardado: $OUT"
    echo
    echo "Pega esto en el .md:"
    echo "----------------------------------------------------------------"
    echo "- [$(echo "$NAME" | tr '_' ' ') (PDF)](../assets/pdf/$(basename "$OUT"))"
    echo
    echo '<iframe src="../assets/pdf/'"$(basename "$OUT")"'" width="100%" height="620" style="border:1px solid #ccc;border-radius:8px"></iframe>'
    ;;
  audio)
    ffmpeg -y -i "$FILE" -codec:a libmp3lame -q:a 5 "$AUDIO/${SLUG}.mp3" >/dev/null 2>&1
    echo "Audio: docs/assets/audio/${SLUG}.mp3"
    echo
    echo "Pega esto en el .md:"
    echo "----------------------------------------------------------------"
    echo '<audio controls style="width:100%">'
    echo "  <source src=\"../assets/audio/${SLUG}.mp3\" type=\"audio/mpeg\">"
    echo '</audio>'
    ;;
  *)
    echo "Tipo no válido: $TIPO" >&2; exit 1 ;;
esac
