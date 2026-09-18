# Model Behavior Report *AI Prompt *

This prompt writes a full technical behavior review of the model rather than isolated explainability charts. It is useful when a project needs a more formal narrative covering feature effects, decision patterns, interactions, and edge cases. The report is intended for technical stakeholders who still want business clarity. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a complete model behavior report suitable for a technical stakeholder review.

The report should cover:

1. What the model learned — top 10 features and their direction of effect, in plain English
2. Decision rules — extract the top 5 decision paths from the model using SHAP or tree rules
3. Edge cases — what input combinations lead to extreme predictions (very high and very low)?
4. Monotonicity check — for features where a directional relationship is expected (e.g. more experience → higher salary), does the model respect that direction?
5. Interaction effects — which two features interact the most strongly? How does their interaction affect predictions?
6. Sensitivity analysis — which single feature, if changed by 10%, has the largest average impact on predictions?

Format as a structured report with section headings, plots, and a non-technical executive summary at the top. 
```

## When to use this prompt 
Use case 01 
You need a written behavior report for model review or governance. 
Use case 02 
Charts alone are not enough for the audience. 
Use case 03 
You want decision logic, edge cases, monotonicity, and sensitivity covered together. 
Use case 04 
The review must balance technical depth with readability. 

## What the AI should return 

A structured report with sectioned findings, supporting plots, executive summary, and explanations of feature effects, decision patterns, interactions, edge cases, and sensitivity. 

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
