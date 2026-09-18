# Dashboard Specification *AI Prompt *

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It creates a handoff-ready specification for building a dashboard with the right metrics, layout, and governance. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a dashboard specification document for a {{dashboard_name}} dashboard for {{audience}}.

The specification should include:

1. Purpose and audience:
 - What decision does this dashboard support?
 - Who are the primary users and what is their technical level?
 - How often will it be used and in what context (daily standup, weekly review, ad-hoc analysis)?

2. KPIs and metrics to display:
 - For each metric: name, definition, formula, data source, refresh frequency

3. Dashboard layout (describe each panel):
 - Panel 1: [metric name] — [chart type] — [why this chart type]
 - List all panels with their position, size, and purpose

4. Filters and interactivity:
 - Date range selector
 - Dimension filters (region, product, segment, etc.)
 - Drill-down capabilities

5. Alerts and thresholds:
 - Which metrics should trigger alerts and at what thresholds?

6. Data sources and refresh:
 - Source tables or APIs, refresh schedule, SLA for data freshness

7. Access and permissions:
 - Who can view, who can edit, any data sensitivity restrictions

Return: complete dashboard specification document. 
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
