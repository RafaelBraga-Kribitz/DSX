# Learning Curve Analysis *AI Prompt *

This prompt shows whether the model is limited by data, model complexity, or both. It is valuable when you need to decide whether to collect more data, regularize, or redesign features. Learning curves provide a practical diagnosis of overfitting versus underfitting. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate and interpret learning curves for this model.

1. Train the model on increasing fractions of the training data: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
2. For each fraction, record: training score and cross-validated validation score
3. Plot both curves on the same chart with the x-axis as training set size
4. Interpret the curves:
 - If training score >> validation score: overfitting → more data or regularization needed
 - If both scores are low and converged: underfitting → more complex model or better features needed
 - If validation score is still increasing at 100% data: adding more training data would help
5. Estimate: how much more data would be needed to close the train/val gap?

Return the learning curve plot and a 3-sentence diagnosis of the model's current state. 
```

## When to use this prompt 
Use case 01 
You are unsure whether the model needs more data or a different architecture. 
Use case 02 
Train and validation scores tell conflicting stories. 
Use case 03 
You want visual evidence of underfitting or overfitting. 
Use case 04 
You need guidance on whether additional training data would help. 

## What the AI should return 

A learning-curve plot, training and validation scores across dataset sizes, and a short diagnosis of the model's current bias-variance state with next-step guidance. 

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
