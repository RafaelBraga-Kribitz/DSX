# Model Specification Document (MSD)

> Document owner: Marco
> Status: DRAFT | IN REVIEW | APPROVED
> Version: 1.0
> Date:
> References MAB version:
> References DAR version:

---

## 1. Model Purpose

*One paragraph. What does this model predict, for whom, and why?*

---

## 2. Model Type

- [ ] Binary classification
- [ ] Multi-class classification
- [ ] Regression
- [ ] Time series forecasting
- [ ] Clustering / segmentation
- [ ] Causal / uplift model
- [ ] Ranking / recommendation

**Prediction target:**

**Unit of prediction:** (user / session / order / SKU / geo)

---

## 3. Label Definition

**Label name:**

**Label construction:**

*Exact logic for how the label is computed. If binary: what event, in what window, defines a positive?*

```
Example:
label = 1 if (user made 0 purchases in the 90 days following their reference_date)
           AND (user was active in the 90 days prior to reference_date)
label = 0 otherwise
```

**Label window:**

**Reference date definition:**

**Known label issues:**

---

## 4. Feature Windows

```
Timeline:
|--- feature window ---|--- buffer ---|--- label window ---|
                   reference_date                       label_date
```

**Feature window:** days before reference_date

**Buffer period:** days between feature cutoff and label start (prevents leakage)

**Label window:** days after reference_date

---

## 5. Feature Set

*List all candidate features. Diego's leakage check must have cleared all of these.*

| Feature name | Source | Description | Available at inference? | Leakage risk |
|-------------|--------|-------------|------------------------|-------------|
| recency_days | events table | Days since last purchase | Yes | None |
| | | | | |

**Excluded features and reasons:**

---

## 6. Evaluation Metrics

### Primary Metric (must match MAB)

| Metric | Formula | Business interpretation |
|--------|---------|------------------------|
| | | |

### Secondary Metrics

| Metric | Threshold to deploy | Notes |
|--------|--------------------|-|
| | | |

### Baseline to Beat

*The naive model performance. Marco must document this before any candidate model.*

**Baseline type:**
- [ ] DummyClassifier (most_frequent)
- [ ] Global mean (for regression)
- [ ] Previous model version
- [ ] Business rule heuristic (describe):

**Baseline performance on test set:**

---

## 7. Train / Test Split Design

**Split type:**
- [ ] Random stratified split
- [ ] Temporal split (required for time-aware data)

**Split ratios:**

**Temporal split date (if applicable):**

**Reasoning:**

---

## 8. Candidate Models

*List models to evaluate. Keep it short. Justify complexity.*

| Model | Justification | Complexity |
|-------|--------------|-----------|
| Logistic Regression | Baseline; interpretable | Low |
| | | |

**Model selection criterion:**

---

## 9. Validation Strategy

**Cross-validation scheme:**

**Tuning strategy:**

**Final evaluation:** held-out test set only (no tuning on test)

---

## 10. Inference Design

**Serving mode:**
- [ ] Batch (daily/weekly scoring table)
- [ ] Real-time API
- [ ] Embedded

**Input at inference time:** (exact features available when scoring)

**Output format:** (score, rank, label, probability)

**Latency requirement (if real-time):**

**Volume:** users/rows scored per run

---

## 11. Deployment Threshold

**Minimum test-set performance required to deploy:**

| Metric | Minimum to deploy |
|--------|------------------|
| | |

**If threshold not met:** action (iterate / revise MAB / escalate)

---

## 12. Retraining Cadence

**Initial retraining schedule:**

**Trigger conditions:** (see Otto's MonSpec)

---

## 13. Ethical Review

**Protected attributes excluded from features:** (gender, age, ethnicity, religion)

**Bias audit plan:** (performance by segment, fairness metric)

**High-risk use check:** (does the model affect credit, employment, or housing? → escalate)

---

## Marco's Gate Checklist

Before writing code:

- [ ] MAB approved and referenced
- [ ] DAR approved and referenced
- [ ] Label defined unambiguously
- [ ] Feature windows defined; leakage buffer present
- [ ] All features confirmed available at inference time
- [ ] Baseline model type selected
- [ ] Evaluation metric matches MAB primary metric
- [ ] Deployment threshold stated
- [ ] MSD reviewed and approved before model code starts
