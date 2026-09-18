# Bayesian Hierarchical Model *AI Prompt *

Specify and interpret a Bayesian hierarchical (multilevel) model for this data. Data structure: {{data_structure}} (units nested in groups: students in schools, measurements in... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: hierarchical model specification, ICC calculation, cross-level interaction interpretation, and MCMC convergence assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin bayesian methods work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Bayesian Methods or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why hierarchical models:, Observations within groups are not independent (ICC > 0), Using a single-level model underestimates standard errors (overestimates precision). The final answer should stay clear, actionable, and easy to review inside a bayesian methods workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Bayesian Methods.
