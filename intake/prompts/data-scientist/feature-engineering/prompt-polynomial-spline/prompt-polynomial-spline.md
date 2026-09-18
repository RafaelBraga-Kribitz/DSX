# Polynomial and Spline Features *AI Prompt *

This prompt adds polynomial and spline transformations to model non-linear feature effects explicitly. It is useful when simple linear representations miss curvature, thresholds, or diminishing returns in the relationship with the target. The workflow evaluates whether these richer forms actually improve cross-validated performance. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create polynomial and spline features to capture non-linear relationships in this dataset.

1. Identify the top 5 numeric features by correlation with {{target_variable}}
2. For each, test whether the relationship is linear, quadratic, or higher-order:
 - Fit linear, quadratic, and cubic regression
 - Compare R² values and plot each fit
3. For features with non-linear relationships:
 a. Add polynomial features (degree 2 and 3)
 b. Add natural cubic spline features with 4 knots at the 25th, 50th, 75th, and 90th percentiles
4. Add the polynomial/spline features to the model and compare:
 - CV score before adding
 - CV score after adding
 - Risk of overfitting (train vs val gap)
5. Use SHAP to verify the model is using the polynomial features meaningfully

Return: relationship type table, feature code, and CV performance comparison. 
```

## When to use this prompt 
Use case 01 
Important numeric features may have curved rather than linear effects. 
Use case 02 
You want to compare linear, quadratic, cubic, and spline fits systematically. 
Use case 03 
You need feature code plus evidence that the new terms help. 
Use case 04 
You want to monitor overfitting while expanding the feature space. 

## What the AI should return 

A table describing the relationship shape for each tested feature, code for selected polynomial and spline terms, and CV performance comparison before and after adding them. 

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

Once you have the first result, continue deeper with related prompts in Feature Engineering.
