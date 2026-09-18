# Cost of Monitoring Analysis *AI Prompt *

This prompt analyzes the operational cost of model monitoring and proposes optimizations such as sampling, storage tiering, and frequency tiering. It is useful when monitoring is already in place but has become expensive at scale. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze and optimize the cost of the production model monitoring infrastructure.

Current monitoring stack: {{monitoring_stack}}
Number of models monitored: {{num_models}}
Current monthly monitoring cost: {{current_cost}}

1. Cost breakdown:
 - Log storage: how many GB of prediction logs are stored? At what cost per GB?
 - Compute: how many monitoring jobs run per day? What is the compute cost per job?
 - Query costs: how many analytical queries run against the monitoring database? Cost per query?
 - Alerting: external alerting services (PagerDuty, OpsGenie) cost per seat/alert
 - Dashboard: Grafana Cloud or self-hosted cost

2. Sampling strategy for high-throughput models:
 - For models with > 1M predictions/day: log a stratified sample instead of 100%
 - Sample rate recommendation: 10% for >1M/day, 50% for 100k-1M/day, 100% for <100k/day
 - Ensure sample is stratified by prediction score bucket (preserve distribution shape)
 - Log ALL anomalous predictions regardless of sample rate (score > 0.95 or < 0.05 for classifiers)

3. Log retention optimization:
 - Tiered storage: hot (last 7 days, queryable), warm (7–90 days, compressed), cold (>90 days, archival)
 - Pre-aggregate daily statistics (mean, std, percentiles) and retain indefinitely
 - Delete raw logs after 90 days — aggregate statistics are sufficient for long-term trend analysis

4. Monitoring frequency tiering:
 - Tier 1 (revenue-critical): real-time serving metrics, hourly drift checks, daily performance
 - Tier 2 (operational): hourly serving metrics, daily drift checks, weekly performance
 - Tier 3 (experimental): daily serving metrics, weekly drift checks, no automatic performance tracking

5. Estimated savings from each optimization:
 - Sampling: saves X% on log storage and compute
 - Tiered storage: saves Y% on storage
 - Monitoring frequency tiering: saves Z% on compute

Return: cost breakdown analysis, sampling implementation, tiered storage design, and total estimated savings. 
```

## When to use this prompt 
Use case 01 
when monitoring costs are growing with traffic or model count 
Use case 02 
when deciding how much prediction logging to sample 
Use case 03 
when storage retention and compute schedules need optimization 
Use case 04 
when you need quantified savings from different cost controls 

## What the AI should return 

A monitoring cost analysis with cost breakdown, sampling design, retention strategy, frequency tiering, and estimated savings. 

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
