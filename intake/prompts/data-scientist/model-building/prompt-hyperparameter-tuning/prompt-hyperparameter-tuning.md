# Hyperparameter Tuning *AI Prompt *

This prompt runs systematic hyperparameter optimization instead of manual guesswork. It is most useful after a promising model family has been identified and you want measurable gains from tuning. The workflow emphasizes Bayesian search, reproducibility, and comparison to defaults. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Tune the hyperparameters of this model to maximize performance on {{target_variable}}.

Model to tune: {{model_type}} (e.g. LightGBM, XGBoost, Random Forest)

Approach:
1. Define the hyperparameter search space:
 - For tree models: n_estimators, max_depth, learning_rate, min_child_samples, subsample, colsample_bytree, reg_alpha, reg_lambda
 - For linear models: C, penalty, solver
2. Use Optuna (Bayesian optimization) with 100 trials
3. Evaluate each trial with 5-fold cross-validation
4. Plot the optimization history: score vs trial number
5. Report the best hyperparameters and best cross-validated score
6. Compare: default params vs tuned params — how much did tuning improve performance?

Return: best params dict, improvement table, and training code using the best params. 
```

## When to use this prompt 
Use case 01 
You already have a candidate model worth tuning seriously. 
Use case 02 
Manual parameter tweaking is too slow or inconsistent. 
Use case 03 
You want Optuna-based search with cross-validation and clear reporting. 
Use case 04 
You need proof that tuning improved performance versus defaults. 

## What the AI should return 

The best parameter set, optimization history summary, comparison of tuned versus default performance, and clean training code using the selected hyperparameters. 

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
