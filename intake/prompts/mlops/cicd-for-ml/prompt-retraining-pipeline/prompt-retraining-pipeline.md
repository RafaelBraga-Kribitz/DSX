# Automated Retraining Pipeline *AI Prompt *

This prompt builds an automated retraining pipeline that responds to monitoring triggers such as drift, performance decline, new labeled data, or schedules. It is intended for teams that want retraining to be systematic, rate-limited, and connected to model registry and deployment gates. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an automated model retraining pipeline triggered by monitoring signals.

Trigger conditions (any one sufficient):
1. Performance trigger: rolling 7-day AUC drops below {{performance_threshold}}
2. Drift trigger: PSI > 0.2 on any of the top-5 most important features
3. Data volume trigger: {{new_labeled_samples}} new labeled samples accumulated since last training
4. Schedule trigger: weekly retrain regardless of performance (for models in fast-changing domains)

Pipeline steps:

1. Trigger detection job (runs daily):
 - Query monitoring database for each trigger condition
 - If any condition is met: log which trigger fired, create a retraining job request
 - Deduplication: if multiple triggers fire simultaneously, create only one retraining job
 - Rate limiting: do not trigger more than {{max_retrains_per_week}} retrains per week (prevents trigger storms)

2. Data preparation:
 - Fetch training data from the feature store: last {{training_window}} days of labeled data
 - Apply the same preprocessing pipeline as the current production model
 - Validate: training set must have ≥ {{min_training_samples}} labeled samples
 - Log dataset statistics: row count, label distribution, date range, feature means

3. Training job:
 - Use the same hyperparameters as the current production model (only data is updated)
 - Allow for hyperparameter re-search if triggered by {{hp_retune_trigger}} (e.g. monthly)
 - Track the run in the experiment tracker: link to trigger event, dataset version, git commit

4. Evaluation and gate:
 - Run the performance gate against the challenger model
 - If gate passes: register in model registry as 'Staging'
 - If gate fails: alert team, keep current production model, investigate why new data did not improve the model

5. Deployment:
 - Auto-deploy to staging environment
 - Run integration tests in staging
 - If all tests pass: auto-promote to production (or require human approval for high-stakes models)

Return: trigger detection script, pipeline orchestration code (Airflow DAG or Prefect flow), and gate integration. 
```

## When to use this prompt 
Use case 01 
when retraining should be triggered by monitoring signals instead of manual requests 
Use case 02 
when drift, performance, and data-volume triggers must be deduplicated 
Use case 03 
when retraining, evaluation, and staging promotion should be orchestrated together 
Use case 04 
when you need a DAG or flow linked to a performance gate 

## What the AI should return 

An automated retraining workflow with trigger detection, orchestration, data preparation, training, evaluation, and deployment handoff. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for ML.
