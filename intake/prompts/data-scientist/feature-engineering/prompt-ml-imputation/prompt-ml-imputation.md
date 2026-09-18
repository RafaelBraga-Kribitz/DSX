# Missing Value Imputation for ML *AI Prompt *

This prompt compares several imputation strategies specifically for machine learning use, not just data cleaning. It is helpful when missingness may itself be informative and the best imputation approach is not obvious. The masking evaluation adds evidence instead of relying on intuition alone. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement missing value imputation for machine learning on this dataset.

1. Profile missing values: count, percentage, and missingness pattern (MCAR, MAR, or MNAR) for each column
2. Implement and compare three imputation strategies:
 a. Simple imputation: median for numeric, mode for categorical
 b. KNN imputation: k=5 nearest neighbors based on complete features
 c. Iterative imputation (MICE): model each feature as a function of others, iterate until convergence
3. Evaluate each strategy by: artificially masking 10% of known values and measuring reconstruction error (RMSE)
4. Add missingness indicator columns (is_missing_[col]) for columns with more than 5% missing — these can be predictive features
5. Always fit imputation on training data only, then apply to validation and test sets

Return: comparison table of imputation strategies, code for the best strategy, and list of missingness indicator columns created. 
```

## When to use this prompt 
Use case 01 
Missing values are common enough to affect model quality. 
Use case 02 
You want to compare simple and advanced imputation methods empirically. 
Use case 03 
Missingness indicators may carry signal. 
Use case 04 
You need train-only fitting to avoid leakage into validation or test data. 

## What the AI should return 

A missingness profile, comparison of imputation strategies using reconstruction error, code for the selected method, and a list of any missingness indicator features created. 

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
