# Statistical Analysis of Research Data *AI Prompts *

11 Research Scientist prompts in Statistical Analysis of Research Data. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 10 single prompts · 1 chain. 

## AI prompts in Statistical Analysis of Research Data 
11 prompts Advanced Chain 01 
### Analysis Plan Chain 

Step 1: Primary analysis specification — specify the primary outcome, primary predictor, and the exact statistical test with its parameters (test type, alpha level, directionali... 
Prompt text Step 1: Primary analysis specification — specify the primary outcome, primary predictor, and the exact statistical test with its parameters (test type, alpha level, directionality). Specify this before seeing data.
Step 2: Secondary analyses — list all secondary outcomes and exploratory analyses in priority order. Specify multiple comparison correction strategy. Distinguish confirmatory from exploratory analyses clearly.
Step 3: Assumption checks — for each planned analysis, list all statistical assumptions and the procedure to test them. Specify in advance what will be done if each assumption is violated.
Step 4: Missing data plan — specify the expected missing data mechanism, the primary handling strategy, and sensitivity analyses for alternative mechanisms.
Step 5: Power analysis — calculate required sample size for the primary analysis at 80% and 90% power. Account for expected attrition. Run sensitivity analysis showing N required across a range of effect sizes.
Step 6: Subgroup analyses — specify any pre-planned subgroup analyses. State the interaction test that will be used. Explicitly flag all unplanned post-hoc subgroup analyses as exploratory.
Step 7: Write the statistical analysis plan (SAP) — produce a complete, timestamped statistical analysis plan that will be preregistered before data collection begins. Include: primary estimand, all analysis specifications, assumption checks, missing data plan, and planned reporting format. Copy prompt Open prompt details Advanced Single prompt 02 
### Bayesian vs Frequentist Analysis 

Help me decide between a frequentist and Bayesian analysis approach for my study, and implement the chosen approach. Study context: {{study_context}} Prior knowledge available:... 
Prompt text Help me decide between a frequentist and Bayesian analysis approach for my study, and implement the chosen approach.

Study context: {{study_context}}
Prior knowledge available: {{prior_knowledge}}
Inference goal: {{inference_goal}}

1. Key conceptual differences:

 Frequentist:
 - Probability = long-run frequency of events in repeated experiments
 - Parameters are fixed (unknown) constants; data are random
 - Inference: p-value (probability of data at least as extreme as observed, given H0 is true)
 - Output: point estimate, confidence interval (if experiment repeated 100 times, 95% of CIs would contain the true value)
 - No prior knowledge formally incorporated

 Bayesian:
 - Probability = degree of belief
 - Parameters are random variables with probability distributions; data are fixed once observed
 - Inference: posterior distribution (updated beliefs after seeing data)
 - Output: posterior mean/median, credible interval (probability that parameter falls in this interval given the data)
 - Prior knowledge explicitly incorporated through prior distribution

2. When to prefer each approach:

 Prefer frequentist when:
 - Strong prior knowledge is not available or hard to justify publicly
 - Results need to be communicated to a broadly frequentist audience
 - Simple hypothesis testing with a clear alpha level is the goal
 - Regulatory context requires NHST (e.g. clinical trial primary endpoint)

 Prefer Bayesian when:
 - Informative prior knowledge exists (previous studies, domain expertise) that should influence inference
 - You want to quantify evidence for the null hypothesis (Bayes factor)
 - Sequential/adaptive designs where interim analyses are needed
 - Complex hierarchical models where priors regularize unstable estimates
 - Small samples where priors stabilize estimates
 - Direct probability statements about parameters are needed ('there is a 92% probability the effect is positive')

3. If using Bayesian analysis:
 - Specify priors: weakly informative priors (regularizing) vs strongly informative priors (based on prior studies)
 - Sensitivity analysis: show results under different prior specifications
 - Report: prior distribution, posterior distribution, posterior mean with 95% credible interval, Bayes factor if testing hypotheses
 - Software: Stan / brms (R), PyMC (Python), JASP (GUI)

4. Bayes Factor interpretation:
 - BF > 100: decisive evidence for H1
 - BF 30–100: very strong evidence for H1
 - BF 10–30: strong evidence for H1
 - BF 3–10: moderate evidence for H1
 - BF 1–3: anecdotal evidence for H1
 - BF = 1: no evidence either way
 - BF < 1/3: moderate evidence for H0

Return: recommendation with rationale, prior specification for Bayesian approach, sensitivity analysis plan, and code in R (brms) or Python (PyMC). Copy prompt Open prompt details Beginner Single prompt 03 
### Effect Size Interpretation 

Help me calculate, report, and interpret effect sizes for my study. Study type: {{study_type}} Statistical results: {{results}} Field norms: {{field}} (what are typical effect s... 
Prompt text Help me calculate, report, and interpret effect sizes for my study.

Study type: {{study_type}}
Statistical results: {{results}}
Field norms: {{field}} (what are typical effect sizes in this field?)

1. Why effect sizes matter more than p-values:
 - A p-value tells you whether an effect exists (given sufficient sample size)
 - An effect size tells you HOW LARGE the effect is
 - With large enough samples, trivially small effects become statistically significant
 - Effect sizes allow comparison across studies and meta-analysis
 - Always report both: the p-value for the inference decision, the effect size for the magnitude interpretation

2. Effect size families and when to use each:

 Standardized mean difference family:
 - Cohen's d: difference between two means divided by pooled standard deviation. For independent groups.
 - Glass's Δ: uses only the control group SD in the denominator. Preferred when SDs differ substantially.
 - Hedges' g: small-sample correction of Cohen's d. Use when n < 20 per group.
 - Interpretation: d = 0.2 (small), 0.5 (medium), 0.8 (large) — but these are field-agnostic; use field norms when available.

 Correlation family:
 - Pearson r: linear association between two continuous variables. r = 0.1 (small), 0.3 (medium), 0.5 (large).
 - R²: proportion of variance explained. Report alongside r.
 - Partial eta squared (η²p): proportion of variance in the outcome explained by the predictor, removing other effects. For ANOVA designs.
 - Omega squared (ω²): less biased estimator of η²p. Prefer over η²p for small samples.

 Odds ratio and relative risk:
 - Odds ratio (OR): for logistic regression and case-control studies. OR = 1 means no effect.
 - Relative risk (RR): for cohort studies with binary outcomes. More interpretable than OR.
 - Number needed to treat (NNT): 1 / absolute risk reduction. Most clinically interpretable.

3. Calculate effect sizes from my results:
 - Apply the appropriate formula to my specific results
 - Include confidence intervals around each effect size estimate

4. Contextualizing the effect size:
 - Compare to typical effect sizes in {{field}}
 - Compare to effect sizes in related prior studies
 - Translate to practical significance: what does an effect of this size mean in the real world?

Return: calculated effect sizes with CIs, interpretation against field benchmarks, and a practical significance statement. Copy prompt Open prompt details Intermediate Single prompt 04 
### Mediation and Moderation Analysis 

Design and analyze a mediation or moderation analysis for my study. Conceptual model: {{conceptual_model}} (e.g. 'X → M → Y' or 'X × W → Y') Hypotheses: {{hypotheses}} Data avai... 
Prompt text Design and analyze a mediation or moderation analysis for my study.

Conceptual model: {{conceptual_model}} (e.g. 'X → M → Y' or 'X × W → Y')
Hypotheses: {{hypotheses}}
Data available: {{data}}

1. Clarify the conceptual question:

 Mediation (X → M → Y):
 - Asks: does X affect Y through its effect on M?
 - M is the mechanism through which X influences Y
 - Example: does a training intervention (X) improve job performance (Y) by increasing self-efficacy (M)?

 Moderation (X × W → Y):
 - Asks: does the effect of X on Y depend on the level of W?
 - W is the boundary condition that strengthens or weakens the X-Y relationship
 - Example: does the training effect on performance (X → Y) differ by employee tenure (W)?

 Moderated mediation (the indirect effect is moderated):
 - Asks: does the mediated pathway (X → M → Y) operate differently at different levels of W?

2. Mediation analysis — using Hayes PROCESS or lavaan:

 Requirements:
 - Temporal precedence: X must precede M must precede Y in time
 - Causal inference requires ruling out reverse causation and confounding of M-Y relationship
 - Distinguish between mediation (mechanism) and moderation (boundary condition)

 Steps:
 a. Test total effect of X on Y (path c)
 b. Test effect of X on M (path a)
 c. Test effect of M on Y controlling for X (path b)
 d. Test direct effect of X on Y controlling for M (path c')
 e. Calculate indirect effect = a × b with bootstrap CI (5000 bootstraps; 95% CI not crossing 0 = significant mediation)

 Note: Baron and Kenny's causal steps approach (requiring significant c path) is outdated. Use bootstrap indirect effects.

3. Moderation analysis:
 - Center continuous predictors before computing interaction terms
 - Test the interaction term (X × W)
 - If significant: probe the interaction with simple slopes at W = mean ± 1SD (or for binary W, at each level)
 - Plot the interaction: fitted values of Y across the range of X, separately for levels of W
 - Report: interaction coefficient, simple slopes with SEs and p-values, region of significance (Johnson-Neyman technique)

4. Common errors to avoid:
 - Do not interpret partial mediation as a finding — it is just incomplete mediation
 - Do not conclude mediation from cross-sectional data without acknowledging this is assumed, not demonstrated
 - Do not probe an interaction that is not statistically significant

Return: analysis code, results interpretation, interaction plot, and a methods paragraph. Copy prompt Open prompt details Intermediate Single prompt 05 
### Missing Data Handler 

Analyze the missing data in my study and implement the appropriate handling strategy. Dataset description: {{dataset}} Missingness pattern: {{missingness_description}} Analysis... 
Prompt text Analyze the missing data in my study and implement the appropriate handling strategy.

Dataset description: {{dataset}}
Missingness pattern: {{missingness_description}}
Analysis plan: {{analysis_plan}}

1. Classify the missing data mechanism:

 MCAR (Missing Completely At Random):
 - Missingness is unrelated to any variable in the dataset, observed or unobserved
 - Test: Little's MCAR test; compare characteristics of completers vs incomplete cases
 - Consequence: complete case analysis is unbiased but loses power
 - Implication: any missing data method gives unbiased results; simple methods are acceptable

 MAR (Missing At Random):
 - Missingness depends on OBSERVED variables but not on the missing values themselves
 - Example: older participants are more likely to miss a follow-up assessment, and age is recorded
 - Cannot be tested definitively (requires knowledge of unobserved data)
 - Most common practical assumption; required for multiple imputation and maximum likelihood
 - Implication: multiple imputation or FIML is valid; complete case analysis is biased

 MNAR (Missing Not At Random):
 - Missingness depends on the missing values themselves
 - Example: depressed participants are more likely to drop out, and depression is the outcome
 - Most problematic; no standard method fully corrects for MNAR
 - Implication: sensitivity analyses required; results are provisional

2. Evaluate and recommend a handling strategy:

 Complete case analysis (listwise deletion):
 - Valid only under MCAR; biased under MAR
 - Appropriate if: missingness rate < 5% AND MCAR is plausible

 Multiple imputation (MI):
 - Valid under MAR
 - Procedure: impute M datasets (M = 20–100 depending on missingness rate), analyze each separately, pool using Rubin's rules
 - Include all analysis variables, auxiliary variables correlated with outcome or missingness, and the outcome in the imputation model
 - Report: number of imputations, imputation model specification, convergence diagnostics

 Full Information Maximum Likelihood (FIML):
 - Valid under MAR; for structural equation models and mixed models
 - Preferred over MI for SEM and when the analysis model is well-specified

 Sensitivity analysis for MNAR:
 - Pattern-mixture models
 - Selection models
 - Delta adjustment: perturb imputed values systematically and check how much results change

3. Reporting:
 - Report the amount and pattern of missing data for every variable
 - Report the assumed mechanism and justification
 - Report the handling method and software
 - If MI: report number of imputations and imputation model

Return: missing data analysis, mechanism assessment, recommended strategy with implementation code, and reporting text. Copy prompt Open prompt details Advanced Single prompt 06 
### Multiverse Analysis 

Design and execute a multiverse analysis to assess the robustness of my findings across reasonable analytical choices. Main finding: {{main_finding}} Analysis pipeline: {{analys... 
Prompt text Design and execute a multiverse analysis to assess the robustness of my findings across reasonable analytical choices.

Main finding: {{main_finding}}
Analysis pipeline: {{analysis_pipeline}}

A multiverse analysis reports results across all defensible combinations of analytical decisions, rather than cherry-picking one analysis path.

1. Map the decision nodes in my analysis:

 For each step in the pipeline, identify all defensible alternatives:

 Data processing decisions:
 - Outlier exclusion: none, ±2 SD, ±3 SD, Winsorization at 5th/95th percentile
 - Missing data: complete case, single imputation, multiple imputation (5 datasets, 20 datasets)
 - Variable transformation: raw, log, square root, z-score
 - Covariate inclusion: minimal (pre-specified), expanded (additional theoretically relevant covariates)

 Analytical decisions:
 - Model family: OLS, robust regression, mixed model
 - Predictor operationalization: continuous vs dichotomized vs categorical
 - Outcome operationalization: if multiple measures of the same construct, which one is primary?
 - Control variables: which covariates to include

 Sampling decisions:
 - Exclusion criteria: strict application vs lenient (e.g. include vs exclude participants who missed >20% of items)
 - Subpopulation: full sample vs specific age range vs specific subgroup

2. Execute the multiverse:
 - Define all combinations of decisions: this produces the 'multiverse' of analyses
 - Run the primary test across all combinations
 - Extract: effect size, p-value, and confidence interval for each universe

3. Summarize and visualize:
 - Specification curve: plot all effect sizes sorted from smallest to largest, with indicator strips showing which decisions each specification used
 - Proportion of specifications showing a statistically significant effect in the expected direction
 - Proportion of specifications showing a significant effect in the unexpected direction

4. Interpretation:
 - Robust finding: significant and in the expected direction in the large majority of specifications (> 80%)
 - Fragile finding: result depends heavily on specific analytical choices
 - Which specific decisions drive the result? Are those the more or less defensible choices?

5. Reporting:
 - Report the main analysis AND the multiverse results
 - Never use the multiverse to find the significant result — preregister the primary analysis

Return: decision node mapping, analysis code, specification curve plot, robustness interpretation, and reporting text. Copy prompt Open prompt details Intermediate Single prompt 07 
### Peer Review Statistics Critique 

Critically evaluate the statistical methods and reporting in this paper I am reviewing. Paper abstract/methods/results: {{paper_content}} Systematically check for the following... 
Prompt text Critically evaluate the statistical methods and reporting in this paper I am reviewing.

Paper abstract/methods/results: {{paper_content}}

Systematically check for the following statistical issues:

1. Study design and causal inference:
 - Does the study design support the causal claims made in the discussion?
 - Are observational data used to support causal conclusions without adequate justification?
 - Is confounding adequately addressed?

2. Sample size and power:
 - Was a power analysis reported? Does the achieved sample size match the power analysis?
 - Is the study adequately powered for the primary outcome? (Effect size and sample size allow calculation)
 - Is the study appropriately cautious about null results given potential underpowering?

3. Multiple comparisons:
 - How many outcomes were tested? Were corrections for multiple comparisons applied?
 - Are results from exploratory analyses clearly labeled as such?
 - Is there evidence of outcome switching (primary outcome appears to have been changed post-hoc)?

4. Effect sizes and practical significance:
 - Are effect sizes reported for all main findings?
 - Are confidence intervals reported?
 - Is the distinction between statistical significance and practical significance made?

5. Specific red flags:
 - p-hacking indicators: p-values clustered just below 0.05, unusual number of 'marginally significant' results (p = .06, .07, .08)
 - HARKing (Hypothesizing After Results are Known): post-hoc hypotheses presented as a priori
 - Selective reporting: were all pre-specified outcomes reported? Are non-significant results reported?
 - Base rate neglect: does the probability of a true finding justify the strength of the conclusion?
 - Overfitting: in predictive models, is there a held-out test set? Is in-sample fit used to claim out-of-sample performance?

6. For each issue identified:
 - Severity: does this issue invalidate the conclusions, weaken them, or require clarification?
 - Recommended author action: specific request for analysis, reporting, or language change
 - Reviewer language: suggest wording appropriate for a peer review

Return: structured peer review critique organized by issue, severity ratings, and specific revision requests. Copy prompt Open prompt details Intermediate Single prompt 08 
### Power Analysis 

Conduct a power analysis to determine the sample size needed for my study. Study design: {{design}} Primary statistical test: {{test}} Effect size: {{effect_size_estimate}} and... 
Prompt text Conduct a power analysis to determine the sample size needed for my study.

Study design: {{design}}
Primary statistical test: {{test}}
Effect size: {{effect_size_estimate}} and its source (prior study, meta-analysis, minimum clinically/practically important difference)
Desired power: 0.80 (conventional minimum) or {{desired_power}}
Alpha level: 0.05 (two-tailed) or {{alpha}}

1. Choose the effect size input correctly:

 Priority order for effect size estimation:
 a. Minimum effect size of practical/clinical importance: 'What is the smallest effect that would matter for practice or policy?' Use this if you have domain knowledge.
 b. Meta-analytic estimate: if a meta-analysis of similar studies exists, use its pooled effect size.
 c. Well-powered prior study: a single prior study estimate is noisy; treat it with caution and consider using a smaller estimate.
 d. Cohen's benchmarks (d = 0.2/0.5/0.8): use only as a last resort — these are not field-specific and lead to widely varying conclusions.

 Common mistake: using an effect size from a small pilot study. Small studies overestimate effect sizes (winner's curse). If using a pilot estimate, shrink it by 50%.

2. Run the power analysis:
 - Calculate required N for power = 0.80 and power = 0.90
 - Calculate the minimum detectable effect size at the available N
 - For the recommended design, account for: attrition (inflate N by expected dropout rate), multiple testing (if testing multiple outcomes), clustering (design effect for clustered samples)

3. Sensitivity analysis:
 - Show how required N changes if the true effect size is 50%, 75%, 100%, and 125% of the assumed effect size
 - This illustrates how sensitive the study is to assumptions about effect size

4. Present the power analysis transparently:
 Report: assumed effect size and its source, alpha level, desired power, calculated N, attrition adjustment, final recommended N. State the software/package used.

5. What to do if the required N is not feasible:
 - Use a larger alpha (0.10) only if pre-specified and justified
 - Accept lower power (0.70) only for preliminary studies
 - Narrow the target population to increase homogeneity (reduces within-group variance, increases power)
 - Use a within-subjects design (more efficient than between-subjects)
 - Use a more sensitive primary outcome
 - Abandon and redesign if power cannot exceed 0.50 — an underpowered study is usually not worth running

Return: power analysis results at multiple power levels, sensitivity analysis table, sample size recommendation with attrition adjustment, and methods text. Copy prompt Open prompt details Intermediate Single prompt 09 
### Results Reporting Checklist 

Review my results section for completeness and adherence to best practices in statistical reporting. Results draft: {{results_draft}} Analyses used: {{analyses}} Apply the follo... 
Prompt text Review my results section for completeness and adherence to best practices in statistical reporting.

Results draft: {{results_draft}}
Analyses used: {{analyses}}

Apply the following reporting standards to every statistical result:

1. Descriptive statistics:
 - Report M and SD (not SEM, which is rarely interpretable) for continuous variables
 - Report frequencies and proportions for categorical variables
 - Report the sample size at each analysis step, accounting for missing data
 - Use APA format for numbers: two decimal places for statistics, three for p-values

2. Inferential statistics — every result must include:
 - The test statistic and its degrees of freedom: t(48) = 2.34 or F(2, 145) = 8.91
 - Exact p-value (not 'p < .05' or 'ns'): p = .023 or p = .412
 - Effect size with 95% confidence interval: d = 0.48 [0.12, 0.84]
 - Do not use asterisks (*, **, ***) as a substitute for reporting exact p-values

3. Common reporting deficiencies to flag:
 - Reporting only p-values without effect sizes
 - Reporting 'p < .05' instead of the exact p-value
 - Reporting SEM instead of SD for descriptive statistics
 - Missing confidence intervals on effect size estimates
 - Reporting results for tests on violated assumptions without acknowledging violations
 - Claiming nonsignificance as evidence of no effect
 - Failing to report results for non-significant outcomes (selective reporting)
 - Rounding to fewer than 2 decimal places for key statistics

4. Specific test reporting standards:

 t-test: t(df) = X.XX, p = .XXX, d = X.XX [95% CI: X.XX, X.XX]
 ANOVA: F(df_effect, df_error) = X.XX, p = .XXX, ω² = .XX [95% CI]
 Chi-squared: χ²(df, N = XX) = X.XX, p = .XXX, φ = .XX
 Correlation: r(df) = .XX, p = .XXX, 95% CI [.XX, .XX]
 Regression coefficient: B = X.XX, SE = X.XX, β = .XX, t(df) = X.XX, p = .XXX
 Mediation indirect effect: ab = X.XX, 95% bootstrap CI [X.XX, X.XX]

5. Tables and figures:
 - Every table must be interpretable standalone with a complete caption
 - Figures must include error bars with a caption specifying what they represent (SD, SE, 95% CI)
 - Raw data or aggregated data sufficient for meta-analysis should be available

Return: annotated results section with specific corrections, reporting deficiencies flagged by line, and a corrected version of the results. Copy prompt Open prompt details Intermediate Single prompt 10 
### Statistical Assumption Checker 

Check the statistical assumptions underlying my planned analyses and recommend how to handle any violations. Planned analyses: {{analyses}} Data characteristics: {{data_descript... 
Prompt text Check the statistical assumptions underlying my planned analyses and recommend how to handle any violations.

Planned analyses: {{analyses}}
Data characteristics: {{data_description}}

For each planned analysis, check the following assumptions:

1. Linear regression assumptions:
 - Linearity: is the relationship between predictors and outcome linear? Check: scatter plot, residual vs fitted plot. Violation: use polynomial terms, transformations, or GAM.
 - Independence: are observations independent? Check: study design. Violation: use clustered standard errors, mixed models, or GEE.
 - Homoscedasticity (constant variance): does residual variance remain constant across fitted values? Check: scale-location plot. Violation: use robust standard errors (HC3) or transform the outcome.
 - Normality of residuals: are residuals approximately normally distributed? Check: Q-Q plot, Shapiro-Wilk (for small n). Note: normality of RESIDUALS is required, not of the outcome itself. Violation: with n > 30, Central Limit Theorem generally protects. For small n: use robust or nonparametric methods.
 - No perfect multicollinearity: Check: VIF. VIF > 10 is problematic. Violation: drop or combine predictors, use ridge regression.

2. ANOVA assumptions:
 - Normality of group distributions (robust with large n)
 - Homogeneity of variance: Levene's test. Violation: Welch's ANOVA does not require equal variances — use by default.
 - Independence: same as above.

3. Chi-squared test assumptions:
 - Expected cell frequencies ≥ 5 in all cells. Violation: use Fisher's exact test, combine categories, or use exact tests.
 - Independence of observations.

4. Logistic regression assumptions:
 - No perfect separation: if a predictor perfectly predicts the outcome, estimates become unstable. Check: examine cross-tabs of predictors with outcome.
 - Linearity of log-odds: continuous predictors should have a linear relationship with the log-odds. Check: Box-Tidwell transformation test.
 - No influential outliers: Check: Cook's distance, leverage statistics.

5. For each violated assumption:
 - State the likely impact on results (conservative? anti-conservative? biased estimates?)
 - Provide the specific code or procedure to implement the appropriate remedy
 - Explain how to report the assumption check and its handling in the paper

Return: assumption checklist per analysis, violation assessment, remedies with implementation guidance, and reporting language. Copy prompt Open prompt details Beginner Single prompt 11 
### Statistical Test Selector 

Help me choose the correct statistical test for my research question and data. Research question: {{research_question}} Outcome variable type: {{outcome_type}} (continuous, bina... 
Prompt text Help me choose the correct statistical test for my research question and data.

Research question: {{research_question}}
Outcome variable type: {{outcome_type}} (continuous, binary, count, ordinal, time-to-event)
Predictor/grouping variable: {{predictor}} (categorical with N groups, continuous)
Study design: {{design}} (between-subjects, within-subjects, mixed, longitudinal)
Sample size: {{n}}

1. Decision tree for test selection:

 Comparing means or distributions:
 - 2 independent groups, continuous outcome → Independent samples t-test (if normal) or Mann-Whitney U (if not)
 - 2 related groups / repeated measures, continuous outcome → Paired t-test (if normal) or Wilcoxon signed-rank
 - 3+ independent groups, continuous outcome → One-way ANOVA (if normal) or Kruskal-Wallis
 - 3+ groups with covariates → ANCOVA
 - Repeated measures with 3+ time points → Repeated measures ANOVA or linear mixed model

 Associations:
 - Two continuous variables → Pearson correlation (if both normal) or Spearman (if not)
 - Continuous outcome, multiple predictors → Multiple linear regression
 - Binary outcome → Logistic regression
 - Count outcome → Poisson regression (or negative binomial if overdispersed)
 - Time-to-event outcome → Cox proportional hazards regression
 - Ordinal outcome → Ordinal logistic regression

 Categorical associations:
 - Two categorical variables → Chi-squared test (if expected cell counts ≥ 5) or Fisher's exact (if small cells)

2. Check the assumptions of the recommended test:
 - State each assumption
 - Explain how to test whether each assumption is met
 - For each violated assumption: state the appropriate alternative or robust version

3. The model-based alternative:
 For most research questions, a regression model is preferable to a simple test because:
 - It accommodates covariates and confounders
 - It provides effect size estimates with confidence intervals
 - It handles unbalanced designs gracefully
 - It generalizes to more complex designs
 Recommend the regression equivalent of the chosen test.

4. Multiple outcomes:
 If testing more than one outcome, explain:
 - The multiple comparisons problem
 - Whether a family-wise correction (Bonferroni, Holm) or false discovery rate approach is appropriate
 - How to designate a primary outcome to preserve Type I error rate

Return: recommended test and its regression equivalent, assumptions and how to test them, multiple comparisons guidance. Copy prompt Open prompt details 
## Recommended Statistical Analysis of Research Data workflow 
1 
### Analysis Plan Chain 

Start with a focused prompt in Statistical Analysis of Research Data so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Bayesian vs Frequentist Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Effect Size Interpretation 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Mediation and Moderation Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
