"""Hooks de MkDocs para el proyecto _MIA.

Para cada página generada desde un notebook (.ipynb) se inserta un bloque con dos
botones:
  - "Abrir en Colab"  -> enlace a Google Colab (usa extra.colab de mkdocs.yml)
  - "Descargar .ipynb" -> enlace a la fuente raw del notebook (usa extra.raw_base)

Si no se configuran `extra.colab` / `extra.raw_base`, los botones omitidos se ignoran.
"""

from mkdocs.config.defaults import MkDocsConfig


def on_page_markdown(
    markdown: str,
    *,
    page,
    config: MkDocsConfig,
    files,
) -> str:
    src = getattr(page.file, "src_path", "")
    if not src.endswith(".ipynb"):
        return markdown

    extra = config.get("extra", {})
    buttons: list[str] = []

    colab = extra.get("colab")
    if colab and colab.get("user") and colab.get("repo"):
        branch = colab.get("branch", "main")
        base = (
            f"https://colab.research.google.com/github/"
            f"{colab['user']}/{colab['repo']}/blob/{branch}/{src}"
        )
        buttons.append(
            f'<a class="md-button md-button--primary" href="{base}">'
            f'Abrir en Colab</a>'
        )

    raw_base = extra.get("raw_base")
    if raw_base:
        dl = f'{raw_base.rstrip("/")}/{src}'
    else:
        dl = src
    buttons.append(f'<a class="md-button" href="{dl}">Descargar .ipynb</a>')

    banner = (
        '<div class="notebook-actions" style="margin:0 0 1rem 0">\n'
        + "\n".join(buttons)
        + "\n</div>\n\n"
    )
    return banner + markdown
