---
name: recursive-improve
description: >
  End-to-end agent improvement pipeline. Analyzes raw execution traces, extracts
  insights, manages a skillbook, gathers domain context, defines metrics, builds a
  rubric, creates a prioritized action plan, presents it for review, and implements
  approved fixes. Trigger when the user says "improve my agent", "run the improvement
  pipeline", "apply insights", "/recursive-improve", when eval/traces/ contains trace files,
  or when any MADS agent suggests running improvement after a project phase.
when_to_use: improve agent, run improvement pipeline, apply insights, recursive improve, agent traces, self-improve, improve carla, improve diego, improve eva, improve marco, improve petra, improve otto, improve mads
allowed-tools: Read Write Edit Bash Glob Grep
---

# recursive-improve: Agent Improvement Pipeline

End-to-end pipeline: trace analysis → skill extraction → domain context → metrics → rubric → action plan → review → fixes.

## MADS Integration

This skill is embedded in all BMADS-MKT agents. Each agent:
1. Instruments their sessions with `ri.patch()` + `ri.session()` to generate traces
2. Accumulates traces in `eval/traces/` over multiple project runs
3. Invokes `/recursive-improve` to analyze patterns and apply targeted improvements
4. Uses `/benchmark` to measure metric deltas
5. Uses `/ratchet` for autonomous overnight improvement

The improvement loop compounds: each project makes the agents better for the next one.

## Prerequisites

Traces must exist in `eval/traces/`. If they don't:
- Ask the user for their traces directory
- Copy `.json`, `.md`, and `.toon` files into `eval/traces/`

**Skip condition:** If `eval/stage1_insights_summary.md` already exists, skip Stages 0 and 1.

---

## Stage 0: Trace Analysis

Analyze raw execution traces to extract learnings. Uses ACE's recursive reflector methodology — a structured 6-phase strategy.

### Phase 1: Discover
Map the data shape and inventory. Catalog what you have without judging outcomes yet.

### Phase 2: Derive Evaluation Criteria
Define specific evaluation criteria based on discovery: what to look for, what a violation looks like.

### Phase 3: Survey
Read ALL traces (if ≤ 20) or stratified sample (if > 20, target ~15 or 30%).

### Phase 4: Categorize
Group by task type and outcome. Select 2-3 deep-dive targets prioritizing:
- Divergent outcomes (same task, one succeeded, one failed)
- Confident-but-wrong traces
- Most common failure pattern

### Phase 5: Deep-dive
Re-read the FULL raw trace for each target. Two passes:
- **Pass 1 — Verification:** Separate what the agent claimed from what data it received
- **Pass 2 — Root cause analysis:** What should the agent do differently?

### Phase 6: Synthesize
Produce atomic learnings with: learning text, atomicity score, evidence, severity, category (`code_fix` | `prompt_fix` | `process_fix`).

Output: `eval/stage0_trace_analysis.md`

---

## Stage 1: Skill Management

Transform raw learnings into a structured skillbook with quality gates.

- Quality gate: atomicity score (reject < 0.40, split 0.40-0.69, accept ≥ 0.85)
- Format as imperative commands (not observations)
- Deduplicate against existing skillbook (>70% semantic overlap = UPDATE not ADD)
- Reject meta-commentary, vague terms, overgeneralizations

Output: `eval/skillbook.json` + `eval/stage1_insights_summary.md`

---

## Stage 2: Domain Context Gathering

Detect trace format, architecture (single vs multi-agent), system prompt, tool definitions, domain documentation, and behavior patterns.

Output: `eval/stage2_domain_context.md`

---

## Stage 3: Metrics and Programmatic Analysis

Define metrics from insights, implement as code, run, review (3-iteration cap).

```bash
recursive-improve eval eval/traces --branch main
python eval/compute_baselines.py --traces-dir eval/traces --output eval/baseline_metrics.json
recursive-improve store-baseline
```

Output: `eval/compute_baselines.py` + `eval/baseline_metrics.json`

---

## Stage 4: Rubric Definition

Tier each metric (LEADING / LAGGING / QUALITY). Flag low-confidence baselines (n < 5). Set improvement direction. Map every insight to a metric.

Output: `eval/baseline_metrics.md`

---

## Stage 5: Action Plan

Triage each insight: discard / code-fix / prompt-fix. Prioritize by:
```
Priority Score = Impact × Confidence × Tier Bonus ÷ Risk Factor
```

Output: `eval/action_plan.md`

---

## Stage 6: Human-In-The-Loop Gate

Present the action plan for informed approval.

Three options:
- **[A] Approve all** — create branch, implement all fixes
- **[B] Approve with modifications** — walk through each fix individually
- **[C] Reject** — collect feedback, re-run Stage 5

All fixes are applied on a dedicated branch (`ri/improve-<YYYYMMDD-HHMMSS>`), not directly on the current branch.

**Do NOT auto-approve. Do NOT proceed until clear approval is recorded.**

---

## Stage 7: Fix Implementation

For each approved fix:
1. Create improvement branch: `git checkout -b ri/improve-$(date +%Y%m%d-%H%M%S)`
2. Implement minimal, targeted changes
3. Log to `eval/changes_log.md`
4. Commit with descriptive message

**Do NOT modify trace files. Do NOT make changes beyond what was recommended.**
