# Model Monitoring Setup *AI Prompt *

This prompt sets up production model monitoring across service metrics, prediction logging, drift checks, confidence shifts, and delayed ground-truth evaluation. It is intended for teams that need ongoing visibility into both operational health and model quality after deployment. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Set up a comprehensive production model monitoring system.

1. Prediction logging:
 - Log every prediction to a structured store: timestamp, request_id, model_version, input_features, prediction, confidence, latency_ms
 - Use async logging to avoid adding latency to the serving path
 - Rotate logs daily and archive to object storage after 7 days

2. Service-level monitoring (Prometheus + Grafana):
 - Metrics to track: requests/sec, error rate (4xx, 5xx), p50/p95/p99 latency, queue depth
 - Alerts: error rate > 1%, p99 latency > {{latency_sla_ms}}, model load failure
 - Dashboard: request volume, latency percentiles, error rate, model version deployed

3. Model-level monitoring:
 - Prediction distribution: compare daily prediction distribution to training distribution (PSI)
 - Confidence distribution: alert if mean confidence drops significantly (model is uncertain)
 - Output drift: KS test on prediction scores between current week vs baseline week

4. Feature/data drift monitoring:
 - For each of the top 10 features: compute PSI weekly
 - PSI < 0.1: no significant change
 - PSI 0.1–0.2: moderate drift, investigate
 - PSI > 0.2: significant drift, trigger retraining evaluation

5. Ground truth feedback loop:
 - If labels become available with a delay (e.g. churn labels available after 30 days): join predictions to outcomes and compute actual model accuracy over time
 - Alert if rolling 30-day accuracy drops below {{accuracy_threshold}}

Return: prediction logging implementation, Prometheus metrics setup, drift monitoring scripts, and Grafana dashboard spec. 
```

## When to use this prompt 
Use case 01 
when a production model needs observability beyond simple uptime checks 
Use case 02 
when Prometheus and Grafana should monitor latency, errors, and traffic 
Use case 03 
when feature drift or output drift should be measured regularly 
Use case 04 
when labels arrive later and rolling real-world accuracy must be tracked 

## What the AI should return 

Prediction logging implementation, monitoring metrics and alerts, drift scripts, and a dashboard specification for service and model health. 

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
