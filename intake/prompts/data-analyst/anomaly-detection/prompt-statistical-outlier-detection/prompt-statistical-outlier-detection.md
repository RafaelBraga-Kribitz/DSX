# Statistical Outlier Detection *AI Prompt *

Statistical Outlier Detection is a beginner prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect outliers across all numeric columns using three methods:

1. Z-score — flag values beyond ±3 standard deviations
2. IQR — flag values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR
3. Isolation Forest — use if the dataset has more than 1,000 rows

For each outlier detected:
- Column, row index, value, and which method(s) flagged it
- Your assessment: likely data error, or genuine extreme value?

Return a ranked list sorted by severity (most extreme first). 
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
