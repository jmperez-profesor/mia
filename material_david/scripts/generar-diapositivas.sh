#!/usr/bin/env bash
# Genera las diapositivas de una unidad (PDF + HTML) desde su guion Marp.
#
#   ./generar-diapositivas.sh UD00        # todas las de la unidad
#   ./generar-diapositivas.sh UD00 UD00_1_ES.md
#
# Requisitos: node (para npx) y un Chromium para el PDF. Se apoya en el que trae Playwright si
# está disponible; CHROME_NO_SANDBOX es necesario en esta máquina o el PDF falla sin mensaje claro.
set -euo pipefail
cd "$(dirname "$0")/.."
UD="${1:?Uso: ./generar-diapositivas.sh UDxx [fichero.md]}"
DIR="docs/$UD/Presentacion"
[ -d "$DIR" ] || { echo "No existe $DIR"; exit 1; }

if [ -z "${CHROME_PATH:-}" ]; then
  CHROME_PATH="$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux64/chrome 2>/dev/null | head -1 || true)"
fi
export CHROME_PATH CHROME_NO_SANDBOX=true

shift || true
FICHEROS=("$@")
[ ${#FICHEROS[@]} -eq 0 ] && mapfile -t FICHEROS < <(cd "$DIR" && ls *.md 2>/dev/null)

HOY="$(date +%F)"
for f in "${FICHEROS[@]}"; do
  base="${f%.md}"
  echo "· $UD/$f"
  # La version de la portada es la fecha de modificacion: se sella al generar.
  sed -i -E "s/^###### version: .*/###### version: $HOY/" "$DIR/$f"

  # Marp no renderiza mermaid: los bloques ```mermaid saldrian como texto plano en la
  # diapositiva. Se rasterizan a PNG y se sustituyen en una COPIA (el guion original conserva
  # el codigo mermaid editable). La copia vive en el mismo directorio para no romper las rutas
  # relativas a ../assets e img/. Si no hay mermaid, el script devuelve el original tal cual.
  FUENTE="$(python3 scripts/prerender_mermaid_marp.py "$DIR/$f")"
  FUENTE_REL="$(basename "$FUENTE")"

  # Tanto el HTML como el PDF se generan desde la copia rasterizada: los diagramas se ven en
  # ambos formatos, no solo en el PDF.
  (cd "$DIR" && npx --yes @marp-team/marp-cli@latest "$FUENTE_REL" --allow-local-files -o "$base.html" >/dev/null 2>&1)
  if [ -n "${CHROME_PATH:-}" ] && [ -x "${CHROME_PATH:-}" ]; then
    (cd "$DIR" && npx --yes @marp-team/marp-cli@latest "$FUENTE_REL" --pdf --allow-local-files -o "$base.pdf" >/dev/null 2>&1) \
      && echo "  PDF y HTML generados" || echo "  HTML generado; el PDF ha fallado (revisa CHROME_PATH)"
  else
    echo "  HTML generado; sin Chromium no se puede hacer el PDF"
  fi

  # La miniatura de la primera diapositiva (poster-slide1.png) es lo que se ve en la pagina
  # UDxx_Diapositivas.md y en el PDF del libro. Hasta el 2026-08-27 se hacia a mano, asi que se
  # quedaba desfasada al cambiar la portada: ahora se regenera aqui, con --image (solo la 1.a).
  if [ -n "${CHROME_PATH:-}" ] && [ -x "${CHROME_PATH:-}" ]; then
    mkdir -p "$DIR/img"
    (cd "$DIR" && npx --yes @marp-team/marp-cli@latest "$FUENTE_REL" --image png --allow-local-files \
        -o "img/poster-slide1.png" >/dev/null 2>&1) \
      && echo "  miniatura regenerada" || echo "  la miniatura ha fallado"
  fi

  if [ "$FUENTE_REL" != "$f" ]; then
    rm -f "$FUENTE"
  fi
done
