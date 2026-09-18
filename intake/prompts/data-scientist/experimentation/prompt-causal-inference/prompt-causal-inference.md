# Causal Inference Analysis *AI Prompt *

This prompt estimates causal effects from observational data when randomized experiments are unavailable. It is useful for policy, operations, and product questions where treatment assignment may be confounded. By comparing several estimators, it helps judge how robust the inferred effect appears. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Estimate the causal effect of {{treatment_variable}} on {{outcome_variable}} from this observational dataset (no random assignment).

1. Describe the confounding problem: which variables are likely confounders that affect both treatment assignment and the outcome?
2. Apply Propensity Score Matching (PSM):
 - Estimate propensity scores using logistic regression
 - Match treated to control units on propensity score (1:1, nearest neighbor)
 - Check covariate balance before and after matching (standardized mean differences)
3. Estimate the Average Treatment Effect on the Treated (ATT) using matched pairs
4. Apply Inverse Probability of Treatment Weighting (IPTW) as a cross-check
5. Apply a Doubly Robust estimator combining propensity score and outcome model
6. Compare ATT estimates from all three methods — are they consistent?

Return: balance table, ATT estimates with 95% CIs, and a plain-English interpretation of the causal effect. 
```

## When to use this prompt 
Use case 01 
Randomized assignment was not possible but causal impact still matters. 
Use case 02 
You have plausible confounders available in the dataset. 
Use case 03 
You want matching, weighting, and doubly robust estimates compared. 
Use case 04 
A plain-English interpretation of ATT is needed for stakeholders. 

## What the AI should return 

Covariate balance diagnostics, ATT estimates with confidence intervals from multiple causal methods, comparison of consistency across methods, and a plain-language interpretation of the estimated treatment effect. 

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

Once you have the first result, continue deeper with related prompts in Experimentation.
