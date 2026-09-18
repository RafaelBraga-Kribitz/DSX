# Class Imbalance Handling *AI Prompt *

This prompt tackles classification problems where the minority class matters more than raw accuracy. It compares common resampling and weighting approaches under a consistent evaluation setup. The goal is to choose the strategy that aligns best with both data imbalance and business costs. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Handle class imbalance in this classification dataset where {{minority_class}} is the minority class.

1. First, quantify the imbalance: ratio of majority to minority class
2. Explain why accuracy is a misleading metric for this problem
3. Implement and compare four strategies:
 a. Class weight adjustment (class_weight='balanced' in sklearn)
 b. Random oversampling of the minority class (RandomOverSampler)
 c. SMOTE — Synthetic Minority Oversampling Technique
 d. Undersampling the majority class (RandomUnderSampler)
4. For each strategy, train a LightGBM model and evaluate using: AUC-ROC, Precision, Recall, F1, and the confusion matrix
5. Recommend the best strategy for this specific imbalance ratio and business context

Note: apply all resampling only to the training set, never to validation or test sets. 
```

## When to use this prompt 
Use case 01 
The target classes are substantially imbalanced. 
Use case 02 
Accuracy alone would hide poor minority-class detection. 
Use case 03 
You want to compare weighting, oversampling, SMOTE, and undersampling side by side. 
Use case 04 
You need a recommendation grounded in metrics and practical trade-offs. 

## What the AI should return 

An imbalance diagnosis, side-by-side evaluation of each handling strategy, confusion matrices and key classification metrics, and a recommendation for the best approach for the given problem context. 

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
