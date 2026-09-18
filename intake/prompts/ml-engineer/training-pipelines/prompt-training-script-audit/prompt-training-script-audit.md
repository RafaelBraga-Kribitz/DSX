# Training Script Audit *AI Prompt *

This prompt reviews an ML training script for correctness, reproducibility, evaluation integrity, and operational training hygiene. It is useful for catching common but costly issues such as data leakage, nondeterministic splits, weak validation setup, and inefficient training defaults before a model is trusted or scaled. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit this ML training script for correctness and best practices.

Check for the following issues and flag each as Critical / Warning / Info:

1. Data leakage:
 - Is preprocessing (scaling, encoding, imputation) fitted on training data only, then applied to val/test?
 - Are any features derived from the target variable?
 - For time series: is there any forward-looking data in the features?

2. Reproducibility:
 - Are random seeds set for: Python random, NumPy, PyTorch/TensorFlow, and CUDA?
 - Is the dataset split deterministic?

3. Evaluation correctness:
 - Is the evaluation metric appropriate for the problem type and class imbalance?
 - Is evaluation done on a truly held-out set, never used during training or tuning?

4. Training hygiene:
 - Is learning rate scheduling used?
 - Is gradient clipping applied for RNNs or transformers?
 - Are validation metrics logged per epoch, not just at the end?

5. Resource efficiency:
 - Is DataLoader using num_workers > 0 and pin_memory=True?
 - Is mixed precision (torch.cuda.amp) enabled?
 - Are unused tensors detached from the computation graph during validation?

Return: issue list with severity, line references where possible, and fix recommendations. 
```

## When to use this prompt 
Use case 01 
when you want a structured audit of a PyTorch or TensorFlow training script 
Use case 02 
when you suspect leakage, reproducibility gaps, or incorrect evaluation logic 
Use case 03 
when preparing a training pipeline for code review or productionization 
Use case 04 
when you need issue severity, line references, and concrete fixes 

## What the AI should return 

An audit report listing critical, warning, and info issues in the training script, with line references where possible and recommended fixes. 

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

Once you have the first result, continue deeper with related prompts in Training Pipelines.
