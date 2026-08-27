# AGENTS.md — ModelosIA

## What this is

MkDocs Material site with course notes for "Modelos de Inteligencia Artificial" (CE IA&BD). No application code — pure documentation.

## Commands

```bash
mkdocs serve          # dev server with live reload
mkdocs build          # build static site
mkdocs build --clean  # fresh build
```

The PDF (`docs/Libro.pdf`) is generated automatically during `mkdocs build` via the `mkdocs-with-pdf` plugin — no separate step needed.

## Setup

```bash
python3 -m venv ~/virtual-envs/mkdocs
source ~/virtual-envs/mkdocs/bin/activate
pip install -r requirements.txt
```

Or just run `./serve.sh` which does all the above then `mkdocs serve`.

## Key config

- `mkdocs.yml` is the single source of truth for nav, theme, plugins, and extensions
- `use_directory_urls: false` — page URLs use `.html` extension
- Math rendering via MathJax (configured in `js/mathjax-config.js`); math in markdown uses `\(...\)` / `\[...\]` (enabled by `pymdownx.arithmatex`)
- **Do NOT add `polyfill.io`** — the service was sold to a malicious actor (2024) and removed from `extra_javascript`
- Mermaid diagrams via `pymdownx.superfences` custom fence
- Extra CSS from `extra_sass/style.css.scss` compiled by `mkdocs-extra-sass-plugin`

## PDF output

- `mkdocs-with-pdf` outputs `docs/Libro.pdf`, but only runs when `PRERENDER_MERMAID=1`
  (`enabled_if_env` in `mkdocs.yml`) — the plain web build (`mkdocs build`, no env var) skips it
  entirely. `ci.yml` does two separate builds: a web build for the live site, and a
  `PRERENDER_MERMAID=1` build into `site-pdf/` whose PDF gets copied into the real `site/` before
  deploy. Reason: `mkdocs-with-pdf` fails intermittently on the GitHub Actions runner with
  hundreds of "No anchor" errors, not reproducible locally (2026-08-25) — the web build no longer
  pays that risk since it doesn't need the PDF anyway, only the one build that does.
- Custom cover/back-cover templates in `templates/`
- `pdf_event_hook/` was **deleted on 2026-08-26**. It was never wired into `mkdocs.yml`, but that
  did not make it dead: `mkdocs-with-pdf` auto-imports a module of exactly that name from the CWD
  (`drivers/event_hook.py`, `_module_name = 'pdf_event_hook'`), so it *was* loaded on every PDF
  build — the CI log for `32858601564` shows `Found PDF rendering event hook module.` plus one
  `(hook on inject_link: …)` line per page. Both of its functions had become no-ops, which is why
  it looked orphaned: `inject_link` looks for `md-header-nav` or a `<nav class="md-header__inner">`
  and Material 9 renders that node as a `<div>`, so it returned the HTML untouched; `pre_pdf_render`
  absolutized relative `<img src>` left behind by the plugin's `convert_iframe`, and
  `convert_iframe` was retired from `mkdocs.yml` on 2026-08-24 — it never logged a single fixed
  image again. Removing it is safe because with-pdf now falls back to `themes/material.py`'s own
  `inject_link`, which appends a "download PDF" link to the footer of the **`site-pdf/` build**,
  and CI copies only `site-pdf/docs/Libro.pdf` into the real `site/` (`ci.yml`) — that HTML is
  discarded. Side benefit: ~200 log lines per build gone. The PDF download icon in the header (top
  right, next to the GitHub link on desktop / next to the search icon on mobile) is added
  independently in `hooks.py`'s `on_post_page`, which skips the `PRERENDER_MERMAID=1` build.
- The `offline` plugin is commented out (it would break SEO)

## Structure

```
docs/          → markdown source files, one per nav entry
  UD01..UD05/  → units, each with theory, slides, guided activities, deliverables
  assets/      → images, portada.png
  css/         → extra.css
mkdocs.yml     → site config
```

## Style conventions

- Content language is Spanish (`language: es` in mkdocs.yml, `search.language: es`)
- Admonitions heavily used (note, tip, warning, danger, example, etc.)
- Light/dark mode toggle via Material palette
- CC BY-NC-SA 4.0 license
