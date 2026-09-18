# Metric Discrepancy Investigation *AI Prompt *

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It helps diagnose why two reports disagree on the same metric and how to align them. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Investigate why two reports are showing different values for the same metric: {{metric_name}}

Report A shows: {{value_a}} | Report B shows: {{value_b}} | Difference: {{difference}}

Systematically investigate each possible cause:

1. Definition differences:
 - Is the metric formula identical in both reports?
 - Are the same inclusion/exclusion filters applied?
 - Are the same business rules applied (e.g. how refunds are treated)?

2. Date range differences:
 - Are both reports using the same date range?
 - Is one using event date and the other using processing date?
 - Is one using UTC and the other using local time?

3. Data source differences:
 - Do both reports pull from the same source table?
 - If different sources, when were they last synced and could there be a lag?

4. Aggregation differences:
 - Is one report double-counting rows due to joins?
 - Is one report deduplicating differently?

5. Access differences:
 - Does one report include data the other user doesn't have access to?

For each hypothesis: confirmed / ruled out / needs investigation.

Return: investigation log, root cause finding, and recommended fix to align both reports. 
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
