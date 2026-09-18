# Anomaly Detection for Data Pipelines *AI Prompt *

Implement automated anomaly detection for data metrics in this pipeline. Metrics to monitor: {{metrics}} (row counts, revenue, event counts, null rates) Historical data availabl... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement automated anomaly detection for data metrics in this pipeline.

Metrics to monitor: {{metrics}} (row counts, revenue, event counts, null rates)
Historical data available: {{history}} (weeks of data)
False positive tolerance: {{tolerance}} (strict vs lenient)

1. Statistical anomaly detection approaches:

 Z-score (simple, works for normally distributed metrics):
 anomaly if |value - rolling_mean| / rolling_std > threshold
 threshold = 3 for strict (0.3% false positive), 2 for lenient (5% false positive)

 IQR-based (robust to outliers):
 Q1 = 25th percentile, Q3 = 75th percentile, IQR = Q3 - Q1
 anomaly if value < Q1 - 1.5 × IQR OR value > Q3 + 1.5 × IQR

 Percentage deviation from rolling average:
 anomaly if |value - rolling_avg_7d| / rolling_avg_7d > 0.3
 -- 30% deviation from the 7-day average
 Works well for business metrics with weekly seasonality

2. SQL implementation (row count anomaly detection):
 WITH daily_counts AS (
 SELECT DATE(created_at) AS d, COUNT(*) AS row_count
 FROM orders
 WHERE DATE(created_at) >= CURRENT_DATE - 30
 GROUP BY 1
 ),
 stats AS (
 SELECT d, row_count,
 AVG(row_count) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING) AS avg_7d,
 STDDEV(row_count) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING) AS std_7d
 FROM daily_counts
 )
 SELECT d, row_count, avg_7d,
 ABS(row_count - avg_7d) / NULLIF(std_7d, 0) AS z_score
 FROM stats
 WHERE ABS(row_count - avg_7d) / NULLIF(std_7d, 0) > 3;

3. Seasonality adjustment:
 - Day-of-week seasonality: compare to the same day of week in prior weeks
 - Holiday effects: create a holiday flag and exclude from the baseline
 - Elementary handles seasonality automatically using STL decomposition

4. Alert routing:
 - Z-score 2-3: warn in Slack; no action required unless confirmed by an analyst
 - Z-score > 3: alert to on-call; requires acknowledgment within 15 minutes
 - Consecutive anomalies (2+ days): escalate to a data incident

Return: anomaly detection SQL, threshold calibration, seasonality handling, and alert routing rules. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data quality operations work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Quality Operations or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Statistical anomaly detection approaches:, SQL implementation (row count anomaly detection):, Seasonality adjustment:. The final answer should stay clear, actionable, and easy to review inside a data quality operations workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Data Quality Operations.
