# Interaction Features *AI Prompt *

This prompt searches for pairwise feature interactions that add predictive value beyond the original variables. It is useful when the target may depend on combinations, contrasts, or ratios rather than single features alone. The output focuses on interactions that are both meaningful and not excessively redundant. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate and evaluate interaction features between the most important variables in this dataset.

1. Identify the top 6 numeric features by correlation with {{target_variable}}
2. Create all pairwise interactions between them:
 - Multiplication: feature_a × feature_b
 - Ratio: feature_a / (feature_b + epsilon)
 - Difference: feature_a - feature_b
3. For each interaction feature, compute its correlation with {{target_variable}}
4. Keep only interaction features with |r| > 0.05 with the target and that outperform their parent features
5. Check for multicollinearity between interaction features and parents

Return the top 10 interaction features ranked by correlation with the target, with code to create them. 
```

## When to use this prompt 
Use case 01 
You suspect interactions matter more than single raw variables. 
Use case 02 
You want to test multiplicative, ratio, and difference features systematically. 
Use case 03 
You need a quick way to rank interactions by relationship to the target. 
Use case 04 
You want to avoid keeping noisy interactions that only add multicollinearity. 

## What the AI should return 

A ranked shortlist of the top interaction features, their target correlations, screening logic used to keep or discard them, multicollinearity notes, and code to recreate the selected interactions. 

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
