# Baseline Model *AI Prompt *

This prompt establishes honest baseline performance before more complex modeling begins. It is useful because many projects jump straight to sophisticated algorithms without proving that they beat trivial or simple alternatives. The prompt helps define the minimum bar a useful model must clear. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build baseline models for predicting {{target_variable}} in this dataset.

1. Determine the problem type: binary classification, multiclass classification, or regression
2. Choose the correct evaluation metric: AUC-ROC for binary, accuracy/F1 for multiclass, RMSE/MAE for regression
3. Build a naive baseline first:
 - Regression: predict the training set mean for all observations
 - Classification: predict the majority class for all observations
4. Build two simple baselines: Logistic Regression (or Linear Regression) and a Decision Tree with max_depth=3
5. Evaluate all three on a held-out validation set (20% split, stratified for classification)

Return a comparison table: model | train score | validation score | fit time
Identify which baseline to beat before calling any model 'useful'. 
```

## When to use this prompt 
Use case 01 
You are starting a modeling project and need credible baselines. 
Use case 02 
You want to verify the problem type and evaluation metric first. 
Use case 03 
You need a naive benchmark and a couple of simple ML baselines. 
Use case 04 
You want a clean table showing what future models must outperform. 

## What the AI should return 

A comparison table for naive and simple baseline models including train score, validation score, and fit time, plus a short recommendation on the baseline threshold any serious model should beat. 

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
