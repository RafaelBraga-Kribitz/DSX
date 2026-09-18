# Counterfactual Explanations *AI Prompt *

This prompt generates actionable counterfactual explanations for unfavorable model outcomes. It is useful in domains where people need to understand what realistic changes could improve their predicted outcome. The focus is on minimal, feasible, and user-actionable changes rather than impossible edits. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate counterfactual explanations for rejected or unfavorable predictions from this model.

A counterfactual answers the question: 'What is the minimal change to the input that would flip the prediction?'

For the top 10 most impactful negative predictions (e.g. loan rejected, churn predicted, fraud flagged):
1. Find the nearest counterfactual: the smallest change to input features that would result in a positive prediction
2. Constraints: only change features that are actionable (not age, not historical data — only things the person can change)
3. For each counterfactual show: original values | counterfactual values | what changed | magnitude of change
4. Rank the required changes from easiest to hardest to achieve
5. Generate a plain-English 'what you could do differently' explanation for each case

Return: counterfactual table for each case and template text suitable for a customer-facing explanation. 
```

## When to use this prompt 
Use case 01 
You need explanations for rejected, flagged, or otherwise unfavorable predictions. 
Use case 02 
The audience cares about what can be changed, not just why the result happened. 
Use case 03 
Only actionable features should be modified in the explanation. 
Use case 04 
You want outputs suitable for customer-facing or operations-facing use. 

## What the AI should return 

Counterfactual tables for each selected case, ranked actionable changes, and plain-English explanation templates describing what changes could flip the prediction. 

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

Once you have the first result, continue deeper with related prompts in Explainability.
