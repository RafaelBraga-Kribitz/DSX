# Known-bad corpus

Hand-built analysis specs that each contain a real, named defect. They serve two
purposes. For most of them, the corpus is proof that a DSX check catches the defect.
For a few, it is an honest record that no check does. **Do not assume that the
gate detects every defect in this directory.** The five MISS fixtures listed below are
not caught.

## What is in here

Every fixture is a pair, plus optional sidecars:

| File | Always? | What it holds |
|---|---|---|
| `<slug>-ANALYSIS-SPEC.yaml` | yes | The analysis spec that carries the defect. |
| `<slug>-POSTMORTEM.md` | yes | What was concluded, why it was wrong, the source, and which code catches it (or why none does). |
| `<slug>-ATTRIBUTION.yaml` | MISS and backlog cases | The code that *would* catch the defect and the backlog item that would build it. `kind: miss` means that code fires nowhere on this fixture. |
| `<slug>-NARRATIVE.md`, `<slug>-entrypoint.py` | some | Deliverables the spec points at, for checks that read them. |
| `EXPECTED-FINDINGS.json` | one file | What every fixture is expected to fire, per gate point and severity tier. The test suite reads it (see below). |

`DECISIONS.jsonl` may appear here after a manual `dsx gate` or `dsx audit` run
without `--phase-dir`. It is the decision trail those commands append to. It is
gitignored and is not part of the corpus.

## Expected findings

`EXPECTED-FINDINGS.json` is the source of truth for what each fixture should fire.
`tests/test_known_bad_corpus.py` builds all its expectation maps from it. For each
slug the file records:

- `miss`: `true` when nothing fires on the encoded defect.
- `severity_band`: the highest severity among the fixture's own target codes
  (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`), or `null` for a MISS.
- `target_codes`: every code the fixture exists to demonstrate.
- Per-point maps (`critical_by_point`, `caught_at_plan_and_execute`, `high_by_point`,
  `medium_by_point`, `low_by_point`) that say where each code must fire.
- `incidental_by_point`: codes tolerated at a point that are not the fixture's own
  catch (today only `magnitude-without-computed-effect`).
- `note`: a one-line reason. The post-mortem has the full story.

Severity tiers matter for what "caught" means. A `CRITICAL` or `HIGH` code blocks
`dsx gate verify`/`ship` at the default threshold. A `MEDIUM` or `LOW` code blocks
nothing at any default threshold (plan and execute block on CRITICAL, verify and ship
on HIGH). The eight MEDIUM and three LOW fixtures (all `chart-*`) exit 0 at the
default threshold and are only credited as caught under `--block-on MEDIUM` or
`--block-on LOW`. The test suite checks them that way.

As of 2026-09-30: 43 fixtures. 10 CRITICAL, 17 HIGH, 8 MEDIUM, 3 LOW, 5 MISS.

## MISS fixtures: what the gate does not catch

Each of these encodes a real defect that **no shipped check fires on**. Some are
blocked by the gate, but only by corpus-completeness gaps unrelated to the defect:
evidence pointing at an uncommitted `RESULTS.md`, an assumption neither checked nor
waived, a metric with no SQL definition, a missing narrative, or no reproducibility
harness. Those are listed in `_INCIDENTAL_GAP_CODES` in the corpus test. Fix those
gaps and the spec would pass with its defect intact.

| Fixture | The defect | What the gate does NOT catch | Code that would attribute it (see `-ATTRIBUTION.yaml`) |
|---|---|---|---|
| `feature-origin-only-leak` | A churn model feature (`account_health_index`) is recomputed from activity that includes the outcome window. | Target leakage that shows only through where a feature comes from. The name matches no leakage pattern, no fit call is visible, and the honest spec declares no per-feature origin list. | `DSX-ML-034`, which reads `model.feature_provenance[]` and stays silent when none is declared. |
| `garden-of-forking-paths-p-hacking` | An undisclosed specification search, reported as a single comparison. | Forking paths and p-hacking. `comparisons_looked_at` equals the reported test count, so the multiplicity check has nothing to fire on. | `DSX-EXP-051`. Catching it needs a specification-sensitivity check that has not been written (§6.5 item 1). |
| `retracted-fabricated-field-experiment` | A published field experiment whose data were fabricated. | Fabricated data. A plausible warehouse source and period are declared, and a declaration-only gate cannot verify that data were really collected. | `DSX-REP-020` (§6.5 item 7, provenance). |
| `operator-known-answer-selective-exclusion` | Observations dropped and a weighting chosen after seeing the answer, and never declared. | Selective exclusion that is not declared. `DSX-VAL-080` only fires on a *declared* exclusion rule with no justification. Here nothing is declared. Compare `exclusion-rule-without-justification`, which is caught. | `DSX-VAL-080` (§6.5 item 1). |
| `magnitude-without-computed-effect` | The headline churn magnitude (27% vs 18%) is quoted for a metric that no test computes. | A claimed magnitude that no test computed. The claim's numbers coincide with two other metrics' effects, so the numeric-overlap check (`DSX-CLM-033`) clears. It is blocked by `DSX-COH-001` CRITICAL, but that code is about claim strength against question type, not about the magnitude, and is recorded as an incidental. | `DSX-CLM-034`, which needs a declared claim-to-test pointer that this spec does not have. |

These five make up the ABSENT partition of the corpus calibration. The headline miss
rate in `test_stratified_catch_rate_and_fpr_report` is measured over them. They stay
MISS until a check is built for each. When one is built, move the fixture's code into
its `EXPECTED-FINDINGS.json` entry, set `miss` to `false`, and change the sidecar's
`kind`. Each MISS post-mortem carries a one-line **Known MISS** note that points here.

## Running a fixture

Audit fixtures **from the repository root**. Several specs (every `chart-*` fixture
and the `exclusion-rule-without-justification` fixture) name their entrypoint,
narrative and evidence with repo-relative paths such as
`examples/good-corpus/_control_readout.py`. Run from any other directory, those paths
do not resolve and HIGH findings unrelated to the defect appear. Pass a fresh
`--phase-dir` so the decision trail is not written into this directory:

```sh
python3 -m dsx audit --spec examples/known-bad/chart-pie-nine-slices-ANALYSIS-SPEC.yaml \
  --phase-dir "$(mktemp -d)" --block-on LOW --json
```

`dsx gate verify` and `dsx gate ship` also need a plan-time trail header in the phase
directory. The test harness seeds one with `tests/_trail_seed.py`.

## Adding a fixture

1. Add `<slug>-ANALYSIS-SPEC.yaml` and `<slug>-POSTMORTEM.md`. The post-mortem must
   name the code that catches the defect, or say plainly that none does.
2. Add one entry for `<slug>` to `EXPECTED-FINDINGS.json`. If nothing catches it, set
   `miss: true`, add a `kind: miss` `-ATTRIBUTION.yaml`, add a **Known MISS** line to
   the post-mortem, and list the fixture in the table above.
3. Run `python3 -m unittest tests.test_known_bad_corpus -q`. Its manifest checks will
   tell you if the entry does not match the catalogue or the files on disk.
4. Count references elsewhere (for example
   `docs/literature/the-ai-data-scientist.md`) may need updating.
