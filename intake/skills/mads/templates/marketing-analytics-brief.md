# Marketing Analytics Brief (MAB)

> Document owner: Carla
> Status: DRAFT | IN REVIEW | APPROVED
> Version: 1.0
> Date:
> Project ID:

---

## 1. Business Question

*State the business question in one plain-language sentence. No model language. No data language.*

> Example: "Are customers who receive the loyalty email more likely to renew their subscription than those who do not?"

**Business question:**

---

## 2. Decision This Analysis Will Inform

*Who makes this decision? What will they decide differently if the analysis shows X vs. Y?*

**Decision:** 

**Decision-maker:**

**Decision timeline:**

**What "act on this" looks like:**
- If result confirms hypothesis →
- If result contradicts hypothesis →
- If result is inconclusive →

---

## 3. Baseline / Status Quo

*How is this problem being addressed today? What do we currently believe?*

**Current approach:**

**Current known performance:**

**Why this is no longer sufficient:**

---

## 4. Success Metrics

### Primary Metric

| Field | Value |
|-------|-------|
| Metric name | |
| Definition | |
| Unit | |
| Current baseline value | |
| Target value | |
| Target timeframe | |
| Who owns this metric | |

### Guardrail Metrics

*Things we must not harm. List at least one.*

| Metric | Definition | Acceptable range |
|--------|-----------|-----------------|
| | | |
| | | |

---

## 5. Project Type

*Carla selects from the decision tree in carla.md*

**Project type:**

- [ ] Causal inference (MMM / Uplift / DiD / SCM)
- [ ] Controlled experiment (A/B test)
- [ ] Propensity / classification model
- [ ] Demand forecasting
- [ ] Customer segmentation
- [ ] Attribution modeling (MTA / MMM)
- [ ] Customer lifetime value
- [ ] Root cause / decomposition analysis

**Methodology direction:**

---

## 6. Stakeholders

| Role | Name / Team | Involvement |
|------|------------|-------------|
| Business owner | | Final approval |
| Primary consumer | | Uses output |
| Data provider | | Data access |
| DS lead | | Delivery |
| Secondary consumer | | FYI |

---

## 7. Data Sources (Preliminary)

*List suspected relevant data sources. Diego will audit these in Phase 2.*

| Source | Type | Owner | Access status |
|--------|------|-------|---------------|
| | | | Confirmed / Unconfirmed / Unknown |
| | | | |

---

## 8. Constraints

**Timeline:**

**Budget:**

**Technical constraints:**

**Regulatory / privacy constraints:**

**Organizational constraints:**

---

## 9. Delivery Format

*How will the output be consumed?*

- [ ] Model API (real-time scoring)
- [ ] Batch scoring (daily/weekly file or table)
- [ ] Dashboard
- [ ] Written report / slide deck
- [ ] Embedded in campaign tool / CRM
- [ ] Other:

**Target delivery date:**

**Refresh cadence (if ongoing):**

---

## 10. Prior Work

*Any past analysis, model, or experiment on this topic we should know about?*

---

## 11. Risk Log

*Filled by Carla during Risk Assessment.*

| Risk | Type | Likelihood | Impact | Mitigation |
|------|------|-----------|--------|-----------|
| | Data | | | |
| | Causal | | | |
| | Ethical | | | |
| | Legal/Privacy | | | |
| | Model | | | |
| | Stakeholder | | | |

---

## 12. Approval

| Reviewer | Role | Date | Status |
|----------|------|------|--------|
| | Business owner | | APPROVED / CHANGES REQUESTED |
| | DS lead | | APPROVED / CHANGES REQUESTED |

---

## Carla's Gate Checklist

Before marking APPROVED:

- [ ] Business question: one sentence, no model language
- [ ] Primary metric: has unit, direction, target, timeframe, owner
- [ ] At least one guardrail metric defined
- [ ] Decision-maker named
- [ ] Project type confirmed
- [ ] Major risks identified
- [ ] Data sources listed (even if unconfirmed)
- [ ] Exactly one business question (no scope creep)
