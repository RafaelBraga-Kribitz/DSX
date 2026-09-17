# Changelog notes

Migration and behaviour-change notes moved here from the README's
[The contract](../README.md#the-contract) section, verbatim.

## Migrating a pre-v2.0.0 spec

From v2.0.0, `validity_frame:` is required starting at the `plan` gate, at
CRITICAL severity — so a spec written against v1.x begins blocking the moment
you upgrade. The supported path is to fill the frame: `estimand`, `units`,
`identification`, `dependence`, `interference`, `triggering`, `stability`,
`sampling_frame`, `missingness`, `measurement`.

The supported *interim* path is the existing `suppressions[]` mechanism (see
[Finding suppressions](../README.md#finding-suppressions) below): declare the missing-frame
findings there with a `reason` and an `authority` naming a real ADR or SPEC
file. Suppressions apply after checks and before the blocking threshold, and
an unknown code aborts the run with exit 2.

Say this plainly: a suppression is an attributable, dated decision with a
named authority, not a way to make the finding go away. A suppression with no
resolvable `authority` reference already produces `DSX-SPEC-070` — the
grandfather path is deliberate, not silent.

## The entrypoint leak scan now parses your code

Phase 11.1.1 changed how `DSX-CODE-001` and `DSX-CODE-021` (fit-before-split
and fit-after-split-on-the-wrong-frame) decide what a line of your entrypoint
means. The scan used to read the file as plain text, matching patterns
against each physical line's characters in turn. It now reads the file as
Python — using the standard library's abstract syntax tree (AST), the same
structure a compiler builds before running your code — and looks directly at
which function calls exist and what they are called on. When a file cannot
be parsed as Python, the scan falls back to the old text-matching approach,
and it says so on every finding it produces from that fallback.

**Some files that are blocked today will start passing — read this part
first, because nobody files a bug about a gate that stopped complaining.**
A module, class or function docstring that merely mentions a fit call —
for example a comment reading "we never call `scaler.fit(X)` on the full
frame" — used to block at CRITICAL severity, because the old scan matched
the text of the sentence, not the code. It no longer does, because a
docstring holds no function call for the new scan to find. The same is true
of a Jupyter notebook markdown cell that describes a leakage rule in prose.
Both were false alarms, and both are now fixed. In the same breath: code
assembled as a string and run with Python's `exec` or `eval` functions used
to be blocked — the old text scan could see the fit call written inside the
string — and it is **not** blocked after this change, because a string is
just data to a real Python parser, not a function call. This is a genuine
leak the new scan cannot see, and it belongs here rather than buried in the
limits section below.

This phase closes three more false alarms of the same shape, for three
different checks — read this part first too, for the same reason as above.
A module, class or function docstring, a bare string statement, or the
interior lines of a multi-line string — writing that merely *describes* a
full-frame cleaning idiom rather than performing one, for example a
sentence saying the file deliberately avoids filling missing values with a
column's average before splitting — used to block at CRITICAL severity
under `DSX-CODE-020`. It no longer does, for the same reason as the
docstring case above: the sentence describes the operation, and the
executable code never actually calls it. The same is true of `DSX-CODE-030`
(CRITICAL) and `DSX-CODE-031` (HIGH) when the prose mentions a
statistical-test call on the column your model targets. A second, related
shape closes alongside these three: `DSX-CODE-030` and `DSX-CODE-031`
decide whether a statistical-test call is about your target column by
checking whether that call's own line, or one of the three lines
immediately above it, mentions the target column's name. A mention of the
target column that appears only inside a docstring or a bare string
statement in that three-line window no longer counts — so a real
statistical-test call sitting a few lines below an explanatory sentence
stops being blocked on the strength of that sentence alone. Say this
plainly, for all four of these: in every case the executable code never
performed the operation the prose sentence described, so removing the
block is a corrected false alarm, not a weakened check. A file blocked
yesterday for any of these reasons can pass today.

**Some files that pass today will start failing, and every one of those new
findings is a true positive** — the leak was always in the file, and the old
scan could not see it. The shapes a reader can match against their own code:
a space or a tab before the opening parenthesis (`model.fit (df)`); a fit
call split across two lines by a trailing backslash or by an open
parenthesis; a fit call written with a keyword argument, such as
`model.fit(X=data, y=target)`; a second fit call on a line that also has a
safe first one, joined by a semicolon; a fit call whose argument is itself
another function call (`model.fit(loader.get_full_frame())`); and
`model.partial_fit(data)` written after the split, which used to draw
nothing there even though the same call before the split already blocked.

One more true positive belongs in this list, narrower than the rest because
it applies only on the FALLBACK path — the weaker text scan that runs when
a file cannot be parsed as Python at all. A fit call whose recognised
training-frame keyword arrives after another keyword — `model.fit(y=y_train,
X=full_frame)`, or the same call with several unrelated keywords in front of
the frame keyword — used to draw nothing there, even though the identical
call already blocked on the path that reads the file as real Python. It
blocks on the fallback now too. This is a true positive, not a new rule: the
leak was always in the file, and the parser-based path already caught it —
only the weaker fallback scan changed to agree with it. This matters only
for the files that reach the fallback in the first place — files that
cannot be parsed as Python at all, for example a genuine syntax error or an
unrepaired notebook command — so a file that parses cleanly is unaffected by
this particular fix.

There is also a substitution worth naming plainly, rather than filing it
under "stricter": a train/test split marker that appears only as a string
literal, or is reached only through an alias or a helper function imported
from elsewhere, no longer counts as a declared split. A file built that way
may now draw `DSX-CODE-001` or `DSX-CODE-010` where it used to draw
`DSX-CODE-021` instead. Where that happens, `DSX-CODE-010`'s own wording —
"entrypoint has no declared split marker" — can be false for a file that
plainly contains one; this document says so here because a finding's own
text is not the place to discover a contradiction.

The reported line number follows one rule: it is the physical line on which
the fit call's expression *begins*. For a call spread across several
physical lines, the reported line can move earlier than a per-line scan
would have reported it, and never later. No finding that fired before this
change stops firing because of that rule.

Two smaller, cosmetic changes. First, when a `DSX-CODE-021` finding quotes
the argument you fitted on, a token written with double quotes is now
rendered with single quotes (`data[["Age"]]` becomes `data[['Age']]`); the
verdict is unaffected, only the punctuation in the quoted text. Second,
every report now carries one extra line naming which scan path ran — even
the project's own clean example gains this line, which is a visible,
intended change to that fixture's output, not an accident.

One more change belongs here, stated plainly rather than as a footnote,
because it changes what a caller sees rather than what the scan catches. A
Jupyter notebook file can be valid JSON and still not be a notebook. This
now covers: a document that is not an object at all; a document whose list
of cells holds something that is not an object; a document with no list of
cells, or one whose `cells` value is a number, a boolean or an object; a
cell whose source is a list holding something that is not text; a cell
whose source is neither text nor a list; and a document nested too deeply
to decode. Before this phase, a file shaped like any of these crashed the
whole run: a raw Python error and exit code 1 — the same number the gate
uses to mean "this file was scanned and blocked." A caller reading only
the exit code could not tell a genuine leak apart from a notebook the tool
never managed to read at all. It is now reported as NOT scanned, the same
outcome the tool already gives a file it cannot open at all, so the exit
code and the report both say what actually happened. In the other
direction, a notebook that legitimately contains no cells is still read
and scanned as an empty file, not reported as unreadable.

When a file cannot be parsed as Python at all — a syntax error, an
unsupported construct, or a file that is not really Python — the weaker,
older text scan runs in its place, and every finding it produces says so in
its own detail text, in the report's summary of what passed, and in the
recorded decision for that run. A clean result from the fallback scan is
weaker evidence than a clean result from the parser, and the tool now tells
you which one you got, rather than leaving you to guess.

If a new finding appears in your file, the fix has not changed: split the
data first, then fit only on the training fold — the same remedy the
finding itself already prints.
