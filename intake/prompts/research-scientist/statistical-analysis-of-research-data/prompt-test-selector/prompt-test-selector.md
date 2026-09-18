# Statistical Test Selector *AI Prompt *

Help me choose the correct statistical test for my research question and data. Research question: {{research_question}} Outcome variable type: {{outcome_type}} (continuous, bina... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me choose the correct statistical test for my research question and data.

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

Return: recommended test and its regression equivalent, assumptions and how to test them, multiple comparisons guidance. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical analysis of research data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Analysis of Research Data or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Decision tree for test selection:, 2 independent groups, continuous outcome → Independent samples t-test (if normal) or Mann-Whitney U (if not), 2 related groups / repeated measures, continuous outcome → Paired t-test (if normal) or Wilcoxon signed-rank. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Analysis of Research Data.
