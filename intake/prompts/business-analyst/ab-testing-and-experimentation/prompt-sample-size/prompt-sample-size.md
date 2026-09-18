# Sample Size Calculator *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It estimates how much traffic and time an experiment needs before the results can be trusted. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate the required sample size for this A/B test.

Inputs:
- Primary metric type: {{metric_type}} (conversion rate / continuous metric)
- Baseline value: {{baseline}} (e.g. current conversion rate of 5%, or mean revenue of $42)
- Minimum detectable effect (MDE): {{mde}} (e.g. 10% relative lift, or absolute +0.5%)
- Significance level α: 0.05 (two-tailed)
- Statistical power: 80%
- Number of variants: {{variants}} (e.g. 2 = one control + one treatment)

Calculate and return:
1. Required sample size per variant
2. Total sample size across all variants
3. Required test duration given daily traffic of {{daily_traffic}} users/sessions
4. Sensitivity table: how does sample size change as MDE varies?
 - MDE at 50%, 75%, 100%, 125%, 150% of the specified MDE
5. Power curve: plot statistical power vs sample size for the specified MDE
6. Flag if the required duration exceeds 4 weeks — longer tests are vulnerable to seasonality and novelty effects

Return: sample size calculation, duration estimate, sensitivity table, and power curve. 
```

## When to use this prompt 
Use case 01 
Use when a product, growth, or operations team wants to test a change rigorously. 
Use case 02 
Use before launch to design an experiment or after launch to interpret results. 
Use case 03 
Use when you need to calculate sample size, validate significance, or diagnose weak tests. 
Use case 04 
Use when a decision depends on evidence rather than intuition or stakeholder opinion. 

## What the AI should return 

The AI should return a decision-ready experiment output with the requested calculations, assumptions, and interpretation clearly labeled. Statistical reasoning should be explained in plain language, and the response should distinguish significance, practical impact, risks, and next steps. Any recommendation should be explicit, defensible, and tied to the evidence provided. 

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

Once you have the first result, continue deeper with related prompts in AB Testing and Experimentation.
