# Anomaly Detection *AI Prompts *

5 Data Analyst prompts in Anomaly Detection. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in Anomaly Detection 
5 prompts Intermediate Single prompt 01 
### Business Metric Spike Detection 

Business Metric Spike Detection is a intermediate prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Scan all business metrics in this dataset for unusual spikes or drops:

1. For each metric, compute the week-over-week and month-over-month percentage change
2. Flag any change greater than 2 standard deviations from the historical average change rate
3. For flagged metrics, check whether the spike is isolated to one dimension (e.g. one region, one product) or affects the whole metric
4. Determine whether the spike is a one-off event or the start of a new trend
5. Rank flagged metrics by business impact (highest volume or revenue first)

Return a spike report table and a plain-English summary of the top 3 most concerning changes. Copy prompt Open prompt details Advanced Single prompt 02 
### Multivariate Anomaly Detection 

Multivariate Anomaly Detection is a advanced prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Detect anomalies that only appear in the combination of multiple variables:

1. Apply Isolation Forest to the full numeric feature matrix
2. Apply Local Outlier Factor (LOF) with n_neighbors=20
3. Find rows flagged as anomalous by both methods — these are high-confidence anomalies
4. For each high-confidence anomaly: show the full row, which features deviate most, and how they relate to each other
5. Compare anomalous rows against the median row to quantify how extreme each feature value is

Return a ranked anomaly report with confidence score and a plain-English description of what makes each anomaly unusual. Copy prompt Open prompt details Advanced Chain 03 
### Root Cause Analysis Chain 

Root Cause Analysis Chain is a advanced chain for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Identify the anomaly — which metric, which timestamp, and how large is the deviation from expected?
Step 2: Slice the anomalous metric by every available dimension (region, product, channel, user segment, etc.). Where is the anomaly most concentrated?
Step 3: Check all other metrics in the same time window. Are there correlated anomalies that suggest a common cause?
Step 4: Compare the anomaly period against the same period from the prior week, prior month, and prior year. Is this pattern seasonal or truly novel?
Step 5: Synthesize your findings into a root cause report: top 3 hypotheses ranked by likelihood, supporting evidence for each, and recommended next diagnostic step. Copy prompt Open prompt details Beginner Single prompt 04 
### Statistical Outlier Detection 

Statistical Outlier Detection is a beginner prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Detect outliers across all numeric columns using three methods:

1. Z-score — flag values beyond ±3 standard deviations
2. IQR — flag values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR
3. Isolation Forest — use if the dataset has more than 1,000 rows

For each outlier detected:
- Column, row index, value, and which method(s) flagged it
- Your assessment: likely data error, or genuine extreme value?

Return a ranked list sorted by severity (most extreme first). Copy prompt Open prompt details Intermediate Single prompt 05 
### Time Series Anomaly Detection 

Time Series Anomaly Detection is a intermediate prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Detect anomalies in this time series data:

1. Build a rolling mean ± 2 standard deviation envelope (window = 7 periods)
2. Flag all points outside the envelope as anomalies
3. Check for abrupt level shifts using a changepoint detection method
4. Identify seasonality anomalies — values that are unusual specifically for their time of day, weekday, or month

For each anomaly found:
- Timestamp, observed value, expected range
- Severity score from 1 (mild) to 10 (extreme)
- Hypothesis: what might have caused this anomaly? Copy prompt Open prompt details 
## Recommended Anomaly Detection workflow 
1 
### Business Metric Spike Detection 

Start with a focused prompt in Anomaly Detection so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Multivariate Anomaly Detection 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Root Cause Analysis Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Statistical Outlier Detection 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
