# Statistician *AI Prompts *

Statistician AI prompt library with 17 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Statistician prompt categories 
6 categories 
### Hypothesis Testing 

AI prompts for hypothesis testing workflows including test selection, assumptions checks, p-value interpretation, and practical significance reporting. 
4 prompts Full Statistical Analysis Chain Hypothesis Test Selector → 
### Causal Inference 

AI prompts for causal inference workflows including confounding checks, identification strategy, treatment effects, and defensible causal interpretation. 
3 prompts Difference-in-Differences Design Instrumental Variables Analysis → 
### Experimental Design 

AI prompts for experimental design including hypothesis framing, sample size logic, randomization strategy, and bias reduction principles. 
3 prompts Factorial and Adaptive Designs Observational Study Design → 
### Regression and Modeling 

AI prompts for regression and statistical modeling including model assumptions, fit diagnostics, interpretation, and practical decision support. 
3 prompts Generalized Linear Models Linear Regression Diagnostics → 
### Bayesian Methods 

AI prompts for Bayesian methods including prior selection, posterior interpretation, credible intervals, and practical decision-making under uncertainty. 
2 prompts Bayesian Hierarchical Model Bayesian Hypothesis Testing → 
### Statistical Communication 

AI prompts for statistical communication including clear explanation of uncertainty, assumptions, findings, and stakeholder-ready narratives. 
2 prompts Statistical Methods Section Writer Statistical Results Interpretation → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 17 Hypothesis Testing 4 Causal Inference 3 Experimental Design 3 Regression and Modeling 3 Bayesian Methods 2 Statistical Communication 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **17 **of 17 prompts 
## Hypothesis Testing 
4 prompt s Hypothesis Testing Advanced Chain 01 
### Full Statistical Analysis Chain 
Step 1: Research question and estimand - state the precise research question in one sentence. Define the estimand: the specific population parameter you are trying to estimate or test. Specify: the target population, the exposure or treatment, the outcome, and the comparison (vs what baseline or control?).
Step 2: Study design assessment - evaluate the study design: was randomization used? If observational, what is the primary confounding threat? Draw the causal DAG and identify the minimal sufficient adjustment set.
Step 3: Data quality check - assess the data for: missing values (pattern and % per variable), outliers (flag observations > 3 SD from mean), distributional assumptions (normality, homoscedasticity), and any data entry anomalies.
Step 4: Descriptive statistics - produce a Table 1: describe all variables by group. For continuous variables: mean (SD) or median [IQR] based on distribution. For categorical: count (%). Test baseline differences if a two-group comparison.
Step 5: Primary analysis - select and run the primary statistical test. Report: test statistic, degrees of freedom, p-value, effect size, and 95% confidence interval. Check all assumptions and note any violations.
Step 6: Secondary and sensitivity analyses - run planned secondary analyses. Conduct a sensitivity analysis: repeat the primary analysis under different assumptions (e.g., complete cases vs imputed, alternative covariate adjustment sets). Assess robustness.
Step 7: Interpretation and reporting - write a plain-language summary of findings. Interpret the effect size in practical terms. Discuss limitations. Specify what the results can and cannot conclude. Produce the statistical methods section text. Copy prompt View page Show more ↓ Hypothesis Testing Beginner Prompt 02 
### Hypothesis Test Selector 
Help me select the correct statistical test for this analysis.

Data description: {{data_description}}
Research question: {{research_question}}
Sample size: {{n}}
Data types: {{data_types}} (continuous, ordinal, nominal, count)
Number of groups: {{n_groups}}
Design: {{design}} (independent groups, paired/repeated measures, one-sample)

1. Apply the test selection decision tree:

 COMPARING MEANS / CENTRAL TENDENCY:
 - 1 group vs known value, continuous, normal: One-sample t-test
 - 2 independent groups, continuous, normal, equal variance: Independent t-test
 - 2 independent groups, continuous, normal, unequal variance: Welch's t-test (prefer over Student's when in doubt)
 - 2 paired groups, continuous, normal: Paired t-test
 - 3+ independent groups, continuous, normal: One-way ANOVA
 - 3+ groups with 2+ factors: Factorial ANOVA or mixed ANOVA
 - 2 independent groups, non-normal or ordinal: Mann-Whitney U
 - 2 paired groups, non-normal or ordinal: Wilcoxon signed-rank
 - 3+ independent groups, non-normal: Kruskal-Wallis
 - 3+ paired groups, non-normal: Friedman test

 COMPARING PROPORTIONS:
 - 1 proportion vs known value: One-sample z-test or exact binomial
 - 2 independent proportions: Chi-square test or Fisher's exact (use Fisher's if any cell < 5)
 - 2 paired proportions: McNemar's test
 - 3+ independent proportions: Chi-square test of independence

 CORRELATION AND ASSOCIATION:
 - 2 continuous variables, linear: Pearson correlation
 - 2 ordinal or non-normal continuous: Spearman correlation
 - 2 binary or nominal: Phi coefficient, Cramér's V
 - 2 continuous, agreement between raters: Intraclass Correlation (ICC)

 REGRESSION:
 - Continuous outcome, 1+ predictors: Linear regression (check assumptions)
 - Binary outcome: Logistic regression
 - Count outcome: Poisson or negative binomial regression
 - Ordinal outcome: Ordinal logistic regression
 - Time-to-event: Cox proportional hazards

2. Assumption check for selected test:
 - What assumptions must be verified before running this test?
 - How to check each assumption (normality: Shapiro-Wilk if n < 50, Q-Q plot; equal variance: Levene's test; independence: by design)
 - What to do if an assumption is violated (non-parametric alternative, transformation, robust methods)

3. Multiple testing consideration:
 - If you are running more than one test on the same dataset, correction for multiple comparisons is needed
 - Bonferroni: divide alpha by the number of tests (conservative)
 - Benjamini-Hochberg FDR: controls false discovery rate (less conservative, preferred for many tests)

Return: recommended test, assumptions to verify, alternative if assumptions are violated, and multiple comparison strategy. Copy prompt View page Show more ↓ Hypothesis Testing Intermediate Prompt 03 
### Multiple Testing Correction 
Apply appropriate multiple testing corrections to this set of hypothesis tests.

Number of tests: {{n_tests}}
Raw p-values: {{p_values}}
Test context: {{context}} (exploratory analysis, confirmatory study, family of related tests)
Error rate to control: {{error_rate}} (FWER or FDR)

1. The multiple testing problem:
 If you run k independent tests each at alpha = 0.05, the probability of at least one false positive is:
 FWER = 1 - (1 - 0.05)^k
 For k=20: FWER = 64%. For k=100: FWER = 99.4%.
 Uncorrected p-values in a multiple testing setting are misleading.

2. Family-wise error rate (FWER) methods:
 Controls the probability of ANY false positive across all tests.

 Bonferroni:
 - Adjusted alpha = original alpha / k
 - Reject H0 if p_i < alpha/k
 - Conservative: assumes all tests are independent
 - Best for: small number of pre-specified tests (k < 10) with strong family-wise control needed

 Holm-Bonferroni (uniformly more powerful than Bonferroni):
 - Sort p-values from smallest to largest: p(1) <= p(2) <= ... <= p(k)
 - Reject H0(i) if p(j) < alpha / (k - j + 1) for all j <= i
 - Rejects at least as many as Bonferroni, never fewer
 - Recommended over plain Bonferroni in almost all cases

3. False discovery rate (FDR) methods:
 Controls the expected proportion of false positives among rejected tests.
 Appropriate when making many tests in an exploratory context (genomics, imaging, marketing).

 Benjamini-Hochberg (BH):
 - Sort p-values from smallest to largest: p(1) <= p(2) <= ... <= p(k)
 - Find the largest i such that p(i) <= (i/k) x alpha
 - Reject all H0(j) for j <= i
 - BH guarantees E[FDP] <= alpha (under independence or positive correlation)
 - Typical FDR threshold: q = 0.05 (expect 5% of rejected hypotheses to be false positives)

4. Apply to provided p-values:
 - List all raw p-values
 - Apply Holm-Bonferroni: which tests survive?
 - Apply BH at q = 0.05: which tests survive?
 - Compare: how many more discoveries does BH yield vs Holm-Bonferroni?

5. Recommendation:
 - For confirmatory studies with strong false positive cost: FWER control (Holm-Bonferroni)
 - For exploratory studies where false negatives are costly: FDR control (BH)
 - For data-driven analysis with thousands of tests: BH or Storey's q-value

Return: FWER and FDR calculations applied to the provided p-values, comparison table, and method recommendation. Copy prompt View page Show more ↓ Hypothesis Testing Intermediate Prompt 04 
### Power Analysis and Sample Size 
Conduct a power analysis and determine the required sample size for this study.

Study design: {{study_design}}
Statistical test: {{test}}
Effect size: {{effect_size}} (or provide: expected means/proportions and standard deviation to compute it)
Significance level: alpha = {{alpha}} (default 0.05)
Desired power: 1 - beta = {{power}} (default 0.80; use 0.90 for high-stakes studies)

1. Effect size calculation:
 If raw parameters are given rather than a standardized effect size:

 Cohen's d (for means): d = (mu_1 - mu_2) / pooled_SD
 - Small: d = 0.2, Medium: d = 0.5, Large: d = 0.8

 Cohen's h (for proportions): h = 2 arcsin(sqrt(p1)) - 2 arcsin(sqrt(p2))
 - Small: h = 0.2, Medium: h = 0.5, Large: h = 0.8

 Cohen's f (for ANOVA): f = sigma_between / sigma_within
 - Small: f = 0.10, Medium: f = 0.25, Large: f = 0.40

 Pearson r (for correlation):
 - Small: r = 0.10, Medium: r = 0.30, Large: r = 0.50

2. Sample size formula per test:

 Two-sample t-test:
 n per group = 2 x ((z_alpha/2 + z_beta) / d)^2
 where z_alpha/2 = 1.96 (alpha=0.05, two-tailed), z_beta = 0.84 (power=0.80)

 One-sample t-test:
 n = ((z_alpha/2 + z_beta) / d)^2

 Chi-square test of two proportions:
 n per group = (z_alpha/2 sqrt(2 p_bar (1-p_bar)) + z_beta sqrt(p1(1-p1) + p2(1-p2)))^2 / (p1-p2)^2
 where p_bar = (p1 + p2) / 2

 Calculate the required n for the stated parameters.

3. Power curve:
 Show how power changes as n increases from n/2 to 3n.
 Identify where additional subjects yield diminishing returns (power > 0.95).

4. Sensitivity analysis:
 - Required n if effect size is 25% smaller than expected
 - Required n at power = 0.90 vs 0.80
 - Required n at alpha = 0.01 vs 0.05

5. Practical considerations:
 - Add 10-20% to account for dropouts or missing data
 - For clustered designs: multiply by the design effect (DEFF = 1 + (m-1) x ICC, where m is cluster size)
 - Is the required n feasible given the study constraints?

Return: standardized effect size, required n with formula, power curve description, sensitivity table, and feasibility assessment. Copy prompt View page Show more ↓ 
## Causal Inference 
3 prompt s Causal Inference Advanced Prompt 01 
### Difference-in-Differences Design 
Design and analyze a difference-in-differences (DiD) study to estimate a causal effect from panel data.

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

Return: DiD estimate, parallel trends test, event study plot description, staggered timing assessment, and clustered SE specification. Copy prompt View page Show more ↓ Causal Inference Advanced Prompt 02 
### Instrumental Variables Analysis 
Specify and implement an instrumental variables (IV) analysis to estimate a causal effect in the presence of unmeasured confounding.

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

Return: instrument validity assessment, 2SLS specification, first-stage F-statistic, IV estimate with CI, and interpretation of LATE. Copy prompt View page Show more ↓ Causal Inference Intermediate Prompt 03 
### Propensity Score Analysis 
Implement and evaluate a propensity score analysis to estimate a causal effect from observational data.

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

Return: PS model specification, overlap assessment, balance table (pre/post), causal effect estimate, and sensitivity analysis. Copy prompt View page Show more ↓ 
## Experimental Design 
3 prompt s Experimental Design Advanced Prompt 01 
### Factorial and Adaptive Designs 
Design a factorial or adaptive experimental design for this study.

Research question: {{research_question}}
Factors: {{factors}} (each factor and its levels)
Adaptive elements needed: {{adaptive_needs}} (interim analysis, arm dropping, response-adaptive randomization)

1. Factorial designs:

 Full factorial:
 - All combinations of factor levels are tested
 - 2^k design: k factors each at 2 levels → 2^k treatment combinations
 - Advantages: tests main effects AND interactions simultaneously
 - Sample size: same n needed per cell as a one-factor design, but tests many more questions
 - Key output: interaction plot — does the effect of factor A depend on the level of factor B?

 Fractional factorial:
 - Test only a fraction of all 2^k combinations (e.g. 2^(k-p) design)
 - Aliasing: main effects are confounded with high-order interactions
 - Use when: k is large and high-order interactions are assumed negligible
 - Resolution III: main effects aliased with 2-way interactions (minimum for screening)
 - Resolution V: main effects and 2-way interactions estimable (preferred for confirmatory)

2. Adaptive designs:

 Group sequential design:
 - Pre-planned interim analyses at specified information fractions (e.g. at 50% and 100% of n)
 - Spending functions control Type I error across looks:
 - O'Brien-Fleming: strict early stopping, liberal late (good when early stopping is rare)
 - Pocock: equal thresholds at each look (more liberal early)
 - Stopping rules: stop for efficacy (p < boundary), futility (conditional power < 20%), or safety

 Response-adaptive randomization:
 - Allocation probabilities update based on accumulating outcome data
 - More participants assigned to the arm showing better performance
 - Pros: ethical (fewer participants in inferior arm)
 - Cons: increases bias risk, complicates inference; FDA skepticism in confirmatory trials

 Platform trials:
 - Multiple interventions tested simultaneously on a shared control arm
 - Arms can enter and exit the platform based on interim results
 - Efficient for rapid testing of many treatments (COVID-19 trials used this)

3. Analysis for adaptive designs:
 - Naive p-values from adaptive designs are invalid (inflation of Type I error)
 - Use: conditional power, stagewise p-values (combination function), or Bayesian posterior probabilities
 - Closed testing principle: preserves familywise error rate when multiple hypotheses are tested

Return: factorial design specification (factors, combinations, sample size), interaction test plan, adaptive design choice with stopping boundaries, and analysis approach. Copy prompt View page Show more ↓ Experimental Design Intermediate Prompt 02 
### Observational Study Design 
Design an observational study and plan the appropriate analysis to control for confounding.

Exposure of interest: {{exposure}}
Outcome of interest: {{outcome}}
Available data: {{data_description}}
Study type: {{study_type}} (cross-sectional, case-control, cohort)

1. Study design selection:

 Cross-sectional:
 - Exposure and outcome measured at the same time
 - Pros: fast, cheap, good for prevalence estimation
 - Cons: cannot establish temporality; prone to reverse causation
 - Best for: estimating associations and generating hypotheses

 Case-control:
 - Sample based on outcome (cases vs controls), then measure past exposure
 - Pros: efficient for rare outcomes
 - Cons: recall bias; selection of controls is critical
 - Analysis: conditional or unconditional logistic regression; effect measure = odds ratio

 Prospective cohort:
 - Sample based on exposure status, follow forward to measure outcomes
 - Pros: can measure incidence, multiple outcomes, avoids recall bias
 - Cons: expensive, slow; loss to follow-up threatens validity
 - Analysis: survival analysis (Cox model), incidence rate ratio; effect measure = hazard ratio, RR

 Retrospective cohort:
 - Historical data used to construct a cohort; follow forward in time using existing records
 - Faster than prospective; subject to data quality of historical records

2. Confounding control methods:

 Design-stage:
 - Restriction: limit study to a homogeneous subgroup (removes confounding from that variable)
 - Matching: match cases and controls (or exposed and unexposed) on potential confounders
 - Advantage: guaranteed balance; disadvantage: cannot study matched variables as exposures

 Analysis-stage:
 - Multivariable regression: include confounders as covariates
 - Propensity score methods (see propensity score prompt)
 - Stratification: estimate effect within strata of the confounder, then pool with Mantel-Haenszel

3. Bias assessment:
 - Selection bias: is the study sample representative of the target population?
 - Information bias: are exposure and outcome measured accurately?
 - Confounding: have all major confounders been measured and controlled?
 - Use a directed acyclic graph (DAG) to identify the minimal sufficient adjustment set

4. Directed Acyclic Graph (DAG):
 - Draw the causal diagram: nodes = variables, arrows = direct causal effects
 - Identify confounders: common causes of exposure and outcome
 - Identify colliders: common effects of two variables (do NOT adjust for colliders — this opens a non-causal path)
 - Use the backdoor criterion to identify the adjustment set

Return: study design recommendation, confounding control plan, DAG specification, and bias assessment. Copy prompt View page Show more ↓ Experimental Design Intermediate Prompt 03 
### Randomized Controlled Trial Design 
Design a randomized controlled trial (RCT) to answer this research question.

Research question: {{research_question}}
Intervention: {{intervention}}
Primary outcome: {{primary_outcome}}
Population: {{population}}
Practical constraints: {{constraints}} (budget, timeline, ethical restrictions)

1. Randomization design:

 Simple randomization:
 - Each participant independently assigned with probability p = 0.5
 - Works well for large n (> 200); may produce imbalanced groups in small trials

 Block randomization:
 - Participants randomized in blocks of fixed size (e.g. blocks of 4 or 6)
 - Guarantees approximately equal group sizes throughout the trial
 - Use when enrollment is sequential and interim analyses are planned

 Stratified randomization:
 - Randomize separately within strata of key prognostic variables (age group, site, disease severity)
 - Prevents chance imbalance on important covariates
 - Combine with block randomization within strata

 Cluster randomization:
 - Randomize groups (clinics, schools, communities) rather than individuals
 - Use when individual randomization causes contamination
 - Requires larger sample size (inflate by design effect = 1 + (m-1) x ICC)

2. Blinding:
 - Open-label: neither participants nor assessors are blinded (highest risk of bias)
 - Single-blind: participants are blinded to treatment assignment
 - Double-blind: both participants and outcome assessors are blinded (gold standard for efficacy)
 - Triple-blind: includes the data analysts
 - Is blinding feasible for this intervention? If not: use blinded outcome assessment at minimum

3. Sample size and allocation:
 - Calculate required n based on primary outcome (see power analysis prompt)
 - Equal allocation (50/50) is most efficient when costs per participant are equal
 - Unequal allocation: use if one arm is more costly or to expose fewer to the control

4. Analysis plan (pre-specified):
 - Primary analysis: intention-to-treat (ITT) — analyze participants as randomized, regardless of adherence
 - Per-protocol analysis: sensitivity analysis for those who completed the protocol
 - Handling missing data: specify imputation method in advance
 - Pre-register the primary outcome and analysis plan (ClinicalTrials.gov, OSF)

5. Validity threats:
 - Selection bias: only randomization fully controls this
 - Attrition: track dropout rate by arm; > 20% differential dropout threatens validity
 - Contamination: control group receives elements of the intervention
 - CONSORT checklist: use for reporting

Return: randomization design recommendation, blinding plan, sample size, ITT analysis plan, and validity threat assessment. Copy prompt View page Show more ↓ 
## Regression and Modeling 
3 prompt s Regression and Modeling Advanced Prompt 01 
### Generalized Linear Models 
Specify and interpret the appropriate Generalized Linear Model (GLM) for this outcome.

Outcome variable: {{outcome}} and its distribution: {{distribution}}
Predictors: {{predictors}}
Data structure: {{data_structure}} (cross-sectional, panel, clustered)

1. GLM family and link function selection:

 Gaussian family, identity link:
 - Outcome: continuous, approximately normal
 - Equivalent to OLS linear regression

 Binomial family, logit link (logistic regression):
 - Outcome: binary (0/1) or proportion
 - Coefficient interpretation: log-odds. exp(beta) = odds ratio
 - Alternative links: probit (normal CDF), complementary log-log (for rare events)

 Poisson family, log link:
 - Outcome: count data (non-negative integers)
 - Assumption: mean = variance (equidispersion)
 - exp(beta) = incidence rate ratio
 - Add offset term (log of exposure) for rate models: log(mu) = offset + X'beta

 Negative binomial family, log link:
 - Outcome: overdispersed count data (variance > mean)
 - Adds a dispersion parameter: variance = mu + mu^2/theta
 - Check: if Poisson residual deviance >> df, use negative binomial

 Gamma family, log or inverse link:
 - Outcome: positive continuous, right-skewed (cost, duration, concentration)
 - Log link preferred for interpretability

 Inverse Gaussian family, log link:
 - Outcome: positive continuous, strongly right-skewed

2. Model fitting and interpretation:
 - Fit the GLM using maximum likelihood
 - Coefficients are on the scale of the link function
 - Back-transform for interpretation: exponentiate log-link coefficients for multiplicative effects
 - Confidence intervals: profile likelihood CI preferred over Wald CI for small samples

3. Overdispersion check (for count models):
 - Residual deviance / df: should be close to 1.0 for Poisson
 - If >> 1: overdispersion → switch to negative binomial or quasi-Poisson
 - If << 1: underdispersion (rare) → investigate data generation process

4. Zero inflation:
 - If there are more zeros than the Poisson/NB distribution predicts: zero-inflated model
 - ZIP (Zero-inflated Poisson): mixture of a point mass at zero and a Poisson distribution
 - ZINB: Zero-inflated negative binomial
 - Test: Vuong test comparing Poisson to ZIP

5. Goodness of fit:
 - Pearson chi-square statistic / df
 - Deviance / df
 - Rootogram (for count data): visual comparison of observed vs fitted count distributions

Return: GLM family and link function selection with rationale, coefficient interpretation, overdispersion check, zero-inflation assessment, and goodness-of-fit evaluation. Copy prompt View page Show more ↓ Regression and Modeling Intermediate Prompt 02 
### Linear Regression Diagnostics 
Diagnose and validate a fitted linear regression model.

Model: {{model_description}} (outcome, predictors, n)
Fitted model output: {{model_output}}

1. The four core OLS assumptions (LINE):

 L — Linearity:
 - Residuals vs fitted values plot: should show random scatter around zero
 - Pattern in residuals = non-linearity → add polynomial terms, interaction terms, or transform predictors
 - Partial regression plots (added variable plots): check linearity of each predictor separately

 I — Independence of errors:
 - By design: is this a cross-sectional dataset (no natural ordering)?
 - For time series or clustered data: Durbin-Watson test for serial autocorrelation (target: DW near 2)
 - If observations are clustered: use clustered standard errors or mixed effects model

 N — Normality of residuals:
 - Q-Q plot of standardized residuals: points should fall on the diagonal
 - Shapiro-Wilk test for normality (reliable for n < 2000)
 - Note: normality of residuals is the LEAST critical assumption for large samples (CLT)
 - Skewed residuals suggest: log-transform the outcome, or consider a GLM with appropriate family

 E — Equal variance (homoscedasticity):
 - Scale-location plot (sqrt(|standardized residuals|) vs fitted): should be flat
 - Breusch-Pagan test: p < 0.05 indicates heteroscedasticity
 - Fix: use heteroscedasticity-consistent (HC) standard errors (HC3 is robust in small samples)
 - Or: weighted least squares if variance structure is known

2. Influential observations:
 - Leverage (h_ii): measures how far an observation's predictor values are from the mean
 High leverage: h_ii > 2(k+1)/n
 - Cook's Distance: measures overall influence of each observation on all fitted values
 Influential if D_i > 4/n (rule of thumb)
 - DFFITS and DFBETAS: influence on fitted values and specific coefficients
 - Action: investigate (not automatically remove) flagged observations

3. Multicollinearity:
 - Variance Inflation Factor (VIF) per predictor
 - VIF > 5: concerning, VIF > 10: severe multicollinearity
 - Fix: remove redundant predictors, combine correlated predictors via PCA, or use ridge regression

4. Model fit assessment:
 - R-squared: proportion of variance explained (note: always increases with more predictors)
 - Adjusted R-squared: penalizes for adding unhelpful predictors
 - AIC/BIC: for model comparison (lower is better)
 - RMSE on a holdout set: most honest measure of predictive accuracy

Return: assumption check results per criterion, influential observation list, multicollinearity report, and model fit summary. Copy prompt View page Show more ↓ Regression and Modeling Intermediate Prompt 03 
### Model Selection and Comparison 
Compare candidate statistical models and select the most appropriate one.

Outcome variable: {{outcome}}
Candidate models: {{models}} (list of model specifications)
Data: {{data_description}}
Goal: {{goal}} (inference / prediction / both)

1. Information criteria:
 AIC = 2k - 2 ln(L)
 BIC = k ln(n) - 2 ln(L)
 where k = number of parameters, L = maximized likelihood, n = sample size

 - Lower AIC/BIC = better model
 - AIC minimizes prediction error; BIC penalizes complexity more (prefers parsimonious models)
 - Delta AIC: difference from the best model
 Delta < 2: substantial support for this model
 Delta 4-7: considerably less support
 Delta > 10: essentially no support
 - For purely predictive goals: use AIC or cross-validation
 - For inference with parsimony: use BIC

2. Likelihood ratio test (LRT) for nested models:
 LRT statistic = -2(ln L_restricted - ln L_full)
 Follows chi-square distribution with df = difference in number of parameters
 Reject the restricted model if p < 0.05
 Use LRT when: comparing a simpler model to a more complex one that contains it as a special case

3. Cross-validation:
 For predictive model selection, k-fold cross-validation gives the most honest estimate:
 - Split data into k folds (k=10 is standard)
 - Train on k-1 folds, test on held-out fold
 - Average test metric (RMSE for continuous, AUC for binary) across folds
 - Select model with best mean CV metric, accounting for standard error
 - One-standard-error rule: prefer the simpler model within 1 SE of the best

4. Goodness-of-fit tests:
 - For linear regression: overall F-test (are any predictors useful?)
 - For logistic regression: Hosmer-Lemeshow test (is the calibration good?)
 - For count models: overdispersion test (is Poisson appropriate, or do we need negative binomial?)

5. Parsimony principle:
 - Between models with similar fit: prefer the simpler one
 - A model that is too complex will overfit: good in-sample fit, poor out-of-sample prediction
 - Report confidence/credible intervals for all selected model parameters

Return: AIC/BIC comparison table, LRT results (if applicable), cross-validation scores, and model selection recommendation with rationale. Copy prompt View page Show more ↓ 
## Bayesian Methods 
2 prompt s Bayesian Methods Advanced Prompt 01 
### Bayesian Hierarchical Model 
Specify and interpret a Bayesian hierarchical (multilevel) model for this data.

Data structure: {{data_structure}} (units nested in groups: students in schools, measurements in subjects)
Outcome: {{outcome}}
Level-1 predictors: {{l1_predictors}} (measured at the unit level)
Level-2 predictors: {{l2_predictors}} (measured at the group level)
Group variable: {{group_variable}}
Number of groups: {{n_groups}}

1. Why hierarchical models:
 - Observations within groups are not independent (ICC > 0)
 - Using a single-level model underestimates standard errors (overestimates precision)
 - Hierarchical models borrow strength across groups (partial pooling):
 - Complete pooling: ignores group membership (too simple)
 - No pooling: estimates each group separately (too noisy for small groups)
 - Partial pooling: shrinks group estimates toward the overall mean (optimal)

2. Model specification:
 Level 1 (within groups):
 y_ij = alpha_j + beta_j * x_ij + epsilon_ij
 epsilon_ij ~ Normal(0, sigma^2)

 Level 2 (between groups):
 alpha_j ~ Normal(mu_alpha, tau_alpha^2) [random intercepts]
 beta_j ~ Normal(mu_beta, tau_beta^2) [random slopes, if specified]

 Hyperpriors (Bayesian):
 mu_alpha ~ Normal(0, 10)
 tau_alpha ~ HalfNormal(0, 1) [must be positive; HalfNormal is a good weakly informative prior]

3. Intraclass correlation coefficient (ICC):
 ICC = tau^2 / (tau^2 + sigma^2)
 - ICC = 0: no clustering; single-level model is fine
 - ICC = 0.10: 10% of variance is at the group level; standard errors inflated by DEFF = 1 + (m-1) x 0.10
 - ICC > 0.20: strong clustering; hierarchical model is essential

4. Cross-level interactions:
 - Does the effect of x_ij (Level 1) vary with w_j (Level 2)?
 - Include: beta_j = gamma_10 + gamma_11 * w_j + u_1j
 - This is the hallmark of hierarchical modeling: testing whether context moderates individual-level effects

5. Convergence diagnostics (for MCMC estimation):
 - R-hat (Gelman-Rubin): should be < 1.01 for all parameters
 - Effective sample size (ESS): should be > 100 (preferably > 400) for each parameter
 - Trace plots: chains should mix well, with no trends or stuck periods
 - Posterior predictive check: does the model reproduce the observed data distribution?

Return: hierarchical model specification, ICC calculation, cross-level interaction interpretation, and MCMC convergence assessment. Copy prompt View page Show more ↓ Bayesian Methods Intermediate Prompt 02 
### Bayesian Hypothesis Testing 
Perform a Bayesian analysis as an alternative or complement to frequentist hypothesis testing.

Hypothesis: {{hypothesis}}
Data: {{data}}
Prior information: {{prior_info}} (literature values, expert knowledge, or 'weakly informative')

1. The Bayesian framework:
 - Prior: P(theta) — your belief about the parameter before seeing the data
 - Likelihood: P(data | theta) — how probable is the data at each value of theta?
 - Posterior: P(theta | data) ∝ P(data | theta) x P(theta)
 - The posterior combines prior belief with the evidence from the data

2. Prior specification:

 Informative prior:
 - Based on previous studies or expert knowledge
 - Example: beta(8, 4) for a success probability believed to be around 0.67
 - Must be documented and justified

 Weakly informative prior:
 - Provides mild regularization without dominating the data
 - Example: Normal(0, 2.5) on logistic regression coefficients (Gelman's recommendation)
 - Prevents extreme estimates while allowing the data to speak

 Non-informative / reference prior:
 - Jeffreys prior: invariant under reparameterization
 - Flat prior: uniform over all values (often improper and not recommended)

3. Bayes factor:
 BF = P(data | H1) / P(data | H0)
 - BF > 10: strong evidence for H1
 - BF 3-10: moderate evidence
 - BF 1-3: weak evidence
 - BF < 1: evidence favors H0
 - BF 1/10 to 1/3: moderate evidence for H0
 - Interpretation: the Bayes factor is how much more probable the data is under H1 vs H0

4. Posterior credible interval:
 - The 95% credible interval contains the true parameter with 95% posterior probability
 - Contrast with frequentist CI: the frequentist CI does NOT have a probability interpretation for the parameter
 - Highest Density Interval (HDI): the shortest interval containing 95% of the posterior mass

5. Decision making under uncertainty:
 - Region of Practical Equivalence (ROPE): define a range of effect sizes that are practically negligible
 - If the posterior is entirely within the ROPE: accept H0 as practically equivalent
 - If the posterior is entirely outside the ROPE: reject H0
 - If the posterior overlaps the ROPE: suspend judgment

Return: posterior distribution, Bayes factor, 95% credible interval, and ROPE-based decision. Copy prompt View page Show more ↓ 
## Statistical Communication 
2 prompt s Statistical Communication Intermediate Prompt 01 
### Statistical Methods Section Writer 
Write the statistical methods section of a research paper or technical report for this analysis.

Study design: {{study_design}}
Data: {{data_description}}
Primary analysis: {{primary_analysis}}
Secondary analyses: {{secondary_analyses}}
Software: {{software}}
Journal / reporting standard: {{reporting_standard}} (CONSORT, STROBE, ARRIVE, APA, etc.)

1. Participants and data:
 - Sample description: how were participants/observations selected?
 - Inclusion and exclusion criteria
 - Sample size and statistical rationale (brief reference to power analysis)

2. Statistical methods:
 - Primary outcome: describe the variable and its measurement level
 - Descriptive statistics: state how continuous variables are summarized (mean ± SD, or median [IQR] if non-normal); categorical variables as count (%)
 - Primary analysis: name the test, state the null hypothesis, and specify the significance threshold
 - Secondary analyses: list any planned comparisons or subgroup analyses
 - Multiple testing: if multiple tests, specify the correction method
 - Handling of missing data: complete case, multiple imputation (state the model), or other

3. Model assumptions:
 - State which assumptions were checked and how
 - State what action was taken if assumptions were violated

4. Software and packages:
 - 'All analyses were conducted in R version {{version}} (R Core Team, {{year}}) using the packages {{list}}'
 - or 'Python version X.X using statsmodels X.X, scipy X.X'

5. Reporting standards to reference:
 - CONSORT (for RCTs): report CONSORT flow diagram
 - STROBE (for observational studies): 22-item checklist
 - PRISMA (for systematic reviews): 27-item checklist
 - ARRIVE 2.0 (for animal research): 21 items

6. Preregistration:
 - If applicable: 'The primary outcome, hypotheses, and analysis plan were pre-registered at {{registry}} (registration number: {{number}})'

Return: complete statistical methods section text suitable for inclusion in a research paper, formatted according to the specified reporting standard. Copy prompt View page Show more ↓ Statistical Communication Beginner Prompt 02 
### Statistical Results Interpretation 
Interpret and communicate these statistical results for a non-technical audience.

Statistical results: {{results}}
Audience: {{audience}} (business stakeholders, clinical team, policymakers, general public)
Context: {{context}}

1. Lead with the scientific conclusion, not the statistic:
 - Start with what it means for people and decisions, not the p-value
 - Wrong: 'The t-test yielded t(48) = 2.3, p = 0.026'
 - Right: 'Patients receiving the new treatment recovered an average of 3 days faster than controls'

2. Effect size before statistical significance:
 - Report the magnitude of the effect, not just whether it is statistically significant
 - 'The intervention increased sales by 12% (95% CI: 7% to 17%)'
 - A large sample can produce a statistically significant but practically meaningless effect
 - A small sample can fail to detect a large and important effect

3. Confidence intervals over p-values:
 - Report 95% CIs alongside point estimates
 - CI communicates uncertainty: a wide interval means we are less sure about the true effect
 - 'We are 95% confident the true effect is between 7% and 17%'
 - Never say 'the probability that the true value is in this interval is 95%' (frequentist CI does not have this interpretation)

4. Practical significance:
 - Is the effect large enough to matter for the decision at hand?
 - Provide a concrete translation: 'An 8% reduction in churn would save approximately $2M annually'
 - Benchmark against a meaningful threshold, not just 'statistically significant'

5. What statistical significance does and does NOT mean:
 - It means: if the null hypothesis were true, we would rarely see results this extreme by chance
 - It does NOT mean: the effect is large, important, replicable, or clinically meaningful
 - p > 0.05 does NOT mean the null hypothesis is true

6. Uncertainty and limitations:
 - What assumptions could be violated?
 - What alternative explanations cannot be ruled out?
 - How would the interpretation change if the sample were different?

Return: plain-language interpretation of each result, effect size with CI, practical significance assessment, and caveats. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
