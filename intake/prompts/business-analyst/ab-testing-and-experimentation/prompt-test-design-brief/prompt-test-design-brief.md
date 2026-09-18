# A/B Test Design Brief *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It creates a structured experiment brief that can be reviewed before a test goes live. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write an A/B test design brief for the following proposed change: {{change_description}}

The brief must include:

1. Hypothesis
 - We believe that [change] will cause [outcome] because [rationale]
 - Null hypothesis: the change has no effect on the primary metric

2. Primary metric: the single metric this test will be judged on
3. Secondary metrics: 2–3 supporting metrics to monitor
4. Guardrail metrics: 2–3 metrics that must not significantly degrade

5. Test setup
 - Unit of randomization: user / session / account / device
 - Traffic split: 50/50 or other (justify any deviation)
 - Targeting: all users, or a specific segment? Why?

6. Statistical parameters
 - Significance level α = 0.05 (two-tailed)
 - Minimum detectable effect (MDE): the smallest change worth detecting
 - Required statistical power: 80%
 - Required sample size per variant (calculate)
 - Required experiment duration given current daily traffic of {{daily_traffic}}

7. Risks: what could go wrong? How will you detect it?
8. Decision criteria: exactly when will you ship, iterate, or kill?

Return: the complete test brief as a shareable document. 
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
