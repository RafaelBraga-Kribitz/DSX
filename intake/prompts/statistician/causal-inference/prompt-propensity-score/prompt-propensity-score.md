# Propensity Score Analysis *AI Prompt *

Implement and evaluate a propensity score analysis to estimate a causal effect from observational data. Treatment variable: {{treatment}} (binary: treated vs untreated) Outcome:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: PS model specification, overlap assessment, balance table (pre/post), causal effect estimate, and sensitivity analysis. 
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

The AI should return a structured result that covers the main requested outputs, such as Estimand clarification:, ATE (Average Treatment Effect): the effect if the entire population were treated vs untreated, ATT (Average Treatment Effect on the Treated): the effect for those who actually received treatment. The final answer should stay clear, actionable, and easy to review inside a causal inference workflow for statistician work. 

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
