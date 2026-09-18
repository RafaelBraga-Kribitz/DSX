# Multivariate Anomaly Detection *AI Prompt *

Multivariate Anomaly Detection is a advanced prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect anomalies that only appear in the combination of multiple variables:

1. Apply Isolation Forest to the full numeric feature matrix
2. Apply Local Outlier Factor (LOF) with n_neighbors=20
3. Find rows flagged as anomalous by both methods — these are high-confidence anomalies
4. For each high-confidence anomaly: show the full row, which features deviate most, and how they relate to each other
5. Compare anomalous rows against the median row to quantify how extreme each feature value is

Return a ranked anomaly report with confidence score and a plain-English description of what makes each anomaly unusual. 
```

## When to use this prompt 
Use case 01 
When a metric suddenly spikes, drops, or behaves differently than expected. 
Use case 02 
When you need to separate genuine business events from likely data issues. 
Use case 03 
When monitoring operational, financial, or product data for exceptions. 
Use case 04 
When you want a ranked list of unusual records or periods for investigation. 

## What the AI should return 

The AI should return a ranked anomaly report with the relevant records, metrics, time periods, or row indices clearly identified. It should explain which detection methods were used, why each anomaly was flagged, and whether it looks like a data issue or a real-world event. Summary tables should be supported by a short interpretation that prioritizes what to investigate first. When appropriate, the answer should include severity scores, hypotheses, and next diagnostic steps. 

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

Once you have the first result, continue deeper with related prompts in Anomaly Detection.
