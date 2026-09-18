# Replication Study Design *AI Prompt *

Design a high-quality replication study of the following original finding. Original finding: {{original_finding}} Original study: {{original_study_citation}} Replication goal: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a high-quality replication study of the following original finding.

Original finding: {{original_finding}}
Original study: {{original_study_citation}}
Replication goal: {{goal}} (direct/close replication, conceptual replication, or adversarial replication)

1. Clarify the type of replication:

 Direct / close replication:
 - Reproduces the original procedure as closely as possible
 - Tests whether the original finding holds in a new sample from the same population
 - Most informative about the reliability of the original finding
 - Design challenge: the original paper may not describe the procedure in enough detail

 Conceptual replication:
 - Tests the same theoretical claim using different operationalizations
 - Different measures, different manipulations, different population
 - More informative about the generalizability of the theoretical claim
 - Does not tell you whether the original finding itself replicates

 Adversarial replication:
 - Collaborative replication where original authors and skeptics jointly design the study
 - Both parties agree in advance that the result will be accepted as definitive
 - Most credible form of replication but requires cooperation

2. Obtain the original materials:
 - Contact the original authors for: stimuli, exact measures, randomization procedure, analysis code
 - If unavailable: document what is known from the paper and what was reconstructed
 - Differences between original materials and reconstructed materials must be reported

3. Power the replication:
 - A replication should be powered at 90% (not 80%) to detect the original effect size
 - But: original effect sizes are likely inflated (winner's curse from small original studies)
 - Recommended: power to detect 75% of the original effect size, giving a more realistic target
 - A replication powered at 90% for 75% of the original effect size typically requires 2–4× the original N

4. Replication success criteria (specify in advance):
 - Narrow criterion: same direction AND p < .05 (most commonly used, but problematic)
 - Recommended criterion: the original effect size falls within the replication's 95% CI
 - Bayesian criterion: Bayes factor > 3 in favor of the original hypothesis
 - Pre-specify which criterion will be used

5. Regardless of outcome, report:
 - Original effect size and replication effect size with CIs
 - Whether the replication effect size is significantly smaller than the original (test of heterogeneity)
 - All procedural differences from the original study

Return: replication protocol, power analysis, pre-specified success criteria, and a comparison table of original vs replication design. 
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

The AI should return a structured result that covers the main requested outputs, such as Clarify the type of replication:, Reproduces the original procedure as closely as possible, Tests whether the original finding holds in a new sample from the same population. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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
