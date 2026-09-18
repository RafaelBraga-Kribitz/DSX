# Anti-Patterns and Guardrails

**Purpose:** Catalogue every known LifeOS failure mode, its diagnostic signal, and the required corrective action.  
**Owner:** Human (reviewed at monthly cadence; new anti-patterns added when incidents are observed).  
**Usage:** Run a mental check against this list before shipping any new workflow, protocol, or playbook.

---

## Anti-Patterns

### AP-1 — Framework Collage Without Precedence Table

**Description:** Two or more methods (e.g. GTD and Zettelkasten, or PARA and COG) give conflicting instructions and there is no resolution order.  
**Signal:** Repeated human decision about "which system to trust" for the same type of object.  
**Root cause:** Methods adopted without documenting where each fits in the precedence hierarchy.  
**Correction:** Apply the method precedence table from `strategy-brief.md` section 6. For each conflict, identify which layer it belongs to and assign one method as canonical. Document the decision in `CLAUDE.md` for that domain.

---

### AP-2 — Policy Duplication Across Layers

**Description:** The same MUST/NEVER rule appears in `settings.json`, root `CLAUDE.md`, and a skill or reference file.  
**Signal:** Claude produces inconsistent behavior depending on which file was loaded; conflicts appear during refactoring.  
**Root cause:** Urgency-driven copy-paste when adding a new rule without checking where it already exists.  
**Correction:** State each rule exactly once at the highest applicable layer. Lower layers link down to it. Run a cross-file search for duplicate MUST/NEVER phrases before merging any governance change.

---

### AP-3 — Long Workflows at Root Layer

**Description:** Step-by-step procedures or long decision trees placed in `settings.json` or root `CLAUDE.md`.  
**Signal:** Root CLAUDE.md exceeds ~400 words; settings.json contains markdown or prose.  
**Root cause:** Over-engineering the root for "clarity" that actually burns context and hides the router.  
**Correction:** Move procedural content to the appropriate skill or domain CLAUDE.md. Root stays as a router table only.

---

### AP-4 — Deep See-X-See-Y Chains Without an Index Hub

**Description:** Following references requires 3+ hops: "see file A → see file B → see file C."  
**Signal:** Claude (or the human) gives up navigating the reference chain and guesses.  
**Root cause:** Incremental document additions without maintaining an index.  
**Correction:** Every folder with more than 2 reference files MUST have an index note that lists all children with one-line descriptions. Maximum 2 hops from root CLAUDE.md to any operational document.

---

### AP-5 — Child CLAUDE.md Contradicts Parent MUST/NEVER

**Description:** A domain or project CLAUDE.md adds a rule that directly conflicts with a parent-layer rule.  
**Signal:** Different behavior in the same domain depending on task context.  
**Root cause:** Child file authored without reading parent constraints first.  
**Correction:** Child files may only narrow or add scoped rules. They MUST NOT contradict parent MUST/NEVER. Run parent-child consistency check before merging any child CLAUDE.md change.

---

### AP-6 — Mirror Pretending to Be Canonical

**Description:** Obsidian checklists are used as the authoritative task state when GitHub is canonical.  
**Signal:** Task shows "done" in Obsidian but is still open in GitHub; discrepancies are resolved by guessing.  
**Root cause:** Convenience of in-note checklists without enforcing the facet ownership rule.  
**Correction:** Obsidian task references are read-only views. Any state change must go through GitHub. If an Obsidian checklist diverges from GitHub, GitHub wins. Obsidian is updated via sync, not the other way around.

---

### AP-7 — Calendar as Optional Infrastructure

**Description:** GCal blocks are not created or are routinely ignored; backlog grows without capacity accounting.  
**Signal:** Projects consistently overrun; DLQ accumulates; human feels "overwhelmed but busy."  
**Root cause:** COG workflow not activated, or calendar proposals not confirmed by human.  
**Correction:** No task in `Next` state should remain there longer than one weekly review without either a staged calendar proposal or an explicit "deferred with reason" note. Activate COG workflow. Human must confirm or reject staged proposals within 24 hours.

---

### AP-8 — Hard Delete

**Description:** Any user artifact (note, task, project, event) is permanently removed from the system.  
**Signal:** Missing UUIDs in references; DLQ entries with no resolution path; "where did that go?" questions.  
**Root cause:** Treating deletion as the correct terminal action.  
**Correction:** Hard delete is forbidden at every layer. Terminal action is: export to cold storage + permanent exclude-from-queries + set state to `archived` or `quarantine`. If a hard delete has already occurred, document it in the incident log and add a DLQ entry noting the missing UUID.

---

### AP-9 — Guessing Confidence Without Evidence

**Description:** Claude assigns a confidence score without computing all three required evidence fields.  
**Signal:** Autonomous operations that produce incorrect results; rollbacks triggered more than 5% of the time.  
**Root cause:** Evidence fields skipped under time pressure or because schema was unclear.  
**Correction:** Missing any evidence field forces `confidence < APPROVAL_MIN` regardless. There is no "partial evidence" mode. Fix the schema validation check before re-enabling the workflow.

---

### AP-10 — Reminting UUIDs in Mirror Systems

**Description:** A mirror system (e.g. Obsidian) generates its own ID for a task that already has a GitHub-minted `task_id`.  
**Signal:** Two IDs refer to the same object; deduplication failures; broken reference chains.  
**Root cause:** Mirror system not configured to receive the canonical ID; note created before ACE workflow linked the issue.  
**Correction:** Mirror systems store references only. If a note predates the GitHub issue, create the issue first, then add `task_id` as a field in the note's YAML front matter. Do not generate a new ID.

---

### AP-11 — Auto-Confirming Calendar Events

**Description:** Claude automatically confirms (not just stages) a GCal event without human approval.  
**Signal:** Events appear on calendar that the human did not intentionally schedule.  
**Root cause:** COG workflow misconfigured; `confirmed` set to `true` by automation.  
**Correction:** `confirmed=true` is always a human action. Automation may only set `staged=true`. Audit GCal for staged-but-unconfirmed events older than 24 hours and surface them in the next daily anchor.

---

### AP-12 — Naming Grammar Violation

**Description:** A note, file, or GitHub object uses a name that violates the global grammar (`<scope>-<topic>--<qualifier>`, lowercase, hyphens only).  
**Signal:** Sort failures; broken links; inconsistent vault navigation.  
**Root cause:** Convenience naming in the moment without checking the global grammar rule.  
**Correction:** Apply the global grammar on create. Do not retroactively rename in bulk without a redirect strategy. Add the compiler rule to the affected area's CLAUDE.md.

---

## Active Guardrails

These are automated checks Claude MUST run on every relevant operation:

| Guardrail | When applied | Failure action |
|---|---|---|
| Facet owner check | Before any write to a system-of-record field | Reject write; log to DLQ |
| Evidence triple check | Before any autonomous mutation | Force blocked/gated if any field missing |
| Transition audit | On every real state change | Append audit JSON; reject transition if audit cannot be written |
| `human_override_lock` check | Before mutating any object | Do not proceed if lock is active; queue for after expiry |
| `sync_locked` check | Before mutating any object | Run reconciliation first; only clear lock after reconciliation passes |
| Kill-switch check | After every mutating operation | Count low-confidence ops in rolling hour; trigger freeze at threshold 3 |
| Hard delete intercept | When any delete command is issued | Block; redirect to voided/quarantine/archive path; log attempt |
| Naming grammar validator | On any object create or rename | Reject if grammar violation; return corrected form |

---

## Fractal Naming Guardrail

- Global grammar is minimal, stable, and applies everywhere.
- Area/project/resource naming extensions MUST compile to valid global tokens.
- Document the compiler rule in the vault-level CLAUDE.md for each area that uses a scoped extension.
- Violations are not "close enough." A name that breaks the global grammar is rejected, not approximated.

---

## Recovery Protocol

When any anti-pattern is detected:

1. **Freeze** the affected automation path or workflow immediately. Do not continue writing conflicting state.
2. **Reconcile** all objects touched by the affected path since the last clean checkpoint. Resolve split-brain per the tie-break rules.
3. **Root-cause** the anti-pattern: identify which layer failed (missing rule, violated rule, wrong layer placement, bad config).
4. **Patch** the governance or protocol layer. Do not patch the symptom; fix the structural cause.
5. **Add a regression check** specific to this failure mode to the anti-pattern list or the relevant playbook.
6. **Re-enable** automation by deployment profile rules. Do not manually bypass profile gates to speed up recovery.
7. **Log** the incident: timestamp, affected objects, root cause, resolution, and regression check added.
