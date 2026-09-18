# Serving Metrics Dashboard *AI Prompt *

This prompt builds a Prometheus and Grafana monitoring stack for model serving, with metrics, dashboard panels, and alert rules tied to latency, error rate, and availability objectives. It is most useful when an ML API needs clear operational visibility and on-call ready alerts. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a production model serving metrics dashboard using Prometheus and Grafana.

Model: {{model_name}}
SLA targets: p99 latency < {{latency_sla_ms}}ms, error rate < {{error_rate_sla}}%, availability > {{availability_sla}}%

1. Prometheus metrics to instrument (add to the serving application):

 Service-level metrics:
 - model_requests_total (counter): labeled by model_version, endpoint, status_code
 - model_request_duration_seconds (histogram): labeled by model_version, endpoint
 Buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
 - model_errors_total (counter): labeled by model_version, error_type
 - model_in_flight_requests (gauge): current concurrent requests

 Model-level metrics:
 - prediction_score_distribution (histogram): distribution of output confidence scores
 - feature_value_distribution (histogram): one per key feature, for drift detection
 - model_load_time_seconds (gauge): time to load model at startup

 Infrastructure metrics:
 - gpu_utilization_percent (gauge): per serving node
 - gpu_memory_used_bytes (gauge): per serving node

2. Grafana dashboard panels:
 Row 1 — SLA Overview:
 - Current request rate (RPS)
 - p50 / p95 / p99 latency (time series)
 - Error rate % (time series, red threshold at SLA)
 - Availability % (stat panel, green/red)

 Row 2 — Model Health:
 - Prediction score distribution (heatmap over time)
 - Request volume by model version (stacked bar — useful during rollouts)
 - Top error types (table)

 Row 3 — Infrastructure:
 - GPU utilization per node (time series)
 - GPU memory used per node (time series)
 - Pod count (gauge)

3. Alerting rules (Prometheus AlertManager):
 - HighErrorRate: error_rate > {{error_rate_sla}}% for 5 minutes → PagerDuty (P1)
 - HighLatency: p99 > {{latency_sla_ms}}ms for 10 minutes → Slack (P2)
 - ModelDown: no successful requests for 2 minutes → PagerDuty (P0)
 - LowThroughput: RPS drops > 50% vs 1-hour average → Slack (P2)

Return: Prometheus instrumentation code, AlertManager rules YAML, and Grafana dashboard JSON. 
```

## When to use this prompt 
Use case 01 
when you need a Grafana dashboard for model serving SLAs 
Use case 02 
when instrumenting Prometheus metrics in an inference service 
Use case 03 
when defining alert thresholds for latency, error rate, throughput, and uptime 
Use case 04 
when you want dashboard JSON, AlertManager rules, and code together 

## What the AI should return 

A serving observability package with Prometheus instrumentation, Grafana dashboard layout or JSON, and AlertManager rules for SLA monitoring. 

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
