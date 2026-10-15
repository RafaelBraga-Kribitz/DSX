# Outcome experiment: does DSX make answers right more often?

DSX's calibration measures DSX itself: how many seeded flaws it catches in the
known-bad corpus, and how many clean analyses it leaves alone. Neither number
says whether an agent working under DSX gets more answers right. This
experiment measures that directly, on a public benchmark with a hidden answer
key.

**Status: not yet run.** This folder holds the protocol and the scorer
(`dsx outcome`). No result exists, and none should be quoted until both arms
have been run as described here.

## The benchmark

DataSpace (HKUST DIAL; arXiv 2608.03451; code at
`github.com/HKUSTDial/DataSpace`) is the benchmark behind the KDD Cup 2026
Data Agents track: 410 tasks over 7,439 files (about 15 GB) in CSV, JSON,
SQLite, Markdown, PDF and video. Its paper reports the best of six frontier
models in five harnesses at 66.34%, and a 15.36-point spread from changing the
harness alone with the model held fixed. That spread is why the comparison
below is worth making: the harness is exactly what DSX changes.

These figures come from secondary summaries, because this repository's
development container could not reach arxiv.org. Check them against the paper
before citing them.

## Design

A paired comparison: every task is answered by both arms, so each task is its
own control.

| | Control | Treatment |
|---|---|---|
| Agent and model | fixed | the same |
| Tools, prompt, budget | fixed | the same |
| DSX | not installed | installed; `dsx scout` available; the Stop hook runs `dsx audit` and the agent must clear it before submitting |
| Output per task | an answer | an answer, or `blocked` if the gate never cleared |

- **Primary outcome:** accuracy over all tasks, with a blocked or missing task
  counted as wrong. A gate that blocked everything must not look accurate.
- **Primary test:** the paired difference in accuracy (treatment minus control)
  with the exact McNemar test, two-sided, α = 0.05, one test. Everything else
  is secondary and reported as such.
- **Secondary outcomes:** accuracy over answered tasks only (does the gate
  remove wrong answers or right ones?); how control did on the tasks treatment
  blocked; accuracy by task category, for the categories DataSpace names as
  bottlenecks (joins and multimodal evidence). Per-category tests are
  exploratory and uncorrected, and are labelled that way.
- **Expected direction, stated in advance:** the treatment should help most on
  multi-table join tasks, where `dsx scout` measures fan-out, and least on
  document and video tasks, which DSX does not read.

### Is 410 tasks enough?

McNemar's power depends on the discordant tasks, not on the total. If the two
arms disagree on 20% of tasks (82 of 410) and the treatment wins 60% of those
disagreements, the expected difference is 4 points and the exact test has
about 40% power (exact calculation, conditioning on
82 discordant tasks). A real but small effect can be missed. Run each arm with
several seeds if the budget allows, and report the result as an interval, not
a verdict. Fix the seeds before the first run.

## Procedure

1. **Freeze everything before the first run.** Commit the agent prompt, the
   model identifier, the tool list, the budgets, the seeds, the DSX version,
   and this protocol. Changing any of them after seeing a result makes the
   result exploratory.
2. **Build the key.** Convert DataSpace's gold answers to JSON Lines, one task
   per line: `{"task_id": "…", "answer": …, "category": "…"}`. An answer is a
   scalar, a list of rows, or `{"columns": […], "rows": [[…], …]}`.
3. **Run the control arm** and write `control.jsonl`:
   `{"task_id": "…", "answer": …}` per task, with `"status": "error"` for a
   crash.
4. **Run the treatment arm** the same way into `treatment.jsonl`, with
   `"status": "blocked"` for a task whose gate never cleared.
5. **Score:**

   ```bash
   dsx outcome --key key.jsonl --control control.jsonl --treatment treatment.jsonl --json > RESULT.json
   ```

6. **Report** the primary difference with its interval and p-value first, then
   the secondary outcomes, then every deviation from this protocol.

The development split of DataSpace can be used to debug the harness. Score the
held-out tasks once.

## Matching rules

`dsx outcome` compares after normalising: strings ignore case and surrounding
whitespace; numbers are rounded to four significant digits (`--sig-digits`);
tables ignore row order and, when columns are named, column order; duplicate
rows count. A percentage written `12%` does not match a key of `0.12`.
DataSpace's own scorer is the reference: if the two disagree on a task, report
both and use DataSpace's.
