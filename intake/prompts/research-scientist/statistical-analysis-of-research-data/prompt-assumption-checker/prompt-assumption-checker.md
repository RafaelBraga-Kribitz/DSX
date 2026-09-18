# Statistical Assumption Checker *AI Prompt *

Check the statistical assumptions underlying my planned analyses and recommend how to handle any violations. Planned analyses: {{analyses}} Data characteristics: {{data_descript... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Check the statistical assumptions underlying my planned analyses and recommend how to handle any violations.

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

Return: assumption checklist per analysis, violation assessment, remedies with implementation guidance, and reporting language. 
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

The AI should return a structured result that covers the main requested outputs, such as Linear regression assumptions:, Linearity: is the relationship between predictors and outcome linear? Check: scatter plot, residual vs fitted plot. Violation: use polynomial terms, transformations, or GAM., Independence: are observations independent? Check: study design. Violation: use clustered standard errors, mixed models, or GEE.. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
