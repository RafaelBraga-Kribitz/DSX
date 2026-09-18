# Overfitting Diagnosis *AI Prompt *

This prompt diagnoses whether a model is memorizing training data more than it generalizes. It is useful when train metrics look strong but validation performance disappoints. The output compares regularization and simplification strategies in a structured way rather than relying on one fix. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and fix overfitting in this machine learning model.

1. Measure the overfitting gap: training score vs validation score. A gap > 5% is a concern.
2. Plot learning curves to confirm overfitting (training score high, validation score lower and not converging)
3. Test regularization techniques in order of invasiveness:
 a. Increase regularization parameters (L1, L2 penalty, or min_child_samples for trees)
 b. Reduce model complexity (max_depth, n_estimators, hidden layer size)
 c. Add dropout (neural networks) or feature subsampling (trees)
 d. Reduce the feature set — remove low-importance features that may add noise
 e. Get more training data if available
4. For each technique, report: training score, validation score, and overfitting gap
5. Select the technique that minimizes the overfitting gap with the smallest validation score sacrifice

Return: overfitting diagnosis, regularization comparison table, and final recommended configuration. 
```

## When to use this prompt 
Use case 01 
There is a noticeable gap between training and validation performance. 
Use case 02 
You want evidence-based overfitting diagnosis rather than guesswork. 
Use case 03 
Several regularization options need to be compared systematically. 
Use case 04 
You need a final recommendation that balances generalization and accuracy. 

## What the AI should return 

An overfitting diagnosis, learning-curve evidence, comparison table for each mitigation tested, and a recommended configuration that reduces the gap with minimal loss in validation score. 

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
