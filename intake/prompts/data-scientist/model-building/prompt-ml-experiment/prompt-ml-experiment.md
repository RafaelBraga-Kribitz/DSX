# End-to-End ML Experiment *AI Prompt *

This prompt runs a complete supervised learning experiment from definition to model card. It is useful when you want one rigorous workflow that covers preparation, selection, tuning, test evaluation, and error analysis. It supports reproducible experimentation rather than isolated notebook steps. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define the problem — target variable, problem type, evaluation metric, and business success threshold (e.g. AUC > 0.85).
Step 2: Prepare data — clean, encode, engineer features, split into train/val/test with no leakage.
Step 3: Run a model comparison with 5 algorithms, default hyperparameters, 5-fold cross-validation. Select top 2.
Step 4: Tune the top 2 models using Optuna (50 trials each). Select the winner.
Step 5: Evaluate the winning model on the held-out test set — report all metrics, confusion matrix, and calibration curve.
Step 6: Analyze errors — inspect the 20 worst-predicted examples. What do they have in common? What does this suggest about the model or data?
Step 7: Write a 1-page model card: problem, approach, final metrics, known limitations, and deployment recommendations. 
```

## When to use this prompt 
Use case 01 
You need an end-to-end project template for a full ML experiment. 
Use case 02 
The goal is to move from raw problem framing to final evaluation cleanly. 
Use case 03 
You want both model selection and post-hoc diagnosis in one flow. 
Use case 04 
You need a final artifact suitable for handoff or review. 

## What the AI should return 

A staged experiment output including problem framing, data prep, model comparison, tuning results, final test evaluation, error analysis findings, and a concise model card. 

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
