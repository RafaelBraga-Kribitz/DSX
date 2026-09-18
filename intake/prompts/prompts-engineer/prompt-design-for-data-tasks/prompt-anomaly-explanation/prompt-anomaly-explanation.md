# Anomaly Explanation Prompt *AI Prompt *

Design a prompt that takes a detected data anomaly and produces a clear, business-friendly explanation with hypotheses. Context: anomaly detection systems generate alerts, but d... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt that takes a detected data anomaly and produces a clear, business-friendly explanation with hypotheses.

Context: anomaly detection systems generate alerts, but data teams spend significant time translating statistical findings into actionable business language. This prompt automates that translation.

1. Anomaly context input structure:
 Define the inputs the prompt receives:
 - metric_name: the metric that anomalized
 - current_value: the observed value
 - expected_value: the baseline or predicted value
 - deviation_pct: percentage deviation from expected
 - time_period: when the anomaly occurred
 - segment_breakdown: how the anomaly distributes across dimensions (region, product, channel)
 - related_metrics: other metrics that moved at the same time
 - recent_events: known business events in the same time window (promotions, deployments, holidays)

2. Prompt instructions:
 - 'You are a senior data analyst. Explain this data anomaly to a business audience.'
 - 'Do not use statistical terminology. Replace with plain business language.'
 - 'Do not speculate beyond what the data supports. Distinguish between confirmed facts and hypotheses.'

3. Output structure (enforce with the prompt):
 - What happened: 1–2 sentences describing the anomaly in plain English
 - Where it is concentrated: which segments, regions, or dimensions account for most of the deviation
 - Likely causes: 2–3 hypotheses ranked by likelihood, each with supporting evidence from the data
 - What is needed to confirm: what additional data or investigation would confirm the top hypothesis
 - Recommended action: a specific next step for the business team

4. Tone calibration:
 - For a 5% deviation: 'A moderate shift worth monitoring'
 - For a 20% deviation: 'A significant change that warrants investigation'
 - For a 50%+ deviation: 'An extreme anomaly requiring immediate attention'
 - Instruct the model to match tone to deviation magnitude

5. Few-shot examples:
 - Provide 2 example anomalies with full context and the ideal explanation output
 - Include one where the cause is known (holiday effect) and one where it is unknown

Return: the complete anomaly explanation prompt, 2 few-shot examples, and a rubric for evaluating explanation quality (accuracy, clarity, actionability). 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt design for data tasks work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Design for Data Tasks or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Anomaly context input structure:, metric_name: the metric that anomalized, current_value: the observed value. The final answer should stay clear, actionable, and easy to review inside a prompt design for data tasks workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Design for Data Tasks.
