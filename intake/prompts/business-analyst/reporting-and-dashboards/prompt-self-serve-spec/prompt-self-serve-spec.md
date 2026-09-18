# Self-Serve Analytics Spec *AI Prompt *

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It designs a self-serve analytics approach so a business team can answer common questions independently. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a self-serve analytics solution for {{business_team}} to answer their most common data questions without needing analyst support.

1. Conduct a question audit:
 - List the top 10 most common questions this team asks the data team
 - Classify each: answerable with a standard report, requires ad-hoc analysis, or needs a new data source

2. Design the self-serve layer:
 - Which questions can be answered with a pre-built dashboard? Specify the dashboard.
 - Which questions need a flexible exploration tool (e.g. Looker, Metabase)? Specify the data model.
 - Which require scheduled reports? Specify format and recipients.

3. Data literacy requirements:
 - What level of data skill does this team currently have?
 - What training or documentation is needed for them to use the self-serve layer confidently?

4. Governance rules:
 - Which metrics need a single agreed definition (to prevent different people getting different answers)?
 - Who approves new metric definitions?
 - How are errors or discrepancies reported and resolved?

5. Success metric: how will you know the self-serve solution is working?

Return: question audit table, self-serve design spec, training plan, and governance rules. 
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
