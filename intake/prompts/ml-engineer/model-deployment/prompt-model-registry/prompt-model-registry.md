# Model Versioning and Registry *AI Prompt *

This prompt designs a model versioning and governance workflow around MLflow Model Registry. It covers model registration, lifecycle stages, production loading by stage, promotion checks, and rollback procedures for safer model operations. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement a model versioning and registry system using MLflow Model Registry.

1. Model registration:
 - Log model with mlflow.pytorch.log_model (or sklearn/tensorflow)
 - Include: model signature (input/output schema), input example, pip requirements
 - Auto-register to registry after training if val metric exceeds threshold
 - Tag with: git_commit, training_run_id, dataset_version, framework_version

2. Model stages lifecycle:
 - Staging: newly registered models under evaluation
 - Production: models approved for serving
 - Archived: deprecated models (never delete, keep for audit)
 - Implement promotion workflow: Staging → Production requires approval + performance check

3. Model loading for inference:
 - Load by stage (always load 'Production') not by version number
 - Implement a model loader class with caching: reload only when registry version changes
 - Graceful fallback: if Production model fails to load, fall back to last known good version

4. Model comparison before promotion:
 - Load challenger (Staging) and champion (Production) models
 - Evaluate both on a fixed holdout set
 - Promote challenger only if it improves primary metric by > {{threshold}}% with no guardrail degradation

5. Rollback procedure:
 - Script to demote current Production model and promote previous version
 - Alert system when a rollback is triggered

Return: registry integration code, promotion workflow script, and rollback procedure. 
```

## When to use this prompt 
Use case 01 
when introducing formal model versioning and promotion workflows 
Use case 02 
when production systems should load models by stage rather than version id 
Use case 03 
when registry-based rollback and auditability are required 
Use case 04 
when champion-challenger comparison should gate promotion 

## What the AI should return 

Registry integration code, promotion workflow logic, and a rollback procedure for MLflow-based model lifecycle management. 

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

Once you have the first result, continue deeper with related prompts in Model Deployment.
