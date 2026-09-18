# Training Pipeline as Code *AI Prompt *

This prompt refactors an ad-hoc training script into a reproducible pipeline with configuration management, stage separation, artifact versioning, and a CLI. It is useful when a one-off training file has grown into something that needs repeatable execution and maintenance. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Refactor this ad-hoc training script into a reproducible, configurable ML pipeline.

1. Configuration management:
 - Move all hyperparameters and paths to a config file (YAML or JSON)
 - Use OmegaConf or Hydra for hierarchical config with command-line overrides
 - Never hardcode paths — all paths are config variables with sensible defaults
 - Log the full resolved config at the start of every run

2. Pipeline stages as separate functions or classes:
 - data_preprocessing(): validate, clean, and split data
 - train(): train model with given config
 - evaluate(): evaluate on test set and return metrics dict
 - export(): save model in deployment format
 - Each stage is independently runnable and testable

3. Artifact management:
 - Every run saves to a versioned output directory: outputs/{run_id}/
 - Artifacts: model checkpoint, config copy, metrics JSON, training plots
 - Symlink outputs/latest → most recent run for convenience

4. CLI interface:
 - python train.py --config configs/base.yaml --overrides learning_rate=1e-4
 - Subcommands: train, evaluate, export, full (all stages)

5. Dependency management:
 - requirements.txt with pinned versions
 - Optional: pyproject.toml with extras for training vs inference

6. Entry point guard:
 - All DataLoader workers require if __name__ == '__main__': guard on Windows

Return: refactored pipeline structure, Hydra config setup, and CLI interface. 
```

## When to use this prompt 
Use case 01 
when a training script has become too hardcoded or difficult to reproduce 
Use case 02 
when config files and command-line overrides are needed 
Use case 03 
when preprocessing, training, evaluation, and export should be separate stages 
Use case 04 
when each run should save versioned artifacts in a predictable structure 

## What the AI should return 

A refactored ML pipeline structure with Hydra or OmegaConf config, CLI commands, stage functions, and artifact management conventions. 

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

Once you have the first result, continue deeper with related prompts in MLOps and CI/CD.
