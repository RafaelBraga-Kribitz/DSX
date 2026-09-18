# Root Cause Analysis Chain *AI Prompt *

Root Cause Analysis Chain is a advanced chain for anomaly detection. This prompt is designed to uncover unusual values, events, or patterns that differ from the normal behavior in a dataset. It helps the AI separate likely data errors from legitimate but important business exceptions. Use it when you need to investigate spikes, drops, outliers, or suspicious records in a structured way. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Identify the anomaly — which metric, which timestamp, and how large is the deviation from expected?
Step 2: Slice the anomalous metric by every available dimension (region, product, channel, user segment, etc.). Where is the anomaly most concentrated?
Step 3: Check all other metrics in the same time window. Are there correlated anomalies that suggest a common cause?
Step 4: Compare the anomaly period against the same period from the prior week, prior month, and prior year. Is this pattern seasonal or truly novel?
Step 5: Synthesize your findings into a root cause report: top 3 hypotheses ranked by likelihood, supporting evidence for each, and recommended next diagnostic step. 
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
