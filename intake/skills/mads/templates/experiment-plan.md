# Experiment Plan (EP) — Pre-Registration Document

> Document owner: Eva
> Status: DRAFT | PRE-REGISTERED | RUNNING | COMPLETE
> Version: 1.0
> Date pre-registered:
> References MAB version:
> References DAR version:

---

## ⚠️ Pre-Registration Lock Notice

Once this document is marked PRE-REGISTERED, no changes to sections 1–8 are permitted
without creating a new version with a documented amendment rationale. Any post-hoc
changes must be flagged explicitly in section 9 (Amendments).

---

## 1. Experiment Hypothesis

**Null hypothesis (H₀):**

> Example: There is no difference in 30-day renewal rate between users who receive the
> loyalty email treatment and users who do not.

**Alternative hypothesis (H₁):**

> Example: Users who receive the loyalty email treatment have a higher 30-day renewal rate.

**Direction:** One-tailed / Two-tailed (and why)

---

## 2. Treatment Description

*Describe the treatment precisely. Someone who did not design the experiment must be able to
implement it correctly from this description alone.*

**Treatment (what the test group experiences):**

**Control (what the control group experiences):**

**Are there multiple treatment arms?** If yes, list each with exact description.

---

## 3. Randomization Design

**Randomization unit:** (user / session / device / geo / cohort)

**Randomization method:** (random hash, stratified random, blocked, cluster)

**Stratification variables (if any):**

**SUTVA assessment:**
*Can the treatment experienced by one unit affect another unit's outcome? If yes, explain
the spillover risk and how it is mitigated.*

**Exclusion criteria:**
*Who is excluded from the experiment and why?*

---

## 4. Metrics (Pre-Registered — Do Not Change After Lock)

### Primary Metric

| Field | Value |
|-------|-------|
| Metric name | |
| Definition (exact formula) | |
| Unit | |
| Direction | Higher is better / Lower is better |
| Baseline value (from DAR) | |

### Guardrail Metrics

| Metric | Definition | Acceptable range | Action if violated |
|--------|-----------|-----------------|-------------------|
| | | | |

### Pre-Specified Segments

*Segments where subgroup analysis is pre-approved. No post-hoc segments allowed.*

| Segment | Definition | Analysis type |
|---------|-----------|--------------|
| | | |

---

## 5. Power Analysis

| Parameter | Value |
|-----------|-------|
| Baseline rate / mean | |
| Minimum detectable effect (MDE) — absolute | |
| Minimum detectable effect (MDE) — relative | |
| Significance level (α) | 0.05 |
| Desired power (1 - β) | 0.80 |
| Required sample size per group | |
| Total required sample size | |
| Expected daily traffic to experiment | |
| Minimum experiment runtime (days) | |

**Power analysis code (Eva runs and documents):**

```python
# Power analysis — computed by Eva on {date}
from scipy import stats
import numpy as np

baseline_rate = {value}
mde_relative = {value}
alpha = 0.05
power = 0.80

treatment_rate = baseline_rate * (1 + mde_relative)
z_alpha = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(power)

p_bar = (baseline_rate + treatment_rate) / 2
n_per_group = int(np.ceil(
    (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar))
     + z_beta * np.sqrt(baseline_rate * (1 - baseline_rate) + treatment_rate * (1 - treatment_rate))) ** 2
    / (treatment_rate - baseline_rate) ** 2
))
print(f"Required n per group: {n_per_group}")
print(f"Total n: {n_per_group * 2}")
```

---

## 6. Timeline

| Milestone | Date |
|-----------|------|
| Pre-registration locked | |
| A/A test period (optional) | |
| Experiment start date | |
| Minimum end date (from power analysis) | |
| Planned end date (business cycle complete) | |
| Analysis date | |
| Results shared with stakeholders | |

**Novelty effect mitigation:**
*How long before novelty effects are expected to decay? How is this reflected in the timeline?*

---

## 7. Analysis Plan

**Statistical test:**

**Variance reduction method:** (CUPED / none)

**Multiple comparisons correction:** (Bonferroni / Benjamini-Hochberg / pre-registration / none)

**Outlier handling:**

**Minimum detectable effect recalibration:** (will we adjust if traffic is lower than expected?)

**Early stopping policy:** (none recommended unless pre-planned sequential testing)

---

## 8. Implementation Checklist

- [ ] Treatment implemented and verified in staging
- [ ] Logging confirmed: events are being tracked for all metrics
- [ ] A/A test run and balance confirmed
- [ ] Randomization unit assignments are stable (same user always gets same variant)
- [ ] Control group is a true holdout (not a historical baseline)
- [ ] Experiment start date and end date locked in experiment tracking system
- [ ] Stakeholders notified of start date and expected results date

---

## 9. Results (Filled After Experiment Completes)

**Experiment status:** RUNNING / COMPLETE / STOPPED EARLY

**If stopped early, reason:**

### Primary Metric Results

| | Control | Treatment | Difference | 95% CI | p-value |
|--|---------|-----------|-----------|--------|---------|
| N (users) | | | | | |
| Primary metric | | | | | |

**Practical significance assessment:**
*Is the observed effect size commercially meaningful, independent of statistical significance?*

### Guardrail Metric Results

| Metric | Control | Treatment | Change | Status |
|--------|---------|-----------|--------|--------|
| | | | | ✅ OK / ⚠️ Review / ❌ Violated |

### Pre-Specified Segment Results

| Segment | Control | Treatment | Difference | p-value |
|---------|---------|-----------|-----------|---------|

### Recommendation

- [ ] Ship treatment (primary metric improved, no guardrail violations)
- [ ] Do not ship (no significant lift or guardrail violated)
- [ ] Iterate and retest (effect too small; redesign treatment)
- [ ] Escalate (guardrail violated; stop immediately)

**Recommended action:**

---

## 10. Amendments

*Any deviation from the pre-registered plan must be documented here with rationale and date.*

| Amendment | Date | Reason | Approved by |
|-----------|------|--------|-------------|
| | | | |

---

## Eva's Quality Gate

- [ ] H₀ and H₁ stated formally
- [ ] Primary metric pre-registered and matches MAB
- [ ] Guardrail metrics pre-registered
- [ ] SUTVA stated and assessed
- [ ] Power analysis computed and documented with code
- [ ] Runtime covers at least one full business cycle
- [ ] Pre-specified segments listed (none added post-hoc)
- [ ] Analysis plan written before data collection begins
- [ ] Document locked before experiment launches
