# Examples

Worked specs that show what the gate passes and what it blocks. They are also test
inputs: `scripts/check.sh` and the test suite read almost every file here.

| Path | What it is |
|---|---|
| `good-ANALYSIS-SPEC.yaml` and its `good-*` siblings | The known-good exemplar, an onboarding-activation A/B test. It must pass every gate point. |
| `bad-ANALYSIS-SPEC.yaml`, `bad-*` | A deliberately defective spec that shows most of the finding catalogue in one run. It must block at every gate point. |
| `RESULTS.md` | The evidence file behind the good spec's claims (see below). |
| `analysis/` | The good spec's entrypoint (`activation_readout.py`), figure generator (`charts.py`), lockfile stub, and `leaky_model.py`, the bad spec's deliberately leaky entrypoint (it is fitted before the split). |
| `figures/` | The three sealed SVG figures the good spec declares (see below). |
| `good-corpus/` | Clean control specs. They are the false-positive denominator for the corpus calibration. |
| `known-bad/` | One spec per named defect, each with a post-mortem. See [`known-bad/README.md`](known-bad/README.md), which lists the fixtures the gate does **not** catch. |

`DECISIONS.jsonl` files that appear here are decision trails written by manual
`dsx gate` / `dsx audit` runs. They are gitignored, not fixtures. Pass a fresh
`--phase-dir` to keep them out of the tree.

## Run everything from the repository root

Audit and gate these specs **with the repository root as the working directory**.
The specs use two path conventions:

- The good and bad exemplars name most sibling files relative to the spec's own
  directory (`RESULTS.md#...`, `figures/...`, `good-NARRATIVE.md`). Those resolve
  from anywhere. The exception is `reproducibility.reproduce_report`
  (`examples/good-REPRO-REPORT.md`), which the repro check resolves against the
  working directory.
- The `good-corpus/` specs and the known-bad fixtures copied from them (every
  `chart-*` fixture and `exclusion-rule-without-justification`) name their entrypoint,
  narrative and evidence with repo-relative paths such as
  `examples/good-corpus/_control_readout.py`. Those resolve against the working
  directory only.

Run from anywhere else, those paths do not resolve, and a clean control reports HIGH
findings that have nothing to do with the analysis. Measured 2026-09-30: running
`bin/dsx audit` on `good-corpus/freq-continuous-aov-ANALYSIS-SPEC.yaml` from `/tmp`
reports DSX-CLM-031, DSX-NAR-010 and DSX-REP-031 (all HIGH). From the repo root it
passes with one INFO. This is a property of the fixtures, not a bug to work around.
The test suite and `scripts/check.sh` always run from the repo root.

```sh
python3 -m dsx audit --spec examples/good-ANALYSIS-SPEC.yaml --phase-dir "$(mktemp -d)"
```

## RESULTS.md

`RESULTS.md` is the evidence file for the good spec. Its claims and its
`validity_frame.stability.evidence` point at anchors in it (`RESULTS.md#activation-uplift`,
`#retention`, `#guardrails`), resolved against the spec's own directory. It is what
makes the good spec pass the claim-evidence check. Measured 2026-09-30: on a copy of
`examples/` without `RESULTS.md`, `dsx gate ship` blocks with three DSX-CLM-031 (HIGH,
"Evidence pointer does not resolve to an existing file"). No other file refers to
`examples/RESULTS.md` by that full path, which is why it can look unreferenced. Keep
it, and keep its headings in step with the good spec's `evidence:` anchors.

## Figures are frozen, sealed artefacts

`figures/*.svg` are drawn by `analysis/charts.py`, then sealed: their sha256 is
recorded as `svg_sha256` in `good-ANALYSIS-SPEC.yaml`, and `.gitattributes` stores
them as binary so the seal survives checkout. Nothing regenerates them automatically.
They change only when someone re-runs `charts.py` and then `dsx seal`.

`tests/test_example_figures_regenerate.py` checks that they still match the
generator. It re-renders all three into a temporary directory and compares them with
the committed files after normalising line endings (the committed files were rendered
on Windows, so they have CRLF endings) and the matplotlib version string in the SVG
metadata. Every other byte must match. It skips when matplotlib is not installed, and
when the installed matplotlib's major.minor differs from the version recorded in the
SVGs, because output geometry can move between minor releases. Measured 2026-09-30
with matplotlib 3.11.2, against files rendered with 3.11.1: identical after those two
normalisations. A raw byte comparison is not possible across platforms.

## The good example still passes the current gate

`scripts/check.sh` copies `examples/` to a temporary directory and requires the good
spec to pass `dsx gate plan`, `execute`, `verify` and `ship`, and the bad spec to
block at each. Re-run 2026-09-30 (project audit L47) against the current checks,
including the entrypoint scan of `analysis/`: all four points pass. Plan and execute
report one INFO. Verify and ship report three MEDIUM and one INFO, and nothing at
HIGH or above.
