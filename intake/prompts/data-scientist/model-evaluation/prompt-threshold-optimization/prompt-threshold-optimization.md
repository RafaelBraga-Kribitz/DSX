# Threshold Optimization *AI Prompt *

This prompt chooses a classification threshold based on explicit business objectives rather than the default 0.5 cutoff. It is useful when recall floors, precision targets, or asymmetric costs drive operational decisions. The result makes threshold choice transparent and defensible. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Find the optimal classification threshold for this model given the business context.

1. Generate predicted probabilities for the validation set
2. Evaluate performance across all thresholds from 0.01 to 0.99 (step 0.01):
 - Precision, Recall, F1, FPR, TPR at each threshold
3. Plot the threshold vs each metric curve
4. Identify the optimal threshold for three different objectives:
 a. Maximize F1-score
 b. Maximize precision while keeping recall ≥ {{min_recall}}
 c. Minimize total cost given: FP cost = {{fp_cost}}, FN cost = {{fn_cost}}
5. Show the confusion matrix at each of the three optimal thresholds
6. Recommend the final threshold with a business justification

Return: threshold analysis table, metric curves plot, 3 confusion matrices, and final recommendation. 
```

## When to use this prompt 
Use case 01 
The default probability threshold is unlikely to be optimal. 
Use case 02 
Business rules impose recall or cost constraints. 
Use case 03 
You want to compare several threshold objectives side by side. 
Use case 04 
Stakeholders need confusion matrices at meaningful operating points. 

## What the AI should return 

A threshold performance table, metric-versus-threshold curves, confusion matrices for the selected operating points, and a final threshold recommendation tied to business goals. 

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
