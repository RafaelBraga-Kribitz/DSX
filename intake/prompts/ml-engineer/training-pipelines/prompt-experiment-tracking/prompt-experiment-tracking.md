# Experiment Tracking Setup *AI Prompt *

This prompt integrates experiment tracking into an ML training pipeline using MLflow, Weights & Biases, or Neptune. It focuses on consistent run naming, hyperparameter logging, metric logging, artifact capture, and reproducibility metadata so experiments are easy to compare and audit. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Set up comprehensive experiment tracking for this ML training pipeline.

Use {{tracking_tool}} (MLflow / Weights & Biases / Neptune).

1. Run initialization:
 - Create a run with a descriptive name including: model architecture, dataset version, timestamp
 - Tag run with: git commit hash, environment (dev/staging/prod), dataset version

2. Hyperparameter logging:
 - Log all hyperparameters at run start: learning rate, batch size, epochs, optimizer, scheduler, architecture config
 - Log data config: train/val split, augmentations, preprocessing steps

3. Metric logging per epoch:
 - Training: loss, primary metric, learning rate, gradient norm
 - Validation: loss, primary metric, all secondary metrics
 - System: GPU memory used, step time, throughput (samples/sec)

4. Artifact logging:
 - Best model checkpoint
 - Final model checkpoint
 - Confusion matrix or prediction plots at end of training
 - Feature importance if applicable

5. Run comparison:
 - Show how to use the tracking UI to compare runs by val metric
 - Show how to retrieve the best run programmatically

6. Reproducibility:
 - Log environment: requirements.txt or conda env YAML
 - Log random seeds

Return: tracking setup code integrated into the training loop, and a run naming convention guide. 
```

## When to use this prompt 
Use case 01 
when adding systematic experiment tracking to a training pipeline 
Use case 02 
when runs need comparable metadata, metrics, and artifacts 
Use case 03 
when reproducibility requires logging seeds, environment, and dataset versions 
Use case 04 
when your team wants to compare runs and fetch the best one programmatically 

## What the AI should return 

Tracking setup code integrated into the training loop, plus a run naming convention and examples of comparing and retrieving top runs. 

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
