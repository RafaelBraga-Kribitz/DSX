# Results Reporting Checklist *AI Prompt *

Review my results section for completeness and adherence to best practices in statistical reporting. Results draft: {{results_draft}} Analyses used: {{analyses}} Apply the follo... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Review my results section for completeness and adherence to best practices in statistical reporting.

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

Return: annotated results section with specific corrections, reporting deficiencies flagged by line, and a corrected version of the results. 
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

The AI should return a structured result that covers the main requested outputs, such as Descriptive statistics:, Report M and SD (not SEM, which is rarely interpretable) for continuous variables, Report frequencies and proportions for categorical variables. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
