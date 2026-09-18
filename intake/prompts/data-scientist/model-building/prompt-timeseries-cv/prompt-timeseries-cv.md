# Time Series Cross-Validation *AI Prompt *

This prompt applies proper walk-forward evaluation to forecasting problems where ordinary cross-validation would leak future data. It is useful for getting realistic estimates of how the model behaves in production-like temporal settings. It also checks whether performance worsens over time. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement correct cross-validation for this time series forecasting problem.

Standard k-fold cross-validation is not appropriate for time series because it causes data leakage (future data used to predict the past).

1. Implement expanding window cross-validation (walk-forward validation):
 - Start with the first 60% of data as training
 - Predict the next 10% (first validation fold)
 - Expand training to 70%, predict the next 10% (second fold)
 - Continue until all data is used
2. Report performance metrics (MAPE, RMSE) for each fold and the overall mean ± std
3. Plot: actual vs predicted values across all folds in a single chart, with fold boundaries marked
4. Compare expanding window vs sliding window cross-validation — which gives more stable estimates for this dataset?
5. Check for temporal degradation: does model performance worsen for more recent folds? This indicates distribution shift.

Return: fold performance table, actual vs predicted plot, and degradation analysis. 
```

## When to use this prompt 
Use case 01 
The task is forecasting or any time-ordered prediction problem. 
Use case 02 
Random k-fold would leak future information. 
Use case 03 
You want expanding-window evaluation and fold-by-fold diagnostics. 
Use case 04 
You need to detect temporal degradation or distribution shift. 

## What the AI should return 

Fold-wise forecasting metrics, aggregate performance summary, an actual-versus-predicted plot with fold boundaries, and commentary on whether performance degrades in more recent periods. 

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

Once you have the first result, continue deeper with related prompts in Model Building.
