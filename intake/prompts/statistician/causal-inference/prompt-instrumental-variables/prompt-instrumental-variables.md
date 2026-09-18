# Instrumental Variables Analysis *AI Prompt *

Specify and implement an instrumental variables (IV) analysis to estimate a causal effect in the presence of unmeasured confounding. Exposure (endogenous treatment): {{treatment... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: instrument validity assessment, 2SLS specification, first-stage F-statistic, IV estimate with CI, and interpretation of LATE. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin causal inference work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Causal Inference or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What IV analysis does:, Three conditions for a valid instrument:, The instrument Z must be associated with the treatment X. The final answer should stay clear, actionable, and easy to review inside a causal inference workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Causal Inference.
