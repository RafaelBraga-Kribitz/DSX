# Regression Evaluation *AI Prompt *

This prompt evaluates regression models from several complementary angles. It is useful for checking raw accuracy, residual structure, bias patterns, and specific failure cases. The aim is to understand not only how wrong the model is, but where and why. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Evaluate this regression model comprehensively.

1. Compute: MAE, RMSE, MAPE, R², and Adjusted R²
2. Plot predicted vs actual values — how close are points to the diagonal?
3. Plot residuals vs predicted values — check for patterns (heteroscedasticity, non-linearity)
4. Plot residual distribution — should be approximately normal with mean near zero
5. Identify the top 10 largest errors (by absolute residual) — do they share any characteristics?
6. Check for systematic bias: does the model over-predict or under-predict for certain segments?

Return: metric table, 4 diagnostic plots, a table of worst predictions with row details, and a one-paragraph model assessment. 
```

## When to use this prompt 
Use case 01 
You are validating a regression model before trusting it. 
Use case 02 
You want residual diagnostics and not just RMSE or MAE. 
Use case 03 
You need to inspect the worst predictions in detail. 
Use case 04 
You want to identify segment-specific bias or heteroscedasticity. 

## What the AI should return 

A regression metric table, four diagnostic plots, a worst-error table with row-level detail, and a concise written assessment of model quality and likely issues. 

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

Once you have the first result, continue deeper with related prompts in Model Evaluation.
