# Hypothesis Test Selector *AI Prompt *

Help me select the correct statistical test for this analysis. Data description: {{data_description}} Research question: {{research_question}} Sample size: {{n}} Data types: {{d... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: recommended test, assumptions to verify, alternative if assumptions are violated, and multiple comparison strategy. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin hypothesis testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Hypothesis Testing or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Apply the test selection decision tree:, 1 group vs known value, continuous, normal: One-sample t-test, 2 independent groups, continuous, normal, equal variance: Independent t-test. The final answer should stay clear, actionable, and easy to review inside a hypothesis testing workflow for statistician work. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Hypothesis Testing.
