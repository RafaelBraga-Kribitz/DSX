# A/B Deployment Pattern *AI Prompt *

This prompt implements an A/B deployment pattern for serving a challenger model alongside a champion model, with deterministic routing, per-variant metrics, and rollout or rollback automation. It is useful for safe online model experimentation in production. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement an A/B model deployment pattern to safely roll out a new model version alongside the current production model.

1. Traffic splitting:
 - Route {{traffic_split}}% of requests to the new model (challenger) and the remainder to the current model (champion)
 - Ensure consistent assignment: the same user/request_id always gets the same model using hash-based routing
 - Support instant traffic shift without redeployment (feature flag or config-based)

2. Request routing implementation:
 - Routing middleware in the serving layer
 - Log which model version served each request: model_version, variant (champion/challenger), request_id

3. Metrics collection:
 - Tag all prediction logs with the model variant
 - Track per-variant: p50/p95/p99 latency, error rate, throughput
 - Track per-variant business metrics: conversion rate, click-through, or other downstream outcome

4. Statistical comparison:
 - Run two-sample t-test or z-test on business metrics per variant
 - Automated alerting if challenger has significantly worse latency or error rate than champion

5. Rollout automation:
 - If challenger is statistically better after {{min_samples}} requests: automatically increase traffic to 100%
 - If challenger is significantly worse: automatically roll back to 0% traffic
 - Otherwise: hold and wait for more data

6. Shadow mode (optional first step):
 - Send all requests to champion for production responses
 - Mirror all requests to challenger for comparison only (no response returned)

Return: routing middleware, metrics logging, statistical comparison, and automated rollout/rollback logic. 
```

## When to use this prompt 
Use case 01 
when testing a new model against a production baseline with live traffic 
Use case 02 
when you need consistent request assignment and per-variant logging 
Use case 03 
when rollout decisions should depend on latency, errors, or business outcomes 
Use case 04 
when shadow mode or gradual exposure is preferred over full replacement 

## What the AI should return 

Routing middleware, metrics logging, significance testing logic, and automated rollout or rollback controls for champion-challenger deployment. 

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
