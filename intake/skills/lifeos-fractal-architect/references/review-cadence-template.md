# Review Cadence Template

**Purpose:** Define the required inputs, process steps, outputs, and owners for each review cycle.  
**Owner:** Human (executes with Claude support).  
**Canonical trigger:** Calendar event (preferred) or manual invocation.

---

## Daily Review (10–20 min)

**Trigger:** Morning anchor — first working action of the day.  
**Owner:** Human + Claude (Claude runs automated checks before human sits down).  
**Preconditions:** Obsidian vault accessible; GitHub accessible; GCal accessible.

**Process:**
1. Reconcile inbox: process any fleeting notes that entered since last anchor; run IDI on captures where `confidence >= AUTO_EXECUTE_MIN`.
2. Review DLQ: surface any items added since last anchor; assign resolution or defer with reason.
3. Sweep expired `human_override_lock` entries: list any objects with expired locks; prompt reconciliation if needed.
4. Confirm today's scheduled blocks: validate GCal staged events awaiting confirmation; flag capacity conflicts.
5. Set today-focus: confirm top 1–3 outcomes aligned to active project priorities.
6. Review carry-forward queue from yesterday: move stale carry-forwards to `clarified → next` or `voided`.

**Inputs:** Inbox queue; DLQ; GCal today view; GitHub `Next` column; carry-forward queue.

**Outputs:**
- `today-focus` note updated in Obsidian daily note.
- Carry-forward queue cleared or explicitly deferred.
- DLQ items triaged (resolved or given a named owner + deadline).
- Staged GCal events approved or rejected.
- Blocker list with specific required inputs.

**Failure path:** If any canonical system is unavailable, enter read-only degradation. Queue decisions locally. Do not skip the anchor.

---

## Weekly Review (45–90 min)

**Trigger:** Last working session of each work week.  
**Owner:** Human + Claude.  
**Preconditions:** Daily reviews were completed at least 4 of the past 5 days; no unresolved system outages.

**Process:**
1. Inbox to zero: process all remaining fleeting notes via IDI.
2. Audit active projects: for each project in GitHub, confirm state is accurate; update health score; flag stalled projects.
3. Review next actions: ensure every active project has at least one task in `Next` state.
4. Rebalance across PARA Areas: check that active project count per area is intentional.
5. Schedule deep-work blocks for next week via COG workflow (staged proposals only).
6. Review knowledge graph: check stale note ratio; run a linking sprint if stale > `5%`.
7. Publish weekly accountability summary (private or shared; format in vault template).
8. Compute and record weekly KPIs.

**Inputs:** All active GitHub projects; all fleeting notes; previous week's GCal actuals; DLQ status.

**Outputs:**
- Inbox at zero.
- Weekly plan in Obsidian weekly note.
- Updated project health scores in GitHub labels or Obsidian project-notes.
- Staged GCal blocks for next week (human confirms asynchronously).
- Escalation queue with named owner and deadline for each item.
- Weekly KPI record appended to KPI log.

**KPI checkpoints:**
- Task completion reliability ≥ 75%
- Overdue ratio ≤ 15%
- DLQ age: no item > 3 days
- Active projects ≤ `MAX_ACTIVE_PROJECTS` (default 12)

**Failure path:** If KPI breaches detected, add breach playbook items to next week's carry-forward. Do not defer the breach investigation.

---

## Monthly Review (60–120 min)

**Trigger:** First working session of each calendar month.  
**Owner:** Human + Claude.  
**Preconditions:** At least 3 of the past 4 weekly reviews were completed; all DLQ items resolved.

**Process:**
1. Review system drift: evaluate friction points, workarounds, and shadow systems (ad hoc tools outside the stack).
2. Tune policy variable registry: propose changes to `MIN_LINKS_PER_ATOM`, `MAX_ACTIVE_PROJECTS`, `CAPACITY_ALERT_PCT` based on KPI data; human approves.
3. Archive stale objects: archive all projects in `done` state older than 30 days; archive all voided notes older than 30 days per retention policy.
4. Reallocate priorities by life area: check PARA Area balance; promote or demote projects.
5. Evaluate deployment profile: check whether profile promotion gate criteria are met.
6. Review autonomy matrix: check if any operation class needs re-classification based on recent incident data.
7. Kill-switch drill: simulate a kill-switch event; confirm freeze and recovery steps work.
8. Compute and record monthly KPIs.

**Inputs:** Full KPI log for the month; DLQ history; registry current values; GitHub project archive queue; deployment profile gate checklist.

**Outputs:**
- Registry change proposals (human-approved before applying).
- Portfolio rebalance: new active project list with priority order.
- Archive report: list of archived projects and notes with retention expiry dates.
- Deployment profile decision (promote, hold, or regress).
- Kill-switch drill log entry.
- Monthly KPI record.

**Profile promotion gate checks:**
- Profile A → B: zero harmful automation incidents; human signs gate checklist.
- Profile B → C: DLQ SLA met; reconciliation drill passed; kill-switch drill logged.

---

## Quarterly Review (2–4 h)

**Trigger:** First working session of each calendar quarter.  
**Owner:** Human (primary); Claude (data preparation and proposal generation).  
**Preconditions:** All three monthly reviews completed; all DLQ items resolved; KPI log current.

**Process:**
1. Reassess goals and strategic bets: review Cascading Goals hierarchy from Annual down to quarterly.
2. Update long-horizon projects: review and update 12-month project list and GTM vault.
3. Re-validate autonomy boundaries: review full autonomy matrix against quarterly incident data; propose changes.
4. Re-evaluate PARA Area structure: consider adding, merging, or retiring Areas.
5. Update quarterly execution map: define top 3–5 projects and key results for the quarter.
6. Review and update Obsidian evergreen note set: identify molecules ready for promotion to evergreen.

**Inputs:** Annual goals; quarterly KPI aggregates; autonomy matrix; PARA structure; evergreen note list; GTM vault.

**Outputs:**
- Updated Cascading Goals hierarchy (Obsidian note updated).
- New quarterly execution map (Obsidian note created or updated).
- Updated autonomy matrix (autonomy-policy-matrix.md, human-approved).
- List of newly promoted evergreen notes.
- PARA Area structure change log (if any).

---

## Annual Review

**Trigger:** End of calendar year (or chosen system anniversary).  
**Owner:** Human (primary).  
**Preconditions:** All four quarterly reviews completed; KPI log complete for the year.

**Process:**
1. Evaluate system performance against KPIs: full-year aggregate.
2. Retire ineffective methods: identify any method in the integration map that generated friction with no measurable benefit.
3. Refresh Principles: review each Principle for continued relevance.
4. Review GovernanceRules: identify rules that were never violated (may be redundant) or frequently violated (may need strengthening or redesign).
5. Refresh policy variable thresholds: review `AUTO_EXECUTE_MIN` and `APPROVAL_MIN` against full-year confidence data.
6. Update architecture change log.
7. Define next-year design constraints.

**Inputs:** Full-year KPI log; method integration map; Principles; GovernanceRules; policy variable registry; incident log.

**Outputs:**
- Architecture change log (new entries for any structural changes made).
- Next-year design constraints document.
- Updated Principles (or confirmation no changes needed, with rationale).
- Updated GovernanceRules (or confirmation).
- Updated policy variables `AUTO_EXECUTE_MIN` and `APPROVAL_MIN`.

---

## KPI Reference Table

| KPI | Owner | Source | Healthy threshold | Breach playbook |
|---|---|---|---|---|
| Task completion reliability | Human + Claude | GitHub issue timestamps | ≥ 75% (rolling 4 weeks) | Shrink WIP; re-estimate; review task decomposition |
| Overdue ratio | Human | GitHub labels | ≤ 15% of active tasks | Re-baseline capacity; split overdue tasks; pause lowest-value project |
| Calendar adherence | Human | GCal actuals vs planned | ≥ 70% | Adjust `CAPACITY_ALERT_PCT`; reduce scheduled blocks; investigate interruption patterns |
| Active project WIP | Human | GitHub project count | ≤ `MAX_ACTIVE_PROJECTS` (default 12) | Pause or archive lowest-value project before accepting new one |
| Stale note ratio | Claude | Obsidian query | ≤ 5% fleeting notes > 7 days | Run IDI sprint; quarantine abandoned captures |
| DLQ age | Human + Claude | DLQ timestamps | No item > 3 days | Daily anchor priority item until cleared |
| Confidence accuracy | Claude | Audit log | ≥ 95% auto-executed ops with no rollback | Review evidence computation; tighten schema validation |
| Escalation resolution latency | Human | DLQ to resolution timestamps | ≤ 72 hours | Bump to next daily anchor; escalate if > 72 hours |
