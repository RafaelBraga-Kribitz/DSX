# Roadmap: gsd-dsx

**Active:** v2.7 Figure Pipeline — Phases 31–34 (opened 2026-09-16)
**Shipped:** v2.6 Exploration Depth and Backlog Evidence — Phases 25–30 (2026-09-10); v2.4 Visual Excellence — Phases 21–24 (2026-09-03); v2.3 Test Catalog — Phases 17–20 (2026-09-02); v2.2 Analytic Surface — Phases 13–16 (2026-08-29); v2.0.0 DSX Validity Frame — Phases 6–12 (2026-08-28); v1.1.0–v1.5.0 — Phases 1–5

> **Milestone name vs. release tag.** The DSX Validity Frame is named **v2.0.0**
> throughout planning (its archives are `v2.0.0-ROADMAP.md`, `v2.0.0-REQUIREMENTS.md`,
> `v2.0.0-MILESTONE-AUDIT.md`), but it ships under the git tag **`v2.1.0`**. The
> `v2.0.0` tag was already published on origin (2026-08-10) against an earlier,
> partial merge of this same branch, and moving a published ref would silently break
> anyone who had already fetched it — so the completed milestone got the next free
> tag instead. The follow-on **Analytic Surface** milestone was correspondingly
> renamed from v2.1 to **v2.2** so it does not collide with that release tag. Its
> milestone name and release tag match: **v2.2.0**.

## Milestones

- ✅ **v1.1.0–v1.5.0** — Phases 1–5 (shipped incrementally; ten quality dimensions gated where decidable)
- ✅ **v2.0.0 DSX Validity Frame** — Phases 6–12 (shipped 2026-08-28, tag `v2.1.0`)
- ✅ **v2.2 Analytic Surface** — Phases 13–16 (shipped 2026-08-29, tag `v2.2.0`)
- ✅ **v2.3 Test Catalog** — Phases 17–20 (shipped 2026-09-02, tag `v2.3.0`)
- ✅ **v2.4 Visual Excellence** — Phases 21–24 (shipped 2026-09-03, tag `v2.4.0`)
- ✅ **v2.6 Exploration Depth and Backlog Evidence** — Phases 25–30 (shipped 2026-09-10, tag `v2.6.0`)
- 🔄 **v2.7 Figure Pipeline** — Phases 31–34 (opened 2026-09-16; ships as tag `v2.7.0`)

## Phases

<details>
<summary>✅ v1.1.0–v1.5.0 (Phases 1–5) — SHIPPED</summary>

- [x] Phase 1: DQ + Evidence + Coherence (v1.1.0)
- [x] Phase 2: Viz proof + plot construction (v1.2.0)
- [x] Phase 3: Storytelling + code reality (v1.3.0)
- [x] Phase 4: Analytical logic depth + stats extensions (v1.4.0)
- [x] Phase 5: Chart review + suppressions (v1.5.0)

</details>

<details>
<summary>✅ v2.0.0 DSX Validity Frame (Phases 6–12) — SHIPPED 2026-08-28</summary>

Phase detail (plan counts, completion dates) is recorded above.
`.planning/milestones/v2.0.0-ROADMAP.md` is the milestone's pre-execution scoping
snapshot, not a post-completion archive.

- [x] Phase 6: Contract extension, decision record, paradigm manifest (M1) — 13/13 plans — completed 2026-08-10
- [x] Phase 7: Validity frame checks (`DSX-VAL-*`) (M2a) — 8/8 plans — completed 2026-08-20
- [x] Phase 8: Interference, triggering, stability (`DSX-INT-*`) (M2b) — 10/10 plans — completed 2026-08-14
- [x] Phase 9: Monitoring discipline, symmetric (`DSX-PAR-*`) (M2c) — 7/7 plans — completed 2026-08-13
- [x] Phase 10: Pre-registered inference plan (`DSX-PRE-*`) (M3) — 6/6 plans — completed 2026-08-20
- [x] Phase 11: Frequentist admissibility adjudicator (`DSX-ADM-*`) (M4) — 8/8 plans — completed 2026-08-28
- [x] Phase 11.1: Generated-pipeline reality (INSERTED) — 8/8 plans — completed 2026-08-21
- [x] Phase 11.1.1: Detection-code hardening (INSERTED) — 7/7 plans — completed 2026-08-22
- [x] Phase 11.2: Prescriptive claim layer (INSERTED) — 8/8 plans — completed 2026-08-26
- [x] Phase 11.3: Reporting completeness and missing-data discipline (INSERTED) — 7/7 plans — completed 2026-08-27
- [x] Phase 12: Calibration (M5, terminal) — 7/7 plans — completed 2026-08-27

</details>

<details>
<summary>✅ v2.2 Analytic Surface (Phases 13–16) — SHIPPED 2026-08-29</summary>

Phase detail (plan counts, completion dates) is recorded above.
`.planning/milestones/v2.2-ROADMAP.md` is the milestone's pre-execution scoping
snapshot (not a post-completion archive); `.planning/milestones/v2.2-phases/` holds
the individual phase plans. Milestone audit `passed`
(`.planning/milestones/v2.2-MILESTONE-AUDIT.md`): 23/23 requirements, 4/4
phases verified, 10/10 cross-phase integration seams, Nyquist compliant, 0
unsatisfied/orphaned. Finding catalogue grew 256 → 260 (additive; the frozen
Phase-12 snapshot at 256 was never mutated).

- [x] Phase 13: Task playbooks that fill the spec (skill-only) — 5/5 plans — completed 2026-08-28
- [x] Phase 14: Compounding and data onboarding — 5/5 plans — completed 2026-08-28
- [x] Phase 15: CUPED and BI declaration checks (`DSX-EXP-070`, `DSX-MET-021`) — 6/6 plans — completed 2026-08-29
- [x] Phase 16: Re-run verification off the gate path (`DSX-REP-060`, `DSX-REP-061`) — 4/4 plans — completed 2026-08-29

</details>

<details>
<summary>✅ v2.3 Test Catalog (Phases 17–20) — SHIPPED 2026-09-02</summary>

Phase detail (plan counts, completion dates) is recorded above.
`.planning/milestones/v2.3-ROADMAP.md` is the milestone's pre-execution scoping
snapshot (not a post-completion archive); `.planning/milestones/v2.3-phases/` holds
the individual phase plans. Milestone audit `passed`
(`.planning/milestones/v2.3-MILESTONE-AUDIT.md`): 22/22 requirements, 4/4
phases verified, 5/5 cross-phase integration seams, Nyquist compliant, 0
unsatisfied/orphaned. Finding catalogue grew 260 → 275 (additive; both frozen
snapshots — Phase-12 at 256, v2.2's set — never mutated). 27 D-05 citations
independently re-verified against primary sources at close-out; 7 corrected.

- [x] Phase 17: Foundation — repairs and spec vocabulary — 3/3 plans — completed 2026-09-01
- [x] Phase 18: Correlation, association and agreement (`DSX-STA-050`…`062`) — 2/2 plans — completed 2026-09-02
- [x] Phase 19: RM, trend, categorical, resampling, post-hoc (`DSX-STA-070`…`122`) — 2/2 plans — completed 2026-09-02
- [x] Phase 20: Calibration and reporting close — 4/4 plans — completed 2026-09-02

</details>

<details>
<summary>✅ v2.4 Visual Excellence (Phases 21–24) — SHIPPED 2026-09-03</summary>

Phase detail (plan counts, completion dates) is recorded above.
`.planning/milestones/v2.4-ROADMAP.md` is the milestone's pre-execution scoping
snapshot (not a post-completion archive); `.planning/milestones/v2.4-phases/` holds
the individual phase plans. Milestone audit `passed`
(`.planning/milestones/v2.4-MILESTONE-AUDIT.md`): 16/16 requirements, 4/4
phases verified, 5/5 cross-phase integration seams, Nyquist compliant, 0
unsatisfied/orphaned. Finding catalogue grew 275 → 276 (additive; all three
frozen snapshots — Phase-12 at 256, v2.2's, v2.3's — never mutated). 13 D-05
citations independently re-verified against primary sources at close-out; 7
corrected, including a perceptual-ranking claim unsupported by either cited
paper. A separate license-audit round caught a mislabeled style palette
(claimed Apache-2.0/Urban Institute; actually GPL-3.0-disputed with 3 of 6
colors being unattributed ColorBrewer stops) before ship.

- [x] Phase 21: Viz vocabulary reconciliation — 1/1 plan — completed 2026-09-03
- [x] Phase 22: Catalog spine, uncertainty family, selection heuristic — 4/4 plans — completed 2026-09-03
- [x] Phase 23: Style and snippet layer — 3/3 plans — completed 2026-09-03
- [x] Phase 24: Portfolio exemplar and viz calibration — 3/3 plans — completed 2026-09-03

</details>

<details>
<summary>✅ v2.6 Exploration Depth and Backlog Evidence (Phases 25–30) — SHIPPED 2026-09-10</summary>

- [x] Phase 25: Hermetic profile depth (4/4 plans; zero-mint) — completed 2026-09-07
- [x] Phase 26: Per-skill read contracts (4/4 plans; skill-only, zero-mint) — completed 2026-09-07
- [x] Phase 27: Evidence case — feature-origin-only leak (2/2 plans; LIVE MISS → `DSX-ML-034`, attribution-only) — completed 2026-09-07
- [x] Phase 28: Evidence case — magnitude no test computed (2/2 plans; LIVE MISS → `DSX-CLM-034`, attribution-only) — completed 2026-09-08
- [x] Phase 29: Evidence case — subgroup harm under a prescriptive recommendation (2/2 plans; LIVE MISS → `DSX-COH-041`, the corpus's first `kind: target` — a real catch) — completed 2026-09-10
- [x] Phase 30: Calibration re-baseline (2/2 plans; miss 5/5, FPR 0/15 with its one-sided 95% bound ≈0.181 stated; zero-mint 279→279) — completed 2026-09-10

Phase detail is archived at `.planning/milestones/v2.6-ROADMAP.md`; requirements
(18/18 Met) at `.planning/milestones/v2.6-REQUIREMENTS.md`; the milestone audit
(`passed`) at `.planning/milestones/v2.6-MILESTONE-AUDIT.md`; the ceremony's own
ledger and queue at `.planning/milestones/v2.6-LOOP-LEDGER*.md` /
`v2.6-HUMAN-QUEUE.md`.

</details>

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. DQ + Evidence + Coherence | v1.1.0 | — | Complete | v1.1.0 |
| 2. Viz proof + plot construction | v1.2.0 | — | Complete | v1.2.0 |
| 3. Storytelling + code reality | v1.3.0 | — | Complete | v1.3.0 |
| 4. Analytical logic depth + stats extensions | v1.4.0 | — | Complete | v1.4.0 |
| 5. Chart review + suppressions | v1.5.0 | — | Complete | v1.5.0 |
| 6. Contract extension, decision record, paradigm manifest | v2.0.0 | 13/13 | Complete | 2026-08-10 |
| 7. Validity frame checks (`DSX-VAL-*`) | v2.0.0 | 8/8 | Complete | 2026-08-20 |
| 8. Interference, triggering, stability (`DSX-INT-*`) | v2.0.0 | 10/10 | Complete | 2026-08-14 |
| 9. Monitoring discipline, symmetric (`DSX-PAR-*`) | v2.0.0 | 7/7 | Complete | 2026-08-13 |
| 10. Pre-registered inference plan (`DSX-PRE-*`) | v2.0.0 | 6/6 | Complete | 2026-08-20 |
| 11. Frequentist admissibility adjudicator (`DSX-ADM-*`) | v2.0.0 | 8/8 | Complete | 2026-08-28 |
| 11.1 Generated-pipeline reality | v2.0.0 | 8/8 | Complete | 2026-08-21 |
| 11.1.1 Detection-code hardening | v2.0.0 | 7/7 | Complete | 2026-08-22 |
| 11.2 Prescriptive claim layer | v2.0.0 | 8/8 | Complete | 2026-08-26 |
| 11.3 Reporting completeness | v2.0.0 | 7/7 | Complete | 2026-08-27 |
| 12. Calibration | v2.0.0 | 7/7 | Complete | 2026-08-27 |
| 13. Task playbooks that fill the spec | v2.2 | 5/5 | Complete | 2026-08-28 |
| 14. Compounding and data onboarding | v2.2 | 5/5 | Complete | 2026-08-28 |
| 15. CUPED and BI declaration checks | v2.2 | 6/6 | Complete | 2026-08-29 |
| 16. Re-run verification (off the gate path) | v2.2 | 4/4 | Complete | 2026-08-29 |
| 17. Foundation — repairs and spec vocabulary | v2.3 | 3/3 | Complete | 2026-09-01 |
| 18. Correlation, association and agreement | v2.3 | 2/2 | Complete | 2026-09-02 |
| 19. RM, trend, categorical, resampling, post-hoc | v2.3 | 2/2 | Complete | 2026-09-02 |
| 20. Calibration and reporting close | v2.3 | 4/4 | Complete | 2026-09-02 |
| 21. Viz vocabulary reconciliation | v2.4 | 1/1 | Complete | 2026-09-03 |
| 22. Catalog spine, uncertainty family, selection heuristic | v2.4 | 4/4 | Complete | 2026-09-03 |
| 23. Style and snippet layer | v2.4 | 3/3 | Complete | 2026-09-03 |
| 24. Portfolio exemplar and viz calibration | v2.4 | 3/3 | Complete | 2026-09-03 |
| 25. Hermetic profile depth | v2.6 | 4/4 | Complete | 2026-09-07 |
| 26. Per-skill read contracts | v2.6 | 4/4 | Complete | 2026-09-07 |
| 27. Evidence case — feature-origin-only leak | v2.6 | 2/2 | Complete | 2026-09-07 |
| 28. Evidence case — magnitude no test computed | v2.6 | 2/2 | Complete | 2026-09-08 |
| 29. Evidence case — subgroup harm (prescriptive) | v2.6 | 2/2 | Complete | 2026-09-10 |
| 30. Calibration re-baseline | v2.6 | 2/2 | Complete | 2026-09-10 |

**v2.0.0 totals:** 11 phases, 89 plans, 208 tasks. Milestone audit `passed` (`.planning/milestones/v2.0.0-MILESTONE-AUDIT.md`); all 11 phases verified and Nyquist-validated; cross-phase integration INTEGRATED.

**v2.2 totals:** 4 phases, 20 plans. Milestone audit `passed` (`.planning/milestones/v2.2-MILESTONE-AUDIT.md`); all 4 phases verified and Nyquist-validated; cross-phase integration INTEGRATED (10/10 seams).

**v2.3 totals:** 4 phases, 11 plans. Milestone audit `passed` (`.planning/milestones/v2.3-MILESTONE-AUDIT.md`); all 4 phases verified and Nyquist-validated; cross-phase integration INTEGRATED (5/5 seams).

**v2.4 totals:** 4 phases, 11 plans. Milestone audit `passed` (`.planning/milestones/v2.4-MILESTONE-AUDIT.md`); all 4 phases verified and Nyquist-validated; cross-phase integration INTEGRATED (5/5 seams).

**v2.6 totals:** 6 phases, 16 plans. Milestone audit `passed` (`.planning/milestones/v2.6-MILESTONE-AUDIT.md`); all 6 phases verified and Nyquist-validated; cross-phase integration WIRED (4/4 seams). Catalogue 276 → 279 (three D-13 evidence mints, each under a human-read D-05 citation); known-bad corpus 39 → 42 with 15 good-control specs; full suite 1629 OK on the real interpreter.

## Active milestone — v2.7 Figure Pipeline (Phases 31–34) — ACTIVE since 2026-09-16

**Status:** Active — opened 2026-09-16 by operator direction after the rendered
nine-chart smoke test of 2026-09-11 (decisions **v2.7-01** / **v2.7-02** in
PROJECT.md). Branch `gsd/v2.7.0-figure-pipeline`, cut from `main` at `e04966e`.
Ships as tag `v2.7.0`. Requirements REQ-P31-01 … REQ-P34-03 (22) in
`.planning/REQUIREMENTS.md`. Full scope in `.planning/research/V2.7-SCOPE.md`
(2026-09-16), written against the live tree at `e04966e` — the loop re-verifies
that scope before any planning.

**The measured miss this milestone answers:** nine charts, one per relationship
family except geographic, rendered through the shipped v2.4 stack exactly as the
cookbook models it, then opened and read. Five of nine titles clipped. Zero of
nine carried units. Zero carried an annotation. Zero used emphasis. Two plotted
categorical quantities on continuous axes (rank ticks at 1.5/2.5/3.5; five
categories at 0.0–4.0 in 0.5 steps). One bar chart came out unsorted and vertical
against this project's own documented default. **All nine passed every
spec-level gate**, because the gate reads `ANALYSIS-SPEC.yaml`, not the picture.
Four verified causes at file:line are in scope §1.2.

**Scope boundary (do not re-litigate):** the renderer is analyst-side and
matplotlib stays FORBIDDEN on the gate path (D-01,
`tests/test_gate_path_hermetic.py`); the pixel check parses the sealed SVG as XML
with the standard library and never renders or reads live data (D-02).
Phases 31, 32 and 34 mint zero codes. Phase 33 measures every candidate against
the corpus at all four gate points **before** the check is designed, and zero
mints is a valid outcome that must not be talked into a mint (D-13). Catalogue
arithmetic is additive from **279** (D-06). No vendor identity is imitated; no
unread source is cited — the Tableau 538 piece and van Schaick's Economist
article both returned HTTP 403 with no local copy and are therefore uncitable.

**Ordering — a hard chain, no cross-phase wave parallelism:** 31 → 32 → 33 → 34.
The renderer consumes the resolver's defaults; the pixel check needs rendered
artifacts to check; the rewiring needs all three. Within **Phase 32** the layout
engine and the mark-specific builders may split into parallel plans — that is the
only parallelism this milestone allows.

**Contingency (pre-agreed, scope §4):** if the BBC `bbplot` licence cannot be read
first-hand, Phase 32 derives its band layout from the Economist/538 descriptions
plus our own measurement and the record says so — slower, not blocked. If Phase
33's candidates all measure as already-caught, the phase closes with zero mints
and its golden fixtures. If the resolver needs a judgement the table cannot make,
the table's domain narrows and the record names which cases stay agent-judged —
never an invented rule with no source.

**Coverage:** 22 of 22 v2.7 requirements mapped, exactly one phase each; 0
unmapped, 0 orphaned.

- [ ] **Phase 31: Deterministic mark resolver** - a declared data signature resolves to one mark plus its render defaults, inspectably and from a sourced table
- [ ] **Phase 32: The renderer** - `render(spec, data)` builds the figure from its declaration; the smoke test's layout defects become unreachable, not discouraged
- [ ] **Phase 33: The pixel check** - stdlib predicates read the sealed SVG; the nine-chart miss becomes evidence fixtures and goldens
- [ ] **Phase 34: Rewiring and calibration** - snippets, skill and critic call the pipeline; calibration re-baselined (terminal, zero mints)

### Phase 31: Deterministic mark resolver

**Goal**: `dsx charts` answers "which one" as well as "which are admissible" — a
declared data signature (input type or coarse family, relationship, category
count, longest category label length, series count, has-time, has-interval)
resolves through a stdlib table to exactly one mark plus its render defaults,
with the rule row that produced it printable, and the existing alphabetical
admissible set left untouched.
**Depends on**: Nothing (first phase of v2.7; builds on the shipped v2.4 vocabulary)
**Requirements**: REQ-P31-01, REQ-P31-02, REQ-P31-03, REQ-P31-04, REQ-P31-05, REQ-P31-06
**Success Criteria** (what must be TRUE):

  1. `dsx charts IT005 --relationship comparison --resolve` prints **one** mark with its render defaults (orientation, sort order, baseline rule, label mode, emphasis mode, and the uncertainty mark where the relationship is `uncertainty`) and the rule row that chose it — where today `permitted()` returns the four-member alphabetical set `bar, bullet, dot_plot, horizontal_bar` and an unattended agent takes `bar` (REQ-P31-01, REQ-P31-02, REQ-P31-05).
  2. `permitted()` returns a byte-identical sorted set to today for every (input type × relationship) pair — the resolver is additive, proven by a golden test over all 40 input types × 11 relationships, and exit codes keep their existing contract (REQ-P31-01, REQ-P31-05).
  3. The resolver is total and deterministic over the declared vocabulary: every pair for which `permitted()` is non-empty resolves to a mark **inside that set**, and identical inputs give identical output across runs — one test per table row plus the totality and determinism property tests (REQ-P31-04).
  4. Every resolver row names its source in the table itself and no row states a rule no source supports; the Chart_Audit_Framework rows cite commit `c69dbf3`, never `main`; Cleveland & McGill appears as six tied ranks, never a strict seven (REQ-P31-03).
  5. The resolver imports no matplotlib and no third-party package, and `tests/test_gate_path_hermetic.py` passes unchanged (REQ-P31-06).

**Plans**: TBD

### Phase 32: The renderer

**Goal**: A figure is built from its declaration by code the analyst *calls* —
`render(spec, data, *, style=…) -> Figure` in `templates/`, off the gate path,
with a layout engine that owns the canvas and its reserved bands — so the nine
smoke-test defects become unreachable rather than discouraged, and determinism
(GA-2/GA-3) is preserved end to end.
**Depends on**: Phase 31 (consumes the resolver's render defaults)
**Requirements**: REQ-P32-01, REQ-P32-02, REQ-P32-03, REQ-P32-04, REQ-P32-05, REQ-P32-06, REQ-P32-07, REQ-P32-08
**Success Criteria** (what must be TRUE):

  1. Zero of the nine re-rendered smoke-test charts clips its title: a title longer than the canvas wraps by **measured** width into a reserved title band, proven on the smoke test's own five clipping titles, with title / subtitle / plot / footer bands reserved on every named canvas size (REQ-P32-02).
  2. Omitting `units=` or `subtitle=` is a `TypeError` at call binding, not a silently unitless chart — the keyword-only, no-default pattern `source=` already uses for `DSX-VIZ-062`, extended to the two things zero of nine charts carried; a test asserts the `TypeError` for each (REQ-P32-03).
  3. Each smoke-test defect is unreachable by construction and proven on the chart that exposed it: chart 05's ranks and chart 09's five categories land on categorical ticks (no 0.5-step axis), charts 02 and 07 come out sorted and oriented as the resolver directs, bar and area baselines are zero, numbers carry thousands/percent/currency formatting — and direct labels with collision avoidance, hero emphasis with the remainder greyed, declared annotations on named points and labelled reference lines exist as callable, tested functions rather than prose (REQ-P32-04, REQ-P32-05).
  4. `render()` lives beside `templates/dsx_plotstyle.py` and is imported by **no** `GATE_PROFILES` module (a test asserts it); `save_deterministic` remains the only writer, `dsx seal` the only hashing authority, the GA-3 recipe is unchanged, and a double-render hash-equality test covers every rendered reference figure (REQ-P32-01, REQ-P32-06).
  5. Every layout constant either names a licence read first-hand or the record states it was derived from the Economist/538 descriptions plus our own measurement — the HQ-27/HQ-33 standard applied to layout; and `sankey` is out of the representative flow set, marked reference-only in `references/chart-catalog.md` with the reason recorded, with the catalogue row-count invariant test updated to the new count (REQ-P32-07, REQ-P32-08).

**Plans**: TBD

### Phase 33: The pixel check

**Goal**: The rendered artifact is checked, so "the gate passed" and "the chart is
good" stop being independent — stdlib predicates over the sealed SVG parsed as
XML, thresholds traceable to named sources, the nine-chart miss committed as
evidence, and every candidate code measured before it is designed.
**Depends on**: Phase 32 (needs rendered artifacts to check)
**Requirements**: REQ-P33-01, REQ-P33-02, REQ-P33-03, REQ-P33-04, REQ-P33-05
**Success Criteria** (what must be TRUE):

  1. The predicates read a sealed SVG as XML with the standard library — no matplotlib, no third-party dependency, no live data — and decide: nothing clipped beyond the canvas box, no two text elements overlapping, a subtitle element present, a unit token present in the subtitle or an axis label. They fire on the 2026-09-11 SVGs and are silent on the Phase-32 re-renders of the same nine charts (REQ-P33-01).
  2. Every predicate's threshold is an observable condition naming its source, with the Chart_Audit_Framework `rules/scoring-anchors.md` cited **by commit `c69dbf3`** and never as `main` — clipped-or-colliding and legend-sole-decoder-above-six as its stated caps, the ranking as its stated floor (REQ-P33-02).
  3. The nine 2026-09-11 SVG/PNG pairs ship as committed fixtures with their per-chart defect list, and the same nine relationships have golden SVGs that a test diffs on change (REQ-P33-03).
  4. `33-MEASUREMENT.md` carries a `VERDICT:` line per candidate, measured against the corpus at all four gate points from a fresh temp directory **before** the check was designed, and the orchestrator re-runs it rather than trusting it; a candidate the gate already catches closes with no mint (REQ-P33-04).
  5. Any code that does mint is additive from 279, carries a D-05 citation and a structural criterion in its docstring, and names a known-bad fixture as its declared target in the same commit (the v2.5-01 family rule); zero mints is recorded as a valid outcome if that is what the measurement says (REQ-P33-05).

**Plans**: TBD

### Phase 34: Rewiring and calibration (terminal)

**Goal**: Every caller uses the pipeline — snippets, the visualize skill and the
critic — and the calibration numbers are re-baselined against the changed
surface, with zero codes minted, as at Phases 12 / 20 / 30.
**Depends on**: Phase 33 (needs the resolver, the renderer and the pixel check to wire together)
**Requirements**: REQ-P34-01, REQ-P34-02, REQ-P34-03
**Success Criteria** (what must be TRUE):

  1. Every snippet in `references/chart-snippets.md` calls the renderer, passes units and subtitle and shows one annotation, and the extended `tests/test_snippet_catalog_routing.py` fails when a snippet hand-rolls what the renderer owns — against today's baseline of zero `set_ylabel`, zero `subtitle=`, zero `figsize`, zero `note=` and zero `annotate` across its eleven sections (REQ-P34-01).
  2. `skills/dsx-visualize/SKILL.md` states resolve → render → seal → check and names `dsx charts --resolve` explicitly, and `agents/dsx-viz-critic.md` gains a step that **opens the rendered PNG** after the pixel check is clean — a grep of that file for `png|svg|render|image`, which matches nothing today, now matches (REQ-P34-02).
  3. Catch rate over the known-bad corpus and false-positive rate over the good-control corpus are re-measured with the new figure cases classified, the one-sided bound stated rather than implied, and the docs re-pinned to the live corpus by the existing agreement test (REQ-P34-03).
  4. Zero codes minted in this phase; the finding catalogue is current (`--check` exit 0), every frozen snapshot unmutated, `scripts/check.sh` green, `node install.mjs --check` green, and the full suite green on the real interpreter (REQ-P34-03).

**Plans**: TBD

## Next

v2.0.0, v2.2, v2.3, v2.4 and v2.6 are shipped and archived
(`.planning/milestones/`); v2.4.1, v2.5.0 and v2.6.1 shipped interactively
(`.planning/MILESTONES.md`). **v2.7 Figure Pipeline is the open milestone.**

Deferred to **v2.8**, every entry condition unchanged and nothing promoted on an
estimate (D-13):

- `SEED-001` E-27 … E-31 — deeper exploration-protocol items (E-26 shipped in v2.6
  Phase 26).
- `SEED-002`'s residue — a producer-side `parse_health` block; a gate reading it
  stays a separate D-02/D-06 decision.
- `SEED-003` — analyst conduct, notebook execution integrity, share-vs-risk
  quantity kinds (six gate candidates, all D-13 entry-conditioned; the medium
  question was settled 2026-09-10 — two media with an explicit boundary).
- `SEED-004` — concurrent `DECISIONS.jsonl` writers; dormant until a scope
  actually races two gates against one root.
- Good-control corpus growth past 15 specs — the false-positive denominator is
  thin (one-sided 95% bound ≈0.181 on 0/15). It lost to v2.7 on precedence, not
  on merit; the figure miss is measured and visible to a portfolio reader.
- EDA brief §6.5 items 1–6 — paradigm-paired items wait for their mirrors (D-12a).
- A real Sankey ribbon implementation — if a consumer ever needs one; Phase 32
  drops `sankey` to reference-only rather than shipping matplotlib's arrow diagram.

Running v2.7 under the autonomous ceremony still needs the operator steps recorded
in `STATE.md`: a fresh `LOOP-BRIEF.md` / `LOOP-LEDGER.md` / `HUMAN-QUEUE.md`, and
`$Branch` in `scripts/run-ceremony-firing.ps1` repointed from the deleted
`gsd/v2.6.0-exploration-depth` to `gsd/v2.7.0-figure-pipeline` **before**
`.planning/loop-logs/.paused` is removed. Next planning action:
`/gsd-plan-phase 31`.
