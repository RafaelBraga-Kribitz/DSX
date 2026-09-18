# Known limits

The full text of each limit summarised under
[Known limits](../README.md#known-limits) in the README, verbatim.

## The verbless recommendation is not caught

The coherence and claim checks catch a recommendation two ways: by its
**type** (a claim typed `prescriptive` under a `descriptive` question breaches
the type ceiling, `DSX-COH-001`) and by its **verb** (a causal verb such as
`reduce` in a claim or a decision rule under a descriptive question,
`DSX-CLM-011` / `DSX-COH-010`, via the purpose-gated causal-verb lexicon). A
recommendation that evades **both** is not caught. Type an intervention as
`descriptive` rather than `prescriptive`, and phrase it with no causal verb —
"offer bundled incentives", "prioritise segment Y", "the optimal action is X" —
and the type ceiling sees a descriptive claim under a descriptive question, the
identification check (`DSX-CLM-020`, which fires only on a claim typed
`prescriptive` or `causal`) sees nothing to hold to an identification standard,
and the causal-verb widening finds no verb to match. The recommendation ships
unflagged.

This is a **named, deferred limit**, not something the current checks catch.
Nothing here recognises an imperative by its *mood* — the grammatical fact that
"offer bundled incentives" is a command. Closing it would take an imperative
lexicon (a check that reads the recommendation's mood rather than its declared
type or its verbs), which is a future phase. Until then, the honest statement is
that a recommendation mis-typed as descriptive and phrased without a causal verb
is a hole the gate does not close.

## What the amendment counter does not enforce

`dsx explain` surfaces how many times a specification's `validity_frame:` or
`inference:` blocks changed across recorded gate runs — an amendment counter
drawn from the decision trail. Four things about it are limits, stated as what
is **not** checked rather than as anything the gate enforces:

- **It is not tamper-proof.** `DECISIONS.jsonl` is a plain, unsigned, local text
  file read tolerantly (a malformed line is skipped, not fatal). The counter is
  a committed-trail honesty signal — it records what the trail happens to hold —
  not a control that would survive someone editing or truncating the file. It
  detects drift; it does not prevent it.
- **It is blind outside two blocks.** The digest it counts changes to covers
  only `validity_frame:` and `inference:`. An amendment to any other part of the
  specification — the decision rule, the metrics, the claims — moves nothing in
  the counter and is invisible to it.
- **The identity-free floor re-opens a cross-spec false positive.** Recorded
  invocation headers carry no specification identity, so a decision trail shared
  by more than one specification under a single root mixes their headers. On a
  shared root the counter cannot tell one specification's amendments from
  another's, and an unrelated specification's edits can read as this one's.
- **The reason is checked for form, not truth.** Where an amendment reason is
  required, the gate checks that a non-blank reason is present, not that it is
  accurate. A plausible-looking reason that misdescribes why the frame changed
  clears the same bar as an honest one.

## Concurrent `dsx gate` invocations are not supported

Run `dsx gate` points against one analysis directory sequentially, not in
parallel. The per-invocation identifier in `DECISIONS.jsonl` is derived by
reading and counting existing invocation headers, and nothing locks that
read against a second process's write. Two concurrent `dsx gate` runs
against the same directory can both derive the same invocation identifier
and both append a header carrying it, merging their decision trails under
one invocation in `dsx explain`'s output. This does not affect any gate's
exit code — the trail stays a side channel — but it does corrupt the
grouping guarantee the trail is supposed to provide for that one invocation.
Serialising `dsx gate` runs against a given analysis directory is the
operator's responsibility today.

## What the declared-versus-executed reconciliation cannot see

The pre-registered inference plan check (`DSX-PRE-*`) reconciles a declared
inference plan against what actually ran. Four things about that
reconciliation are worth stating plainly, because correct code alone does
not make them obvious from the outside.

First, `declared_at`. This field records whether the operator says the
inference plan was declared before the data was observed (`pre_data`) or
after it (`post_data`). It is an operator self-declaration that the tool
cannot verify — nothing in the gate can tell a true `pre_data` claim from a
false one. Declaring `post_data` honestly is legal and produces no finding.
This is deliberate: if an honest post-hoc declaration were blocked, staying
silent about the truth would be cheaper than declaring it, and that is
exactly the incentive this project exists to avoid.

Second, the executed side. The reconciliation reads the procedure it treats
as "executed" from `analysis.test`. That field is scaffolded into the
specification at plan time, by the same template that scaffolds everything
else — so "executed" is a convention imposed by the gate point at which this
check runs, not a property the field itself carries. It is the same class of
limit as `declared_at`.

Third, the content lock. Where `dsx gate plan` has run, the reconciliation
compares a hash computed over the `validity_frame:` and `inference:` blocks
as they were recorded at that point against the same hash computed now — it
compares recorded bytes, not a declared string. The limit: nothing in the
code enforces an ordering between the four gate points (`plan`, `execute`,
`verify`, `ship`). An operator who re-runs `dsx gate plan` after seeing
results registers the edited frame and clears the check. The lock is only as
strong as the operator's discipline in not doing that. The hash also covers
only those two blocks, so an edit anywhere else in the specification does
not move it — this is change detection, not a security control.

Fourth, the missing-lock case. A `dsx gate verify` or `dsx gate ship` run
that finds no plan-time header recorded anywhere in the decision trail stops
at exit 2 — could not run — rather than passing. A specification that
legitimately predates the plan gate takes the existing `suppressions[]`
route, which requires citing the architecture decision record (ADR) or
specification that authorises it.

The declared fallback rule (`inference.fallback_rule`) may only reference a
closed set of three facts: `alpha` (read from `design.alpha`),
`comparisons_looked_at` (read from `results.comparisons_looked_at`), and
`interim_looks` (read from `results.interim_looks`). A rule naming anything
outside that set produces a finding rather than being silently ignored. The
arrow (`->`) is what makes a `fallback_rule` value a rule at all — a value
with no arrow is read as ordinary prose and left alone. `dsx vocab` emits the
same three names under `prereg_facts`, so that command is the
machine-readable source for this set rather than this paragraph.

## Two tiers of evidentiary rigour

Not every finding code in the catalogue carries the same evidentiary bar.

**Tier one — codes introduced in v2.0.0.** Every new finding code carries, in
its docstring, a `Citation:` line naming author, year, work and the exact
formulation, plus a `Reference value:` line (or `Structural criterion:` where
the check is structural rather than numeric), plus a `# D-05: <CODE>` marker
comment in `tests/` linking the code to the test that proves it fires. All
three are enforced mechanically:

```bash
python3 scripts/gen-finding-catalogue.py --check
```

**Tier two — pre-existing codes.** The finding codes that predate this rule
are carried on a finite allow-list inside `gen-finding-catalogue.py`. Many
are structural (contract shape, SQL fan-out) with no primary statistical
source to cite — forcing a citation there would manufacture exactly the fake
authority the rule exists to prevent. The allow-list is designed to shrink:
as an old code earns a citation, it comes off the list.

The `# D-05: <CODE>` test-linkage convention isn't cosmetic bookkeeping — it
is how every check family from here forward proves its citation is actually
exercised by a test, not just quoted in a comment. It binds every later
milestone phase from the moment it lands.

The `DSX-PAR-*` family's own symmetry argument — why neither the frequentist
nor the Bayesian half of its monitoring-discipline pair is cheaper to satisfy
dishonestly than the other — is committed separately at
[`references/paradigm-symmetry.md`](../references/paradigm-symmetry.md).

## What the entrypoint scan does not catch

A clean run of the entrypoint leak scan (`DSX-CODE-001`, `DSX-CODE-021` and
their siblings) is evidence that these particular shapes were not found in
your file. It is not evidence that the file does not leak, and no sentence
anywhere in this project should be read the other way — including the fact
that the scan now uses a real Python parser. Parsing your code means the
scan resolves the *structure* of a function call correctly; it does not mean
the scan understands what your code does at runtime, and the forms below are
real leaks, or real blind spots, that this change does not close.

The scan works by reading the one file you declared as your entrypoint,
looking for calls it recognises by name, and reasoning about which of those
calls happen before or after a declared train/test split. Every limit below
follows from one of three narrower facts: a function call whose target it
cannot resolve to a name, an argument shape it does not read, or a file it
never opens.

**A call the scan cannot resolve to a name.** Python lets you call a
function through a level of indirection the scan does not follow. Dynamic
dispatch — calling `getattr(model, "fit")(data)`, or looking a function up
in a dictionary with `handlers["fit"](data)` — draws nothing, because
neither shape is a direct call to something named `fit`. A bound method held
in a variable is the same problem in a different shape: `f = model.fit`
followed later by `f(data)` draws nothing either, because by the time `f` is
called, the scan has already lost the connection to `model.fit`. A fit call
performed inside a helper function or a module the entrypoint imports is
invisible for the same underlying reason — only the one declared entrypoint
file is read. And a train/test split performed through an alias or through
an imported helper function, rather than a direct call the scan recognises
by name, is read as if the file never split at all; the fit calls after it
can then be misclassified as fit-before-split.

**An argument shape the scan does not read.** `DSX-CODE-021` looks for a
recognised training-frame name — one that starts with something like
`X_train` or `train_df`, kept in the `TRAINING_FRAME_NAMES` list — as the
first argument to a fit call made at or after the split. A keyword whose
name is outside the small set the scan recognises, such as
`model.fit(training_frame=data)`, draws nothing: this is a deliberate trade,
accepting one kind of miss in exchange for never mistaking an unrelated
keyword's value for the frame you fitted on. A starred first argument —
`model.fit(*args)` — is skipped rather than resolved, for the same reason. A
full, unsplit frame renamed to something that merely *looks* like a training
frame — `X_train_like = data` followed by `model.fit(X_train_like)` — passes,
because the check matches the variable's name against the recognised list
and never follows the assignment back to what the name actually refers to;
this is a laundered name, and it is a real leak the scan cannot see.

**A file the scan never opens.** Only your declared entrypoint is read.
Anything that exists only while your code is running — source assembled as
a string and executed with `exec` or `eval`, code generated at runtime, or a
data frame mutated between the split and the fit — cannot be seen by a tool
that reads a file rather than running one. This is worth restating plainly
because it changed direction in this phase: `exec`-assembled fit-shaped
source used to be blocked by the old text scan (which could see the fit
call's text sitting inside the string literal) and is not blocked now — see
the announcement above.

**A notebook file the scan cannot decode, or whose shape it cannot trust.**
Four things belong here.

First, the deliberate asymmetry between the two reads. A Python file whose
bytes are not valid UTF-8 is still scanned, with the bytes that would not
decode replaced, because most of such a file is still readable code. A
notebook file carrying that same defect is REJECTED OUTRIGHT instead
— the gate exits 2 with an error message and does not run any check at all,
rather than exiting 0 with a NOT-scanned pass line — because a notebook
must decode as a whole before any of it can be read, and a partial decode
would let the tool claim it parsed text it could not actually read. This is
not a NOT-scanned outcome and must not be described as one: it is a
blocking "could not run" outcome, the same family a missing spec file
produces, and it predates this plan untouched. The two file types don't
just differ in degree here — one keeps running and reports a pass, the
other stops the run and reports an error.

Second, a notebook nested more deeply than the running interpreter's
recursion limit allows is reported as NOT scanned rather than scanned. This
is a guard against a crash, and it means a legitimately very deeply nested
document reads as unscannable.

Third, no size limit is applied before the file is read, so a large enough
declared entrypoint can exhaust memory; where that surfaces as a memory
error during the read it is reported as NOT scanned, and where it does not,
it is not caught.

Fourth, and most important to state plainly: NOT scanned is a passing
outcome. It exits 0 and produces no finding. In the default plain-text
render — no `--json`, no `--report` — the line that says the file was
not scanned prints only when `--verbose` is passed, so a notebook that
is corrupted, by accident or on purpose, makes the leak scan go quiet
rather than loud there, and a reader running the default renderer
without `--verbose` sees a passing code check that looks like a clean
scan. `--json` output and an `--report FILE.md` markdown report both
carry this line unconditionally — inside `passed_checks` and the
`## Passed` section respectively — regardless of `--verbose`, so a
machine-readable or archived report always carries the signal even when
the terminal does not. This is a limit of the default terminal output,
not one that is fixed.

**What the fallback text scan additionally misses, and when it runs.** When
a file cannot be parsed as Python — a syntax error, an unrepaired notebook
magic command, or genuinely non-Python content — the scan falls back to the
older, per-physical-line text match, and every finding produced that way
says so. The fallback cannot see a fit call split across a backslash-
continued line; it cannot resolve an argument that is itself a function
call; and every text guard in this module checks only for a comment that
*starts* a line, so a trailing comment on an otherwise real line of code
still reaches the pattern match. Concretely: `z = 1  # scaler.fit(data)` on
the fallback path still blocks at CRITICAL, even though the fit call lives
entirely inside a comment — a persisting false positive on that one path
that this phase did not close, named here rather than left for a user to
discover on their own.

The fallback's keyword-order fix, announced above, has its own stated edge.
It resolves a recognised training-frame keyword arriving after up to eight
other, non-recognised keyword arguments in the same call. A call whose
recognised keyword arrives after more than eight others still draws nothing
on the fallback, even though the path that reads the file as real Python
still catches it — a bound, not an oversight, and pinned by this project's
own tests so a future change cannot silently narrow or widen it without
someone noticing.

The docstring and prose fixes announced above, for `DSX-CODE-020`,
`DSX-CODE-030` and `DSX-CODE-031`, apply only on the path that reads the
file as real Python. The fallback has no parsed structure to build that
mask from, so on the fallback the mask is empty, and a docstring or a bare
string statement describing a cleaning idiom, or mentioning a
statistical-test call on the target column, still blocks `DSX-CODE-020`,
`DSX-CODE-030` and `DSX-CODE-031` there — the same false alarm this phase
just closed on the other path, still open on this one. This is the honest
residue of that fix, not a separate limit.

The prose mask that closes those three false alarms has a boundary worth
stating on its own, because it becomes visible for `DSX-CODE-020` for the
first time here. The mask covers a whole bare string statement and the
strictly interior lines of a multi-line string, but it deliberately spares
the opening line and the closing line of a multi-line string, because
either one can carry real code alongside the quotation marks. A full-frame
cleaning idiom written on the same physical line as a multi-line string's
opening quote — or its closing quote — therefore still fires
`DSX-CODE-020`. The sparing is deliberate, and it buys one specific
guarantee: the mask never hides a line that also carries executable code.

Two related limits stay open on the primary (non-fallback) text checks
that never moved to the parser and were never given the prose mask at all:
`DSX-CODE-002` (scaler fitted on the full frame) and `DSX-CODE-003` (a
resampler such as SMOTE named before the split) still match a comment that
merely *mentions* the pattern they look for — `# StandardScaler().fit_transform(X)`
still blocks `DSX-CODE-002`, and `# never use SMOTE before the split` still
blocks `DSX-CODE-003`. This is a different defect from the mask described
above, not a smaller version of it: `DSX-CODE-002` and `DSX-CODE-003` have
no leading-comment guard in their text loops at all, so even a single
leading `#` does not spare them, while `DSX-CODE-020`, `DSX-CODE-030` and
`DSX-CODE-031` do have the mask now on the path that reads the file as real
Python, and lose it only on the fallback described above. Closing the
`DSX-CODE-002` / `DSX-CODE-003` gap was outside this remediation's scope,
and it stays open. Notebooks reach the fallback more often than plain
Python files do, because an introspection line such as `df.head?` does not
parse and is not repaired.

**The notebook line-number convention is a standing limit, not a fix.** For
a Jupyter notebook, the "Line N" a finding reports counts lines in the
reconstructed concatenation of the notebook's code cells — with each
markdown cell replaced by a matching number of blank lines so that code-cell
line numbers do not shift — not the line of the raw `.ipynb` file on disk,
which a reader could not usefully open at that offset in either case. This
change preserves that numbering exactly; it does not attempt to fix it.

**The interpreter you run the scan with is now part of the answer.** The
scan accepts whatever version of the Python language grammar the running
interpreter accepts. A file using newer syntax can take the parser path on
one machine and the weaker fallback path on another, for byte-identical
input. This is disclosed in the tool's recorded decisions rather than left
for someone to discover by getting two different answers on two machines.

**Where these numbers come from, and why two of them are never compared
directly.** This phase's own before-and-after count of leaky-call variants
is a committed, runnable test — not a number asserted in prose — and is the
figure this document stands behind. A second, earlier count exists in
[`11.1.1-RESEARCH.md`](../.planning/milestones/v2.0.0-phases/11.1.1-detection-code-hardening-inserted/11.1.1-RESEARCH.md):
thirteen variants, six caught and seven missed, measured on 2026-08-21
against only the `DSX-CODE-021` argument-extraction path — a narrower
instrument than the end-to-end count above, and cited here as the
before-figure for that one path, not as a second reading of the same thing.
An older, uncommitted figure circulated during an earlier verification
session and has no committed enumeration behind it anywhere in this
repository; it is not repeated here, and is not printed alongside either of
the two figures above.

None of this makes `DSX-CODE-001`, `DSX-CODE-021`, or any other
`DSX-CODE-*` check sound, complete or exhaustive. Treat a clean scan as
one input to your own judgement, not as a verdict.
