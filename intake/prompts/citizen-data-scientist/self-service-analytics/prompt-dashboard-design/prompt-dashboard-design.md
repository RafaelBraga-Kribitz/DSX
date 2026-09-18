# Team Dashboard Design *AI Prompt *

Help me design a simple dashboard that my team can use independently to monitor performance without needing my help. Team: {{team_description}} Key questions they need to answer... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me design a simple dashboard that my team can use independently to monitor performance without needing my help.

Team: {{team_description}}
Key questions they need to answer: {{team_questions}}
Tool I will build it in: {{tool}} (e.g. Google Sheets, Excel, Tableau, Power BI, Metabase, Looker Studio)

1. What the dashboard is NOT:
 - It is not a data dump — every chart and number must answer a specific question
 - It is not for the builder — design it for people who look at it once a week, not for people who built it
 - It is not a report — it is a decision-support tool. Every element should prompt an action or confirm that no action is needed.

2. Design the dashboard structure:
 For each of the team's key questions, specify:
 - The metric or chart that answers it
 - The time frame it should show
 - The comparison context (vs last week, vs target, vs same period last year)
 - What 'green' looks like (no action needed) and what 'red' looks like (action needed)

3. Layout principles:
 - Most important metric top left (where eyes go first)
 - Single number + trend arrow for quick scanning
 - Detailed breakdowns below for people who want to dig in
 - Maximum 6–8 metrics on the main view — if you need more, create a second level

4. Making it self-service:
 - Add filter controls that the team can use to slice by region, product, time period
 - Color code automatically: green above target, yellow within 10% of target, red below threshold
 - Add a 'last updated' timestamp so users know if the data is fresh
 - Include a glossary section that defines every metric

5. Adoption tips:
 - Walk the team through it once — show them how to answer their 3 most common questions using it
 - Set a recurring reminder for them to check it at the start of each week
 - Ask for feedback after 2 weeks: which parts do they use, which do they ignore?

Return: dashboard wireframe (described in text), metric definitions, color coding rules, and a 30-minute walkthrough plan for the team. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin self-service analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Self-Service Analytics or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What the dashboard is NOT:, It is not a data dump — every chart and number must answer a specific question, It is not for the builder — design it for people who look at it once a week, not for people who built it. The final answer should stay clear, actionable, and easy to review inside a self-service analytics workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in Self-Service Analytics.
