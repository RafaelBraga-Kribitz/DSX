# Business Metric Spike Detection *AI Prompt *

Business Metric Spike Detection is a intermediate prompt for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Scan all business metrics in this dataset for unusual spikes or drops:

1. For each metric, compute the week-over-week and month-over-month percentage change
2. Flag any change greater than 2 standard deviations from the historical average change rate
3. For flagged metrics, check whether the spike is isolated to one dimension (e.g. one region, one product) or affects the whole metric
4. Determine whether the spike is a one-off event or the start of a new trend
5. Rank flagged metrics by business impact (highest volume or revenue first)

Return a spike report table and a plain-English summary of the top 3 most concerning changes. 
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
