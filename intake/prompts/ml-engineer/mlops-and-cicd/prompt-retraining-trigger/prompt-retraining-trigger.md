# Automated Retraining Trigger *AI Prompt *

This prompt designs an automated retraining system driven by monitored signals such as accuracy degradation, drift, new data volume, or time-based schedules. It focuses on reliable trigger detection, retraining execution, and safe promotion gates. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an automated model retraining system that triggers based on monitored signals.

1. Retraining trigger conditions (any one is sufficient):
 - Performance degradation: model accuracy on recent data drops below {{performance_threshold}}
 - Data drift: PSI > 0.2 for any top-10 feature by importance
 - Prediction drift: KS test p-value < 0.05 on prediction distribution vs baseline
 - Scheduled: time-based trigger every {{retrain_schedule}} (e.g. weekly, monthly)
 - New data volume: {{new_data_threshold}} new labeled samples available since last training

2. Trigger detection pipeline:
 - Run drift checks daily as a scheduled job
 - Log trigger signals to a monitoring database
 - When a trigger fires: log which signal, the metric value, and the threshold exceeded

3. Retraining execution:
 - Submit training job to compute cluster (Kubernetes Job, Airflow DAG, or SageMaker Pipeline)
 - Use the latest full dataset (not just new data) with a sliding window if dataset grows unbounded
 - Run with the same config as the current production model to enable fair comparison

4. Model promotion gate:
 - New model must beat current production model on a fixed evaluation set by > {{min_improvement}}%
 - If gate passes: automatically promote to staging, trigger deployment pipeline
 - If gate fails: alert the ML team, do not auto-promote

5. Human-in-the-loop option:
 - For high-stakes models: require human approval before any promotion, even if gate passes

Return: drift detection script, trigger condition implementation, retraining job submission code, and promotion gate logic. 
```

## When to use this prompt 
Use case 01 
when model retraining should happen automatically based on measurable signals 
Use case 02 
when drift and performance monitoring must trigger jobs consistently 
Use case 03 
when new models should be compared fairly against production before promotion 
Use case 04 
when human approval may still be required for higher-risk deployments 

## What the AI should return 

Drift detection and trigger logic, retraining job submission code, and promotion gate rules for automated or semi-automated retraining. 

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
