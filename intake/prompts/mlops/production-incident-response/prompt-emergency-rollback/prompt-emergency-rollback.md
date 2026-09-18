# Emergency Rollback Procedure *AI Prompt *

This prompt designs fast rollback options for model registry, Kubernetes deployments, and traffic-routing based releases, along with verification and drills. It is best when production rollback must be reliable, fast, and executable under pressure. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement a fast, reliable emergency rollback procedure for production ML models.

Target: complete rollback in < 5 minutes from decision to previous version serving traffic.

1. Pre-conditions for rollback:
 - Rollback is appropriate when: model is causing user-facing errors, model is producing obviously wrong predictions, or model is degrading a critical business metric
 - Rollback is NOT appropriate when: drift is detected but predictions are technically correct, a gradual performance decline is ongoing (investigate first)

2. Rollback implementation options (fastest to slowest):

 Option A — Model registry rollback (< 2 minutes):
 - Demote the current Production model version to Archived
 - Promote the previous version back to Production
 - Serving pods detect the version change via polling and hot-swap the model
 - No pod restart required
 ```
 mlflow_client.transition_model_version_stage(name='{{model_name}}', version='{{current_version}}', stage='Archived')
 mlflow_client.transition_model_version_stage(name='{{model_name}}', version='{{previous_version}}', stage='Production')
 ```

 Option B — Kubernetes deployment rollback (< 3 minutes):
 - kubectl rollout undo deployment/{{deployment_name}} -n {{namespace}}
 - Verify: kubectl rollout status deployment/{{deployment_name}}

 Option C — Traffic routing rollback (< 1 minute):
 - If A/B deployment is active: set challenger traffic weight to 0%
 - Only works if champion model is still deployed and healthy

3. Rollback verification checklist:
 - [ ] Error rate returned to pre-incident baseline
 - [ ] Latency p99 returned to pre-incident baseline
 - [ ] Prediction distribution matches pre-incident baseline
 - [ ] Confirm which model version is now serving
 - [ ] Downstream systems have recovered

4. Post-rollback actions:
 - Create a post-mortem ticket with: incident timeline, rollback trigger, business impact
 - Lock the rolled-back version to prevent automatic re-deployment
 - Do not re-deploy the same version without fixing the root cause

5. Rollback drill:
 - Conduct a rollback drill quarterly in staging to verify the procedure works and engineers are familiar with it

Return: rollback scripts for all three options, verification checklist, post-rollback action template, and drill procedure. 
```

## When to use this prompt 
Use case 01 
when production model rollback must complete within minutes 
Use case 02 
when multiple rollback mechanisms should be documented and automated 
Use case 03 
when post-rollback verification needs a clear checklist 
Use case 04 
when regular rollback drills are part of operational readiness 

## What the AI should return 

A rollback playbook with scripts for multiple rollback paths, verification steps, post-rollback actions, and drill procedures. 

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

Once you have the first result, continue deeper with related prompts in Production Incident Response.
