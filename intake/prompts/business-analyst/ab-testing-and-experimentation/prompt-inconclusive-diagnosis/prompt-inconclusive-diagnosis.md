# Inconclusive Test Diagnosis *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It explains why a test may have failed to reach significance and what to do next. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
This A/B test returned an inconclusive result (p > 0.05, no significant effect detected). Diagnose why and recommend next steps.

1. Check statistical power:
 - Was the test adequately powered? Calculate post-hoc power given observed effect size and sample size.
 - If power < 80%, the test was underpowered — this is likely a false negative, not proof of no effect.

2. Check the effect size:
 - What was the observed effect size, even if not significant?
 - Is the observed effect smaller than the MDE? If yes, the test was powered for a larger effect.

3. Check test duration:
 - Was the test run long enough to cover at least one full weekly cycle?
 - Was the test affected by external events (seasonality, promotions, product launches)?

4. Check for segment heterogeneity:
 - Does the effect appear in specific segments even if the overall result is null?
 - This could indicate the change is right for a subset of users.

5. Based on the diagnosis, recommend one of:
 - Re-run with larger sample size (provide new calculation)
 - Re-run targeting only the segment where effect appeared
 - Redesign the test with a stronger treatment
 - Accept the null — the change genuinely has no effect

Return: power analysis, effect size assessment, duration check, segment analysis, and recommendation. 
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
