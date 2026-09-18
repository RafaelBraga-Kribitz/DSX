# Target Encoding *AI Prompt *

This prompt applies target encoding to categorical variables with many levels while guarding against leakage. It is designed for cases where one-hot encoding would explode dimensionality or lose useful target signal. The emphasis is on out-of-fold encoding, smoothing, and safe inference-time handling. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply target encoding to the high-cardinality categorical columns in this dataset for predicting {{target_variable}}.

For each high-cardinality categorical column (more than 10 unique values):
1. Compute the mean of {{target_variable}} per category value
2. Apply smoothing to avoid overfitting on rare categories: smoothed_mean = (n × category_mean + m × global_mean) / (n + m) where m = smoothing_factor (default 10)
3. Handle unseen categories at inference time by defaulting to the global mean
4. Use 5-fold out-of-fold encoding to prevent target leakage on the training set

Return:
- The encoded features as new columns (keep originals)
- A table showing the top 10 and bottom 10 category values for each encoded column
- Code to apply the same encoding to a test set without leakage 
```

## When to use this prompt 
Use case 01 
You have high-cardinality categoricals such as user_id, product_code, or city. 
Use case 02 
One-hot encoding is too sparse or too wide for the problem. 
Use case 03 
You want a leakage-aware target encoding workflow for training and inference. 
Use case 04 
You need interpretable summaries of which categories map to high or low target values. 

## What the AI should return 

Leakage-safe encoded columns, out-of-fold training logic, test-set application code, and summary tables showing the strongest and weakest encoded category values for each transformed feature. 

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
