# Model Registry Workflow *AI Prompt *

This prompt designs a full model registry workflow including registration metadata, stage transitions, approvals, serving-time loading, and audit reporting. It is useful when the registry is the backbone of model lifecycle management across training and production. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the complete model lifecycle workflow using a model registry.

Registry: {{registry_tool}} (MLflow / SageMaker Model Registry / Vertex AI Model Registry)

1. Model registration (triggered after successful training run):
 - Register model only if performance gate passes
 - Required metadata at registration:
 - model_version (auto-incremented)
 - training_run_id (link to experiment tracker)
 - git_commit_hash (reproducibility)
 - dataset_version (which data was used)
 - evaluation_metrics (all performance metrics on holdout set)
 - model_signature (input/output schema)
 - dependencies (requirements.txt snapshot)
 - tags: model_family, use_case, owner_team

2. Stage transitions:
 - None → Staging: automatic after registration + gate pass
 - Staging → Production: requires human approval + integration test pass in staging
 - Production → Archived: when replaced by a newer version
 - Never delete versions — only archive

3. Approval workflow for Staging → Production:
 - Approver must be a senior ML engineer or ML team lead (not the model's author)
 - Approval checklist: performance gate results, canary test results, monitoring setup verified, runbook updated
 - Approval is recorded in the registry with approver identity and timestamp
 - Approval expires after {{approval_expiry}} hours — stale approvals require re-approval

4. Model loading at serving time:
 - Always load by stage ('Production'), never by version number
 - Cache the loaded model in memory, poll the registry every {{poll_interval}} seconds for version changes
 - On version change: load new model in parallel, switch traffic only after new model is warmed up
 - Graceful switch: in-flight requests complete on the old model, new requests go to the new model

5. Audit and compliance:
 - All stage transitions logged with: who, when, why, and from/to version
 - Monthly audit report: models promoted, models rolled back, approval SLA compliance

Return: registration code, stage transition automation, approval workflow, and serving-side model loader with polling. 
```

## When to use this prompt 
Use case 01 
when a model registry should control promotion from training to production 
Use case 02 
when stage transitions need human approvals and auditability 
Use case 03 
when serving systems must hot-swap models by stage rather than version 
Use case 04 
when lifecycle governance and operational loading logic need one design 

## What the AI should return 

A registry-centered lifecycle workflow with registration code, stage automation, approval process, and a serving-side loader with version polling. 

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
