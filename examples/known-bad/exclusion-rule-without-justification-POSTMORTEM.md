# Post-mortem: a row-exclusion rule with no stated reason

Paired spec: `exclusion-rule-without-justification-ANALYSIS-SPEC.yaml`

Added 2026-09-30 to close the project audit's finding that `DSX-VAL-080` (the
exclusion-rule check) had unit tests but no known-bad corpus coverage
(`.planning/PROJECT-AUDIT-2026-09-30.md`, Low severity item 38). The spec is a copy of
the clean `examples/good-corpus/freq-proportion-checkout` control with exactly one
change: a `validity_frame.exclusions` entry whose `justification` is blank. It clears
`dsx gate plan` and `dsx gate execute` like its base, so the only thing wrong with it
is the undisclosed exclusion.

## What was concluded

The commerce team reported that one-click checkout raised cart completion by 2.2
percentage points. Before analysing, they dropped every cart whose session ran past
30 minutes, and recorded the rule but not the reason for it.

## Why it was wrong

Which rows to exclude is one of the researcher degrees of freedom Simmons, Nelson &
Simonsohn (2011) show can turn noise into a significant result: when the rule is
chosen, or kept, because of how the numbers come out, the estimate no longer answers
the question that was asked. A rule with no stated reason cannot be checked against
the claim population. Long sessions may be abandoned tabs (a defensible exclusion) or
careful comparison shoppers (an exclusion that removes the users the feature was
meant to help). Without the justification, a reader cannot tell which.

## Source

Simmons, J.P., Nelson, L.D. & Simonsohn, U. (2011), "False-Positive Psychology:
Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as
Significant", *Psychological Science* 22(11):1359-1366, DOI 10.1177/0956797611417632.
The same citation is carried in `dsx/frame/val.py::_check_exclusions`; the exact
requirement number inside the paper is not asserted here.

## Which code catches it

`DSX-VAL-080` (HIGH) — `_check_exclusions` in `dsx/frame/val.py` fires for each
`validity_frame.exclusions` entry that has a non-blank `rule` and a blank
`justification`. The `val` family is registered at plan, verify and ship. HIGH does
not block at plan (default threshold CRITICAL), so the fixture is recorded in the HIGH
verify/ship stratum. Measured 2026-09-30 with a fresh temporary phase directory per
gate point: plan exit 0 (`DSX-VAL-080` HIGH reported, not blocking); execute exit 0;
verify and ship exit 1 with `DSX-VAL-080` as the only finding at HIGH or above. The
one MEDIUM finding (`DSX-STA-011`, negligible standardized effect) also fires on the
unmodified control and does not block. No new finding code is minted.
