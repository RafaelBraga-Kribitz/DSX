---
name: ratchet
description: >
  Autonomous ratchet loop for agent improvement. Configures optimization targets,
  then loops: improve agent → run agent → eval → keep or revert. Uses the
  /recursive-improve pipeline internally with auto-approval. Invoke with /ratchet
  or "run the ratchet loop", "improve my agent overnight", "autonomous improvement".
  Also used by Otto (MLOps) to schedule autonomous improvement of MADS agents.
when_to_use: ratchet, autonomous improvement, improve overnight, improvement loop, autonomous agent improvement, self-improving agent, keep or revert, otto improve mads
allowed-tools: Bash Read Write Edit Glob Grep
---

# /ratchet — Autonomous Improvement Loop

An autoresearch-style ratchet that continuously improves your agent. Each iteration:
improve → run agent → eval → keep (if better) or revert (if worse) → repeat.

## Step 1: Configure (MANDATORY)

Ask the user to confirm configuration before starting the loop. Never proceed without explicit confirmation.

Questions:
1. **Objective** — what do you want to improve?
2. **Agent run command** — shell command that runs the agent and generates traces
3. **Traces directory** — where traces are written (default: `eval/traces`)
4. **Metrics to optimize** — which metrics, direction (minimize/maximize), weight
5. **Stopping conditions** — max iterations (default: 20), max duration hours (default: 8), plateau patience (default: 3)

Write confirmed config to `program.md`. **Do NOT proceed to Step 2 until confirmed.**

## Step 2: Create ratchet branch

```bash
recursive-improve ratchet branch
```

Creates `ri/ratchet-<timestamp>` so all changes happen on a dedicated branch.

## Step 3: Establish baseline

```bash
recursive-improve ratchet eval --config program.md
```

Record the `score` as baseline.

## Step 4: Ratchet Loop

For each iteration:

### 4a. Run the improvement pipeline
Execute full `/recursive-improve` (stages 0–7) with:
- **Stage 6: AUTO-APPROVE** — do not ask the user
- **Stage 7: NO IMPROVEMENT BRANCH** — apply fixes directly to working tree

### 4b. Run the agent
```bash
rm -f {traces_dir}/*.json
{agent_run_command}
```

### 4c. Evaluate
```bash
recursive-improve ratchet eval --config program.md
```

### 4d. Keep or revert
- If `new_score > baseline_score`: `recursive-improve ratchet commit {iteration} {new_score}` → **KEEP**
- If `new_score <= baseline_score`: `recursive-improve ratchet revert` → **REVERT**

### 4e. Log the iteration
```bash
recursive-improve ratchet log {iteration} {score} {keep|revert} ...
```

### 4f. Check stopping conditions
```bash
recursive-improve ratchet status --config program.md
```

Stop if: iterations >= max_iterations, elapsed time exceeds max_duration_hours, or plateau_count >= plateau_patience.

## Step 5: Summary

Tell the user:
- **Branch:** `ri/ratchet-<timestamp>` has all kept improvements
- **Review:** `git diff main...ri/ratchet-<timestamp>`
- **Merge:** `git merge ri/ratchet-<timestamp>`
- **Dashboard:** `recursive-improve dashboard`

## Rules

- Do NOT ask for approval during the loop — this is autonomous
- ALWAYS revert on regression — never keep a worse score
- ALWAYS log every iteration
- Keep fixes small and targeted
- Read the ratchet log before each improvement step to avoid repeating failed approaches
