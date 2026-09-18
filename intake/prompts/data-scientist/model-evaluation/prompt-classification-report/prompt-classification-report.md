# Classification Report *AI Prompt *

This prompt produces a full evaluation package for a classification model, not just one headline metric. It is useful when threshold choice, trade-offs between precision and recall, and class-specific behavior matter. The output is meant to support model review and decision-making. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Produce a comprehensive evaluation report for this classification model.

1. Compute and display the full classification report: precision, recall, F1-score, and support for each class
2. Plot the confusion matrix as a heatmap — show both counts and percentages
3. Plot the ROC curve with AUC value (for binary classification)
4. Plot the Precision-Recall curve with Average Precision score
5. Find the optimal classification threshold using:
 - F1 maximization
 - Youden's J statistic (max sensitivity + specificity - 1)
6. Show how precision, recall, and F1 change across threshold values (threshold plot)

Interpret: which class is hardest to predict? What type of error is more costly in this business context? 
```

## When to use this prompt 
Use case 01 
You need a thorough classification evaluation beyond accuracy alone. 
Use case 02 
Threshold selection is an important business decision. 
Use case 03 
You want confusion matrix, ROC, PR, and threshold analysis together. 
Use case 04 
You need to explain which error type matters most in context. 

## What the AI should return 

A complete classification report, plots for confusion matrix and discrimination performance, threshold analysis, and an interpretation of the hardest class and most costly error trade-off. 

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
