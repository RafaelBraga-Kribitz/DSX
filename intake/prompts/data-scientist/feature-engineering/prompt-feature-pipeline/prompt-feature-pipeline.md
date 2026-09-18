# Full Feature Pipeline Chain *AI Prompt *

This prompt designs a full feature pipeline from profiling through selection. It is useful when you want a disciplined end-to-end approach instead of ad hoc transformations. The chain connects cleaning, encoding, feature creation, leakage checks, and importance-based pruning into one workflow. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Profile the raw features — types, missing rates, cardinality, correlation with {{target_variable}}. Identify the weakest features (near-zero variance, low target correlation).
Step 2: Clean and encode — impute missing values, encode categoricals (ordinal for low-cardinality, target encoding for high-cardinality), scale numerics.
Step 3: Engineer new features — create interaction features, lag features if time-ordered, group aggregations, and domain-specific features based on the dataset context.
Step 4: Select features — use SHAP values from a quick LightGBM model to rank all features. Drop features with SHAP importance below a threshold.
Step 5: Check for leakage — verify no feature uses future information. Check correlation of each feature with the target is not suspiciously perfect (>0.95).
Step 6: Output a final feature list with: name, description, type, importance rank, and the code to reproduce it end-to-end. 
```

## When to use this prompt 
Use case 01 
You want a full feature engineering workflow rather than a single technique. 
Use case 02 
The project is advanced enough to justify ranking and pruning engineered features. 
Use case 03 
You need to combine profiling, encoding, creation, and SHAP-based selection. 
Use case 04 
You want a final reproducible feature list with traceability. 

## What the AI should return 

A staged pipeline output covering profiling findings, cleaning and encoding choices, engineered features, leakage checks, SHAP-based ranking, and a final reproducible feature catalog with descriptions and importance ranks. 

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
