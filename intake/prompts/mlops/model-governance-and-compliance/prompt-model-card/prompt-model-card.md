# Model Card Writer *AI Prompt *

This prompt writes a model card that documents intended use, training data, performance, limitations, risks, and operational context. It is useful for internal governance, stakeholder communication, and responsible model release practices. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a comprehensive model card for this production ML model.

Model cards are documentation artifacts that describe a model's intended use, performance characteristics, limitations, and ethical considerations.

Model: {{model_name}}
Owner: {{owner_team}}

1. Model overview:
 - Model name and version
 - Model type: {{model_type}} (e.g. gradient boosted classifier)
 - Purpose: what task does this model solve? One paragraph.
 - Intended users: who uses this model and in what context?
 - Out-of-scope uses: what should this model NOT be used for?

2. Training data:
 - Data sources: where did the training data come from?
 - Time range: what period does the training data cover?
 - Dataset size: number of examples and features
 - Known biases or limitations in the training data
 - Data preprocessing and feature engineering summary

3. Performance:
 - Primary metric and its value on the test set
 - All secondary metrics
 - Performance broken down by key subgroups (age, region, device, etc.)
 - Performance comparison to baseline
 - Confidence: how reliable are these estimates?

4. Limitations and risks:
 - Known failure modes: when does this model perform poorly?
 - Distribution shift sensitivity: how sensitive is performance to input changes?
 - Uncertainty: what does the model not know it does not know?
 - Potential for harm: could this model produce unfair or harmful outcomes for any group?

5. Ethical considerations:
 - Fairness assessment: performance disparity across demographic groups
 - Privacy: does the model encode or memorize sensitive information?
 - Explainability: can individual predictions be explained?

6. Operations:
 - Model version and registry location
 - Serving infrastructure
 - Monitoring in place
 - Retraining frequency and trigger conditions
 - Owner and escalation path

Return: complete model card document in Markdown format. 
```

## When to use this prompt 
Use case 01 
when a production model needs formal documentation for stakeholders 
Use case 02 
when intended use, limitations, and risks should be written clearly 
Use case 03 
when performance by subgroup and operational ownership must be documented 
Use case 04 
when governance artifacts are required before or after launch 

## What the AI should return 

A complete model card in Markdown covering overview, training data, performance, limitations, ethical considerations, and operations. 

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

Once you have the first result, continue deeper with related prompts in Model Governance and Compliance.
