# Calibration Analysis *AI Prompt *

This prompt checks whether predicted probabilities can be trusted as probabilities, not just rankings. It is useful for decision systems that depend on calibrated risk estimates, thresholds, or expected value calculations. The workflow compares raw and calibrated models with proper holdout discipline. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Assess and improve the probability calibration of this classification model.

1. Plot a reliability diagram (calibration curve): predicted probability vs actual fraction of positives, using 10 bins
2. Compute the Expected Calibration Error (ECE) and Maximum Calibration Error (MCE)
3. Determine if the model is overconfident (predictions too extreme) or underconfident (predictions too moderate)
4. Apply two calibration methods and compare:
 a. Platt Scaling (logistic regression on model outputs)
 b. Isotonic Regression
5. Plot calibration curves before and after each method
6. Report ECE before and after calibration

Note: calibration must be fitted on a held-out calibration set (not the training set) to avoid overfitting. 
```

## When to use this prompt 
Use case 01 
You care about probability quality, not only classification ranking. 
Use case 02 
The model will be used for thresholding, triage, or expected-cost decisions. 
Use case 03 
You want to compare Platt scaling and isotonic regression properly. 
Use case 04 
You need reliability diagrams and calibration error metrics. 

## What the AI should return 

Calibration plots before and after adjustment, ECE and MCE metrics, a statement about overconfidence or underconfidence, and a recommendation on whether calibration should be applied in production. 

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
