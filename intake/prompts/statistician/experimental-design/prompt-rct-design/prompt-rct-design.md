# Randomized Controlled Trial Design *AI Prompt *

Design a randomized controlled trial (RCT) to answer this research question. Research question: {{research_question}} Intervention: {{intervention}} Primary outcome: {{primary_o... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a randomized controlled trial (RCT) to answer this research question.

Research question: {{research_question}}
Intervention: {{intervention}}
Primary outcome: {{primary_outcome}}
Population: {{population}}
Practical constraints: {{constraints}} (budget, timeline, ethical restrictions)

1. Randomization design:

 Simple randomization:
 - Each participant independently assigned with probability p = 0.5
 - Works well for large n (> 200); may produce imbalanced groups in small trials

 Block randomization:
 - Participants randomized in blocks of fixed size (e.g. blocks of 4 or 6)
 - Guarantees approximately equal group sizes throughout the trial
 - Use when enrollment is sequential and interim analyses are planned

 Stratified randomization:
 - Randomize separately within strata of key prognostic variables (age group, site, disease severity)
 - Prevents chance imbalance on important covariates
 - Combine with block randomization within strata

 Cluster randomization:
 - Randomize groups (clinics, schools, communities) rather than individuals
 - Use when individual randomization causes contamination
 - Requires larger sample size (inflate by design effect = 1 + (m-1) x ICC)

2. Blinding:
 - Open-label: neither participants nor assessors are blinded (highest risk of bias)
 - Single-blind: participants are blinded to treatment assignment
 - Double-blind: both participants and outcome assessors are blinded (gold standard for efficacy)
 - Triple-blind: includes the data analysts
 - Is blinding feasible for this intervention? If not: use blinded outcome assessment at minimum

3. Sample size and allocation:
 - Calculate required n based on primary outcome (see power analysis prompt)
 - Equal allocation (50/50) is most efficient when costs per participant are equal
 - Unequal allocation: use if one arm is more costly or to expose fewer to the control

4. Analysis plan (pre-specified):
 - Primary analysis: intention-to-treat (ITT) — analyze participants as randomized, regardless of adherence
 - Per-protocol analysis: sensitivity analysis for those who completed the protocol
 - Handling missing data: specify imputation method in advance
 - Pre-register the primary outcome and analysis plan (ClinicalTrials.gov, OSF)

5. Validity threats:
 - Selection bias: only randomization fully controls this
 - Attrition: track dropout rate by arm; > 20% differential dropout threatens validity
 - Contamination: control group receives elements of the intervention
 - CONSORT checklist: use for reporting

Return: randomization design recommendation, blinding plan, sample size, ITT analysis plan, and validity threat assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Randomization design:, Each participant independently assigned with probability p = 0.5, Works well for large n (> 200); may produce imbalanced groups in small trials. The final answer should stay clear, actionable, and easy to review inside a experimental design workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design.
