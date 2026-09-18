# Causal Inference *AI Prompts *

3 Statistician prompts in Causal Inference. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Causal Inference 
3 prompts Advanced Single prompt 01 
### Difference-in-Differences Design 

Design and analyze a difference-in-differences (DiD) study to estimate a causal effect from panel data. Treatment: {{treatment}} (a policy, intervention, or event that affects s... 
Prompt text Design and analyze a difference-in-differences (DiD) study to estimate a causal effect from panel data.

Treatment: {{treatment}} (a policy, intervention, or event that affects some units but not others)
Timing: {{timing}} (when did the treatment occur?)
Panel data: {{data_description}} (units observed before and after the treatment)
Comparison groups: {{treatment_group}} (treated) vs {{control_group}} (untreated)

1. DiD logic:
 DiD = (Mean_treated_post - Mean_treated_pre) - (Mean_control_post - Mean_control_pre)
 The control group's change over time is used to estimate the counterfactual trend for the treated group.
 The key identifying assumption is parallel trends: absent the treatment, treated and control units would have evolved in parallel.

2. Parallel trends assumption:
 - Check pre-treatment trends: plot the outcome for treated and control groups across all pre-treatment periods
 - If trends are parallel pre-treatment: assumption is plausible (not proven)
 - Formal test: interact treatment group with pre-treatment time dummies; if coefficients are jointly zero, trends are parallel
 - Event study plot: plot the treatment effect coefficient for each period relative to treatment, including pre-treatment leads. Pre-treatment coefficients should be near zero.

3. DiD regression specification:
 y_it = alpha + beta1 Treated_i + beta2 Post_t + delta (Treated_i x Post_t) + epsilon_it
 - delta is the DiD estimator
 - Add unit fixed effects (absorbs all time-invariant unit characteristics)
 - Add time fixed effects (absorbs common shocks)
 - Two-way fixed effects (TWFE): y_it = alpha_i + alpha_t + delta D_it + epsilon_it
 where D_it = 1 if unit i is treated in period t

4. Staggered treatment timing:
 - If different units receive treatment at different times, TWFE can be biased
 - Modern estimators for staggered DiD: Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-d'Haultfoeuille
 - These estimators form clean 2x2 DiD comparisons and average them correctly
 - Use the csdid (Stata) or did (R) package

5. Standard errors:
 - Cluster standard errors at the unit level (accounts for serial correlation within units)
 - If few treated clusters (< 10): wild cluster bootstrap for valid inference
 - Placebo tests: apply DiD to a period before treatment; the estimated effect should be near zero

Return: DiD estimate, parallel trends test, event study plot description, staggered timing assessment, and clustered SE specification. Copy prompt Open prompt details Advanced Single prompt 02 
### Instrumental Variables Analysis 

Specify and implement an instrumental variables (IV) analysis to estimate a causal effect in the presence of unmeasured confounding. Exposure (endogenous treatment): {{treatment... 
Prompt text Specify and implement an instrumental variables (IV) analysis to estimate a causal effect in the presence of unmeasured confounding.

Exposure (endogenous treatment): {{treatment}}
Outcome: {{outcome}}
Proposed instrument: {{instrument}}
Data: {{data_description}}

1. What IV analysis does:
 IV exploits an external source of variation (the instrument) that affects the treatment but does NOT directly affect the outcome except through the treatment.
 It can identify a causal effect even when there are unmeasured confounders.
 The causal estimate is the LATE: Local Average Treatment Effect — the effect for 'compliers' (those whose treatment status is changed by the instrument).

2. Three conditions for a valid instrument:

 Relevance:
 - The instrument Z must be associated with the treatment X
 - Testable: regress X on Z; the F-statistic for Z should be > 10 (rule of thumb for weak instruments)
 - Weak instrument problem: if F < 10, IV estimates are biased toward OLS and SEs are inflated

 Independence (Exogeneity):
 - Z must be independent of unmeasured confounders U
 - Not directly testable: requires a substantive argument
 - Examples of plausible instruments: geographic variation in access, distance to a facility, lottery assignment, policy cutoffs, genetic variants (Mendelian randomization)

 Exclusion restriction:
 - Z affects Y ONLY through X (no direct effect of Z on Y)
 - Not directly testable: requires a substantive argument
 - Violations: instrument affects outcome through other pathways (e.g., distance to a hospital affects health through access AND through living in a different environment)

3. Two-stage least squares (2SLS):
 Stage 1: X_hat = alpha + beta_1 Z + covariates
 Stage 2: Y = gamma + delta X_hat + covariates
 IV estimate delta = Cov(Z, Y) / Cov(Z, X)

 In practice: use ivreg() in R or ivregress in Stata/Python (do not manually run 2SLS in two steps — standard errors will be wrong).

4. Diagnostics:
 - First-stage F-statistic: test instrument relevance (target > 10, prefer > 16 for reliable inference)
 - Sargan-Hansen test: overidentification test if multiple instruments (test exclusion restriction)
 - Anderson-Rubin test: robust inference under weak instruments

5. Interpretation and limitations:
 - IV estimates are typically larger than OLS (because IV estimates a local effect for compliers, who may respond more strongly)
 - Large IV SEs: IV is less efficient than OLS when instrument is only moderately relevant
 - The LATE may not generalize to the full population (only compliers)

Return: instrument validity assessment, 2SLS specification, first-stage F-statistic, IV estimate with CI, and interpretation of LATE. Copy prompt Open prompt details Intermediate Single prompt 03 
### Propensity Score Analysis 

Implement and evaluate a propensity score analysis to estimate a causal effect from observational data. Treatment variable: {{treatment}} (binary: treated vs untreated) Outcome:... 
Prompt text Implement and evaluate a propensity score analysis to estimate a causal effect from observational data.

Treatment variable: {{treatment}} (binary: treated vs untreated)
Outcome: {{outcome}}
Potential confounders: {{confounders}}
Data: {{data_description}}

1. Estimand clarification:
 - ATE (Average Treatment Effect): the effect if the entire population were treated vs untreated
 - ATT (Average Treatment Effect on the Treated): the effect for those who actually received treatment
 - ATC: average effect for the controls if they had been treated
 - Choose based on the scientific question; ATT is most common in observational studies

2. Propensity score estimation:
 PS = P(Treatment = 1 | X)
 - Fit a logistic regression with treatment as the outcome and all confounders as predictors
 - Include: all variables that affect the outcome OR that affect both treatment and outcome
 - Do NOT include: instrumental variables (variables affecting treatment but NOT outcome)
 - Do NOT include: colliders (effects of treatment or outcome)
 - Check common support: there should be overlap in PS distributions between treated and controls
 Limited overlap = inability to estimate causal effect for some subgroups

3. PS matching:
 - Nearest neighbor matching: each treated unit matched to the closest control by PS
 - Caliper matching: require |PS_treated - PS_control| < 0.2 x SD(PS) (discard poor matches)
 - 1:1 vs 1:k matching: k>1 increases precision but introduces bias if poor matches are forced
 - Matching with replacement: allows controls to be reused (reduces bias, increases variance)

4. Balance assessment:
 - Standardized mean differences (SMD) before and after matching for each confounder
 - SMD < 0.10 after matching: good balance
 - Love plot: visualize SMD for each confounder before and after adjustment
 - Do NOT use p-values for balance checking — they are affected by sample size, not balance

5. Analysis after matching:
 - Estimate the treatment effect using a paired or stratified outcome model
 - Use doubly robust estimation: combine PS weighting with outcome regression (consistent if either is correct)
 - Report: estimated causal effect, 95% CI (using robust standard errors), and the matched sample size

6. Sensitivity analysis for unmeasured confounding:
 - Rosenbaum bounds: how strong would an unmeasured confounder need to be to explain away the result?
 - Gamma parameter: if Gamma = 2, the odds of treatment could differ by a factor of 2 for matched pairs with identical observed covariates
 - E-value: minimum association a confounder would need with both treatment and outcome to fully explain the observed effect

Return: PS model specification, overlap assessment, balance table (pre/post), causal effect estimate, and sensitivity analysis. Copy prompt Open prompt details 
## Recommended Causal Inference workflow 
1 
### Difference-in-Differences Design 

Start with a focused prompt in Causal Inference so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Instrumental Variables Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Propensity Score Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
