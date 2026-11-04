# Spike: per-hypothesis procedure adjudication

Status: recommendation, awaiting operator decision. No product code was changed. The per-row container is not implemented.

Origin: Senior Statistician Roadmap check, item 7. The question: does the single-procedure adjudication (`inference.primary_procedure` against one `validity_frame` estimand and dependence pair) miss a hypothesis row whose procedure is inadmissible for that row's design?

Labels used below: **MEASURED** means a command in this note produced the quoted output. **UNVERIFIED** means a judgement or an inference that no run established.

## Method

All specs were built by a script outside the repository (temp directory, base spec `examples/good-corpus/freq-proportion-checkout-ANALYSIS-SPEC.yaml`, copied). Each spec has 36 reported tests (`results.tests`, `design.comparisons_looked_at: 36`). The frame declares estimand `difference_in_proportions` and dependence `clustered`. Commands were run from the worktree with `python -m dsx` (Python 3.12); each variant used its own empty `--phase-dir`, so no trail was written into the repository.

| Variant | Spec-level `inference.primary_procedure` and `analysis.test` | Per-row data |
|---|---|---|
| A | `two_proportion_z_cluster_robust` (admissible for the clustered frame) | none |
| B | same as A | every row also carries `procedure` and `design_dependence`; row 17 has `procedure: fishers_exact` (not in the clustered candidate set), the other 35 rows have `two_proportion_z_cluster_robust` |
| C | `fishers_exact` at spec level (control: the same inadmissible procedure, declared where the check reads it) | none |

Row 16 and row 17 of variant B, verbatim from the spec file:

```yaml
    - metric: completion_rate
      p_value: 0.0006
      effect: 0.022
      standardized_effect: 0.044
      effect_size_kind: h
      ci: [0.014, 0.030]
      interpretation: "Hypothesis H16: treatment raises completion."
      minimum_practical_effect: 0.02
      procedure: two_proportion_z_cluster_robust
      design_dependence: clustered
    - metric: completion_rate
      p_value: 0.0006
      effect: 0.022
      standardized_effect: 0.044
      effect_size_kind: h
      ci: [0.014, 0.030]
      interpretation: "Hypothesis H17: treatment raises completion."
      minimum_practical_effect: 0.02
      procedure: fishers_exact
      design_dependence: clustered
```

## Results (MEASURED)

### Variant A: 36 rows, one admissible procedure

```text
$ python -m dsx validate --spec <tmp>\A-36-rows-single-procedure-ANALYSIS-SPEC.yaml --json
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
(no findings)
```
```text
$ python -m dsx check admissibility --spec <tmp>\A-36-rows-single-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-A --json --verbose
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
(no findings)
```
```text
$ python -m dsx gate plan --spec <tmp>\A-36-rows-single-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-A --json
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 1, "INFO": 1, "LOW": 0, "MEDIUM": 0}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
```
```text
$ python -m dsx audit --spec <tmp>\A-36-rows-single-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-A --json
exit=1 block=True counts={"CRITICAL": 0, "HIGH": 2, "INFO": 1, "LOW": 0, "MEDIUM": 36}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-STA-041 HIGH @ spec.analysis.test :: Declared test 'two_proportion_z_cluster_robust' does not match the data's shape :: For a proportion outcome across 2 independent group(s), the indicated test is 'two_proportion_z' — Two independent proportions with adequate expected cell counts. Acceptable alternatives: boschloo_exact (any expected cell < 5), chi_square, bootstrap.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
DSX-STA-011 MEDIUM x36 @ spec.results.tests[0..35] (one per row, identical text)
```

### Variant B: row 17 declares an inadmissible procedure

```text
$ python -m dsx validate --spec <tmp>\B-per-row-procedure-row17-bad-ANALYSIS-SPEC.yaml --json
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
(no findings)
```
```text
$ python -m dsx check admissibility --spec <tmp>\B-per-row-procedure-row17-bad-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-B --json --verbose
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
(no findings)
```
```text
$ python -m dsx gate plan --spec <tmp>\B-per-row-procedure-row17-bad-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-B --json
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 1, "INFO": 1, "LOW": 0, "MEDIUM": 0}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
```
```text
$ python -m dsx audit --spec <tmp>\B-per-row-procedure-row17-bad-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-B --json
exit=1 block=True counts={"CRITICAL": 0, "HIGH": 2, "INFO": 1, "LOW": 0, "MEDIUM": 36}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-STA-041 HIGH @ spec.analysis.test :: Declared test 'two_proportion_z_cluster_robust' does not match the data's shape :: For a proportion outcome across 2 independent group(s), the indicated test is 'two_proportion_z' — Two independent proportions with adequate expected cell counts. Acceptable alternatives: boschloo_exact (any expected cell < 5), chi_square, bootstrap.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
DSX-STA-011 MEDIUM x36 @ spec.results.tests[0..35] (one per row, identical text)
```

### Variant C: the inadmissible procedure declared at spec level

```text
$ python -m dsx validate --spec <tmp>\C-spec-level-bad-procedure-ANALYSIS-SPEC.yaml --json
exit=0 block=False counts={"CRITICAL": 0, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
(no findings)
```
```text
$ python -m dsx check admissibility --spec <tmp>\C-spec-level-bad-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-C --json --verbose
exit=1 block=True counts={"CRITICAL": 1, "HIGH": 0, "INFO": 0, "LOW": 0, "MEDIUM": 0}
DSX-ADM-020 CRITICAL @ spec.primary_procedure :: No admissible procedure for the declared frame :: The declared procedure 'fishers_exact' resolved to family 'fishers_exact', which is outside this frame's own candidate set (estimand='difference_in_proportions', dependence='clustered').
```
```text
$ python -m dsx gate plan --spec <tmp>\C-spec-level-bad-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-C --json
exit=1 block=True counts={"CRITICAL": 1, "HIGH": 1, "INFO": 1, "LOW": 0, "MEDIUM": 0}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
DSX-ADM-020 CRITICAL @ spec.primary_procedure :: No admissible procedure for the declared frame :: The declared procedure 'fishers_exact' resolved to family 'fishers_exact', which is outside this frame's own candidate set (estimand='difference_in_proportions', dependence='clustered').
```
```text
$ python -m dsx audit --spec <tmp>\C-spec-level-bad-procedure-ANALYSIS-SPEC.yaml --phase-dir <tmp>\phase-C --json
exit=1 block=True counts={"CRITICAL": 1, "HIGH": 2, "INFO": 1, "LOW": 0, "MEDIUM": 36}
DSX-EXP-050 HIGH @ spec.design.multiplicity.correction :: 36 hypotheses tested with no multiplicity correction :: At alpha=0.05 the chance of at least one false positive across 36 independent tests is 84%, not 5%.
DSX-STA-041 HIGH @ spec.analysis.test :: Declared test 'fishers_exact' does not match the data's shape :: For a proportion outcome across 2 independent group(s), the indicated test is 'two_proportion_z' — Two independent proportions with adequate expected cell counts. Acceptable alternatives: boschloo_exact (any expected cell < 5), chi_square, bootstrap.
DSX-PAR-001 INFO @ spec.inference.paradigm :: paradigm manifest — inference.paradigm: frequentist :: applied: DSX-ADM-, DSX-INT-, DSX-PAR-002, DSX-PAR-010, DSX-PRE-, DSX-SPEC-08, DSX-VAL-
not applied: DSX-PAR-011 (not selected for the declared paradigm)
DSX-ADM-020 CRITICAL @ spec.primary_procedure :: No admissible procedure for the declared frame :: The declared procedure 'fishers_exact' resolved to family 'fishers_exact', which is outside this frame's own candidate set (estimand='difference_in_proportions', dependence='clustered').
DSX-STA-011 MEDIUM x36 @ spec.results.tests[0..35] (one per row, identical text)
```

### A against B, finding by finding (computed from the full JSON of each run)

| Command | Findings of A and B identical |
|---|---|
| `dsx validate` | True |
| `dsx check admissibility` | True |
| `dsx gate plan` | True |
| `dsx audit` | True |

The admissibility decision record, verbatim:

- A: `DSX-ADM clear: the resolved procedure is not dominated by any cited ordering rule, and an admissible procedure exists for this frame`
- B: `DSX-ADM clear: the resolved procedure is not dominated by any cited ordering rule, and an admissible procedure exists for this frame`

The variant C finding, verbatim:

```text
DSX-ADM-020 CRITICAL @ spec.primary_procedure :: No admissible procedure for the declared frame :: The declared procedure 'fishers_exact' resolved to family 'fishers_exact', which is outside this frame's own candidate set (estimand='difference_in_proportions', dependence='clustered').
```

## What per-spec adjudication catches and misses

- MEASURED, catches: an inadmissible procedure declared at spec level. Variant C draws DSX-ADM-020 CRITICAL at `check admissibility`, `gate plan` and `audit`, and blocks.
- MEASURED, misses: the same inadmissible procedure carried by one row of 36 (variant B). Every command returns the same findings as variant A, and `check admissibility` reports clear. The row-level `procedure` and `design_dependence` keys are accepted by `dsx validate` (exit 0, no findings) and read by no check.
- MEASURED, by contrast: some checks are already per row. DSX-STA-011 fires once per `results.tests[i]` row (36 findings in A, B and C alike), so a per-row location convention already exists. Admissibility has none.
- MEASURED, related and not new: with 36 tests and no `design.multiplicity`, DSX-EXP-050 (HIGH) fires in every variant. The multiplicity gate sees the number of tests, not their procedures.
- Spike noise, not a finding about the feature: DSX-STA-041 HIGH fires in A, B and C because the cluster-robust label I set on `analysis.test` is not the label the data-shape recommender expects (`two_proportion_z`), and DSX-PAR-001 INFO is the paradigm note. Neither depends on the per-row key. In variant C the same two codes appear with DSX-ADM-020 added.

## Migration cost of a per-row container (UNVERIFIED: judgement from reading the code, no change was attempted)

1. Schema: a pre-data container, for example `inference.procedures[]` keyed by a hypothesis id, with each entry carrying its own estimand and dependence. It cannot live on `results.tests` rows, because `results` is filled after the data exists. The plan-time lock (`frame_digest` over `validity_frame:` and `inference:`) would then cover it.
2. `dsx/frame/admissibility.py` takes one frame (`estimand`, `dependence`, `declared_procedure(spec)`). It would loop over entries and resolve each against its own candidate set. DSX-ADM-010 and DSX-ADM-020 need a per-entry `where` and a rule for the aggregate verdict.
3. DSX-PRE-030 (executed against declared branch) and `analysis.test` are single-valued. They need a per-hypothesis mapping or an explicit statement that they cover the primary hypothesis only.
4. Tests, `references/` text, the finding catalogue (`scripts/gen-finding-catalogue.py --check`) and the golden ship-finding sets for the 59 fixtures under `examples/`. If the container is optional, the golden sets should not move; that is also unverified.
5. Operator burden: a spec with 36 hypotheses would declare 36 entries, or a default plus exceptions. Authoring cost grows with test count.

## Recommendation (awaiting operator decision)

Recommendation: **drop for now; keep as a conditional adopt**. Do not build the per-row container yet.

Reason: the measured miss does not need different designs. Variant B has one estimand and dependence pair for every row, and only the procedure on row 17 differs. So a row-level procedure mismatch can be missed inside a single frame. The recommendation to wait rests on a judgement, not on the measurement: no row-level procedure is a contract field today, so nothing obliges an author to declare one, and this spike used a constructed case. Whether real specs carry row-level procedures, in one frame or in several, is UNVERIFIED. Rows with a different design could also be separate specs, each adjudicated on its own; this is a policy preference and does not close the single-frame miss.

Entry condition (D-13, measured first, never widened to manufacture a miss): adopt only when a real or corpus-derived spec exists in which (a) one decision legitimately reports hypotheses with different procedures, under one frame or under several estimand or dependence pairs, and (b) the existing gates measurably miss an inadmissible procedure on one of those rows, as variant B did. Build that case, run it at all four gate points, and record the codes. If the present gate already catches the case, the entry condition is not met and nothing is minted.

A cheaper alternative to evaluate first if the condition is met: a documentation rule that each distinct design gets its own spec and decision record, with a lint that flags `results.tests` rows carrying a `procedure` key the gate ignores. This is UNVERIFIED and not part of this spike.

## Limits of the spike

- One constructed spec family, one base fixture, one inadmissible procedure (`fishers_exact`, clustered frame). No real user spec was used.
- The per-row key names (`procedure`, `design_dependence`) are mine; the project has not defined a row-level schema.
- The spike did not test the Bayesian paradigm path or `gate verify` and `gate ship`.
