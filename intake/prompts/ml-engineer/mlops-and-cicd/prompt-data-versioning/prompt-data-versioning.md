# Data Versioning with DVC *AI Prompt *

This prompt introduces DVC-based data versioning and pipeline tracking for an ML project. It covers remote storage, tracked datasets, stage definitions, experiments, metrics, and CI integration so data and pipeline state remain reproducible over time. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Set up data versioning and pipeline tracking for this ML project using DVC.

1. DVC initialization:
 - dvc init in the Git repository
 - Configure remote storage: S3, GCS, or Azure Blob
 - .dvcignore file for files to exclude

2. Data versioning:
 - Track large data files and directories: dvc add data/raw/
 - Commit .dvc files to Git, push data to remote: dvc push
 - Retrieve a specific data version: git checkout {commit} && dvc pull
 - List data versions and their Git commits for audit trail

3. DVC pipeline definition (dvc.yaml):
 - Define pipeline stages: preprocess → train → evaluate
 - For each stage: deps (inputs), outs (outputs), params (config values), metrics (metrics.json)
 - Cache: DVC caches stage outputs — skips re-running unchanged stages
 - Run the pipeline: dvc repro

4. Experiment tracking:
 - dvc exp run for tracking experiments with different params
 - dvc exp show to compare experiments in a table
 - dvc exp branch to create a Git branch from a promising experiment

5. Metrics and params tracking:
 - Save metrics as JSON: accuracy, loss, etc.
 - dvc metrics show, dvc metrics diff to compare across commits
 - dvc params diff to see which params changed between runs

6. CI/CD integration:
 - dvc pull in CI before running tests
 - dvc repro in CI to re-run the pipeline if deps changed
 - dvc push in CI to save new data artifacts after processing

Return: dvc.yaml pipeline definition, Git workflow for data versioning, and CI/CD integration. 
```

## When to use this prompt 
Use case 01 
when large datasets should be versioned alongside code without storing them in Git 
Use case 02 
when preprocessing, training, and evaluation should be defined as reproducible stages 
Use case 03 
when experiment comparison should include params and metrics in version control 
Use case 04 
when CI should be able to pull data and reproduce the pipeline 

## What the AI should return 

A DVC setup including dvc.yaml stages, data versioning workflow, experiment commands, and CI integration guidance. 

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
