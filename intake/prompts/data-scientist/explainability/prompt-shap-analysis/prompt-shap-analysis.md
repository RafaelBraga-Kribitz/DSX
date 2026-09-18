# SHAP Analysis *AI Prompt *

This prompt uses SHAP to explain both global model behavior and individual predictions. It is useful when you need richer insight than a single importance ranking, including effect direction and case-level reasoning. It is one of the strongest all-around explainability prompts for tabular models. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate a complete SHAP-based model explanation.

1. Compute SHAP values for all predictions in the validation set
2. Global explanations:
 - Beeswarm plot: feature importance + direction of effect
 - Bar plot: mean absolute SHAP value per feature (top 20)
3. Dependence plots for the top 3 most important features:
 - SHAP value on y-axis, feature value on x-axis
 - Color by the most important interaction feature
4. Local explanations — waterfall plots for:
 - The most confidently correct prediction
 - The most confidently wrong prediction
 - One typical prediction near the decision boundary
5. Plain-English summary: what are the top 3 drivers of high predictions vs low predictions?

Return all plots and the plain-English summary. 
```

## When to use this prompt 
Use case 01 
You need both global and local interpretability. 
Use case 02 
Stakeholders want to know why specific predictions were made. 
Use case 03 
You want direction-of-effect plots rather than just rankings. 
Use case 04 
The model is complex enough that standard importances are not enough. 

## What the AI should return 

SHAP beeswarm and bar plots, dependence plots, selected local waterfall explanations, and a plain-English summary of the main factors that drive high versus low predictions. 

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
