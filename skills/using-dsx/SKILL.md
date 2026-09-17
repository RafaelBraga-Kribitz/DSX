---
name: using-dsx
description: Use when starting any conversation that touches data — an analysis, a metric, an experiment, a model, a chart, a dashboard, a readout. Establishes the DSX contract before anything else happens, including clarifying questions.
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute one specific task, ignore this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If the work touches data — a number someone will act on, a metric, an A/B test, a model, a chart, a dashboard, a report — it runs under DSX. This is not negotiable. You cannot rationalise your way out of it.
</EXTREMELY-IMPORTANT>

## The two rules

**1. No data is touched before `ANALYSIS-SPEC.yaml` exists.** The spec is the contract every later check reads: the decision it serves, the question type, the design, the metric definitions, the claims. Writing it after the analysis turns a decision rule into a rationalisation. Run `dsx init`, then invoke `dsx-scope-analysis`.

**2. No result is claimed before `dsx audit` passes.** Not "should be significant". Not "looks right". Run it, read the exit code, and say what it said:

| Exit | Meaning | What you do |
|---|---|---|
| 0 | Pass | State the result, with the numbers. |
| 1 | Blocked | State the finding codes. Fix the spec or the analysis. Do not reword the claim around a finding. |
| 2 | Could not run | Say so plainly. A gate that could not run is not a gate that passed. |

A Stop hook runs the audit again before the session can end and refuses to finish on exit 1. Better you run it first.

## Which skill, when

Invoke the skill BEFORE responding, exploring, or asking clarifying questions. Announce "Using dsx-<name> to <purpose>."

| The work is… | Invoke |
|---|---|
| A question arriving as "can you look into X" | `dsx-scope-analysis` |
| A new or changed dataset | `dsx-explore-data` |
| An A/B test, a quasi-experiment, or a readout of one | `dsx-design-experiment` |
| A metric, a dashboard, or two sources that disagree | `dsx-define-metrics` |
| Classification, regression, forecasting | `dsx-build-model` |
| Any chart or figure | `dsx-visualize` |
| Reviewing figures someone else made | `dsx-chart-audit` |
| The executive summary, readout or report | `dsx-narrate` |
| Reviewing an analysis before it ships | `dsx-review-analysis` |

On a fresh question, `dsx-scope-analysis` comes first. Then the domain skill.

## Red flags — you are rationalising

| Thought | Reality |
|---|---|
| "It's just a quick number" | Quick numbers get forwarded. Spec it. |
| "The effect is obviously real" | Obvious is not identified. What is the design? |
| "Not significant, so no effect" | An underpowered null says nothing. What was the power? |
| "I'll write the spec after I see the data" | That is the rationalisation the spec exists to prevent. |
| "Three metrics moved" | At α = 0.05 with no correction, one of them was expected to. |
| "The split is random, that's fine" | On time-ordered data a random split leaks the future. |
| "The chart makes the point" | Check the baseline, the axis, the encoding. `dsx check viz`. |
| "The audit is being pedantic" | The audit is deterministic. Argue with the spec, not the gate. |
| "I'll run the audit at the end" | The Stop hook will. Better you than it. |

## What DSX does not do

It checks declarations against declarations. A spec that lies passes. Your job is to make the spec true, and to say what you could not verify.

## User instructions

Direct instructions from your human partner, and files such as CLAUDE.md or AGENTS.md, take precedence over this skill. `DSX_STOP_GATE=off` disables the end-of-session gate for one shell.
