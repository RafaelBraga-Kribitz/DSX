# Multi-Model Monitoring System *AI Prompt *

This prompt designs a centralized monitoring platform for many production models with shared infrastructure but model-specific rules. It is helpful for teams that need scalable monitoring, ownership routing, and cost-aware operations across a growing model portfolio. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a centralized monitoring system that scales to {{num_models}} production ML models.

Challenge: each model has different input features, output types, and business metrics. A one-size-fits-all approach does not work.

1. Model registry integration:
 - Each registered model provides a monitoring config alongside the model artifact
 - Monitoring config specifies: key features to monitor, output type and drift thresholds, business metric to track, retraining trigger conditions, and alert routing

2. Centralized collection layer:
 - Standardized prediction log schema with model-specific payload field for input/output details
 - All models write to the same Kafka topic, partitioned by model_name
 - Central consumer writes to a unified monitoring database partitioned by model_name/date

3. Per-model monitoring jobs:
 - Template monitoring job parameterized by model config
 - Spins up one monitoring job per registered model automatically on new model deployment
 - Each job: reads from the unified monitoring database, applies the model-specific config, and writes results to a monitoring metrics table

4. Unified monitoring dashboard:
 - Overview page: table of all models with health status (🟢/🟡/🔴) based on recent alerts
 - Drill-down per model: serving metrics, prediction distribution, drift scores, recent alerts
 - Cross-model comparison: compare drift patterns across models — correlated drift suggests a shared upstream data issue

5. Alert deduplication and routing:
 - Group alerts from the same model within a 1-hour window to avoid alert storms
 - Route to the correct on-call engineer based on model ownership in the registry
 - Escalation: if alert is not acknowledged within {{escalation_window}} minutes, page the team lead

6. Cost management:
 - Tier models by importance (Tier 1: revenue-critical, Tier 2: operational, Tier 3: experimental)
 - Different monitoring frequencies per tier: T1 = real-time, T2 = hourly, T3 = daily
 - Estimated monitoring cost per model per month

Return: monitoring config schema, centralized collection architecture, per-model job template, and unified dashboard spec. 
```

## When to use this prompt 
Use case 01 
when one team operates many production models with different monitoring needs 
Use case 02 
when monitoring configs should be stored with registered models 
Use case 03 
when you need unified collection plus model-specific monitoring jobs 
Use case 04 
when building a fleet-wide dashboard with routing, deduplication, and cost controls 

## What the AI should return 

A multi-model monitoring architecture including config schema, centralized collection, per-model job template, dashboard specification, and alert routing design. 

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

Once you have the first result, continue deeper with related prompts in Model Monitoring.
