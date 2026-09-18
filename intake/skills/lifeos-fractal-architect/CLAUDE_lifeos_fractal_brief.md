# CLAUDE Brief: LifeOS Fractal System Architect

## Objective
Produce a high-quality architecture package that defines a fractal personal operating system ("LifeOS") and a specialist Claude role that can operate it with maximum safe autonomy.

The package must match the quality bar of mature skill docs: explicit triggers, strong constraints, clear workflows, anti-patterns, validation gates, and reusable templates.

## Source Corpus
Use these clippings as primary grounding:

- `Master System.md`
- `Fractal Planning A Holistic Approach to Productivity.md`
- `The Fractal Organization Designing Self-Repeating Patterns of Excellence.md`
- `A comprehensive guide to Systems Thinking.md`
- `Systems Thinking A Holistic Framework to Understand Complexity, Improve Decision-Making, and Find Leverage Points - Weekly Sharing.md`
- `System Design Principles for Long Term Success.md`
- `4 principles of good modular design.md`
- `Designing and Implementing an Organizing System – The Discipline of Organizing 4th Professional Edition.md`
- `Frameworks & Systems for Organizing, Learning, and Creating.md`
- `The PARA Method The Simple System for Organizing Your Digital Life in Seconds.md`
- `The PARA Method How to Organize Your Life in 4 Categories.md`
- `Time-Blocking Digital Planner & Calendar.md`
- `How to Organize Your Life With an Ever-Evolving System.md`
- `How I Built a Productivity System to Organize My Life.md`
- `How to Build a Modular Organization A Step-by-Step Guide for Leaders.md`

Corpus root (local): `~/lifeOS/Clippings/`

## Design Intent
Create an architecture that:

1. Stays simple at the top (few strong rules), and becomes more specific only when cascading downward.
2. Combines hierarchical execution systems with networked knowledge systems.
3. Integrates and customizes GTD, PARA, Zettelkasten, Johnny Decimal, ACE, IDI, COG, Second Brain, Modified Zettelkasten (Atoms, Molecules, Projects, Fleeting), Two-layer second brain (human + AI), Claudesidian, Firstbrain, Cascading goals, and founder GTM vault patterns.
4. Makes organization and execution easy for the user.
5. Makes it easy for Claude to maintain high-fidelity context across all life domains and act proactively.

## Operating Stack
Assume the implementation stack includes:

- Claude (primary orchestrator agent)
- Obsidian (knowledge/action workspace)
- GitHub (execution/change ledger and automation surface)
- Google Calendar (capacity and commitment ledger)

## Required Output (Three Deliverables)
Return all three outputs in one response:

1. **Strategy brief**
   - Architecture intent, scope, design principles, boundary conditions, and rollout approach.
2. **Production SKILL.md**
   - A ready-to-use skill spec for "LifeOS Fractal System Architect."
3. **Companion references**
   - Practical templates/checklists/rubrics for execution and quality control.

## Mandatory Architecture Model
Use this fractal layering model:

- `Principles`
- `GovernanceRules`
- `OperatingModels`
- `Workflows`
- `Protocols`
- `TaskPlaybooks`

Each layer must:

- Have a narrow, explicit role.
- Inherit constraints from parent layers.
- Add only necessary specificity.
- Include escalation rules for exceptions.

## Mandatory Dual-System Design
Define and connect two systems:

1. **Action hierarchy**
   - GTD/PARA-style outcomes, projects, tasks, schedules, reviews.
2. **Knowledge network**
   - Zettelkasten-style atomic notes, links, synthesis, evergreen knowledge.

The output must define bidirectional interfaces between both systems.

## Autonomy Policy (Max-Autonomy Target)
Design for highest feasible autonomy, but with explicit guardrails.

- Claude should proactively run safe deterministic operations without waiting for prompts.
- Claude should auto-queue human-required items and propose schedules.
- Claude should track incomplete commitments and accountability loops.
- Claude must enforce hard safety boundaries for high-risk actions.

## Hard Constraints
- No vague "it depends" architecture sections without decision criteria.
- No framework mashups without precedence/conflict rules.
- No hidden assumptions about source of truth.
- No generic advice unsupported by operational mechanisms.

## Decisions You Must Explicitly Specify
Provide explicit rules for:

1. Source-of-truth per object type (task, project, note, event, deliverable).
2. Conflict resolution across Obsidian, GitHub, and Google Calendar.
3. Lifecycle transitions (active, waiting, scheduled, archived, deleted).
4. Review cadence and outputs (daily, weekly, monthly, quarterly, annual).
5. Privacy/security boundaries for autonomous actions.
6. Escalation policy when autonomy is blocked.
7. Definitions and intended role of ACE, IDI, COG, Johnny Decimal in this system.

## Quality Gates
Your output is acceptable only if:

- It is actionable and implementation-ready.
- Every workflow has: inputs, outputs, owner, trigger, completion criteria.
- It includes anti-patterns and failure modes.
- It includes measurable KPIs for system health.
- It is compact, non-redundant, and structured for reuse.

## Output Format Contract
Return in this exact section order:

1. `# Strategy Brief`
2. `# SKILL.md`
3. `# Companion Pack`
   - `## Fractal Layering Rubric`
   - `## Autonomy Policy Matrix`
   - `## LifeOS Data Model Template`
   - `## Review Cadence Template`
   - `## Anti-Patterns and Guardrails`

Use markdown. Keep language precise, imperative, and testable.

---

# Authoritative architecture (local v1)

This section is the **grounded copy** maintained in-repo when NotebookLM is unavailable. Keep NotebookLM outputs aligned with it; revise here first, then refresh guides.

## Fractal Simplicity Law (all layers)

1. **Top layers MUST be short, universal, and stable.** Principles and GovernanceRules fit in a small surface area; no tool-specific playbooks at that level.
2. **Complexity increases only downward.** A child layer MAY add rules only if it: inherits parent constraints; does not contradict parent MUST/NEVER; adds measurable value; states its scope explicitly.
3. **Naming is fractal:**
   - **Global grammar (top):** charset, separators, max length, forbidden ambiguity (one short spec).
   - **PARA-scoped extensions:** Areas, Projects, Resources MAY add suffixes or tokens **on top of** the global grammar, never breaking it.
   - **Examples:** `doc-2025-annual-review` (global); `area-health--sleep-protocol` (area); `proj-website-v2--milestone-3` (project).

## Fractal Claude harness (token-efficient)

Canonical detail: [lifeos-fractal-architect/references/fractal-claude-harness.md](lifeos-fractal-architect/references/fractal-claude-harness.md)

**Invariant:** `settings.json` = toggles/env only. **Root `CLAUDE.md`** (this tree: `~/.claude/CLAUDE.md`) = routing + universal heuristics. **Nested `CLAUDE.md`** = domain/project decision trees. **`SKILL.md` / `AGENT.md`** = dense execution. No duplicate MUST/NEVER across layers; link down.

## System intent (summary)

Deterministic LifeOS: strict **Firstbrain** (human meaning) vs **Second Brain** (AI execution) separation; immutable-style governance; explicit state; max autonomy with gates.

## Scope and constraints

- **Single source of truth per object facet** (not per whole “project” blob).
- **No hard delete.** Terminal action for quarantine: **export-to-cold-storage + permanent exclude-from-queries**. Use `voided`, `#quarantine`, archive patterns with retention.
- **Tunable variables** live only in the **Canonical Policy Variable Registry**; tuned in Monthly Review unless blast radius requires Annual.

## Method precedence (conflict order)

1. Safety and capacity (**Google Calendar**)
2. Action execution (**GitHub** + GTD clarification)
3. Containment (**Obsidian** + PARA + Johnny Decimal)
4. Knowledge synthesis (Zettelkasten)
5. Cascading goals

## Facet ownership map

| Object facet | Canonical owner | Mirror | Sync |
|--------------|-----------------|--------|------|
| Object identity (UUIDs) | Originating system (minter) | Receiving system (reference only) | Origin → mirror |
| Execution state | GitHub | Obsidian (queries) | GitHub → Obsidian |
| Scheduling / time | Google Calendar | Obsidian (daily note) | GCal → Obsidian |
| Narrative / context | Obsidian | GitHub (snippet / link) | Obsidian → GitHub |
| Archival (execution truth) | GitHub (closed/archived) | Obsidian (archive paths) | GitHub → Obsidian |

**UUID minting:** GitHub mints task/milestone IDs; Obsidian mints note IDs; GCal mints event IDs. Mirrors reference; they do not remint.

## Confidence bands (evidence required)

Every autonomous action MUST emit `confidence` 0–100 and:

- `schema_validation_pass` (bool)
- `source_coverage_count` (int)
- `conflict_check_pass` (bool)

**If any evidence field is missing,** set `confidence` to **below `APPROVAL_MIN`** (treat as blocked or gated — never guess).

Boundaries (no ambiguity at equality):

- `confidence >= AUTO_EXECUTE_MIN` → auto-execute
- `APPROVAL_MIN <= confidence < AUTO_EXECUTE_MIN` → approval-gated
- `confidence < APPROVAL_MIN` → blocked

Registry defaults: `AUTO_EXECUTE_MIN = 90`, `APPROVAL_MIN = 75` (tune via registry).

## Policy variable registry (defaults)

| Variable | Default | Owner review |
|----------|---------|----------------|
| `AUTO_EXECUTE_MIN` | 90 | Annual |
| `APPROVAL_MIN` | 75 | Annual |
| `MAX_FOLDER_DEPTH` | 3 | Annual |
| `MIN_LINKS_PER_ATOM` | 2 | Monthly |
| `MAX_ACTIVE_PROJECTS` | 12 | Monthly |
| `CAPACITY_ALERT_PCT` | 20 | Monthly |

## Retention lifecycle (no hard delete)

| State | Retention | Visibility | Terminal action |
|-------|-----------|------------|------------------|
| Active | indefinite | default | → done / archived |
| Voided | 30d | hidden | → archived |
| Quarantine | 30d | admin | export + exclude-from-queries |
| Archived | indefinite | archive queries | none |

## Deployment profiles

- **Profile A (Advisory):** read/plan only; promotion uses measurable gates (e.g. zero harmful automation incidents over window — define in monthly review).
- **Profile B (Bounded):** auto local vault hygiene; external writes gated; DLQ SLA + reconciliation drills required before Profile C.
- **Profile C (Full policy):** confidence bands + kill-switch + DLQ monitoring.

## Human override lock

Manual human edit sets `human_override_lock=true` on that object (default **24h**, single-object scope). Automation mutates that object only after lock expiry **and** reconciliation passes. If `sync_locked=true` simultaneously, **reconciliation wins first**; then clear override lock only if safe.

## Service degradation mode

If GitHub, GCal, or vault is unavailable: **read-only degradation** — queue mutating ops locally; single daily digest; re-entry after **health probe success** (not only “3× HTTP 200” — include auth validity + successful read-only API probe). Document exact probes in project `CLAUDE.md`.

## Split-brain reconciliation (sketch)

1. Detect stale mirror (clock skew / version).
2. Tie-break: canonical timestamp → monotonic version → actor priority `human > system > claude`.
3. Class 2 loser diff: cap **2000** chars; overflow → cold artifact URI in comment.
4. DLQ for missing dependency UUIDs; `sync_locked=true`.

## Idempotency + audit

- `transition(S,S)` = **no_op**; **no** audit row.
- Any real transition MUST append the JSON audit: `transition_id`, `timestamp`, `actor`, `from_state`, `to_state`, `reason`, `evidence{schema_validation_pass, source_coverage_count, conflict_check_pass}`.

## Operational runbook (10 bullets)

1. Daily anchor: inbox, staged approvals, expired `human_override_lock` sweep.
2. Weekly: active projects, DLQ, capacity vs backlog.
3. DLQ triage: missing UUID / failed sync — assign or void.
4. Reconciliation: after outage or lock expiry.
5. Profile promotion: only with checklist + metrics from registry.
6. Kill-switch: if `<APPROVAL_MIN` three times in one hour on mutating path — freeze mutations, reconcile.
7. Kill-switch drill: monthly simulated outage.
8. Audit sample: 5 transition records / month.
9. Cold export: quarantine exit — encrypt + access policy in project docs.
10. Registry tune: monthly review adjusts variables within bounds.

## Assumptions pending confirmation

- **ACE / IDI / COG:** interim definitions belong in project `CLAUDE.md` until you lock them.
- Effort estimation format; COG cron vs manual — decide once and document in registry owner row.

## ACE / IDI / COG (interim)

- **ACE:** GitHub issue shape: Action = verb-led title; Context = Obsidian link / JD id; Execution = definition of done + evidence field.
- **IDI:** Inbox → digest → integrate (permanent note + links).
- **COG:** Categorize (PARA) → organize (GitHub state) → generate (calendar proposals).

---

## File map (this repo)

| Path | Role |
|------|------|
| `~/.claude/settings.json` | Global harness toggles |
| `~/.claude/CLAUDE.md` | Root router |
| `~/.claude/notebooklm_lifeos_fractal_brief.md` | This document |
| `~/.claude/lifeos-fractal-architect/SKILL.md` | Agent skill entry |
| `~/.claude/lifeos-fractal-architect/references/*.md` | Deep templates |
