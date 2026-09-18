# Power Analysis and Sample Size *AI Prompt *

Conduct a power analysis and determine the required sample size for this study. Study design: {{study_design}} Statistical test: {{test}} Effect size: {{effect_size}} (or provid... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a power analysis and determine the required sample size for this study.

Study design: {{study_design}}
Statistical test: {{test}}
Effect size: {{effect_size}} (or provide: expected means/proportions and standard deviation to compute it)
Significance level: alpha = {{alpha}} (default 0.05)
Desired power: 1 - beta = {{power}} (default 0.80; use 0.90 for high-stakes studies)

1. Effect size calculation:
 If raw parameters are given rather than a standardized effect size:

 Cohen's d (for means): d = (mu_1 - mu_2) / pooled_SD
 - Small: d = 0.2, Medium: d = 0.5, Large: d = 0.8

 Cohen's h (for proportions): h = 2 arcsin(sqrt(p1)) - 2 arcsin(sqrt(p2))
 - Small: h = 0.2, Medium: h = 0.5, Large: h = 0.8

 Cohen's f (for ANOVA): f = sigma_between / sigma_within
 - Small: f = 0.10, Medium: f = 0.25, Large: f = 0.40

 Pearson r (for correlation):
 - Small: r = 0.10, Medium: r = 0.30, Large: r = 0.50

2. Sample size formula per test:

 Two-sample t-test:
 n per group = 2 x ((z_alpha/2 + z_beta) / d)^2
 where z_alpha/2 = 1.96 (alpha=0.05, two-tailed), z_beta = 0.84 (power=0.80)

 One-sample t-test:
 n = ((z_alpha/2 + z_beta) / d)^2

 Chi-square test of two proportions:
 n per group = (z_alpha/2 sqrt(2 p_bar (1-p_bar)) + z_beta sqrt(p1(1-p1) + p2(1-p2)))^2 / (p1-p2)^2
 where p_bar = (p1 + p2) / 2

 Calculate the required n for the stated parameters.

3. Power curve:
 Show how power changes as n increases from n/2 to 3n.
 Identify where additional subjects yield diminishing returns (power > 0.95).

4. Sensitivity analysis:
 - Required n if effect size is 25% smaller than expected
 - Required n at power = 0.90 vs 0.80
 - Required n at alpha = 0.01 vs 0.05

5. Practical considerations:
 - Add 10-20% to account for dropouts or missing data
 - For clustered designs: multiply by the design effect (DEFF = 1 + (m-1) x ICC, where m is cluster size)
 - Is the required n feasible given the study constraints?

Return: standardized effect size, required n with formula, power curve description, sensitivity table, and feasibility assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin hypothesis testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Hypothesis Testing or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Effect size calculation:, Small: d = 0.2, Medium: d = 0.5, Large: d = 0.8, Small: h = 0.2, Medium: h = 0.5, Large: h = 0.8. The final answer should stay clear, actionable, and easy to review inside a hypothesis testing workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Hypothesis Testing.
