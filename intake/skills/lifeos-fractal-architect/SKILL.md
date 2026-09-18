---
name: lifeos-fractal-architect
description: >
  Use when designing, operating, or refactoring the LifeOS fractal system
  across Obsidian, GitHub, and Google Calendar. Invoke for: raw capture triage,
  cross-tool planning, review cadence execution, detected mirror/canonical
  divergence, confidence-gated autonomous operations, and deployment profile
  transitions. Do NOT use for off-LifeOS Q&A, financial/security execution,
  or purely local formatting with no cross-tool state impact.
---

# LifeOS Fractal System Architect

## Overview

Operate a deterministic LifeOS: **simple universal rules at top, complexity only at lower layers**. Enforce facet-level source of truth, confidence-gated autonomy, and **no hard delete** (export + exclude-from-queries for terminal quarantine). Every invocation returns a decision log, state diff, confidence with evidence, and — only when gated or blocked — the next human input required.

**Strategy brief (intent, scope, principles, rollout):** `strategy-brief.md`  
**Full authoritative architecture:** `~/.claude/notebooklm_lifeos_fractal_brief.md` → section *Authoritative architecture*  
**Harness stack and UUID rules:** `references/fractal-claude-harness.md`

---

## Fractal Simplicity Law (MUST enforce in all outputs)

1. Top layers (Principles, GovernanceRules) stay short and stable. No tool playbooks, no long examples at those layers.
2. Child layers add detail only if: they inherit parent constraints; do not contradict parent MUST/NEVER; add measurable value; state their scope explicitly.
3. **Naming:** global grammar at root (`<scope>-<topic>--<qualifier>`, lowercase, hyphens, max 64 chars). PARA buckets (Areas, Projects, Resources) MAY add scoped suffix rules on top of global grammar. They MUST NOT break it.

---

## Fractal Claude Harness (routing)

| Layer | Path | Purpose | Size target |
|-------|------|---------|-------------|
| Global toggles | `~/.claude/settings.json` | Env, budgets, feature flags only | Small JSON |
| Root memory | `~/.claude/CLAUDE.md` | Heuristics + routing table | ≤ 400 words |
| Domain | `<area>/CLAUDE.md` | Area decision trees + contracts | ≤ 800 words |
| Project | `<project>/CLAUDE.md` | Project contracts + naming extensions | ≤ 1200 words |
| Execution | This skill + `references/*` | Dense procedures, templates, checklists | Unbounded, load on demand |

**NEVER** duplicate the same MUST/NEVER across layers. State it once at the highest appropriate layer; link downward.

---

## Triggers

**Invoke this skill when:**
- Raw inbox item needs triage (IDI workflow)
- Action item surfaces from note or conversation (ACE workflow)
- Issue with estimate is ready for scheduling (COG workflow)
- Mirror and canonical system disagree on any facet
- Running a daily, weekly, monthly, quarterly, or annual review
- Evaluating or executing a deployment profile transition
- Auditing DLQ or reconciling after outage/lock expiry

**Do NOT invoke when:**
- Pure conversational Q&A with no tool state changes
- Off-LifeOS knowledge question
- User requests financial or security write operations (blocked category; escalate immediately)
- Request is purely local text formatting with zero cross-tool impact

---

## Mandatory Decisions (all invocations)

Before any mutating operation, resolve these explicitly:

1. **Facet owner:** use the table below. If ambiguous, default to the canonical system.
2. **Conflict resolution:** apply precedence order (capacity → execution state → containment → knowledge synthesis → convenience).
3. **Retention:** no hard delete. Terminal action: export + exclude-from-queries. Use voided / quarantine / archive lifecycle.
4. **Lock state:** check `human_override_lock` and `sync_locked` before any write. Reconcile first if either is set.

### Facet Ownership Table

| Facet | Canonical | Mirror | Sync |
|-------|-----------|--------|------|
| Object UUIDs | Originating system (minter) | Reference only | Origin → mirror |
| Execution state | GitHub | Obsidian (queries only) | GitHub → Obsidian |
| Time / capacity | Google Calendar | Obsidian daily note | GCal → Obsidian |
| Narrative / context | Obsidian | GitHub (snippet + link) | Obsidian → GitHub |
| Note graph | Obsidian | — | — |
| Policy registry | Versioned repo doc | — | — |

---

## Confidence and Evidence (mandatory for every mutation)

```yaml
confidence: 0–100
evidence:
  schema_validation_pass: bool    # required
  source_coverage_count: int      # required
  conflict_check_pass: bool       # required
```

**Missing any evidence field → force `confidence < APPROVAL_MIN` → blocked or gated. Never guess.**

**Bands (registry defaults; tune via Canonical Policy Variable Registry):**

| Condition | Band | Behavior |
|-----------|------|----------|
| `confidence >= AUTO_EXECUTE_MIN` (default 90) | Auto | Execute; write audit row on real state change |
| `APPROVAL_MIN <= confidence < AUTO_EXECUTE_MIN` (75–89) | Gated | Stage in Pending Approval queue; await human confirm |
| `confidence < APPROVAL_MIN` (default 75) | Blocked | Queue in DLQ; human triage; no mutation |

**Equality rule:** `>=` and `<` are inclusive/exclusive as written. No rounding up.

---

## Three Core Workflows

### Workflow 1 — IDI (Knowledge Inbox Processing)

**Trigger:** Unprocessed inbox note or fleeting note > 7 days old.  
**Input:** Raw markdown / extract with optional source metadata.  
**Process:** Inbox → Digest (extract main claim, find existing links) → Integrate (permanent note + links).  
**Output:** JD-addressed Obsidian note; typed (atom / molecule / project-note / evergreen); YAML front matter present; H1 title is a single claim; `links_out >= MIN_LINKS_PER_ATOM` (default 2).  
**Owner:** Claude if `confidence >= AUTO_EXECUTE_MIN`. Human if gated or blocked.  
**Completion criteria:** Note exits inbox folder; YAML complete; links validated; `note_id` minted and stable.  
**Failure path:** `confidence < AUTO_EXECUTE_MIN` → set `sync_locked=true`; tag `#review-required`; surface in daily anchor.

### Workflow 2 — ACE (Action Extraction and Creation)

**Trigger:** Action item surfaces from a note, conversation, or review output.  
**Input:** Natural-language intent + optional `project_id` + optional `area_id`.  
**Process:** Action = verb-led title; Context = Obsidian note link / JD address; Execution = definition of done + evidence fields + estimate.  
**Output:** GitHub issue in ACE format with `note_id` link, `project_id`, `risk_class`, `estimate`.  
**Owner:** Claude if `confidence >= AUTO_EXECUTE_MIN`. Human if gated or blocked.  
**Completion criteria:** Issue exists in GitHub; ACE fields complete; `task_id` minted; linked back in Obsidian note.  
**Failure path:** `confidence < APPROVAL_MIN` → create issue in `Blocked/Clarify` state; assign to human; no auto-assignment.

### Workflow 3 — COG (Capacity and Calendar Scheduling)

**Trigger:** GitHub issue transitions to `Next` state and has an `estimate`.  
**Input:** Issue + estimate + current calendar free-time query.  
**Process:** Categorize (PARA area) → Organize (GitHub state transition) → Generate (staged GCal block proposal with issue URL, title, duration).  
**Output:** Staged GCal event (not confirmed); human receives approval request with proposed slot + issue context.  
**Owner:** Claude generates proposal in Profile B+. Human confirms all calendar events. Auto-confirm never permitted in any profile.  
**Completion criteria:** GCal event staged; human has received notification; issue remains in `Scheduled` state until human confirms.  
**Failure path:** API unavailable or capacity conflict → DLQ entry; add to `Scheduling_Queue` label; alert human in daily digest.

---

## Lifecycle State Machine

```
inbox → clarified → next → scheduled → inprogress → done
                                                       ↓
                                               voided (rollback)
                                                       ↓
                                                   archived
```

**Rules:**
- `transition(S,S)` = no_op. No audit row.
- Every real transition appends audit JSON: `{transition_id, timestamp, actor, from_state, to_state, reason, evidence}`.
- `voided` → `archived` is the only permitted path out of voided.
- `archived` is terminal. No transitions out.
- `quarantine` is a side state: object is hidden from queries; export + exclude is the exit.

---

## Retention Policy

| State | Retention | Visibility | Exit |
|-------|-----------|------------|------|
| Active | Indefinite | Default | → done / archived |
| Voided | 30 days | Hidden | → archived |
| Quarantine | 30 days | Admin only | Export + exclude-from-queries |
| Archived | Indefinite | Archive queries | Terminal; no exit |

---

## Autonomy Policy Summary

| Risk class | Example | Band | Rollback |
|---|---|---|---|
| Knowledge hygiene | IDI inbox → atom note | Auto (evidence ok) | `#quarantine` on failure |
| Task creation | ACE issue creation | Auto (evidence ok) | Mark `voided`; never delete |
| Review planning | Weekly stack proposal | Gated | Discard proposal |
| Time blocking | GCal block proposal | Gated (Profile B+) | Cancel staged event + notify |
| PR / comms draft | Draft pull request | Gated | Close PR with annotation |
| Auth / secrets | Any auth mutation | Blocked | Escalate to human |
| Financial write | Any account write | Blocked | Escalate to human |

**Kill-switch:** three confidence-below-APPROVAL_MIN mutating operations within one hour on same path → freeze mutations; alert human; reconcile before re-enabling.

---

## Review Cadence Triggers

| Cadence | Trigger | Owner | Key outputs |
|---|---|---|---|
| Daily (10–20 min) | Morning anchor | Human + Claude | Today focus list; DLQ sweep; carry-forward queue |
| Weekly (45–90 min) | End of work week | Human + Claude | Clean inbox; project health scores; weekly plan |
| Monthly (60–120 min) | First weekday of month | Human + Claude | Registry tuning proposals; archive report; KPI review |
| Quarterly (2–4 h) | Quarter boundary | Human + Claude | Strategic priorities; autonomy matrix update; quarterly execution map |
| Annual | Year boundary | Human | Architecture change log; design constraint refresh |

---

## Output Contract (every invocation)

Every skill invocation MUST return:

1. **Decision log** — which rule or facet drove each action taken.
2. **State diff** — before/after for every touched object.
3. **Confidence and evidence** — all three fields + numeric score.
4. **Transition audit** — JSON record for every real state change; omit on no_op.
5. **Next human input** — explicit queue item only when gated or blocked. Omit if auto-executed cleanly.

---

## Policy Variable Registry (defaults)

| Variable | Default | Review cadence |
|----------|---------|----------------|
| `AUTO_EXECUTE_MIN` | 90 | Annual |
| `APPROVAL_MIN` | 75 | Annual |
| `MAX_FOLDER_DEPTH` | 3 | Annual |
| `MIN_LINKS_PER_ATOM` | 2 | Monthly |
| `MAX_ACTIVE_PROJECTS` | 12 | Monthly |
| `CAPACITY_ALERT_PCT` | 20 | Monthly |

**Tuning rule:** Variables are adjusted only during the review cadence for their blast radius. Ad hoc mid-cycle changes require a human sign-off recorded in the audit trail.

---

## Deployment Profiles

| Profile | What Claude can do autonomously | Gate to next profile |
|---|---|---|
| **A (Advisory)** | Read, plan, generate proposals. No writes without explicit human approval. | Zero harmful automation incidents over defined window; human signs gate checklist |
| **B (Bounded)** | Auto IDI (vault hygiene); auto ACE (issue creation); staged COG proposals only. External writes gated. | DLQ SLA met; reconciliation drill passed; kill-switch drill logged |
| **C (Full Policy)** | All confidence-gated ops per autonomy matrix. Kill-switch + DLQ monitoring live. | Continuous; regress to B on kill-switch trigger |

---

## Service Degradation

If GitHub, GCal, or Obsidian vault is unreachable:
1. Enter read-only mode immediately.
2. Queue mutating ops locally with timestamps.
3. Emit single daily digest of queued ops.
4. Re-enter after health probe success: HTTP 200 + auth validity + successful read-only API probe. Document exact probes in project CLAUDE.md.
5. Run reconciliation before resuming any autonomous writes.

---

## Split-Brain Reconciliation

1. Detect stale mirror (clock skew or version mismatch).
2. Tie-break: canonical timestamp → monotonic version → actor priority (`human > system > claude`).
3. Loser diff: cap at 2000 characters; overflow → cold artifact URI in comment.
4. DLQ for missing dependency UUIDs; set `sync_locked=true`.
5. Clear `sync_locked` only after reconciliation passes for that object.

---

## Human Override Lock

Manual human edit sets `human_override_lock=true` on that object (default 24h, single-object scope).  
Claude MUST NOT mutate that object until lock expires AND reconciliation passes.  
If `sync_locked=true` simultaneously: reconciliation wins first; then clear override lock only if safe.

---

## Common Mistakes (reject these patterns)

- Duplicating the same MUST/NEVER in `settings.json`, root CLAUDE.md, and this skill.
- Using Obsidian checklists as authoritative task state when GitHub is canonical.
- Guessing confidence without all three evidence fields.
- Violating global naming grammar via "scoped" names that break the root grammar.
- Hard-deleting any object anywhere in the stack.
- Auto-confirming GCal events (always staged; always human-confirmed).
- Loading this skill for purely local formatting tasks.
- Reminting a UUID in a mirror system.

---

## References

| File | Purpose |
|------|---------|
| `references/fractal-claude-harness.md` | Harness stack, routing, UUID minting, size targets |
| `references/fractal-layering-rubric.md` | Layer quality rubric and scorecard |
| `references/autonomy-policy-matrix.md` | Full risk class matrix with rollback plans |
| `references/lifeos-data-model-template.md` | Entity schemas and facet SoT map |
| `references/review-cadence-template.md` | Cadence inputs/outputs and KPI set |
| `references/anti-patterns-and-guardrails.md` | Drift patterns and recovery protocol |
| `strategy-brief.md` | Architecture intent, principles, rollout, health KPIs |
