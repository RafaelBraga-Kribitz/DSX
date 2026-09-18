# AB Testing and Experimentation *AI Prompts *

8 Business Analyst prompts in AB Testing and Experimentation. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain. 

## AI prompts in AB Testing and Experimentation 
8 prompts Beginner Single prompt 01 
### A/B Test Design Brief 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It creates a structured experiment brief that can be reviewed before a test goes live. 
Prompt text Write an A/B test design brief for the following proposed change: {{change_description}}

The brief must include:

1. Hypothesis
 - We believe that [change] will cause [outcome] because [rationale]
 - Null hypothesis: the change has no effect on the primary metric

2. Primary metric: the single metric this test will be judged on
3. Secondary metrics: 2–3 supporting metrics to monitor
4. Guardrail metrics: 2–3 metrics that must not significantly degrade

5. Test setup
 - Unit of randomization: user / session / account / device
 - Traffic split: 50/50 or other (justify any deviation)
 - Targeting: all users, or a specific segment? Why?

6. Statistical parameters
 - Significance level α = 0.05 (two-tailed)
 - Minimum detectable effect (MDE): the smallest change worth detecting
 - Required statistical power: 80%
 - Required sample size per variant (calculate)
 - Required experiment duration given current daily traffic of {{daily_traffic}}

7. Risks: what could go wrong? How will you detect it?
8. Decision criteria: exactly when will you ship, iterate, or kill?

Return: the complete test brief as a shareable document. Copy prompt Open prompt details Intermediate Single prompt 02 
### A/B Test Results Analysis 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It turns raw test results into a decision-ready readout with checks, significance, and business interpretation. 
Prompt text Analyze the results of this A/B test and produce a decision-ready report.

Test data is provided. Include:

1. Pre-analysis checks:
 - Sample ratio mismatch (SRM): is the actual traffic split consistent with the planned split? Use chi-squared test.
 - Was the test run for the full planned duration?
 - Any signs of peeking (early stopping)?

2. Primary metric analysis:
 - Control vs treatment value (mean ± std or conversion rate)
 - Observed absolute and relative difference
 - Statistical test: t-test (continuous) or z-test/chi-squared (proportions)
 - p-value and 95% confidence interval for the difference
 - Is the result statistically significant at α = 0.05?

3. Secondary and guardrail metrics: repeat analysis for each

4. Practical significance: is the observed effect large enough to matter for the business? Compare to the MDE.

5. Segment analysis: break results down by key segments — does treatment work equally across all user types?

6. Decision recommendation: Ship / Do not ship / Iterate / Inconclusive — with clear justification

Return: full analysis report with all tests, segment breakdown, and decision recommendation. Copy prompt Open prompt details Advanced Single prompt 03 
### Experiment Roadmap Builder 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It helps sequence experiment ideas into a realistic roadmap that balances impact, confidence, and effort. 
Prompt text Build a 90-day experimentation roadmap for {{product_area}} based on the provided business objectives and backlog of ideas.

Idea backlog: {{ideas_list}}

1. Score each experiment idea on:
 - Expected impact: how much could this move the primary metric? (1–5)
 - Confidence in hypothesis: how strong is the evidence this will work? (1–5)
 - Implementation effort: engineering days to build (1=<3 days, 5=>20 days)
 - Sample size required: how many weeks at current traffic?
 - Learning value: even if negative, what will we learn? (1–5)

2. Score each idea using ICE score: (Impact × Confidence) / Effort

3. Apply scheduling constraints:
 - Maximum 2 experiments running simultaneously on the same surface
 - Avoid overlapping experiments that share user populations
 - Schedule quick tests (high ICE) first to build velocity

4. Produce a week-by-week experiment calendar for 90 days

5. Identify the top learning that each 30-day block is designed to answer

Return: scored idea table, ICE rankings, experiment calendar, and 30-day learning objectives. Copy prompt Open prompt details Advanced Chain 04 
### Full Experiment Chain 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It connects design, sizing, analysis, stability checks, and business impact into one experimentation workflow. 
Prompt text Step 1: Hypothesis — write a clear falsifiable hypothesis for the proposed change. Define primary metric, secondary metrics, and guardrail metrics.
Step 2: Sample size — calculate required sample size and test duration given baseline metric, MDE, α=0.05, and power=80%.
Step 3: Pre-experiment checks — run an AA test on historical data to verify randomization works. Check for pre-existing imbalances between groups.
Step 4: Run analysis — after experiment completion: check for SRM, run primary statistical test, apply multiple testing correction if needed, segment the results.
Step 5: Novelty and stability check — plot daily results to check for novelty effects or instability. Confirm results are consistent in the second half of the experiment.
Step 6: Business impact calculation — translate the statistical result into business impact: if this effect holds, what is the annual revenue or metric impact?
Step 7: Decision and documentation — write a 1-page experiment summary: hypothesis, method, results, decision (ship/no-ship/iterate), business impact, and lessons learned. Copy prompt Open prompt details Intermediate Single prompt 05 
### Inconclusive Test Diagnosis 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It explains why a test may have failed to reach significance and what to do next. 
Prompt text This A/B test returned an inconclusive result (p > 0.05, no significant effect detected). Diagnose why and recommend next steps.

1. Check statistical power:
 - Was the test adequately powered? Calculate post-hoc power given observed effect size and sample size.
 - If power < 80%, the test was underpowered — this is likely a false negative, not proof of no effect.

2. Check the effect size:
 - What was the observed effect size, even if not significant?
 - Is the observed effect smaller than the MDE? If yes, the test was powered for a larger effect.

3. Check test duration:
 - Was the test run long enough to cover at least one full weekly cycle?
 - Was the test affected by external events (seasonality, promotions, product launches)?

4. Check for segment heterogeneity:
 - Does the effect appear in specific segments even if the overall result is null?
 - This could indicate the change is right for a subset of users.

5. Based on the diagnosis, recommend one of:
 - Re-run with larger sample size (provide new calculation)
 - Re-run targeting only the segment where effect appeared
 - Redesign the test with a stronger treatment
 - Accept the null — the change genuinely has no effect

Return: power analysis, effect size assessment, duration check, segment analysis, and recommendation. Copy prompt Open prompt details Intermediate Single prompt 06 
### Multiple Testing Correction 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It adjusts significance decisions when many metrics or variants were tested at once. 
Prompt text Apply multiple testing corrections to this experiment that tested multiple metrics or multiple variants simultaneously.

Test data provided includes {{num_metrics}} metrics and/or {{num_variants}} variants.

1. Explain the multiple testing problem:
 - With {{num_tests}} independent tests at α=0.05, the probability of at least one false positive is {{familywise_error_rate}}%
 - Without correction, we are likely to see spurious significant results

2. Apply and compare three correction methods:
 a. Bonferroni correction: α_adjusted = 0.05 / number of tests
 b. Holm-Bonferroni (step-down): less conservative than Bonferroni
 c. Benjamini-Hochberg (FDR): controls false discovery rate at 5%

3. For each metric, show: raw p-value | Bonferroni adjusted | Holm adjusted | BH adjusted | significant after each correction?

4. Recommend which correction method to use for this specific test and why

5. Re-state the decision recommendation after applying the correction — does it change?

Return: corrected p-value table, method comparison, and final decision recommendation. Copy prompt Open prompt details Intermediate Single prompt 07 
### Novelty Effect Check 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It checks whether an experiment lift is real and durable or just an early reaction to something new. 
Prompt text Check whether this A/B test result is driven by a novelty effect rather than a genuine sustained improvement.

A novelty effect occurs when users behave differently simply because something is new — the effect fades over time as users habituate.

1. Plot the primary metric for treatment and control groups over time (day by day or week by week)
2. Check for the novelty effect pattern:
 - Large early treatment lift that narrows or disappears over time
 - Treatment performance converges toward control in later weeks
3. Segment analysis by user tenure:
 - Compare treatment effect for new users (first 30 days) vs established users (>90 days)
 - A novelty effect typically only appears in established users, not new ones
4. Compute the treatment effect for the first half vs second half of the experiment
 - If first-half effect is significantly larger than second-half, novelty effect is likely
5. Extrapolate: if the novelty effect is confirmed, what is the expected long-term steady-state lift?

Return: time series plot of treatment vs control, novelty effect diagnosis, user tenure breakdown, and long-term lift estimate. Copy prompt Open prompt details Beginner Single prompt 08 
### Sample Size Calculator 

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It estimates how much traffic and time an experiment needs before the results can be trusted. 
Prompt text Calculate the required sample size for this A/B test.

Inputs:
- Primary metric type: {{metric_type}} (conversion rate / continuous metric)
- Baseline value: {{baseline}} (e.g. current conversion rate of 5%, or mean revenue of $42)
- Minimum detectable effect (MDE): {{mde}} (e.g. 10% relative lift, or absolute +0.5%)
- Significance level α: 0.05 (two-tailed)
- Statistical power: 80%
- Number of variants: {{variants}} (e.g. 2 = one control + one treatment)

Calculate and return:
1. Required sample size per variant
2. Total sample size across all variants
3. Required test duration given daily traffic of {{daily_traffic}} users/sessions
4. Sensitivity table: how does sample size change as MDE varies?
 - MDE at 50%, 75%, 100%, 125%, 150% of the specified MDE
5. Power curve: plot statistical power vs sample size for the specified MDE
6. Flag if the required duration exceeds 4 weeks — longer tests are vulnerable to seasonality and novelty effects

Return: sample size calculation, duration estimate, sensitivity table, and power curve. Copy prompt Open prompt details 
## Recommended AB Testing and Experimentation workflow 
1 
### A/B Test Design Brief 

Start with a focused prompt in AB Testing and Experimentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### A/B Test Results Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Experiment Roadmap Builder 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Full Experiment Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
