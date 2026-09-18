# Pipeline Anomaly Detection *AI Prompt *

This prompt applies statistical anomaly detection to operational pipeline metrics so teams can catch unusual behavior even when a job technically succeeds. It is valuable for spotting silent failures such as row-count drops, unusual runtimes, or business-total shifts. The output should combine statistical baselines with configurable thresholds and practical alert routing. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build statistical anomaly detection for this data pipeline's operational metrics.

Metrics to monitor: row counts, processing time, error rate, and key business measure totals.

1. Baseline computation (run weekly):
 - For each metric and each day-of-week, compute: mean, standard deviation, and 5th/95th percentiles from the last 90 days
 - Store baselines in a metadata table: metric_name, day_of_week, mean, std, p5, p95, computed_at

2. Anomaly detection rules (run after each pipeline execution):
 - Statistical: flag if today's value is outside mean ± {{sigma}}σ (e.g. 3σ)
 - Percentage change: flag if WoW change > {{pct_threshold}}% for the same day of week
 - Absolute minimum: flag if row count = 0 (hard rule, always an error)
 - Absolute maximum: flag if row count > {{hard_cap}} (possible runaway job or data duplication)

3. Seasonal adjustment:
 - Normalize metrics by day-of-week (Monday typically has different volumes than Friday)
 - For businesses with monthly seasonality: also normalize by week-of-month

4. Metric-level thresholds:
 - Different thresholds per metric: row counts may tolerate ±20%, revenue totals should only tolerate ±1%
 - Store thresholds in a configuration table for easy adjustment without code changes

5. Alert routing:
 - Route anomalies to the appropriate team based on metric type (data team vs business team)
 - Include context in the alert: current value, expected range, historical chart link
 - Suppress duplicate alerts: do not re-alert the same anomaly within 4 hours

Return: baseline computation SQL, anomaly detection queries, threshold configuration table, and alert routing logic. 
```

## When to use this prompt 
Use case 01 
When successful jobs can still produce suspicious outputs. 
Use case 02 
When you want automated checks on row counts, runtimes, and measure totals. 
Use case 03 
When day-of-week seasonality makes naive thresholds unreliable. 
Use case 04 
When alerts should be tuned per metric and routed to the right team. 

## What the AI should return 

Return baseline-computation logic, anomaly-detection queries, threshold configuration tables, and alert-routing rules. Show how seasonal adjustment is handled and how duplicate alerts are suppressed. The response should make clear which anomalies are hard failures, which are warnings, and who should receive each alert. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
