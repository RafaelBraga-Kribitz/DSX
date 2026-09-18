# Autonomy Policy Matrix

**Purpose:** Define exactly what Claude can do autonomously, under what conditions, and with what rollback mechanism.  
**Owner:** Human (annual review for thresholds; monthly review for matrix entries).  
**Canonical variable registry:** `strategy-brief.md` → section 12, and this file.

---

## Policy Variable Registry (tune here; applied everywhere)

| Variable | Default | Blast radius | Review cadence |
|---|---|---|---|
| `AUTO_EXECUTE_MIN` | 90 | System-wide | Annual |
| `APPROVAL_MIN` | 75 | System-wide | Annual |
| `MAX_FOLDER_DEPTH` | 3 | Vault structure | Annual |
| `MIN_LINKS_PER_ATOM` | 2 | Knowledge hygiene | Monthly |
| `MAX_ACTIVE_PROJECTS` | 12 | Execution capacity | Monthly |
| `CAPACITY_ALERT_PCT` | 20 | Calendar buffer | Monthly |

**Tuning rule:** Adjust only during the review cadence for the variable's blast radius. Mid-cycle changes require human sign-off in the audit trail.

---

## Evidence (mandatory for every autonomous mutating operation)

| Field | Type | Rule if missing |
|---|---|---|
| `schema_validation_pass` | bool | Force `confidence < APPROVAL_MIN` |
| `source_coverage_count` | int | Force `confidence < APPROVAL_MIN` |
| `conflict_check_pass` | bool | Force `confidence < APPROVAL_MIN` |

**Absolute rule:** any missing evidence field forces the operation to blocked or approval-gated. Confidence is never guessed.

---

## Confidence Bands

| Band | Condition | Behavior | Audit |
|---|---|---|---|
| **Auto** | `confidence >= AUTO_EXECUTE_MIN` (≥ 90) | Execute immediately. Deterministic, reversible operations only. | Append audit row on real state change; no row on no_op |
| **Gated** | `APPROVAL_MIN <= confidence < AUTO_EXECUTE_MIN` (75–89) | Stage in Pending Approval queue. Surface to human in next daily anchor or immediate alert if high-priority. | Audit row added when human approves or rejects |
| **Blocked** | `confidence < APPROVAL_MIN` (< 75) | No mutation. Create DLQ entry. Surface in daily anchor with context and suggested resolution. | Audit row added when human resolves |

**Equality rule:** conditions are inclusive/exclusive exactly as written. No rounding up.

---

## Risk Classification

Every operation that touches system state is classified before execution:

| Class | Definition | Band ceiling |
|---|---|---|
| Reversible, local | Operation affects only the local vault or draft GitHub object; can be fully undone within 5 minutes without external API | Auto (evidence permitting) |
| Reversible, external | Operation creates or modifies a live GitHub issue or staged GCal event; rollback requires API call | Gated minimum; Auto only in Profile C with evidence |
| Irreversible-adjacent | Operation closes/archives; cannot easily re-open without data loss risk | Gated always |
| Security/auth | Any write to authentication, secrets, or API credentials | Blocked always |
| Financial | Any write to financial accounts or payment systems | Blocked always |

---

## Full Autonomy Matrix

| Domain | Specific operation | Risk class | Profile minimum | Band | Rollback / compensation |
|---|---|---|---|---|---|
| **Knowledge** | IDI: inbox note → atom note | Reversible, local | A | Auto (evidence ok) | Tag `#quarantine`; surface in daily anchor |
| **Knowledge** | Rename / re-address existing note | Reversible, external (links) | B | Gated | Revert rename; fix broken links |
| **Knowledge** | Archive stale note | Reversible-adjacent | B | Gated | Move back to active path |
| **Knowledge** | Delete note (prohibited) | — | Never | Blocked | N/A; hard delete is forbidden |
| **Execution** | ACE: create GitHub issue | Reversible, external | B | Auto (evidence ok, Profile B+) | Mark `voided`; never hard delete |
| **Execution** | Transition issue state (e.g., next → scheduled) | Reversible, external | B | Auto (evidence ok, Profile B+) | Reverse transition; add reason to audit |
| **Execution** | Close / archive issue | Reversible-adjacent | B | Gated | Reopen issue; document reason |
| **Execution** | Delete issue (prohibited) | — | Never | Blocked | N/A |
| **Planning** | Weekly project stack proposal | Reversible, local | A | Gated | Discard proposal; no state written |
| **Planning** | Goal/milestone update | Reversible, external | B | Gated | Revert to previous milestone state |
| **Scheduling** | COG: stage GCal block proposal | Reversible, external | B | Gated (Profile B+) | Cancel staged event; notify human |
| **Scheduling** | Confirm / commit GCal event | Irreversible-adjacent | Never autonomous | Blocked | Always human action |
| **Comms** | Draft PR or document | Reversible, local | B | Gated | Close draft PR with annotation |
| **Comms** | Send/publish (email, PR merge, post) | Irreversible-adjacent | Never autonomous | Blocked | Always human action |
| **Security** | Auth / secret mutation | Security | Never | Blocked | Escalate to human immediately |
| **Financial** | Any write to accounts | Financial | Never | Blocked | Escalate to human immediately |
| **System** | Change deployment profile | Irreversible-adjacent | Never autonomous | Blocked | Gate checklist + human sign-off |
| **System** | Tune policy variable | Reversible, local | B | Gated | Revert to previous registry value |
| **System** | Cold storage export | Reversible-adjacent | C | Gated | Retain local copy until human confirms |

---

## Escalation Protocol

When an operation is blocked or lands in the DLQ:

1. Create a DLQ entry with: `{item_id, timestamp, operation_type, reason_blocked, suggested_resolution, earliest_human_slot}`.
2. Surface the item in the next daily anchor (not immediately, to avoid notification spam, unless high-priority class).
3. Do not retry the operation automatically. Wait for human resolution.
4. SLA: DLQ items must be resolved within 72 hours. Breach triggers an alert in the next daily anchor.
5. If 3+ items from the same operation type pile up in DLQ within 24 hours: flag as systemic failure; escalate to weekly review for root-cause analysis.

---

## Kill-Switch Policy

**Trigger:** Three confidence-below-APPROVAL_MIN mutating operations within one hour on the same execution path.  
**Immediate action:** Freeze all mutations on that path. Emit human alert.  
**Recovery steps:**
1. Human acknowledges the alert.
2. Run reconciliation protocol (see `fractal-claude-harness.md`).
3. Identify root cause of low confidence (schema drift, missing source coverage, conflict unresolved).
4. Patch the governance or protocol layer that caused the failure.
5. Add a regression check for that specific failure mode.
6. Re-enable by deployment profile rules (not manually bypassing the gate).

**Drill cadence:** Monthly simulated kill-switch. Log result in the audit trail. Gate to Profile C requires at least one successful drill.

---

## Deployment Profile Gates

### Profile A → B

Requirements (all must be met):
- [ ] Zero harmful automation incidents over a defined window (document the window in monthly review)
- [ ] At least one successful IDI advisory run (Claude proposes; human approves; no errors)
- [ ] At least one successful ACE advisory run
- [ ] Human signs the gate checklist and stores it in the audit trail

### Profile B → C

Requirements (all must be met):
- [ ] DLQ SLA met: zero items older than 72 hours at time of gate check
- [ ] Reconciliation drill completed and passed (no unresolved conflicts)
- [ ] Kill-switch drill logged and passed
- [ ] Monthly review KPIs all within healthy thresholds
- [ ] Human signs the gate checklist and stores it in the audit trail
