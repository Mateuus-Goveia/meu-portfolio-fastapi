"""Ícones SVG inline (Font Awesome Free, CC BY 4.0), sem depender de CDN."""
from functools import lru_cache
from pathlib import Path

from markupsafe import Markup

ICON_DIR = Path(__file__).resolve().parent / "static" / "icons"


@lru_cache(maxsize=None)
def _raw(name: str) -> str:
    return (ICON_DIR / f"{name}.svg").read_text(encoding="utf-8").strip()


def icon(name: str, css_class: str = "icon") -> Markup:
    """Devolve o SVG pronto para inserir no HTML; a cor segue o texto (currentColor)."""
    try:
        svg = _raw(name)
    except FileNotFoundError:
        return Markup("")
    svg = svg.replace(
        "<svg ",
        f'<svg class="{css_class}" aria-hidden="true" focusable="false" fill="currentColor" ',
        1,
    )
    return Markup(svg)
