# CI/CD for ML Pipeline *AI Prompt *

This prompt designs a GitHub Actions-based CI/CD workflow for an ML project, from fast PR checks to post-merge validation and deployment gates. It is aimed at preventing broken training code, silent leakage, poor model quality, and unsafe releases. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement a CI/CD pipeline for this ML project using GitHub Actions.

1. On every pull request — fast checks (< 5 minutes):
 - Code quality: ruff lint, black format check, mypy type checking
 - Unit tests: test data preprocessing, loss functions, metrics, and model architecture
 - Smoke test: train for 2 epochs on 100 samples, assert loss decreases and model saves
 - No data leakage check: run automated leakage detection tests

2. On merge to main — extended checks (< 30 minutes):
 - Integration test: full training run on a small held-out dataset
 - Model performance gate: assert validation metric > {{min_metric_threshold}}
 - Inference test: run the exported model through the serving stack
 - Benchmark: run throughput/latency benchmark and compare to baseline

3. On new model registration — deployment checks:
 - Champion vs challenger comparison on fixed holdout set
 - Deploy to staging if challenger beats champion by > {{improvement_threshold}}%
 - Run smoke test in staging environment
 - Manual approval gate before production deployment

4. GitHub Actions workflow structure:
 - Separate workflow files for each stage
 - Cache: pip dependencies, pre-downloaded datasets for tests
 - Secrets: model registry credentials, cloud storage keys via GitHub Secrets

5. Failure handling:
 - Notify Slack channel on pipeline failure with the failing step and logs link
 - Auto-revert deployment if post-deployment canary metrics degrade

Return: GitHub Actions YAML files for each pipeline stage and a workflow diagram. 
```

## When to use this prompt 
Use case 01 
when introducing CI/CD to an ML repository on GitHub 
Use case 02 
when pull requests need code quality, unit tests, and smoke tests 
Use case 03 
when model performance and serving checks should gate merges or deployments 
Use case 04 
when staging and production promotion need manual or automated approval steps 

## What the AI should return 

GitHub Actions workflow files for PR, main-branch, and deployment stages, plus a diagram or explanation of the full CI/CD flow. 

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
