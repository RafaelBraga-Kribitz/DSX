# Multi-Task Training *AI Prompt *

This prompt creates a multi-task learning setup with a shared backbone, task-specific heads, multiple loss-weighting strategies, and gradient conflict mitigation. It is useful when one model must optimize more than one objective without one task overwhelming the other. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a multi-task learning training setup for a model that simultaneously optimizes {{task_1}} and {{task_2}}.

1. Model architecture:
 - Shared backbone: {{backbone}} that extracts shared representations
 - Task-specific heads: separate output heads for each task
 - Gradient isolation: ensure gradients from one task head do not corrupt features needed by another

2. Loss combination strategies — implement and compare:
 a. Fixed weighting: total_loss = w1 × loss_1 + w2 × loss_2
 b. Uncertainty weighting (Kendall et al. 2018): learn task weights as trainable parameters based on homoscedastic uncertainty
 c. GradNorm (Chen et al. 2018): dynamically adjust weights based on relative gradient magnitudes

3. Task imbalance handling:
 - Normalize each task loss to similar scale before combining
 - Monitor per-task gradient norms — large imbalance indicates weighting issues

4. Training strategy:
 - Option A: alternate between tasks each batch
 - Option B: sample tasks proportionally by dataset size
 - Option C: train all tasks simultaneously in each batch

5. Evaluation:
 - Log per-task metrics separately during validation
 - Use a combined score (e.g. average of normalized per-task metrics) to select the best checkpoint

6. Gradient surgery: implement PCGrad to project conflicting gradients to prevent task interference

Return: multi-task model code, loss combination implementations, and training loop with per-task logging. 
```

## When to use this prompt 
Use case 01 
when training a single model for two related tasks 
Use case 02 
when task losses need fixed, learned, or gradient-based weighting 
Use case 03 
when you want per-task metrics and checkpoint selection logic 
Use case 04 
when gradient interference between tasks is a concern 

## What the AI should return 

Multi-task model code, loss combination implementations, gradient conflict handling, and a training loop with per-task logging and evaluation. 

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
