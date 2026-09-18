# Hypothesis Testing *AI Prompts *

4 Statistician prompts in Hypothesis Testing. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Hypothesis Testing 
4 prompts Advanced Chain 01 
### Full Statistical Analysis Chain 

Step 1: Research question and estimand - state the precise research question in one sentence. Define the estimand: the specific population parameter you are trying to estimate o... 
Prompt text Step 1: Research question and estimand - state the precise research question in one sentence. Define the estimand: the specific population parameter you are trying to estimate or test. Specify: the target population, the exposure or treatment, the outcome, and the comparison (vs what baseline or control?).
Step 2: Study design assessment - evaluate the study design: was randomization used? If observational, what is the primary confounding threat? Draw the causal DAG and identify the minimal sufficient adjustment set.
Step 3: Data quality check - assess the data for: missing values (pattern and % per variable), outliers (flag observations > 3 SD from mean), distributional assumptions (normality, homoscedasticity), and any data entry anomalies.
Step 4: Descriptive statistics - produce a Table 1: describe all variables by group. For continuous variables: mean (SD) or median [IQR] based on distribution. For categorical: count (%). Test baseline differences if a two-group comparison.
Step 5: Primary analysis - select and run the primary statistical test. Report: test statistic, degrees of freedom, p-value, effect size, and 95% confidence interval. Check all assumptions and note any violations.
Step 6: Secondary and sensitivity analyses - run planned secondary analyses. Conduct a sensitivity analysis: repeat the primary analysis under different assumptions (e.g., complete cases vs imputed, alternative covariate adjustment sets). Assess robustness.
Step 7: Interpretation and reporting - write a plain-language summary of findings. Interpret the effect size in practical terms. Discuss limitations. Specify what the results can and cannot conclude. Produce the statistical methods section text. Copy prompt Open prompt details Beginner Single prompt 02 
### Hypothesis Test Selector 

Help me select the correct statistical test for this analysis. Data description: {{data_description}} Research question: {{research_question}} Sample size: {{n}} Data types: {{d... 
Prompt text Help me select the correct statistical test for this analysis.

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

Return: recommended test, assumptions to verify, alternative if assumptions are violated, and multiple comparison strategy. Copy prompt Open prompt details Intermediate Single prompt 03 
### Multiple Testing Correction 

Apply appropriate multiple testing corrections to this set of hypothesis tests. Number of tests: {{n_tests}} Raw p-values: {{p_values}} Test context: {{context}} (exploratory an... 
Prompt text Apply appropriate multiple testing corrections to this set of hypothesis tests.

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

Return: FWER and FDR calculations applied to the provided p-values, comparison table, and method recommendation. Copy prompt Open prompt details Intermediate Single prompt 04 
### Power Analysis and Sample Size 

Conduct a power analysis and determine the required sample size for this study. Study design: {{study_design}} Statistical test: {{test}} Effect size: {{effect_size}} (or provid... 
Prompt text Conduct a power analysis and determine the required sample size for this study.

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

Return: standardized effect size, required n with formula, power curve description, sensitivity table, and feasibility assessment. Copy prompt Open prompt details 
## Recommended Hypothesis Testing workflow 
1 
### Full Statistical Analysis Chain 

Start with a focused prompt in Hypothesis Testing so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Hypothesis Test Selector 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Multiple Testing Correction 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Power Analysis and Sample Size 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
