# Model Comparison *AI Prompt *

This prompt compares several common algorithm families on equal footing. It is useful when you want to identify strong candidates before investing in tuning or ensembling. It also adds operational context through training time, inference speed, and memory usage. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Train and compare multiple candidate models for predicting {{target_variable}}.

Train these models with default hyperparameters:
1. Logistic Regression / Linear Regression
2. Random Forest (n_estimators=200)
3. Gradient Boosting — XGBoost or LightGBM
4. Support Vector Machine (RBF kernel, scaled features)
5. k-Nearest Neighbors (k=10)

For each model:
- 5-fold cross-validated score (mean ± std)
- Training time
- Inference time per 1000 rows
- Memory usage

Return a ranked comparison table.
Recommend the top 2 models to take forward for hyperparameter tuning, with justification.
Flag any model that is significantly overfitting (train score >> validation score). 
```

## When to use this prompt 
Use case 01 
You want to shortlist promising algorithms for a supervised problem. 
Use case 02 
You need more than one metric and care about runtime or memory too. 
Use case 03 
You want cross-validated evidence before tuning models. 
Use case 04 
You need to spot overfitting early across several model families. 

## What the AI should return 

A ranked comparison table across all candidate models with cross-validated performance, variance, training cost, inference speed, memory usage, and a recommendation of the top two models to tune further. 

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
