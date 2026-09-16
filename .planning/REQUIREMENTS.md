# Requirements

**Current milestone:** v2.7 Figure Pipeline (Phases 31–34) — see below.
**Shipped:** v1.1.0–v1.5.0 (Phases 1–5, archived); v2.0.0 DSX Validity Frame
(Phases 6–12, `.planning/milestones/v2.0.0-REQUIREMENTS.md`); v2.2 Analytic Surface
(Phases 13–16, `v2.2-REQUIREMENTS.md`); v2.3 Test Catalog (Phases 17–20,
`v2.3-REQUIREMENTS.md`); v2.4 Visual Excellence (Phases 21–24,
`v2.4-REQUIREMENTS.md`); v2.6 Exploration Depth and Backlog Evidence (Phases 25–30,
`v2.6-REQUIREMENTS.md`); v2.4.1, v2.5.0 and v2.6.1 shipped interactively
(`.planning/MILESTONES.md`).

**Defined:** 2026-09-16
**Core Value:** Gate analytical work on validity before the data is touched.

**Scope source:** `.planning/research/V2.7-SCOPE.md` (2026-09-16) — written against
the live tree at `e04966e`: the measured nine-chart miss with per-chart defects, the
four verified causes at file:line, per-phase content, ordering, contingency, the
critique register and the out-of-scope list. Opened by operator direction after the
rendered smoke test of 2026-09-11.

**Binding constraints:** D-01 (stdlib gate path — the renderer is analyst-side and
matplotlib stays FORBIDDEN on the gate path), D-02 (gates adjudicate declarations and
hermetic artifacts, never compute), D-05 (citation + structural criterion per minted
check), D-06 (additive codes only; live catalogue re-verified at **279** before this
milestone opened), D-13 (evidence phases measure first; a case the gate already
catches closes the phase with no mint), v2.7-01 (a figure-quality milestone opens only
on a rendered, viewed miss), v2.7-02 (quality is a property of code the agent calls).

---

## Phase 31 — Deterministic mark resolver

- [ ] **REQ-P31-01** `dsx charts` resolves a declared data signature to exactly one
  mark. Given input type (IT id or coarse family), relationship, category count,
  longest category label length, series count, has-time and has-interval, a stdlib
  table returns one mark. The existing admissible-set behaviour is unchanged —
  `permitted()` keeps returning its sorted set, and the resolver is additive.

- [ ] **REQ-P31-02** The resolver returns render defaults alongside the mark:
  orientation, sort order, baseline rule, label mode (direct / legend / none),
  emphasis mode (hero / uniform), and the uncertainty mark where the relationship is
  `uncertainty`. These are the values Phase 32's renderer consumes; they are data,
  not prose.

- [ ] **REQ-P31-03** Every resolver row carries a source in the table itself, and no
  row states a rule that no source supports. Sources available in the tree or in
  hand: this project's own `references/chart-selection.md` relationship table;
  Cleveland & McGill's six tied ranks (already corrected in this project — six ranks
  with ties, never a strict seven); Wilke §5.6 for `error_bars` as the uncertainty
  default; the operator's Chart_Audit_Framework branch cited **by commit `c69dbf3`**,
  never as `main`, for card thresholds and the ranking rule.

- [ ] **REQ-P31-04** The resolver is total and deterministic over the declared
  vocabulary, proven by test: every (input type × relationship) pair for which
  `permitted()` returns a non-empty set resolves to a mark in that set, and identical
  inputs return identical output across runs. One test per table row.

- [ ] **REQ-P31-05** `dsx charts <shape> --relationship <rel> --resolve` prints the
  chosen mark, its render defaults and the rule row that produced it, so the choice is
  inspectable rather than opaque. Exit codes keep the existing contract.

- [ ] **REQ-P31-06** The resolver imports no matplotlib and no third-party package;
  `tests/test_gate_path_hermetic.py` continues to pass unchanged.

## Phase 32 — The renderer

- [ ] **REQ-P32-01** `render(spec, data, *, style=…) -> Figure` builds a figure from
  its declaration, lives in `templates/` beside `dsx_plotstyle.py` (outside the
  hermetic `dsx/` closure), and is imported by no `GATE_PROFILES` module.

- [ ] **REQ-P32-02** A layout engine owns the canvas: named canvas sizes, reserved
  bands for title / subtitle / plot / footer, and titles wrapped by **measured**
  width so a long takeaway sentence cannot be clipped. Proven against the smoke
  test's own five clipping titles.

- [ ] **REQ-P32-03** `units` and `subtitle` are keyword-only parameters with no
  default, so omitting either is a `TypeError` at call binding — the same
  signature-property pattern `source=` already uses for `DSX-VIZ-062`. Zero of the
  nine smoke-test charts carried units; this makes that state unreachable.

- [ ] **REQ-P32-04** The renderer is correct by construction on the defects the smoke
  test exposed: categorical axes get categorical ticks (no 0.5-step rank or category
  axes), comparison bars sort by value and orient as the resolver directs, bar and
  area charts start at zero, and numbers are formatted (thousands, percent,
  currency) rather than raw.

- [ ] **REQ-P32-05** Editorial marks exist as callable functions, not prose: direct
  labels at series ends with collision avoidance, hero-series emphasis with the
  remainder greyed, declared annotations attached to named data points, and labelled
  reference lines.

- [ ] **REQ-P32-06** Determinism is preserved end to end: the GA-3 recipe is
  unchanged, `save_deterministic` remains the only writer, `dsx seal` remains the only
  hashing authority, and a double-render hash-equality test covers every rendered
  reference figure.

- [ ] **REQ-P32-07** No layout constant is modelled on a source whose licence has not
  been read first-hand. The BBC `bbplot` cookbook copy in the operator's library
  carries no licence file; if the upstream licence cannot be read, the band layout is
  derived from the Economist and FiveThirtyEight descriptions plus our own
  measurement, and the record says so — the HQ-27 / HQ-33 standard applied to layout.

- [ ] **REQ-P32-08** `sankey` is removed from the representative flow set and marked
  reference-only in `references/chart-catalog.md` with the reason recorded
  (matplotlib's built-in is an arrow diagram, not a publishable flow ribbon). The
  catalogue row count change is accounted for in the invariant test.

## Phase 33 — The pixel check

- [ ] **REQ-P33-01** Stdlib predicates check the **rendered artifact**, parsing the
  sealed SVG as XML: nothing clipped beyond the canvas box, no two text elements
  overlapping, a subtitle element present, a unit token present in the subtitle or an
  axis label. No matplotlib, no third-party dependency, no live data.

- [ ] **REQ-P33-02** Each predicate's threshold is an observable condition traceable
  to a named source, with the operator's Chart_Audit_Framework `rules/scoring-anchors.md`
  cited by commit `c69dbf3` — clipped-or-colliding and legend-sole-decoder-above-six
  are its stated caps, and the ranking is its stated floor.

- [ ] **REQ-P33-03** The nine smoke-test charts of 2026-09-11 ship as evidence
  fixtures with their per-chart defect list, and the same nine relationships render
  through the new pipeline as golden SVGs that are diffed on change.

- [ ] **REQ-P33-04** Every candidate check is measured against the corpus at all four
  gate points **before** it is designed (D-13). A case the gate already catches closes
  with no mint, and the measurement is recorded as a `VERDICT:` line in a
  `33-MEASUREMENT.md` the orchestrator re-runs rather than trusts.

- [ ] **REQ-P33-05** Any minted code is additive from 279, carries a D-05 citation
  and a structural criterion in its docstring, and names a known-bad fixture as its
  declared target in the same commit (the v2.5-01 family rule). Zero mints is a valid
  outcome and must not be talked into a mint.

## Phase 34 — Rewiring and calibration (terminal)

- [ ] **REQ-P34-01** `references/chart-snippets.md` is rewritten so every snippet
  calls the renderer, passes units and subtitle, and shows one annotation; the routing
  test is extended so no snippet hand-rolls what the renderer owns.

- [ ] **REQ-P34-02** `skills/dsx-visualize/SKILL.md` instructs resolve → render →
  seal → check, naming `dsx charts --resolve` explicitly, and
  `agents/dsx-viz-critic.md` gains a step that **opens the rendered PNG** and judges
  what a predicate cannot, after the pixel check is clean.

- [ ] **REQ-P34-03** Calibration is re-baselined against the changed surface: catch
  rate over the known-bad corpus, false-positive rate over the good-control corpus
  with its one-sided bound stated, the new figure cases classified, and the docs
  re-pinned to the live corpus by the existing agreement test. Zero mints (terminal
  phase, as Phases 12 / 20 / 30).

---

## Future Requirements (v2.8 candidates — deferred, entry conditions unchanged)

- `SEED-001` E-27 … E-31 — deeper exploration protocol items.
- `SEED-002` residue — a producer-side `parse_health` block (a gate reading it stays
  a separate D-02/D-06 decision).
- `SEED-003` — analyst conduct, notebook execution integrity, share-vs-risk quantity
  kinds (six gate candidates, all D-13 entry-conditioned).
- `SEED-004` — concurrent `DECISIONS.jsonl` writers (dormant until a scope actually
  races two gates against one root).
- Good-control corpus growth past 15 specs — the false-positive denominator is thin
  (one-sided 95% bound ≈0.181 on 0/15). Lost to v2.7 on precedence, not merit.
- EDA brief §6.5 items 1–6 — paradigm-paired items wait for their mirrors (D-12a).
- A real Sankey ribbon implementation — if a consumer ever needs one.

## Out of Scope

| Item | Reason |
|---|---|
| A gate that renders | Breaks D-01; the pixel check reads the sealed SVG as a hermetic artifact instead |
| Imitating vendor identity (typefaces, logos, proprietary palettes, bespoke pieces) | General chart quality is the target; Econ Sans stays unvendored, `ggthemes` (GPL) and `RDeconomist` (GPL-3) stay unread for code, unlicensed style guides stay cited-never-copied |
| Interactive or web output (plotly, HTML) | SVG and PNG only — the sealed-artifact contract assumes a static file |
| Geographic marks (`choropleth`, `symbol_map`, `cartogram`) | Need a geo dependency; the resolver may name them, the renderer does not build them |
| Citing the Tableau 538 article or Tim van Schaick's Economist article | Both returned HTTP 403 with no local copy — unread, therefore uncitable |

## Traceability

| Requirement | Phase | Status |
|---|---|---|
| REQ-P31-01 … REQ-P31-06 | Phase 31 | Pending |
| REQ-P32-01 … REQ-P32-08 | Phase 32 | Pending |
| REQ-P33-01 … REQ-P33-05 | Phase 33 | Pending |
| REQ-P34-01 … REQ-P34-03 | Phase 34 | Pending |

**Coverage:** 22 requirements total; mapped to phases at roadmap creation; 0 unmapped.

---
*Requirements defined: 2026-09-16*
*Last updated: 2026-09-16 at milestone open*
