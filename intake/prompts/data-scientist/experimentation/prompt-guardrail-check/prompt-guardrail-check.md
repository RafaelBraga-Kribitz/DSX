# Experiment Guardrail Check *AI Prompt *

This prompt checks whether a promising experiment result hides unacceptable side effects. It is especially useful when shipping decisions depend on more than the primary metric alone. The analysis makes trade-offs explicit so gains and harms can be judged together. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Check the guardrail metrics for this experiment to ensure no unintended harm was caused.

Guardrail metrics are metrics that must not be significantly degraded even if the primary metric improves.

1. List all guardrail metrics provided in the dataset (e.g. page load time, error rate, support tickets, refund rate)
2. For each guardrail metric, test whether treatment significantly degraded it vs control (one-sided test, α=0.05)
3. Report: guardrail metric | control mean | treatment mean | % change | p-value | status (✅ Safe / 🔴 Degraded)
4. Flag any guardrail metric that is significantly degraded — this may block shipping even if the primary metric improved
5. Compute the trade-off: if a guardrail is degraded, what is the net business impact of the primary metric gain minus the guardrail loss?

Return the guardrail report and a final ship/no-ship recommendation considering both primary and guardrail results. 
```

## When to use this prompt 
Use case 01 
The experiment has defined guardrail metrics that cannot worsen materially. 
Use case 02 
A lift in the primary metric may come with operational or customer risk. 
Use case 03 
You need a ship decision that incorporates side effects explicitly. 
Use case 04 
You want a structured report for stakeholders beyond the experiment team. 

## What the AI should return 

A guardrail table with treatment-versus-control comparisons, degradation status, trade-off interpretation, and a final ship or no-ship recommendation that considers both upside and harm. 

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
