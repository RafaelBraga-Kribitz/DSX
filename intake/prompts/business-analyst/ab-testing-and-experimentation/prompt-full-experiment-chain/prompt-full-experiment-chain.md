# Full Experiment Chain *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It connects design, sizing, analysis, stability checks, and business impact into one experimentation workflow. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Hypothesis — write a clear falsifiable hypothesis for the proposed change. Define primary metric, secondary metrics, and guardrail metrics.
Step 2: Sample size — calculate required sample size and test duration given baseline metric, MDE, α=0.05, and power=80%.
Step 3: Pre-experiment checks — run an AA test on historical data to verify randomization works. Check for pre-existing imbalances between groups.
Step 4: Run analysis — after experiment completion: check for SRM, run primary statistical test, apply multiple testing correction if needed, segment the results.
Step 5: Novelty and stability check — plot daily results to check for novelty effects or instability. Confirm results are consistent in the second half of the experiment.
Step 6: Business impact calculation — translate the statistical result into business impact: if this effect holds, what is the annual revenue or metric impact?
Step 7: Decision and documentation — write a 1-page experiment summary: hypothesis, method, results, decision (ship/no-ship/iterate), business impact, and lessons learned. 
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

The AI should return a step-by-step deliverable that follows the sequence in the prompt and clearly labels each stage. Each step should build on the previous one, with concise assumptions where information is missing and explicit flags where clarification is needed. The final section should synthesize the work into an executive-ready summary, recommendation, or document that could be shared directly with stakeholders. 

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
