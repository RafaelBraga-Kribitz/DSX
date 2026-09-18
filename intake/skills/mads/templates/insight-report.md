# Insight Report (IR)

> Document owner: Petra
> Status: DRAFT | IN REVIEW | APPROVED | DISTRIBUTED
> Version: 1.0
> Date:
> References: MAB v{n}, DAR v{n}, Model Card v{n} (if applicable)

---

## Executive Summary

*Max 150 words. Start with the answer. Written for a non-technical reader.*

**Finding:**

**Recommendation:**

**Confidence:** High / Medium / Low — *one sentence explaining why*

---

## 1. Context

### Business Question

*Copy directly from MAB. Do not paraphrase.*

### What We Did

*2–3 sentences. Jargon-free. What data, what method, what period.*

### What We Were Looking For

*The primary metric, its target, and the guardrail metrics from the MAB.*

---

## 2. Findings

### Primary Metric

| | Control / Before | Treatment / After | Change | 95% CI | p-value (if experiment) |
|--|--|--|--|--|--|
| {Primary metric} | | | | | |

**Plain-language interpretation:**

*Example: "Customers who received the loyalty email renewed at a rate 4.2 percentage points higher
than those who did not (95% CI: 2.1pp to 6.3pp). At our current renewal volume, this represents
approximately €X in incremental annual recurring revenue."*

### Guardrail Metrics

| Metric | Before / Control | After / Treatment | Status |
|--------|-----------------|------------------|--------|
| | | | ✅ Within bounds / ⚠️ Review / ❌ Violated |

### Supporting Evidence

*Key supporting findings (2–4 points). Each finding = specific number with unit.*

1.
2.
3.

### Segment Findings

*Only pre-specified segments from the MAB or EP.*

| Segment | Result | Interpretation |
|---------|--------|---------------|
| | | |

---

## 3. Uncertainty and Limitations

*Be honest. Every analysis has limitations. Naming them builds trust; hiding them destroys it.*

### What Could Make This Wrong

1.
2.

### What We Deliberately Excluded

*What was out of scope, and why?*

### Data Quality Notes

*Reference DAR for known issues. Flag any that affect confidence in the findings.*

### Confidence Level Assessment

| Dimension | Assessment |
|-----------|-----------|
| Data quality | Strong / Moderate / Weak |
| Sample size | Sufficient / Borderline / Insufficient |
| Causal claim strength | Strong (RCT) / Moderate (quasi-experiment) / Weak (observational) |
| Overall confidence | High / Medium / Low |

---

## 4. Recommendation

*Specific. Actionable. Time-bound. Named owner. One recommended action per row.*

| Action | Owner | Timeline | Expected outcome |
|--------|-------|----------|-----------------|
| | | | |

**Cost of inaction:**

*What happens if we do nothing? Quantify if possible.*

**What success looks like in 90 days:**

---

## 5. Next Steps

*Exactly one next action required from each audience.*

| Audience | Next action | By when |
|---------|------------|---------|
| {Decision-maker} | | |
| {CRM / Marketing team} | | |
| {Data team} | | |

---

## Appendix

### Methodology

*Technical description for data team readers. Reference the MSD or EP for full detail.*

**Method used:**

**Training/evaluation period:**

**Model version (if applicable):** See `reports/model_card_{name}.md`

**Experiment ID (if applicable):**

### Data Sources

| Source | Period | Owner | Known quality issues |
|--------|--------|-------|---------------------|
| | | | |

### Reproducibility

*How to re-run the analysis:*

```bash
# Clone repo
git clone {repo_url}
cd {project_name}
uv sync

# Re-run analysis
make {analysis_command}
```

**Relevant files:**
- Feature pipeline: `src/{project_name}/features/feature_pipeline.py`
- Model: `models/{model_name}_v{n}.pkl`
- Evaluation notebook: `notebooks/04_evaluation_{description}.ipynb`

---

## Petra's Quality Gate

- [ ] Executive summary: readable in under 30 seconds
- [ ] Primary metric result includes confidence interval
- [ ] All guardrail metrics reported
- [ ] Plain-language interpretation written for every key number
- [ ] Recommendation is specific, time-bound, and names an owner
- [ ] Cost of inaction stated
- [ ] Limitations section complete and honest
- [ ] No unsupported causal claims in the body (observational results hedged appropriately)
- [ ] Stakeholder review scheduled (not just emailed)
