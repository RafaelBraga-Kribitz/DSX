# Fractal Layering Rubric

**Purpose:** Verify that any LifeOS architecture artifact is genuinely layered and fractal before accepting it.  
**Owner:** Human (reviewed at monthly cadence for drift).  
**Use:** Apply to every new workflow, policy, or playbook before merging into the active system.

---

## Fractal Simplicity Law (cross-cutting; applies at all layers)

- **Top = short and universal.** Principles and GovernanceRules contain no tool playbooks, no long examples, no step-by-step procedures.
- **Bottom = specific and dense.** Protocols and TaskPlaybooks may include full schemas, API shapes, templates, and examples.
- **Naming follows the same law.** Global grammar is minimal at root; PARA-scoped extensions add allowed tokens on top; they never break the root grammar.
- **Violation test.** If a rule needs a detailed example or a conditional sub-step to be understood, it does not belong at Principles or GovernanceRules. Push it down.

---

## Layer Definitions and Quality Criteria

### Layer 1 — Principles

**Role:** Non-negotiable design truths. The system rejects any rule, tool, or workflow that violates a Principle.  
**Expected output:** 5–9 compact, imperative, testable statements.  
**Owner:** Human (annual review minimum).  
**Trigger:** New architecture decision that requires a design truth check.  
**Inputs:** Architecture decisions, first-principles analysis.  
**Outputs:** Approved principle set with changelog.  
**Completion criteria:** Each principle fits in one sentence; no principle requires a conditional sub-clause to apply; no principle is a tool-specific instruction.  
**Escalation:** Any new design decision requiring a Principle change → escalate to Annual Review. Do not patch in place.

**Smell (reject if present):**
- Principle is an implementation step ("Use GitHub for all tasks").
- Principle contains a conditional ("...unless the project is small").
- More than 9 principles (complexity explosion at the top).

---

### Layer 2 — GovernanceRules

**Role:** Global constraints and decision rights. These are the hard boundaries the system enforces automatically.  
**Expected output:** Policy rules with MUST/NEVER/ALWAYS language. No ambiguity.  
**Owner:** Human (monthly review for limited-blast changes; annual for structural changes).  
**Trigger:** Detected policy gap, conflict between systems, or breach event.  
**Inputs:** Principles (inherited).  
**Outputs:** Rule set with owner, review cadence, and breach action per rule.  
**Completion criteria:** Every rule is testable; every rule names its canonical system or facet owner; every rule has a breach action; no rule uses "should consider" language.  
**Escalation:** Breach of a GovernanceRule triggers immediate review. Do not silently override.

**Smell (reject if present):**
- "Should consider" language (not enforceable).
- Rule that duplicates a Principle word-for-word (hierarchy collapse).
- Rule with no named owner or breach action.

---

### Layer 3 — OperatingModels

**Role:** How the system behaves in steady-state operation. Structural description, not procedural instruction.  
**Expected output:** Ownership maps, state machines, data flow diagrams, facet SoT tables.  
**Owner:** Human + Claude (monthly review).  
**Trigger:** System restructure, tool change, or detected facet ambiguity.  
**Inputs:** GovernanceRules (inherited), tool capabilities.  
**Outputs:** Facet ownership table, lifecycle state machine, sync direction table.  
**Completion criteria:** Every facet has exactly one canonical owner; every state transition is named; every sync direction is explicit.  
**Escalation:** OperatingModel conflict → escalate to GovernanceRules layer for resolution.

**Smell (reject if present):**
- Operating model duplicates a governance rule verbatim.
- A state transition has no named trigger.
- Two systems claim canonical ownership of the same facet.

---

### Layer 4 — Workflows

**Role:** Repeatable domain processes triggered by specific events.  
**Expected output:** `trigger → input → process → output → owner → completion criteria → failure path` chains.  
**Owner:** Claude (executes); Human (approves changes at monthly review).  
**Trigger:** Domain-level event (unprocessed inbox, action item surfaced, issue ready for scheduling).  
**Inputs:** OperatingModels (inherited), domain context.  
**Outputs:** Workflow chains for IDI, ACE, COG, and review cadences.  
**Completion criteria:** Every workflow has a named trigger (not "whenever needed"); explicit completion criteria; named failure path with a specific outcome.  
**Escalation:** Workflow failure → DLQ entry; surface in next daily anchor.

**Smell (reject if present):**
- Trigger: "as needed."
- No completion criteria.
- Workflow that modifies GovernanceRules (belongs higher).

---

### Layer 5 — Protocols

**Role:** Precise run conditions, preconditions, and safety checks for specific operations.  
**Expected output:** Procedure contracts with preconditions, postconditions, and fallback rules.  
**Owner:** Claude (executes with confidence gate); Human (approves).  
**Trigger:** Specific operational condition: reconciliation needed, kill-switch fired, health probe required.  
**Inputs:** Workflows (inherited).  
**Outputs:** Reconciliation protocol, kill-switch protocol, health probe spec, split-brain resolution procedure.  
**Completion criteria:** Every protocol lists preconditions; every protocol has a named fallback; every protocol produces auditable output.  
**Escalation:** Three protocol failures in one hour on same path → kill-switch.

**Smell (reject if present):**
- Protocol reinvents workflow logic (consolidate up).
- No fallback path.
- Assumes external system availability without a degradation branch.

---

### Layer 6 — TaskPlaybooks

**Role:** Concrete execution scripts for specific recurring situations.  
**Expected output:** Step-by-step instructions, fill-in schemas, templates, worked examples.  
**Owner:** Claude (executes with confidence gate).  
**Trigger:** Named recurring task: ACE issue creation, IDI processing, COG scheduling, review execution.  
**Inputs:** Protocols (inherited), domain-specific context.  
**Outputs:** ACE issue template, IDI checklist, COG scheduling checklist, review checklists.  
**Completion criteria:** Required inputs listed at top; every step produces a verifiable artifact; confidence evidence fields included.  
**Escalation:** Playbook cannot complete → surface blocker in daily anchor; do not silently skip steps.

**Smell (reject if present):**
- No listed required inputs.
- A step with no output artifact.
- Bypasses confidence evidence check.

---

## Fractal Scorecard

Score each dimension 0–2: (0 = absent/violated, 1 = partial, 2 = fully compliant).

| Dimension | Score |
|---|---|
| Clear role boundary per layer (no layer-blending) | |
| Parent-to-child constraint inheritance (child inherits and does not contradict parent) | |
| No duplicated MUST/NEVER across layers (each rule stated exactly once) | |
| Every layer has named owner and review cadence | |
| Escalation path defined in each layer | |
| Language is testable and unambiguous (no "should consider") | |

**Maximum: 12**

| Score | Verdict |
|---|---|
| 10–12 | Strong fractal architecture. Ship. |
| 7–9 | Usable but leaks between layers. Fix the two lowest-scoring dimensions before full deployment. |
| 4–6 | Significant restructuring needed. Anchor on highest-scoring layer and rebuild. |
| ≤ 3 | Redesign from Principles. Do not deploy. |

---

## Application Checklist

Run before merging any new architecture artifact:

- [ ] Which layer does this artifact belong to?
- [ ] Does it comply with the Fractal Simplicity Law for that layer?
- [ ] Does it inherit parent constraints without contradiction?
- [ ] Does it add only the specificity required for its scope?
- [ ] Does it have a named owner and review cadence?
- [ ] Does it have an escalation path?
- [ ] Does it score ≥ 2 on all six scorecard dimensions?
- [ ] Does it name the source of truth for every system-of-record reference?
