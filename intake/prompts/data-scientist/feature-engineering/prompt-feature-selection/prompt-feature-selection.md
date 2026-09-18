# Feature Selection *AI Prompt *

This prompt compares several feature selection philosophies to identify a smaller and more robust predictor set. It is useful when the raw feature space is large or when you need stability rather than one lucky importance ranking. The final recommendation rewards agreement across multiple methods. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Select the optimal feature subset for predicting {{target_variable}}.

Run four feature selection methods and compare their results:

1. Filter method: correlation with target (keep features with |r| > 0.05)
2. Wrapper method: Recursive Feature Elimination (RFE) with a Random Forest estimator, 5-fold CV
3. Embedded method: SHAP values from a LightGBM model — keep top features by mean |SHAP|
4. Stability method: run SHAP selection 5 times with different random seeds — keep only features that appear in all 5 runs (stable features)

Compare: how many features does each method select? How much do the selected sets overlap?

Final recommendation: the intersection of features selected by at least 3 of the 4 methods.

Return: selected feature list, overlap Venn diagram, and CV performance with all features vs selected features. 
```

## When to use this prompt 
Use case 01 
You want to reduce feature count without sacrificing much performance. 
Use case 02 
The current feature space may be noisy, redundant, or unstable. 
Use case 03 
You want to compare filter, wrapper, embedded, and stability methods. 
Use case 04 
You need evidence that the selected subset generalizes well. 

## What the AI should return 

Selected feature sets from each method, overlap analysis, a final recommended subset, and performance comparison of using all features versus the chosen reduced set. 

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
