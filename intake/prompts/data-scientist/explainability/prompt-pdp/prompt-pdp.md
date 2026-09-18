# Partial Dependence Plots *AI Prompt *

This prompt maps how changing a feature affects the model on average and across individual cases. It is useful for identifying monotonic, threshold, or highly heterogeneous feature effects. The combination of PDP and ICE helps distinguish average behavior from person-level variability. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate partial dependence plots (PDPs) and individual conditional expectation (ICE) plots for the top features in this model.

For each of the top 5 most important features:
1. Plot the PDP: how does the average model prediction change as this feature varies across its range?
2. Overlay 50 randomly sampled ICE curves to show individual variation around the average
3. Highlight the average ICE curve in bold
4. Mark the actual data distribution (rug plot) on the x-axis to show where data is sparse
5. Describe the relationship: monotonic increasing, monotonic decreasing, non-linear, threshold effect?

Also create one 2D PDP for the top pair of interacting features (identified from SHAP interaction values).

Return all plots and a table summarizing the relationship type for each feature. 
```

## When to use this prompt 
Use case 01 
You want to understand the functional form of key feature effects. 
Use case 02 
A feature may have threshold or non-linear behavior. 
Use case 03 
You need to see whether average effects hide strong individual variation. 
Use case 04 
You want to inspect one important pairwise interaction visually. 

## What the AI should return 

PDP and ICE plots for top features, one 2D interaction plot, and a summary table describing each feature's relationship type and any evidence of heterogeneity. 

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
