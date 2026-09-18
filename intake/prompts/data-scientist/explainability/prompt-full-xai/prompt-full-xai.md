# Full XAI Chain *AI Prompt *

This prompt runs a full explainable AI workflow from global importance to business translation. It is useful when you want one coherent interpretability package that can support both technical validation and stakeholder communication. It also explicitly flags potentially risky or counterintuitive model behavior. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Global importance — compute and plot SHAP feature importances (beeswarm). Identify the top 5 features driving predictions.
Step 2: Effect direction — create SHAP dependence plots for the top 5 features. Describe the relationship between each feature and the prediction (linear, threshold, non-linear).
Step 3: Interaction analysis — compute SHAP interaction values. Identify the strongest pairwise interaction and plot it as a 2D PDP.
Step 4: Local explanation — generate waterfall plots for 3 representative predictions: high, low, and borderline.
Step 5: Business translation — write a 1-page non-technical explanation of how the model makes decisions, using analogies and avoiding all technical terms.
Step 6: Risk flagging — identify any feature effects that seem counterintuitive or potentially problematic from a fairness or business logic perspective. 
```

## When to use this prompt 
Use case 01 
You want a complete XAI workflow rather than a single explainer. 
Use case 02 
Both technical and non-technical audiences need to be served. 
Use case 03 
You need interaction analysis and local examples in the same package. 
Use case 04 
You want to surface fairness or business-logic concerns proactively. 

## What the AI should return 

A multi-step explainability package including global rankings, direction-of-effect plots, interaction findings, local explanations, business translation, and a risk flag section. 

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
