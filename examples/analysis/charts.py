# Chart generators for the known-good onboarding-activation exemplar (Phase 24, REQ-P24-01).
#
# This is the ONLY matplotlib importer in the repo and is deliberately NOT a gate
# module — it must never be imported on the hermetic gate path
# (tests/test_gate_path_hermetic.py keeps ``matplotlib`` in FORBIDDEN). It renders
# all three exemplar figures on the Braga design system v2.1 (bk-viz ``bk_theme``,
# D-053: IBCS roles, one highlight per chart, labels in ink, BKribitz type) through
# templates/dsx_plotstyle.py (use_bk_theme + GA-2 finalise_figure with a MANDATORY
# source kw + save_deterministic, which writes byte-reproducible SVG and never
# hashes — dsx seal remains the single hashing authority). Colours come only from
# bk_theme roles; there is no hex literal here. The point estimate and 95% CI are anchored
# to results.tests[0] in good-ANALYSIS-SPEC.yaml (effect 0.024, CI [0.0101, 0.0384]);
# no headline number is invented here.
#
# Re-rendering the two pre-existing figures intentionally changes their bytes; that is
# exactly why every seal in the spec is refreshed via ``dsx seal`` after this runs.

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless, deterministic — no display backend

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Repo root is three levels up: examples/analysis/charts.py -> repo root.
REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "examples" / "figures"
THEME_MODE = "light"  # the committed figures are the light render

# templates/ is not a package; import the analyst helper by path.
sys.path.insert(0, str(REPO_ROOT / "templates"))
import bk_theme as bk  # noqa: E402  (bk-viz, the Braga design system's chart theme)
from dsx_plotstyle import (  # noqa: E402
    direct_label,
    finalise_figure,
    save_deterministic,
    use_bk_theme,
)

# ── Ground truth (results.tests[0], good-ANALYSIS-SPEC.yaml) ──────────────────
BASELINE_RATE = 0.310          # design.baseline_rate (control activation)
UPLIFT = 0.024                 # results.tests[0].effect
TREATMENT_RATE = BASELINE_RATE + UPLIFT
CI_LOW, CI_HIGH = 0.0101, 0.0384   # results.tests[0].ci -> 1.0pp .. 3.8pp
DECISION_FLOOR = 0.010         # decision.decision_rule: CI lower bound > +1.0pp
SOURCE = "warehouse.fct_signups, 2026-06-01..06-14"
RUN_ID = "2026-06-readout"     # visuals[].run_id in good-ANALYSIS-SPEC.yaml

# Illustrative but deterministic daily series (control flat ~31%, treatment opens the
# gap on day 2 and holds it). The trend figure has always been illustrative — the two
# original SVGs were hand-made placeholders; the load-bearing numbers are the point
# estimate and CI, carried by the bar and uncertainty figures.
DAYS = list(range(1, 15))
CONTROL_DAILY = [0.305, 0.308, 0.310, 0.309, 0.311, 0.312, 0.310,
                 0.311, 0.313, 0.312, 0.311, 0.310, 0.312, 0.311]
TREATMENT_DAILY = [0.307, 0.318, 0.325, 0.329, 0.332, 0.333, 0.334,
                   0.335, 0.334, 0.336, 0.335, 0.334, 0.335, 0.334]


def apply_theme() -> None:
    """Start from matplotlib defaults and install the Braga design system.

    Resetting first makes the render independent of whatever style the caller had
    active, so ``main()`` and the regeneration test draw the same bytes.
    """
    matplotlib.rcdefaults()
    use_bk_theme(THEME_MODE)


def _pct(ax) -> None:
    """Format the y-axis as whole-percent tick labels."""
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _pos: f"{v * 100:.0f}%"))


def render_activation_uplift() -> Path:
    """Point-estimate uplift bar: control vs treatment activation (y starts at zero)."""
    fig, ax = plt.subplots(figsize=(8.0, 5.4))
    arms = ["control", "treatment"]
    # The treatment bar is the one mark that earned the highlight; control is structure.
    ax.bar(arms, [BASELINE_RATE, TREATMENT_RATE],
           color=bk.highlight_palette(arms, highlight="treatment"))
    ax.set_ylim(0, 0.40)
    ax.set_ylabel("7-day activation")
    _pct(ax)
    finalise_figure(
        fig,
        title="Treatment activates 2.4pp higher than control",
        subtitle="7-day activation rate by arm",
        source=SOURCE,
        run_id=RUN_ID,
    )
    out = save_deterministic(fig, FIG_DIR / "activation_uplift.svg")
    plt.close(fig)
    return out


def render_daily_trend() -> Path:
    """Daily activation trend by arm; lines labelled directly (no legend)."""
    fig, ax = plt.subplots(figsize=(8.7, 5.4))
    control_color, treatment_color = bk.highlight_palette(
        ["control", "treatment"], highlight="treatment"
    )
    ax.plot(DAYS, CONTROL_DAILY, label="control", color=control_color)
    ax.plot(DAYS, TREATMENT_DAILY, label="treatment", color=treatment_color)
    ax.set_xlabel("day since signup")
    ax.set_ylabel("7-day activation")
    ax.set_xlim(1, 15.6)
    _pct(ax)
    # whole-percent ticks: the formatter rounds to 0 dp, so finer steps would repeat
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    direct_label(ax)  # labels in ink: the line carries the colour, not the word
    finalise_figure(
        fig,
        title="The gap opens on day 2 and holds — not a novelty effect",
        subtitle="Daily 7-day activation rate by arm",
        source=SOURCE,
        run_id=RUN_ID,
    )
    fig.subplots_adjust(right=0.84)  # room for the direct labels
    out = save_deterministic(fig, FIG_DIR / "daily_activation_trend.svg")
    plt.close(fig)
    return out


def render_uplift_ci() -> Path:
    """Uncertainty figure: the uplift point estimate with its real 95% CI error bars."""
    fig, ax = plt.subplots(figsize=(8.0, 5.4))
    yerr = [[UPLIFT - CI_LOW], [CI_HIGH - UPLIFT]]  # asymmetric = actual CI arms
    ax.errorbar(
        [0], [UPLIFT], yerr=yerr, fmt="o", capsize=6, markersize=8, linewidth=1.5,
        color=bk.c("hl"),  # the estimate and its interval: the one highlighted mark
    )
    # The decision floor is a threshold: a mid hairline, labelled in ink-2 (mid is
    # never text).
    ax.axhline(DECISION_FLOOR, linestyle="--", linewidth=bk.HAIRLINE_PT, color=bk.c("mid"))
    ax.text(0.18, DECISION_FLOOR, "+1.0pp decision floor", va="bottom", ha="left",
            color=bk.c("ink-2"), fontproperties=bk.font("mono", "regular", "mono"))
    ax.axhline(0.0, linewidth=bk.HAIRLINE_PT, color=bk.c("ink"))
    ax.set_xlim(-0.6, 0.9)
    ax.set_xticks([0])
    ax.set_xticklabels(["activation uplift"])
    ax.set_ylim(0, 0.045)
    ax.set_ylabel("uplift (percentage points)")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _pos: f"{v * 100:.1f}")
    )
    finalise_figure(
        fig,
        title="The 2.4pp uplift's 95% CI is 1.0 to 3.8pp",
        subtitle="Activation uplift with 95% confidence interval",
        source=SOURCE,
        note="CI clears the +1.0pp decision floor",
        run_id=RUN_ID,
    )
    out = save_deterministic(fig, FIG_DIR / "activation_uplift_ci.svg")
    plt.close(fig)
    return out


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_theme()
    paths = [render_activation_uplift(), render_daily_trend(), render_uplift_ci()]
    for p in paths:
        print(f"wrote {p.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
