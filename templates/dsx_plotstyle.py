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

Braga design system: ``use_bk_theme(mode)`` installs the Braga design system v2.1
through the optional ``bk-viz`` package (``import bk_theme``; D-053) instead of a
style sheet — BKribitz type, the ``surface`` ground, hairline axes, labels in
``ink``/``ink-2``. While it is active, ``finalise_figure`` sets the title, subtitle
and the provenance footer (``bk_theme.footer``) on the design system's type scale
and reserves room for them, and ``direct_label`` writes labels in ink instead of the
line's colour (colour lives in marks, never in type). Choose mark colours through
``bk_theme`` roles (``bk.c("hl")``, ``bk.highlight_palette``, ``bk.palette``), never
hex. With a vendored style sheet active, every function behaves exactly as before.

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

import sys
import warnings
from pathlib import Path

import matplotlib as mpl
from matplotlib import colors as mpl_colors
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

    The vendored files must win over any system-installed font of the same
    family (Ubuntu's ``fonts-lato`` package ships a different Lato release with
    different metrics, which moves text and breaks the ``svg_sha256`` seals).
    ``findfont`` breaks score ties by list order and system fonts are listed
    first, so every same-family entry that is not a vendored file is dropped
    and the lookup caches are cleared.
    """
    manager = font_manager.fontManager
    vendored = sorted(_FONT_DIR.glob("Lato-*.ttf"))
    for ttf in vendored:
        manager.addfont(str(ttf))
    vendored_paths = {str(ttf.resolve()) for ttf in vendored}
    families = {
        entry.name for entry in manager.ttflist
        if str(Path(entry.fname).resolve()) in vendored_paths
    }
    manager.ttflist = [
        entry for entry in manager.ttflist
        if entry.name not in families or str(Path(entry.fname).resolve()) in vendored_paths
    ]
    # Private but long-standing (matplotlib >= 3.5) lru caches; guarded so a
    # release that renames them degrades to the old ordering, not a crash.
    for cache in (getattr(manager, "_findfont_cached", None),
                  getattr(font_manager, "_get_font", None)):
        if hasattr(cache, "cache_clear"):
            cache.cache_clear()


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


def use_bk_theme(mode: str = "light", **apply_kwargs):
    """Install the Braga design system v2.1 (``bk_theme.apply``) and return ``bk_theme``.

    ``mode`` is ``"light"`` or ``"dark"``; ``apply_kwargs`` pass through to
    ``bk_theme.apply`` (``scale``, ``grid``, ``fonts``). Needs the optional
    ``bk-viz`` package (Python >= 3.10)::

        pip install "bk-viz @ git+https://github.com/RafaelBraga-Kribitz/bk-viz@<pin>"

    A missing package raises ``ImportError`` naming that install line. Calling
    ``use_style`` afterwards switches back to a vendored style sheet.
    """
    try:
        import bk_theme
    except ImportError as exc:
        raise ImportError(
            "use_bk_theme() needs the optional bk-viz package (Python >= 3.10): "
            'pip install "bk-viz @ git+https://github.com/RafaelBraga-Kribitz/bk-viz@'
            'f4f90b2c76b8fed4f27caa9b29282336d779a3da"'
        ) from exc
    bk_theme.apply(mode, **apply_kwargs)
    return bk_theme


def _active_bk():
    """``bk_theme`` when its theme is the one installed in rcParams, else ``None``.

    Detected from the rcParams themselves (the figure ground is the design
    system's ``surface``), so a later ``use_style`` / ``plt.style.use`` switches the
    helpers back to their style-sheet behaviour without any bookkeeping.
    """
    bk = sys.modules.get("bk_theme")
    if bk is None:
        return None
    try:
        surface = bk.c("surface")
    except Exception:  # noqa: BLE001 - an unapplied or foreign module is "not active"
        return None
    if mpl_colors.same_color(mpl.rcParams["figure.facecolor"], surface):
        return bk
    return None


# Figure-space spacing for the bk header and footer, in CSS px (8px grid).
_BK_EDGE_PX = 16      # outer margin: left, right, above the title, below the footer
_BK_GAP_PX = 8        # title -> subtitle
_BK_HEAD_GAP_PX = 24  # header -> plot area
_BK_AXIS_ROOM_PX = 64  # footer rule -> plot area: tick labels and the x label


def _finalise_bk(bk, fig, *, title, source, subtitle, note, run_id, tag) -> Figure:
    """``finalise_figure`` on the Braga design system: finding title, provenance footer."""
    w_in, h_in = fig.get_size_inches()
    w_px, h_px = w_in * fig.dpi, h_in * fig.dpi
    left = _BK_EDGE_PX / w_px
    right = _BK_EDGE_PX / w_px
    span_px = w_px - 2 * _BK_EDGE_PX
    renderer = fig.canvas.get_renderer()

    def height_px(text) -> float:
        return text.get_window_extent(renderer).height

    cursor = _BK_EDGE_PX  # px from the top edge, measured on the rendered text
    title_fp = bk.font("display", "bold", "project")
    head = fig.text(left, 1 - cursor / h_px, bk.wrap_to_px(title, title_fp, span_px),
                    ha="left", va="top", color=bk.c("ink"),
                    linespacing=bk.LINE_HEIGHT["tight"], fontproperties=title_fp)
    cursor += height_px(head)
    if subtitle:
        sub_fp = bk.font("display", "regular", "body")
        cursor += _BK_GAP_PX
        sub = fig.text(left, 1 - cursor / h_px, bk.wrap_to_px(subtitle, sub_fp, span_px),
                       ha="left", va="top", color=bk.c("ink-2"),
                       linespacing=1.15, fontproperties=sub_fp)
        cursor += height_px(sub)
    top = 1 - (cursor + _BK_HEAD_GAP_PX) / h_px

    # Provenance strip: source (and run) left, epistemic tag right, note below.
    before_artists, before_texts = len(fig.artists), len(fig.texts)
    mono_px = bk.SIZE["mono"] * fig.dpi / 72
    bk.footer(fig, source=source, run_id=run_id, tag=tag, note=note,
              left=left, right=right, y=(_BK_EDGE_PX + mono_px) / h_px)
    rules = [a for a in fig.artists[before_artists:] if hasattr(a, "get_ydata")]
    rule_y = max(rules[0].get_ydata()) if rules else (_BK_EDGE_PX + 2 * mono_px) / h_px
    for text in fig.texts[before_texts:]:
        if text.get_window_extent(renderer).width > span_px:
            warnings.warn(
                f"finalise_figure: footer line {text.get_text()!r} is wider than the "
                "figure; widen the figure or shorten the source",
                stacklevel=3,
            )
    bottom = rule_y + _BK_AXIS_ROOM_PX / h_px
    if top > bottom:
        fig.subplots_adjust(top=top, bottom=bottom)
    return fig


def finalise_figure(
    fig: Figure,
    *,
    title: str,
    source: str,
    subtitle: str | None = None,
    note: str | None = None,
    run_id: str | None = None,
    tag: str | None = None,
) -> Figure:
    """Apply the DSX takeaway-title + mandatory-source finishing to ``fig``.

    ``title`` is the takeaway sentence; ``subtitle`` an optional clarifier beneath
    it; ``source`` the mandatory provenance line (rendered as a figure footnote —
    omitting it is a ``TypeError`` at call binding); ``note`` an optional caveat.
    Returns the mutated ``fig``.

    With the Braga design system active (``use_bk_theme``), the title is set on the
    system's type scale and wrapped to the figure, the subtitle in ``ink-2``, and the
    source line becomes the ``bk_theme.footer`` provenance strip, which also carries
    the optional ``run_id`` and epistemic ``tag`` (``VERIFIED``, ``CALIBRATED``,
    ``SIMULATED``, ``ASSUMED``, ``ILLUSTRATIVE``); the plot area's top and bottom
    are set to clear them. Under a vendored style sheet ``run_id`` and ``tag`` are
    ignored and the output is unchanged.
    """
    bk = _active_bk()
    if bk is not None:
        return _finalise_bk(bk, fig, title=title, source=source, subtitle=subtitle,
                            note=note, run_id=run_id, tag=tag)
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
    color_from_line: bool | None = None,
    x_offset: float = 6.0,
    fontsize: float | None = None,
) -> list[Text]:
    """Label each line at its terminal (rightmost) data point instead of a legend.

    ``labels`` optionally maps a line's label to display text (default uses
    ``line.get_label()``); internal matplotlib labels (``_child0`` …) are skipped.
    Colour is inherited from the line when ``color_from_line``. ``x_offset`` is in
    typographic points. Returns the created ``Text`` artists.

    ``color_from_line`` defaults to ``None``: the line's colour under a vendored
    style sheet (the previous default, ``True``), and ``ink`` in BKribitz Mono under
    the Braga design system, where colour lives in marks, never in type.
    """
    bk = _active_bk()
    if color_from_line is None:
        color_from_line = bk is None
    if bk is not None:
        fontprops = bk.font("mono", "medium", "mono")
        if fontsize is not None:
            fontprops.set_size(fontsize)
        font_kwargs = {"fontproperties": fontprops}
    else:
        font_kwargs = {"fontsize": fontsize}
    ink = bk.c("ink") if bk is not None else None
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
        color = line.get_color() if color_from_line else ink
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
            clip_on=False,
            **font_kwargs,
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
