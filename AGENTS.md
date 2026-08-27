# AGENTS.md — Proyecto `_MIA`

## What this is

MkDocs Material (tema Material, español) con apuntes y materiales docentes del módulo **5071 «Modelos de Inteligencia Artificial»** del Curso de Especialización en Inteligencia Artificial y Big Data (CE IA&BD), Comunitat Valenciana, curso 2026-2027. No es código de aplicación: es documentación + notebooks.

El proyecto se planifica por **sesiones de 2 horas** (no por UD), agrupadas en 3 bloques (B01–B03) alineados con los **RA1, RA2 y RA3** (alcance de este docente). Los RA4–RA6 y el RA7 (proyecto intermodular) los imparten otros docentes y quedan fuera de este proyecto.

## Commands

```bash
mkdocs serve          # servidor de desarrollo con live reload
mkdocs build          # build estático del sitio
mkdocs build --clean  # build limpio
```

O simplemente `./serve.sh` (crea venv, instala requirements y lanza `mkdocs serve`).

## Setup

```bash
python3 -m venv ~/virtual-envs/mia-mkdocs
source ~/virtual-envs/mia-mkdocs/bin/activate
pip install -r requirements.txt
```

## Key config

- `mkdocs.yml` es la fuente de verdad para nav, tema, plugins y extensiones.
- `use_directory_urls: false` → las URLs usan `.html`.
- **No hay PDF**: solo web + notebooks. (David sí generaba `Libro.pdf`; aquí se descarta por decisión de 2026-08-27.)
- Render de notebooks vía `mkdocs-jupyter` (`plugins: - jupyter`).
- `hooks.py` inyecta en las páginas generadas desde `.ipynb` dos botones: **Abrir en Colab** y **Descargar .ipynb** (lee `extra.colab` y `extra.raw_base` de `mkdocs.yml`).
- Matemáticas con MathJax (`pymdownx.arithmatex` genérico + CDN en `extra_javascript`).
- Diagramas Mermaid vía `pymdownx.superfences` (fence `mermaid`) + init en `docs/assets/js/init.js`.
- No añadir `polyfill.io` (servicio comprometido en 2024).
- Idioma `es`; admonitions y paleta claro/oscuro.

## Estructura

```
PLAN.md          plan maestro (temporalización por sesiones 2h)
AGENTS.md         este fichero
FUENTES.md        fichas de fuentes legales/técnicas
legislacion/      análisis normativo + programación didáctica + plantilla_sesion.md
material_david/   copia de referencia del proyecto de David (solo análisis)
docs/             fuente markdown; index, normativa/, bloques/B01..B06/, assets/
practicas/        notebooks .ipynb por sesión/bloque
evaluacion/       bancos de pruebas y rúbricas por RA (bajo docs/)
fuentes/          PDFs de normativa oficial
```

## Convenciones de contenido

- Cada sesión de 2h = un fichero `docs/bloques/Bxx_RAy/sesionNN.md` siguiendo `legislacion/plantilla_sesion.md`.
- Los notebooks viven en `practicas/` y se enlazan desde su sesión.
- No copiar literalmente la prosa de David (`material_david/`); se usa solo como referencia de método y para revisar/aportar mejoras.
- Licencia prevista: CC BY-NC-SA 4.0 (coincide con la de David).

## Historial de decisiones (fechas)

- 2026-08-27: enfoque por sesiones de 2h; 2/semana (lun+mié); viernes = RA7 de otros.
- 2026-08-27: solo web + notebooks, sin PDF.
- 2026-08-27: festivos/vacaciones desde `material_david/datos/curriculo.yml` (calendario Carlet 26-27, DOGV 2026/24495).
- 2026-08-27: no ajustar estrictamente a 90 h; prevalece horario real del centro (57 sesiones disponibles).

## Session history

- **Sesión 1 (2026-08-27, modo PLAN):** investigación de normativa, diseño de scaffolding y plantilla de sesión. Creados los ficheros de gobierno y el esqueleto MkDocs. Sin contenido de sesiones todavía (pendiente NotebookLM del profesor).
- **Sesión 2 (2026-08-27):** alcance acotado a RA1–RA3 (RA4–RA6 y RA7 fuera). Tabla de 26 sesiones en PLAN.md con fechas/títulos/contenidos. Generadas las 26 sesiones (`docs/bloques/B01_RA1` 8, `B02_RA2` 10, `B03_RA3` 8), cada una con práctica guiada (solución) y notebook de miniproyecto `.ipynb`. Build limpio (exit 0). Añadidos bancos de pruebas (test+desarrollo) y rúbricas por RA1–RA3 en `docs/evaluacion/`.
- **Verificación build:** `mkdocs build --clean` compila sin errores (exit 0). Ajustes aplicados: `language` va bajo `theme:` (mkdocs 1.6.1 no acepta `language` top-level); el plugin es `mkdocs-jupyter` (no `jupyter`). El venv venía con el paquete `properdocs` (fork que sombrea mkdocs): se desinstaló. Único warning residual: "no git logs" (repo sin commits). falta fijar `repo_url` / `extra.colab` / `extra.raw_base` en mkdocs.yml.
