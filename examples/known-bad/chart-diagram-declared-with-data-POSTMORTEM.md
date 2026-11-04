# Post-mortem: a chart of data declared a diagram to skip the data checks

Paired spec: `chart-diagram-declared-with-data-ANALYSIS-SPEC.yaml`

A DSX-VIZ coverage fixture for `DSX-VIZ-015`, added with the `visual_kind` field. The
underlying spec is a copy of the clean `examples/good-corpus/freq-continuous-timeontask`
control, so it clears `dsx gate plan` and `dsx gate execute` exactly like its base. The
only thing wrong with it is the one chart in `visuals[]`.

## What was concluded

An editor team declared the focused-editing uplift chart `visual_kind: diagram`, the
declaration meant for a figure with no data, while the same entry carries a
`relationship`, a `data_input_type` and a chart `type`. A diagram is exempt from
`DSX-VIZ-010` (relationship), `DSX-VIZ-064` (takeaway magnitude) and `DSX-VIZ-061`
(units). This chart plots numbers, so it is not a diagram.

## Why it was wrong

The exemption exists because a pipeline flow has no relationship, units or magnitude to
check. A chart that plots data and claims the exemption would drop the checks that read
its data. The declaration is closed against that: a diagram that also declares a data
field loses the exemption, and the finding names the field.

## Source

DSX's own contract rule (`references/chart-selection.md`, `skills/dsx-visualize/SKILL.md`).
It is a declaration-consistency rule, not a perceptual finding, so it cites no external
source.

## Which code catches it

`DSX-VIZ-015` (HIGH) in `_declares_no_data`, `dsx/checks/viz.py`. HIGH blocks at
`dsx gate verify` and `dsx gate ship`; the corpus measures it in the HIGH stratum. The
same code fires on an unrecognised `visual_kind` value. This is the one finding code
minted with the `visual_kind` field (catalogue 279 to 280).
