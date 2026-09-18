# Difference-in-Differences Design *AI Prompt *

Design and analyze a difference-in-differences (DiD) study to estimate a causal effect from panel data. Treatment: {{treatment}} (a policy, intervention, or event that affects s... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and analyze a difference-in-differences (DiD) study to estimate a causal effect from panel data.

Treatment: {{treatment}} (a policy, intervention, or event that affects some units but not others)
Timing: {{timing}} (when did the treatment occur?)
Panel data: {{data_description}} (units observed before and after the treatment)
Comparison groups: {{treatment_group}} (treated) vs {{control_group}} (untreated)

1. DiD logic:
 DiD = (Mean_treated_post - Mean_treated_pre) - (Mean_control_post - Mean_control_pre)
 The control group's change over time is used to estimate the counterfactual trend for the treated group.
 The key identifying assumption is parallel trends: absent the treatment, treated and control units would have evolved in parallel.

2. Parallel trends assumption:
 - Check pre-treatment trends: plot the outcome for treated and control groups across all pre-treatment periods
 - If trends are parallel pre-treatment: assumption is plausible (not proven)
 - Formal test: interact treatment group with pre-treatment time dummies; if coefficients are jointly zero, trends are parallel
 - Event study plot: plot the treatment effect coefficient for each period relative to treatment, including pre-treatment leads. Pre-treatment coefficients should be near zero.

3. DiD regression specification:
 y_it = alpha + beta1 Treated_i + beta2 Post_t + delta (Treated_i x Post_t) + epsilon_it
 - delta is the DiD estimator
 - Add unit fixed effects (absorbs all time-invariant unit characteristics)
 - Add time fixed effects (absorbs common shocks)
 - Two-way fixed effects (TWFE): y_it = alpha_i + alpha_t + delta D_it + epsilon_it
 where D_it = 1 if unit i is treated in period t

4. Staggered treatment timing:
 - If different units receive treatment at different times, TWFE can be biased
 - Modern estimators for staggered DiD: Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-d'Haultfoeuille
 - These estimators form clean 2x2 DiD comparisons and average them correctly
 - Use the csdid (Stata) or did (R) package

5. Standard errors:
 - Cluster standard errors at the unit level (accounts for serial correlation within units)
 - If few treated clusters (< 10): wild cluster bootstrap for valid inference
 - Placebo tests: apply DiD to a period before treatment; the estimated effect should be near zero

Return: DiD estimate, parallel trends test, event study plot description, staggered timing assessment, and clustered SE specification. 
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

The AI should return a structured result that covers the main requested outputs, such as DiD logic:, Parallel trends assumption:, Check pre-treatment trends: plot the outcome for treated and control groups across all pre-treatment periods. The final answer should stay clear, actionable, and easy to review inside a causal inference workflow for statistician work. 

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
