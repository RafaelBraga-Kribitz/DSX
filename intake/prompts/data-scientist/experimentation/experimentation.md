# Experimentation *AI Prompts *

9 Data Scientist prompts in Experimentation. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 8 single prompts · 1 chain. 

## AI prompts in Experimentation 
9 prompts Beginner Single prompt 01 
### A/B Test Analysis 

This prompt analyzes a standard A/B test with both statistical and business interpretation. It is useful when you need a clean answer to whether the experiment worked and whether the result is large enough to matter. The workflow includes SRM, significance, confidence intervals, and recommendation logic. 
Prompt text Analyze the results of this A/B test.

1. Describe the experiment: what was tested, what is the primary metric, how many users in each group?
2. Check for sample ratio mismatch (SRM): is the split between control and treatment what was intended? Use a chi-squared test.
3. Run the primary hypothesis test:
 - For conversion rates: two-proportion z-test or chi-squared test
 - For continuous metrics: two-sample t-test or Mann-Whitney U test
4. Report: p-value, observed difference, 95% confidence interval for the difference, and statistical power
5. Calculate practical significance: is the observed effect large enough to matter for the business? Compare to the minimum detectable effect.
6. State the recommendation clearly: ship, do not ship, or run a follow-up experiment — and why. Copy prompt Open prompt details Advanced Single prompt 02 
### Bayesian A/B Analysis 

This prompt analyzes experiment results through a Bayesian lens, focusing on posterior uncertainty and decision-making under risk. It is useful when teams prefer probabilities of winning and expected loss over binary p-value decisions. It also lets you compare Bayesian and frequentist conclusions directly. 
Prompt text Analyze this A/B test using a Bayesian framework instead of frequentist hypothesis testing.

1. Model the conversion rate for control and treatment as Beta distributions:
 - Prior: Beta(1, 1) — uninformative
 - Posterior: Beta(1 + conversions, 1 + non-conversions) for each variant
2. Plot the posterior distributions for control and treatment on the same chart
3. Compute:
 - Probability that treatment beats control: P(θ_treatment > θ_control) using Monte Carlo sampling (100k samples)
 - Expected lift: mean of (θ_treatment - θ_control) / θ_control
 - 95% credible interval for the lift
 - Expected loss from choosing the wrong variant
4. Apply a decision rule: ship treatment if P(treatment > control) > 0.95 AND expected lift > MDE of {{mde}}
5. Compare the Bayesian conclusion to a frequentist t-test conclusion — do they agree?

Return: posterior plots, probability table, decision recommendation, and a plain-English interpretation. Copy prompt Open prompt details Advanced Single prompt 03 
### Causal Inference Analysis 

This prompt estimates causal effects from observational data when randomized experiments are unavailable. It is useful for policy, operations, and product questions where treatment assignment may be confounded. By comparing several estimators, it helps judge how robust the inferred effect appears. 
Prompt text Estimate the causal effect of {{treatment_variable}} on {{outcome_variable}} from this observational dataset (no random assignment).

1. Describe the confounding problem: which variables are likely confounders that affect both treatment assignment and the outcome?
2. Apply Propensity Score Matching (PSM):
 - Estimate propensity scores using logistic regression
 - Match treated to control units on propensity score (1:1, nearest neighbor)
 - Check covariate balance before and after matching (standardized mean differences)
3. Estimate the Average Treatment Effect on the Treated (ATT) using matched pairs
4. Apply Inverse Probability of Treatment Weighting (IPTW) as a cross-check
5. Apply a Doubly Robust estimator combining propensity score and outcome model
6. Compare ATT estimates from all three methods — are they consistent?

Return: balance table, ATT estimates with 95% CIs, and a plain-English interpretation of the causal effect. Copy prompt Open prompt details Intermediate Single prompt 04 
### Experiment Guardrail Check 

This prompt checks whether a promising experiment result hides unacceptable side effects. It is especially useful when shipping decisions depend on more than the primary metric alone. The analysis makes trade-offs explicit so gains and harms can be judged together. 
Prompt text Check the guardrail metrics for this experiment to ensure no unintended harm was caused.

Guardrail metrics are metrics that must not be significantly degraded even if the primary metric improves.

1. List all guardrail metrics provided in the dataset (e.g. page load time, error rate, support tickets, refund rate)
2. For each guardrail metric, test whether treatment significantly degraded it vs control (one-sided test, α=0.05)
3. Report: guardrail metric | control mean | treatment mean | % change | p-value | status (✅ Safe / 🔴 Degraded)
4. Flag any guardrail metric that is significantly degraded — this may block shipping even if the primary metric improved
5. Compute the trade-off: if a guardrail is degraded, what is the net business impact of the primary metric gain minus the guardrail loss?

Return the guardrail report and a final ship/no-ship recommendation considering both primary and guardrail results. Copy prompt Open prompt details Advanced Chain 05 
### Full Experiment Design Chain 

This prompt designs an experiment from first principles before any users are exposed. It is useful for pre-registration, alignment with product and business stakeholders, and avoiding weak experiment setups. The chain covers hypothesis, sample size, randomization, guardrails, and decision rules. 
Prompt text Step 1: Define the experiment — what hypothesis are we testing, what is the primary metric, what is the minimum detectable effect, and what is the business rationale?
Step 2: Calculate sample size — given baseline metric, MDE, α=0.05, power=0.80. Calculate required experiment duration based on available traffic.
Step 3: Design the assignment — define unit of randomization (user, session, device). Check for network effects or contamination risks. Define the holdout strategy.
Step 4: Define guardrail metrics — list 3–5 metrics that must not degrade. Define the threshold for each guardrail.
Step 5: Design the analysis plan — specify the primary statistical test, multiple testing correction method, and pre-registration of hypotheses.
Step 6: Write the experiment brief: hypothesis, primary metric, guardrail metrics, sample size, duration, assignment method, analysis plan, decision criteria for ship/no-ship. Copy prompt Open prompt details Intermediate Single prompt 06 
### Multivariate Test Analysis 

This prompt evaluates A/B/n tests where multiple variants compete simultaneously. It is useful when you need a disciplined workflow that first checks for any overall difference and then controls false positives during pairwise comparisons. It also highlights outright harmful variants. 
Prompt text Analyze the results of this multivariate (A/B/n) test with {{num_variants}} variants.

1. Check for sample ratio mismatch across all variants
2. Run omnibus test first: is there any significant difference across all variants? (chi-squared or ANOVA)
3. If significant, run pairwise comparisons between all variant pairs using:
 - Bonferroni correction for multiple comparisons
 - Report adjusted p-values and whether each pair is significant at α=0.05 after correction
4. Compute the effect size for each variant vs control: Cohen's d (continuous) or relative lift (proportions)
5. Plot: mean metric value per variant with 95% confidence intervals
6. Identify the winning variant — highest metric value with statistical significance vs control
7. Flag any variants that are significantly worse than control (degradation alert) Copy prompt Open prompt details Beginner Single prompt 07 
### Pre-Experiment Sanity Check 

This prompt checks whether an experiment is healthy before launch by validating assumptions that often break real tests. It is useful for avoiding wasted traffic due to bad randomization, unstable metrics, hidden seasonality, or broken instrumentation. The output acts like a launch readiness review for experimentation. 
Prompt text Run a pre-experiment sanity check before launching this A/B test.

1. AA test simulation: randomly split the existing data into two equal groups and test for significant differences on the primary metric — there should be none (p > 0.05). If there is a significant difference, the randomization is broken.
2. Check metric variance: compute the standard deviation of the primary metric per user over the past 4 weeks. High variance increases required sample size.
3. Check for seasonality: does the primary metric vary significantly by day of week or time of year? Adjust experiment timing accordingly.
4. Check for novelty effects: does the user base regularly respond to any UI changes with a short-term spike that fades? How long should the experiment run to see past this?
5. Verify logging: confirm the event tracking is firing correctly for both the primary metric and guardrail metrics by spot-checking recent data.

Return: AA test result, variance estimate, seasonality assessment, and recommended experiment start date and duration. Copy prompt Open prompt details Beginner Single prompt 08 
### Sample Size Calculator 

This prompt estimates how much traffic is needed to detect a meaningful experimental effect. It is useful in planning because underpowered tests waste time and overpowered tests waste opportunity. The sensitivity analysis shows how strongly duration depends on the chosen MDE. 
Prompt text Calculate the required sample size for this experiment.

Inputs:
- Baseline conversion rate or metric value: {{baseline_value}}
- Minimum detectable effect (MDE): {{mde}} — the smallest change worth detecting
- Significance level (α): 0.05 (two-tailed)
- Statistical power (1 - β): 0.80
- Number of variants: {{num_variants}} (control + treatment)

Calculate:
1. Required sample size per variant
2. Total sample size across all variants
3. Required experiment duration given the current daily traffic of {{daily_traffic}} users
4. Show how the required sample size changes if MDE is varied: ±50%, ±25%, ±10% from the specified MDE
5. Plot a power curve: sample size vs statistical power for the specified MDE

Return: sample size, experiment duration, and the power curve plot. Copy prompt Open prompt details Intermediate Single prompt 09 
### Segment Lift Analysis 

This prompt examines whether treatment effects vary meaningfully across user segments. It is useful when average lift may hide strong winners, losers, or targeting opportunities. The forest-plot format also makes heterogeneous effects easier to communicate. 
Prompt text Analyze treatment lift across different user segments in this experiment.

1. Compute the overall lift: (treatment metric - control metric) / control metric
2. Compute lift separately for each segment defined by the available dimension columns (age group, region, device, acquisition channel, etc.)
3. Plot lift per segment as a forest plot (point estimate ± 95% CI for each segment)
4. Test for heterogeneous treatment effects: is the lift significantly different across segments? (interaction test)
5. Identify the segments with the highest and lowest lift
6. Flag any segment where the treatment caused a statistically significant negative effect
7. Recommend: should the feature be shipped to all users, or only to the highest-lift segments?

Return: segment lift table, forest plot, and a targeting recommendation. Copy prompt Open prompt details 
## Recommended Experimentation workflow 
1 
### A/B Test Analysis 

Start with a focused prompt in Experimentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Bayesian A/B Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Causal Inference Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Experiment Guardrail Check 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
