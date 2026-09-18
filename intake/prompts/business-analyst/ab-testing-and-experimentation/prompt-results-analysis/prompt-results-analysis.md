# A/B Test Results Analysis *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It turns raw test results into a decision-ready readout with checks, significance, and business interpretation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the results of this A/B test and produce a decision-ready report.

Test data is provided. Include:

1. Pre-analysis checks:
 - Sample ratio mismatch (SRM): is the actual traffic split consistent with the planned split? Use chi-squared test.
 - Was the test run for the full planned duration?
 - Any signs of peeking (early stopping)?

2. Primary metric analysis:
 - Control vs treatment value (mean ± std or conversion rate)
 - Observed absolute and relative difference
 - Statistical test: t-test (continuous) or z-test/chi-squared (proportions)
 - p-value and 95% confidence interval for the difference
 - Is the result statistically significant at α = 0.05?

3. Secondary and guardrail metrics: repeat analysis for each

4. Practical significance: is the observed effect large enough to matter for the business? Compare to the MDE.

5. Segment analysis: break results down by key segments — does treatment work equally across all user types?

6. Decision recommendation: Ship / Do not ship / Iterate / Inconclusive — with clear justification

Return: full analysis report with all tests, segment breakdown, and decision recommendation. 
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
