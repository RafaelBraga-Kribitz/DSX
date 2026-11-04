"""Check modules. Each exposes a ``check(...) -> Report`` and owns a code prefix.

    design        DSX-EXP-*, DSX-CAU-*   experiment power, SRM, units, identification
    stats         DSX-STA-*              test selection, assumptions, reporting contract
    ml            DSX-ML-*               leakage, splits, metric choice, baselines
    metrics       DSX-MET-*, DSX-SQL-*   definitions, reconciliation, Simpson's, SQL lint
    claims        DSX-CLM-*              causal language, evidence, generalisation
    viz           DSX-VIZ-*              encoding correctness, proportionality, uncertainty
    repro         DSX-REP-*              seeds, environment, data identity, entrypoint, repro_lock
    dq            DSX-DQ-*               profile assertions vs DATA-PROFILE artifact
    coherence     DSX-COH-*              question ↔ claim ↔ decision agreement
    figures       DSX-FIG-*              artifact paths and svg_sha256 seals
    smells        DSX-SMELL-*            declaration-based plot-construction smells
    narrative     DSX-NAR-*              deliverable path, claim⊆narrative, forbidden wording
    code          DSX-CODE-*             fit-before-split entrypoint scan
    decision      DSX-DEC-*              structured decision.replay vs results.tests
    chart_review  DSX-CRV-*              CHART-REVIEW.md conformance

The frame families — paradigm (DSX-PAR-*), val (DSX-VAL-*), interference
(DSX-INT-*), prereg (DSX-PRE-*) and admissibility (DSX-ADM-*) — live in
``dsx/frame/`` (index: ``dsx/frame/__init__.py``), not here, and are
registered beside these in the same ``dsx.cli.CHECKS`` table.

Signatures are NOT uniform; each takes only what it reads:

    check(spec)                                   stats, ml, metrics, viz, smells
    check(spec, *, strict=False)                  design, coherence
    check(spec, phase_dir=None)                   dq, code
    check(spec, phase_dir=None, *, strict=False)  claims, figures, repro, chart_review
    check(spec, *, gate_point=None)               decision
    check(spec, phase_dir=None, *, gate_point=None)  narrative

``dsx.cli.run_checks`` dispatches every family through the ``CheckEntry``
adapters in ``dsx.cli.CHECKS``, which map one per-run ``CheckContext``
(phase_dir, resolve root, strict, gate_point, reconcile_trail) onto each
module's real signature. Adding a check means adding its ``CHECKS`` entry.
"""

from . import (
    chart_review,
    claims,
    code,
    coherence,
    decision,
    design,
    dq,
    figures,
    metrics,
    ml,
    narrative,
    repro,
    smells,
    stats,
    viz,
)

__all__ = [
    "chart_review",
    "claims",
    "code",
    "coherence",
    "decision",
    "design",
    "dq",
    "figures",
    "metrics",
    "ml",
    "narrative",
    "repro",
    "smells",
    "stats",
    "viz",
]
