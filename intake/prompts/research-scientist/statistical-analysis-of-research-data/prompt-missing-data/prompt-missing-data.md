# Missing Data Handler *AI Prompt *

Analyze the missing data in my study and implement the appropriate handling strategy. Dataset description: {{dataset}} Missingness pattern: {{missingness_description}} Analysis... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the missing data in my study and implement the appropriate handling strategy.

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

Return: missing data analysis, mechanism assessment, recommended strategy with implementation code, and reporting text. 
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

The AI should return a structured result that covers the main requested outputs, such as Classify the missing data mechanism:, Missingness is unrelated to any variable in the dataset, observed or unobserved, Test: Little's MCAR test; compare characteristics of completers vs incomplete cases. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
