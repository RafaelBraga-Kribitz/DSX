# AutoML Benchmark *AI Prompt *

This prompt benchmarks AutoML against manual baselines to see whether automated search is adding real value. It is especially useful when you want a quick but serious search over model families and hyperparameters without abandoning interpretability. The output also helps decide whether to continue manual optimization. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Run an AutoML benchmark on this dataset to find the best model for predicting {{target_variable}}.

1. Run MLJAR AutoML with mode='Compete' for 60 minutes on the training set
2. Evaluate using 5-fold cross-validation with {{primary_metric}} as the optimization target
3. Report the top 5 models found by AutoML: algorithm, hyperparameters, CV score, training time
4. Compare AutoML's best model against manually built baselines (Logistic Regression, Random Forest with defaults)
5. Extract the best model's feature importances and compare to manual feature selection
6. Report: what type of model won? What hyperparameter ranges worked best? What did AutoML find that manual search missed?

Return the leaderboard table, best model details, and a recommendation on whether to use the AutoML model or continue manual optimization. 
```

## When to use this prompt 
Use case 01 
You want a fast benchmark of what AutoML can achieve on the problem. 
Use case 02 
You need to compare automated search against hand-built baselines fairly. 
Use case 03 
You want to learn which model families and parameter regions perform best. 
Use case 04 
You need a recommendation on whether AutoML is enough for this stage. 

## What the AI should return 

An AutoML leaderboard, details of the best model and its hyperparameters, comparison to manual baselines, feature-importance notes, and a recommendation on whether to deploy or continue manual work. 

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
