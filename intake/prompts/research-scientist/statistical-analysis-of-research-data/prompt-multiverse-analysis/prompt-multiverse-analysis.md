# Multiverse Analysis *AI Prompt *

Design and execute a multiverse analysis to assess the robustness of my findings across reasonable analytical choices. Main finding: {{main_finding}} Analysis pipeline: {{analys... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and execute a multiverse analysis to assess the robustness of my findings across reasonable analytical choices.

Main finding: {{main_finding}}
Analysis pipeline: {{analysis_pipeline}}

A multiverse analysis reports results across all defensible combinations of analytical decisions, rather than cherry-picking one analysis path.

1. Map the decision nodes in my analysis:

 For each step in the pipeline, identify all defensible alternatives:

 Data processing decisions:
 - Outlier exclusion: none, ±2 SD, ±3 SD, Winsorization at 5th/95th percentile
 - Missing data: complete case, single imputation, multiple imputation (5 datasets, 20 datasets)
 - Variable transformation: raw, log, square root, z-score
 - Covariate inclusion: minimal (pre-specified), expanded (additional theoretically relevant covariates)

 Analytical decisions:
 - Model family: OLS, robust regression, mixed model
 - Predictor operationalization: continuous vs dichotomized vs categorical
 - Outcome operationalization: if multiple measures of the same construct, which one is primary?
 - Control variables: which covariates to include

 Sampling decisions:
 - Exclusion criteria: strict application vs lenient (e.g. include vs exclude participants who missed >20% of items)
 - Subpopulation: full sample vs specific age range vs specific subgroup

2. Execute the multiverse:
 - Define all combinations of decisions: this produces the 'multiverse' of analyses
 - Run the primary test across all combinations
 - Extract: effect size, p-value, and confidence interval for each universe

3. Summarize and visualize:
 - Specification curve: plot all effect sizes sorted from smallest to largest, with indicator strips showing which decisions each specification used
 - Proportion of specifications showing a statistically significant effect in the expected direction
 - Proportion of specifications showing a significant effect in the unexpected direction

4. Interpretation:
 - Robust finding: significant and in the expected direction in the large majority of specifications (> 80%)
 - Fragile finding: result depends heavily on specific analytical choices
 - Which specific decisions drive the result? Are those the more or less defensible choices?

5. Reporting:
 - Report the main analysis AND the multiverse results
 - Never use the multiverse to find the significant result — preregister the primary analysis

Return: decision node mapping, analysis code, specification curve plot, robustness interpretation, and reporting text. 
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

The AI should return a structured result that covers the main requested outputs, such as Map the decision nodes in my analysis:, Outlier exclusion: none, ±2 SD, ±3 SD, Winsorization at 5th/95th percentile, Missing data: complete case, single imputation, multiple imputation (5 datasets, 20 datasets). The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
