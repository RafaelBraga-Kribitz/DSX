# Strategy Brief: LifeOS Fractal System

**Version:** 1.0  
**Status:** Authoritative  
**Owner:** Rafael Bragakribitz  
**Maintained at:** `lifeos-fractal-architect/strategy-brief.md`

---

## 1. Architecture Intent

LifeOS is a deterministic personal operating system. It replaces mood-dependent productivity with a repeatable decision machine governed by explicit rules, confidence-gated automation, and fractal layering. The system has one non-negotiable design target: **zero ambiguity about what is true, who owns it, and what should happen next.**

The architecture solves three recurring failure modes in personal systems:

1. **Context collapse** — Claude (or the human) loses track of state across tools. Solution: facet-level source-of-truth ownership with explicit mirrors.
2. **Framework soup** — multiple productivity methods in conflict with no resolution order. Solution: explicit precedence table with tie-break rules.
3. **Automation gone wrong** — autonomous agents mutate state incorrectly. Solution: confidence-gated bands with evidence requirements, kill-switch, and no hard delete.

The system combines two co-equal structures: an **Action Hierarchy** (GTD/PARA — outcomes, projects, tasks, reviews) and a **Knowledge Network** (Zettelkasten — atomic notes, links, synthesis, evergreen knowledge). Both are active simultaneously and exchange references via defined bidirectional interfaces.

---

## 2. Scope

### In scope
- Personal life domains: professional, health, learning, relationships, finance, projects
- Operating tools: Claude (primary orchestrator), Obsidian (knowledge/action workspace), GitHub (execution/change ledger), Google Calendar (capacity/commitment ledger)
- Automation surface: Claude autonomous operations gated by confidence bands and deployment profile
- Review cadence: daily, weekly, monthly, quarterly, annual
- Governance lifecycle: rules, decisions, registry tuning

### Out of scope
- Team or multi-user workflows (future extension; no assumption of shared write access)
- Financial transaction execution (read-only observation only; no write to accounts)
- Security secret management (acknowledged; human-only for all auth/secret writes)
- Real-time streaming integrations (asynchronous sync only; no webhooks assumed)

---

## 3. Design Principles

These principles are non-negotiable. Any workflow, rule, or tool integration that violates a principle is rejected. There are eight:

**P1 — Fractal Simplicity.**
Top layers must be short, universal, and stable. Complexity increases only downward. A child layer may add rules only if they inherit parent constraints, do not contradict parent MUST/NEVER, add measurable value, and state their scope explicitly.

**P2 — Single Facet Owner.**
Every object facet (execution state, time/capacity, narrative context, identity) has exactly one canonical system. Mirrors are read-only unless a write protocol is explicitly defined. No system claims dual canonical ownership over the same facet.

**P3 — Confidence-Gated Autonomy.**
No autonomous mutation without three evidence fields: `schema_validation_pass`, `source_coverage_count`, `conflict_check_pass`. Missing evidence forces the outcome to blocked or approval-gated. Confidence is never guessed.

**P4 — No Hard Delete.**
Terminal action for any object is export-to-cold-storage plus permanent exclusion from queries. States are voided, quarantined, or archived. Hard deletion is prohibited at every layer.

**P5 — Explicit Precedence.**
Method conflicts resolve via the precedence table in section 6. "It depends" is not an acceptable answer without attached decision criteria.

**P6 — Idempotency.**
`transition(S,S)` is always a no_op. No audit row is written. Every real state transition appends a structured audit record.

**P7 — Firstbrain/Second Brain Separation.**
Meaning, values, and strategic direction live in the Firstbrain (human-owned). Execution, synthesis, scheduling, and maintenance live in the Second Brain (Claude-executable). Claude proposes; human approves at all decision boundaries that cross the line between the two.

**P8 — Progressive Disclosure.**
Load only the context layer needed for the current task. Do not load the full skill stack for a trivial formatting operation. Routing rules in root CLAUDE.md direct to the correct depth.

---

## 4. Dual-System Architecture

### 4.1 Action Hierarchy

**Purpose:** Capture, clarify, organize, and execute discrete commitments.  
**Methods integrated:** GTD (capture/clarify/organize/engage), PARA (containers), Cascading Goals (outcome decomposition), Johnny Decimal (address scheme), COG (capacity scheduling).  
**Canonical tool:** GitHub (execution state) + Google Calendar (time claims).  

**State machine (linear):**
```
inbox → clarified → next → scheduled → inprogress → done
                                                    ↓
                                              voided (rollback only)
                                                    ↓
                                               archived
```

**Lifecycle rule:** `done → archived` is automatic after configurable retention. `voided` means invalid — never completed. `archived` means complete and immutable.

### 4.2 Knowledge Network

**Purpose:** Capture, process, link, and synthesize understanding into reusable knowledge.  
**Methods integrated:** Zettelkasten (atoms, molecules, evergreen), IDI (inbox-digest-integrate), Modified Second Brain (two-layer: human meaning + AI execution), Claudesidian patterns.  
**Canonical tool:** Obsidian (note graph and narrative context).  

**Note types:**
- `fleeting` — raw capture, not yet processed
- `atom` — single permanent idea, minimum 2 outbound links
- `molecule` — synthesis of 2+ atoms around a theme
- `project-note` — context document linked to a GitHub project
- `evergreen` — mature, stable knowledge; stable title as claim

**Bidirectional interface between systems:**

| Direction | Signal | Protocol |
|-----------|--------|----------|
| Knowledge → Action | Atom or molecule surfaces an action item | ACE workflow: extract verb-led task, create GitHub issue with Obsidian note_id as context |
| Action → Knowledge | Issue resolution generates insight | IDI workflow: link closed issue to existing note or create new atom |
| Project → Note | Project planning needs context | project-note references project_id; GitHub issue carries note_id link |
| Note → Calendar | Deep work session needed | COG workflow: stage GCal block proposal linked to note or project |

---

## 5. Method Integration Map

The following methods are integrated. Each entry states its role, its precedence position, and any conflict rule.

| Method | Role in LifeOS | Conflict rule |
|--------|---------------|---------------|
| GTD | Capture + clarify + weekly review backbone | Superseded by PARA on containment; GitHub is canonical for state |
| PARA | Container taxonomy (Projects, Areas, Resources, Archives) | Applies to both Obsidian vault structure and GitHub project labels |
| Zettelkasten | Atomic note format and link discipline | Note_id minted at creation; never rename without redirect |
| Johnny Decimal | Address scheme for Obsidian paths and vault areas | Global grammar root; PARA buckets add scoped suffixes only |
| ACE | GitHub issue shape: Action (verb title) + Context (Obsidian link) + Execution (DoD + evidence) | ACE is the required issue format; deviations flagged |
| IDI | Knowledge inbox processing: Inbox → Digest → Integrate | Trigger: unprocessed fleeting note; owner: Claude if confidence ≥ AUTO_EXECUTE_MIN |
| COG | Capacity scheduling: Categorize (PARA) → Organize (GitHub state) → Generate (calendar proposal) | GCal blocks are always staged proposals; never auto-committed in Profile A/B |
| Cascading Goals | Annual → quarterly → project → task decomposition | Goal hierarchy stored in Obsidian as structured notes; GitHub milestones mirror project-level goals |
| Founder GTM Vault | Patterns for initiative tracking and outcome mapping | Applied as template set inside the Projects PARA bucket |
| Two-layer Second Brain | Human meaning (Firstbrain) + AI execution (Claude) | Claude never overwrites human-authored strategic notes without explicit instruction |

**Framework collision rule:** When two methods give contradictory instructions, apply the precedence table in section 6. If still ambiguous, escalate to human and queue in DLQ.

---

## 6. Source of Truth and Conflict Resolution

### 6.1 Facet Ownership

| Object facet | Canonical owner | Mirror | Sync direction |
|---|---|---|---|
| Object identity (UUIDs) | Originating system (minter) | Receiving system (reference only) | Origin → mirror |
| Execution state | GitHub | Obsidian (queries only) | GitHub → Obsidian |
| Scheduling / time | Google Calendar | Obsidian daily note | GCal → Obsidian |
| Narrative / long context | Obsidian | GitHub (snippet + link) | Obsidian → GitHub |
| Note graph / knowledge | Obsidian | — | — |
| Policy variable registry | Versioned repo doc (`lifeos-fractal-architect/references/`) | — | — |
| Archival execution truth | GitHub (closed/archived issues) | Obsidian archive paths | GitHub → Obsidian |

**UUID minting rule:** GitHub mints `task_id` and `milestone_id`. Obsidian mints `note_id` at note creation. Google Calendar mints `event_id`. Mirrors store references. Mirrors never remint an ID.

### 6.2 Conflict Resolution Precedence

When two systems disagree, apply in order:

1. **Safety and capacity (Google Calendar)** — hard commitments block all other scheduling.
2. **Action execution state (GitHub + GTD clarification)** — issue state overrides Obsidian checklist state.
3. **Containment and structure (Obsidian + PARA + Johnny Decimal)** — vault structure overrides ad hoc naming.
4. **Knowledge synthesis (Zettelkasten graph integrity)** — note links are preserved; do not silently overwrite.
5. **Convenience** — never wins a conflict.

**Tie-break for split-brain (same facet, two values):**
Canonical timestamp → monotonic version → actor priority (`human > system > claude`).

---

## 7. Autonomy Architecture and Deployment Profiles

### 7.1 Confidence Bands

Every autonomous mutating operation MUST compute:

```
confidence: 0–100
evidence:
  schema_validation_pass: bool
  source_coverage_count: int
  conflict_check_pass: bool
```

**Band outcomes:**
- `confidence >= AUTO_EXECUTE_MIN` (default 90) → auto-execute; write audit row on real state change
- `APPROVAL_MIN <= confidence < AUTO_EXECUTE_MIN` (default 75–89) → stage in Pending Approval; human confirms
- `confidence < APPROVAL_MIN` (default <75) → blocked; queue in DLQ; human triage required

**Missing evidence rule:** any missing evidence field forces `confidence < APPROVAL_MIN` regardless of other scores.

### 7.2 Deployment Profiles

Progress through profiles sequentially. Do not skip.

| Profile | Capabilities | Gate to next |
|---------|-------------|--------------|
| **A (Advisory)** | Read-only + plan generation. No writes to GitHub, GCal, or vault except explicit human approval. | Zero harmful automation incidents over agreed window; human signs checklist |
| **B (Bounded)** | Auto local vault hygiene (IDI) + auto GitHub issue creation (ACE) + staged-only GCal proposals (COG). All external writes still gated. | DLQ SLA met; reconciliation drill passed; kill-switch drill logged |
| **C (Full Policy)** | All confidence-gated operations active per autonomy matrix. Kill-switch monitoring live. DLQ monitored. | Continuous; regress to Profile B on kill-switch trigger |

### 7.3 Kill-Switch Policy

**Trigger:** confidence below APPROVAL_MIN on three mutating operations within one hour on the same path.  
**Action:** freeze all mutations on that path immediately; alert human; reconcile before resuming.  
**Drill cadence:** monthly simulated outage; log result.  
**Recovery:** manual human unlock after reconciliation passes.

---

## 8. Naming System

### 8.1 Global Grammar (all layers must obey)

```
<scope>-<topic>--<qualifier>
```

- Separators: `-` within a token; `--` between scope and qualifier.
- Charset: lowercase alphanumeric and hyphens only. No underscores, spaces, or uppercase.
- Max length: 64 characters per segment.
- Forbidden: ambiguous abbreviations without a registry entry.

### 8.2 Scoped Extensions (PARA buckets only)

| Scope prefix | Example | Extension allowed |
|---|---|---|
| Global doc | `doc-2025-annual-review` | None |
| Area | `area-health--sleep-protocol` | Area slug prefix |
| Project | `proj-website-v2--milestone-3` | Project slug + phase |
| Resource | `res-reading--systems-thinking` | Resource type prefix |

**Rule:** PARA extensions compile to valid global grammar tokens. Document the compiler rule in the vault-level CLAUDE.md for each area.

---

## 9. Privacy and Security Boundaries

| Category | Autonomous permission | Requires human |
|---|---|---|
| Vault note read | Allowed (any profile) | — |
| Vault note create/update | Profile B+ with confidence gate | Human override or Profile A |
| GitHub issue create | Profile B+ with confidence gate | Human override or Profile A |
| GitHub issue close | Profile B+ with confidence gate | Human override or Profile A |
| GCal block stage | Profile B+ (always staged, never confirmed) | Human confirms all events |
| GCal block confirm | Never autonomous | Always human |
| Auth / secret mutation | Never autonomous | Always human; blocked category |
| Financial write | Never autonomous | Always human; blocked category |
| Cold storage export | Profile C with audit trail | Human signs off |
| System config changes | Never autonomous | Always human |

---

## 10. Service Degradation

If any canonical system (GitHub, GCal, Obsidian vault) is unavailable:

1. Enter **read-only degradation** immediately.
2. Queue all mutating operations locally with timestamps.
3. Emit single daily digest of queued operations (do not spam).
4. Resume operations after **health probe success**: not just HTTP 200 — include auth validity and a successful read-only API probe. Document exact probe in project CLAUDE.md.
5. On re-entry: run reconciliation protocol before resuming autonomous writes.

---

## 11. Rollout Approach

**Phase 0 — Baseline (Week 1–2)**
- Freeze current vault structure. Document as-is state.
- Install Johnny Decimal addressing in Obsidian.
- Establish GitHub project board with ACE issue template.
- Connect GCal as read-only observer.
- Deploy Profile A only.

**Phase 1 — Knowledge Hygiene (Week 3–6)**
- Run IDI workflow manually first; Claude in advisory.
- Process all fleeting notes to atoms/molecules.
- Achieve `MIN_LINKS_PER_ATOM` compliance across existing notes.
- Gate: note graph health score ≥ 80% before Phase 2.

**Phase 2 — Action Execution (Week 7–10)**
- Activate ACE workflow; Claude creates GitHub issues from captures.
- Run weekly reviews using the cadence template.
- COG remains advisory (staged only, no confirms).
- Gate: zero conflicting states across GitHub and Obsidian for 2 consecutive weeks.

**Phase 3 — Bounded Autonomy (Week 11+)**
- Pass Profile A → B gate checklist.
- Enable Profile B: auto IDI + auto ACE + staged COG.
- Activate DLQ monitoring.
- Monthly review tunes registry variables.

**Phase 4 — Full Policy (Month 4+)**
- Pass Profile B → C gate checklist.
- Kill-switch monitoring live.
- Full confidence-band automation active.
- Quarterly review validates autonomy boundaries.

---

## 12. System Health KPIs

| KPI | Measurement | Healthy threshold | Review cadence |
|---|---|---|---|
| Task completion reliability | Closed issues / opened issues (rolling 4 weeks) | ≥ 75% | Weekly |
| Overdue ratio | Overdue issues / total active | ≤ 15% | Weekly |
| Calendar adherence | Actual blocked time / planned blocked time | ≥ 70% | Weekly |
| Active project WIP | Count of GitHub projects in `inprogress` | ≤ MAX_ACTIVE_PROJECTS (default 12) | Monthly |
| Stale note ratio | Fleeting notes > 7 days old / total notes | ≤ 5% | Monthly |
| DLQ age | Oldest unresolved DLQ item (days) | ≤ 3 days | Daily |
| Confidence accuracy | Auto-executed ops with no rollback / total auto ops | ≥ 95% | Monthly |
| Escalation resolution latency | DLQ item age at resolution | ≤ 72 hours | Weekly |
