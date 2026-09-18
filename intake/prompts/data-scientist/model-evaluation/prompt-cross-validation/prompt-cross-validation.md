# Cross-Validation Deep Dive *AI Prompt *

This prompt stress-tests performance estimates across multiple cross-validation schemes. It is useful when you want to understand score stability and whether a single CV result is overly optimistic or noisy. It also helps explain discrepancies between CV and test performance. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Run a rigorous cross-validation analysis for this model.

1. Evaluate using 5-fold, 10-fold, and stratified 5-fold cross-validation
2. For each fold strategy, report: mean score, std, min, max across folds
3. Plot fold scores as a box plot to visualize variance across folds
4. Run repeated k-fold (5-fold × 3 repeats) to get a more stable estimate
5. Check for fold-to-fold variance — high variance suggests the model is sensitive to the training data composition
6. Compare cross-validated score vs test set score — are they consistent?

If the cross-validated score and test score diverge by more than 5%, investigate potential causes: data leakage, distribution shift, or overfitting. 
```

## When to use this prompt 
Use case 01 
You want more confidence in evaluation than one split can provide. 
Use case 02 
You suspect score variance may depend on fold strategy. 
Use case 03 
You need repeated CV to stabilize estimates. 
Use case 04 
You want to investigate differences between CV and test outcomes. 

## What the AI should return 

A comparison of fold strategies with mean, spread, and extrema, variance visualizations, repeated-CV results, and a diagnosis if cross-validation and test scores disagree materially. 

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

Once you have the first result, continue deeper with related prompts in Model Evaluation.
