# Replication Failure Diagnosis *AI Prompt *

My replication attempt did not reproduce the original finding. Help me diagnose why and what conclusions to draw. Original finding: {{original_finding}} (effect size: {{original... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
My replication attempt did not reproduce the original finding. Help me diagnose why and what conclusions to draw.

Original finding: {{original_finding}} (effect size: {{original_es}})
Replication finding: {{replication_finding}} (effect size: {{replication_es}})
Design differences: {{design_differences}}

1. First: quantify the discrepancy
 - Is the replication effect size significantly different from the original? Use a test of heterogeneity (Q statistic or equivalence test)
 - What is the 95% CI of the replication effect size? Does it exclude the original effect size?
 - Could the discrepancy be explained by sampling variation alone? (Both studies may be sampling from the same distribution)

2. Candidate explanations for replication failure:

 a. Statistical explanation (most common for small original studies):
 - The original effect was a false positive (Type I error)
 - The original effect size was inflated by publication bias and the original study was underpowered
 - Both the original and replication are sampling a real effect with high variance
 Evidence for: p-value just below .05 in original; small original N; effect not replicated across multiple attempts

 b. Methodological differences:
 - The replication differed from the original in a consequential way
 - Which specific differences between original and replication could plausibly moderate the effect?
 - A moderator variable was different between studies (population, context, time, operationalization)
 Evidence for: specific, theoretically justified moderator that differed between studies

 c. Context effects:
 - The effect is real but context-dependent
 - The original study was conducted in a specific context that does not generalize
 - Time effects: the phenomenon may have changed since the original study (technology, cultural change)
 Evidence for: original and replication differ in context in a way consistent with a known moderator

 d. Fraud or QRP in the original:
 - The original data were fabricated or p-hacked
 Evidence for: statistical anomalies in the original (GRIM test, SPRITE test, p-curve analysis)

3. What replication failure does and does not tell us:
 - Does NOT tell us: the original finding was definitely wrong, that the original authors did anything improper
 - DOES tell us: the original finding may not be reliable, the effect size is likely smaller than originally reported, the conditions under which the effect occurs need further investigation

4. Recommended next steps:
 - Conduct a mini meta-analysis of all available replications including your own
 - Design a well-powered study explicitly testing the hypothesized moderator
 - Contact the original authors for a collaborative adversarial replication

Return: discrepancy quantification, ranked candidate explanations with supporting evidence, and recommended next steps. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin reproducibility and open science work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Reproducibility and Open Science or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as First: quantify the discrepancy, Is the replication effect size significantly different from the original? Use a test of heterogeneity (Q statistic or equivalence test), What is the 95% CI of the replication effect size? Does it exclude the original effect size?. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Reproducibility and Open Science.
