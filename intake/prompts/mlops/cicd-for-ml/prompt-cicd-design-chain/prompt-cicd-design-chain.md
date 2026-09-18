# CI/CD Pipeline Design Chain *AI Prompt *

This chain prompt designs the overall CI/CD architecture for an ML system, covering fast CI, extended checks, deployment automation, retraining, rollback, and documentation. It is useful when the goal is to define the full delivery lifecycle rather than a single pipeline job. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Test inventory — catalog all existing tests (unit, integration, smoke). Identify untested code paths in the preprocessing, feature engineering, training, and serving layers. Prioritize which gaps to fill first based on risk.
Step 2: CI pipeline (on every PR) — define the fast CI pipeline: linting, type checking, unit tests, smoke training test, serving health check. Target: completes in < 10 minutes. Block merge on any failure.
Step 3: Extended CI (on merge to main) — define the extended pipeline: full integration tests, performance gate against holdout set, training-serving skew check, latency benchmark. Target: completes in < 30 minutes.
Step 4: CD pipeline (on model registry promotion) — define the deployment pipeline: staging deploy, integration tests in staging, canary deployment to production (1% → 5% → 20% → 100%), automated rollback on health check failure.
Step 5: Retraining pipeline — design the automated retraining trigger, training job, evaluation gate, and staging promotion. Define the human-in-the-loop gates for high-stakes models.
Step 6: Rollback procedure — document and automate the rollback: config repo revert, GitOps reconciliation, verification that the previous model is serving. Target: rollback executable by any on-call engineer in < 5 minutes.
Step 7: Pipeline documentation — write the CI/CD runbook: what each pipeline stage does, how to debug a failing stage, how to manually trigger or skip a stage, and who to escalate to when the pipeline is broken. 
```

## When to use this prompt 
Use case 01 
when an ML team needs a complete CI/CD blueprint 
Use case 02 
when testing, deployment, retraining, and rollback should be designed together 
Use case 03 
when pipeline stages must be prioritized by runtime and risk 
Use case 04 
when operational documentation is part of the delivery process 

## What the AI should return 

A staged CI/CD design covering PR checks, merge-time checks, deployment workflow, retraining flow, rollback automation, and runbook documentation. 

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
