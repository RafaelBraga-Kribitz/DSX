# Anomaly Narrative Writer *AI Prompt *

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It explains an unusual movement in business terms so leaders understand what happened and what to do. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a clear narrative explanation of this data anomaly for a non-technical business audience.

Anomaly: {{anomaly_description}} (e.g. 'Revenue dropped 23% week-over-week in the EMEA region during the week of March 10')

Data provided shows the full context.

1. State the anomaly clearly in the first sentence — what happened, how large was the deviation, and when?
2. Provide immediate context: is this the largest deviation in the past 12 months? How does it compare to normal variance?
3. Diagnose the cause using the data:
 - Drill down by dimension to isolate where the anomaly is concentrated
 - Check for correlated changes in other metrics
 - Identify any known external events (holidays, outages, campaigns)
4. Assess business impact: what is the estimated financial or operational impact?
5. State whether this is:
 - A data quality issue (pipeline error, reporting lag)
 - A temporary one-off event
 - The start of a concerning trend
6. Recommend the next action: investigate further / monitor / escalate / no action needed

Return: 200-word narrative suitable for a Slack message or email to leadership. 
```

## When to use this prompt 
Use case 01 
Use when you need a repeatable report, dashboard design, or executive-ready narrative. 
Use case 02 
Use when different audiences need different levels of detail from the same data. 
Use case 03 
Use when report quality, consistency, and clarity matter more than raw analysis output. 
Use case 04 
Use when you want a specification that can be handed off to BI, analytics, or leadership. 

## What the AI should return 

The AI should return a clean reporting artifact with the requested structure, audience tone, and presentation logic. Metrics should be organized clearly, narrative sections should emphasize the main story, and any recommended actions should be concrete. The result should feel ready for a report, dashboard spec, email, or leadership update. 

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

Once you have the first result, continue deeper with related prompts in Reporting and Dashboards.
