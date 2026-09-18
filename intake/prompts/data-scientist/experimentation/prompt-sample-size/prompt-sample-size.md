# Sample Size Calculator *AI Prompt *

This prompt estimates how much traffic is needed to detect a meaningful experimental effect. It is useful in planning because underpowered tests waste time and overpowered tests waste opportunity. The sensitivity analysis shows how strongly duration depends on the chosen MDE. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate the required sample size for this experiment.

Inputs:
- Baseline conversion rate or metric value: {{baseline_value}}
- Minimum detectable effect (MDE): {{mde}} — the smallest change worth detecting
- Significance level (α): 0.05 (two-tailed)
- Statistical power (1 - β): 0.80
- Number of variants: {{num_variants}} (control + treatment)

Calculate:
1. Required sample size per variant
2. Total sample size across all variants
3. Required experiment duration given the current daily traffic of {{daily_traffic}} users
4. Show how the required sample size changes if MDE is varied: ±50%, ±25%, ±10% from the specified MDE
5. Plot a power curve: sample size vs statistical power for the specified MDE

Return: sample size, experiment duration, and the power curve plot. 
```

## When to use this prompt 
Use case 01 
You are planning an experiment and need to size it correctly. 
Use case 02 
You need to balance traffic, time, and detectable effect size. 
Use case 03 
Stakeholders want to understand why the test must run for a given duration. 
Use case 04 
You want a power curve and sensitivity analysis, not only one number. 

## What the AI should return 

Sample size per variant, total required sample, estimated duration given traffic, sensitivity scenarios for different MDE values, and a power curve visual. 

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
