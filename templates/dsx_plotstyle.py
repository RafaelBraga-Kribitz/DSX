"""Analyst-side figure-finalisation helper (REQ-P23-02/03, GA-2/GA-3).

matplotlib-only, imported by analysts at readout time. This module lives in
``templates/`` — OUTSIDE the hermetic ``dsx/`` gate closure — and is never imported
by any ``GATE_PROFILES`` module. ``tests/test_gate_path_hermetic.py`` forbids
``matplotlib`` on the gate path precisely so this stays true (D-P23-03).

Three keyword-explicit functions (GA-2):
  - ``finalise_figure(fig, *, title, source, subtitle=None, note=None) -> Figure``
    — ``source`` is a *mandatory* keyword with no default; omitting it is a
    ``TypeError`` at call binding, making "every figure cites its source" a
    signature property (mirrors DSX-VIZ-062).
  - ``direct_label(ax, *, ...) -> list[Text]`` — labels each line at its terminal
    point instead of relying on a legend.
  - ``save_deterministic(fig, path, *, metadata=None, **savefig_kwargs) -> Path``
    — writes a byte-reproducible SVG using the GA-3 recipe. It **writes only**; it
    does NOT hash. ``dsx seal`` (stdlib ``hashlib``) stays the single hashing
    authority (GA-2), so this file imports no ``hashlib`` and calls nothing in
    ``dsx.checks.figures``.

Style selection: ``use_style(name)`` applies one of the vendored
``styles/<name>.mplstyle`` sheets by name — ``dsx-urban`` is the house default,
``dsx-538``, ``dsx-bbc`` and ``dsx-econ`` are the alternatives — resolving the path
relative to this file so a caller never depends on the working directory.
``available_styles()`` lists the names it accepts.

GA-3 determinism recipe (verified against installed matplotlib 3.11.1 source,
23-RESEARCH §3/§4/§5):
  - ``svg.hashsalt='dsx'`` — makes SVG element ids a pure function of content
    rather than a per-process ``uuid4`` (``_make_id``).
  - ``metadata={'Date': None}`` merged in — suppresses the per-render
    ``datetime.today()`` timestamp (``_write_metadata`` only auto-stamps when the
    ``'Date'`` key is *absent*; present-but-None omits it entirely). The helper
    owns this default so a caller cannot accidentally re-stamp (Pitfall 2).
  - ``svg.fonttype='path'`` — glyphs baked as vector paths, removing font-name
    dependency from the output.
  - Vendored Lato registered via ``font_manager.addfont`` at import time, BEFORE
    any ``plt.style.use`` resolves ``font.family`` to it (Pitfall 1: the findfont
    cache clears forward-only).

The pinned matplotlib version is recorded in ``FIGURE-MANIFEST.yaml``
(``matplotlib_version``); ``dsx/checks/figures.py`` does not read it, so it is
additive and mints nothing.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
from matplotlib import font_manager
from matplotlib import style as mpl_style
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.text import Text
from matplotlib.transforms import offset_copy

# Fixed salt makes RendererSVG._make_id deterministic across renders and processes.
_HASHSALT = "dsx"
# Vendored fonts live one level up from templates/, in styles/fonts/. The glob in
# register_fonts() picks up both faces shipped there, Lato-Regular.ttf and
# Lato-Bold.ttf (bold is used by finalise_figure's title); the font licence is
# styles/fonts/OFL.txt (SIL Open Font License 1.1).
_FONT_DIR = Path(__file__).resolve().parent.parent / "styles" / "fonts"
# The vendored .mplstyle sheets live beside the fonts, in styles/.
_STYLE_DIR = Path(__file__).resolve().parent.parent / "styles"


def register_fonts() -> None:
    """Register every vendored ``styles/fonts/Lato-*.ttf`` with matplotlib.

    Called once at import time so Lato resolves before any caller's
    ``plt.style.use`` / draw call (Pitfall 1). Idempotent: re-registering an
    already-known font is harmless.
    """
    for ttf in sorted(_FONT_DIR.glob("Lato-*.ttf")):
        font_manager.fontManager.addfont(str(ttf))


# Register at import time — before any style/draw resolves font.family to Lato.
register_fonts()


def available_styles() -> list[str]:
    """Return the names ``use_style`` accepts, e.g. ``['dsx-538', ..., 'dsx-urban']``."""
    return sorted(path.stem for path in _STYLE_DIR.glob("dsx-*.mplstyle"))


def use_style(name: str) -> Path:
    """Apply the vendored style sheet ``styles/<name>.mplstyle`` and return its path.

    ``name`` is the file stem — ``"dsx-urban"`` (house default), ``"dsx-538"``,
    ``"dsx-bbc"`` or ``"dsx-econ"``. The path is resolved relative to this module,
    mirroring ``register_fonts()``, so the call works from any working directory.
    An unknown name raises ``ValueError`` listing the names that exist.
    """
    path = _STYLE_DIR / f"{name}.mplstyle"
    known = available_styles()
    if name not in known or not path.is_file():
        raise ValueError(
            f"unknown DSX style {name!r}; available styles: "
            f"{', '.join(known) if known else f'none found under {_STYLE_DIR}'}"
        )
    mpl_style.use(str(path))
    return path


def finalise_figure(
    fig: Figure,
    *,
    title: str,
    source: str,
    subtitle: str | None = None,
    note: str | None = None,
) -> Figure:
    """Apply the DSX takeaway-title + mandatory-source finishing to ``fig``.

    ``title`` is the takeaway sentence; ``subtitle`` an optional clarifier beneath
    it; ``source`` the mandatory provenance line (rendered as a figure footnote —
    omitting it is a ``TypeError`` at call binding); ``note`` an optional caveat.
    Returns the mutated ``fig``.
    """
    fig.suptitle(title, ha="left", x=0.01, fontsize="x-large", fontweight="bold")
    if subtitle:
        # Sits just below the suptitle, left-aligned to match.
        fig.text(0.01, 0.94, subtitle, ha="left", va="top", fontsize="large")
    # Mandatory source line, bottom-left figure footnote.
    fig.text(0.01, 0.01, f"Source: {source}", ha="left", va="bottom", fontsize="small")
    if note:
        fig.text(0.99, 0.01, note, ha="right", va="bottom", fontsize="small")
    return fig


def direct_label(
    ax: Axes,
    *,
    labels: dict | None = None,
    color_from_line: bool = True,
    x_offset: float = 6.0,
    fontsize: float | None = None,
) -> list[Text]:
    """Label each line at its terminal (rightmost) data point instead of a legend.

    ``labels`` optionally maps a line's label to display text (default uses
    ``line.get_label()``); internal matplotlib labels (``_child0`` …) are skipped.
    Colour is inherited from the line when ``color_from_line``. ``x_offset`` is in
    typographic points. Returns the created ``Text`` artists.
    """
    texts: list[Text] = []
    for line in ax.get_lines():
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        if len(xdata) == 0:
            continue
        key = line.get_label()
        display = labels.get(key, key) if labels is not None else key
        # Skip matplotlib's auto-assigned internal labels.
        if isinstance(display, str) and display.startswith("_"):
            continue
        color = line.get_color() if color_from_line else None
        trans = offset_copy(
            ax.transData, fig=ax.figure, x=x_offset, y=0.0, units="points"
        )
        text = ax.text(
            xdata[-1],
            ydata[-1],
            display,
            transform=trans,
            va="center",
            ha="left",
            color=color,
            fontsize=fontsize,
            clip_on=False,
        )
        texts.append(text)
    return texts


def save_deterministic(
    fig: Figure,
    path: str | Path,
    *,
    metadata: dict | None = None,
    **savefig_kwargs,
) -> Path:
    """Write ``fig`` to ``path`` as a byte-reproducible SVG (GA-3). Writes only.

    Applies the determinism recipe (fixed ``svg.hashsalt``, ``svg.fonttype='path'``,
    ``metadata={'Date': None}`` merged so the timestamp cannot leak) and returns the
    output ``Path``. It does NOT hash — ``dsx seal`` remains the single hashing
    authority (GA-2); this function imports no ``hashlib``.
    """
    mpl.rcParams["svg.hashsalt"] = _HASHSALT
    mpl.rcParams["svg.fonttype"] = "path"
    merged_metadata = {"Date": None, **(metadata or {})}
    out = Path(path)
    fig.savefig(out, format="svg", metadata=merged_metadata, **savefig_kwargs)
    return out
