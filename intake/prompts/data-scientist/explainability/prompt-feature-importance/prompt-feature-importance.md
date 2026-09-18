# Feature Importance *AI Prompt *

This prompt provides a straightforward explanation of what features matter most and whether different importance methods agree. It is a practical first step in explainability for models that support built-in importances or can be probed with permutation tests. It also helps identify candidates for feature pruning. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Explain which features matter most to this model.

1. Extract built-in feature importances from the model (gain, split count, or permutation importance)
2. Plot a horizontal bar chart of the top 20 features, ranked by importance
3. Compute permutation importance on the validation set as a cross-check — compare to built-in importances
4. Flag any features where built-in and permutation importances disagree significantly
5. Identify features with near-zero importance in both methods — candidates for removal
6. Group features by type (original vs engineered) and show which group contributes more total importance

Return: importance table, bar chart, and a one-paragraph plain-English explanation of what the model is learning. 
```

## When to use this prompt 
Use case 01 
You need a quick interpretable summary of model drivers. 
Use case 02 
You want to compare built-in importance with permutation importance. 
Use case 03 
You suspect some engineered features may be doing little work. 
Use case 04 
You need a plain-language explanation for stakeholders. 

## What the AI should return 

An importance table, ranked feature plot, disagreement flags between methods, near-zero-importance candidates, and a plain-English summary of what the model appears to learn. 

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

Once you have the first result, continue deeper with related prompts in Explainability.
