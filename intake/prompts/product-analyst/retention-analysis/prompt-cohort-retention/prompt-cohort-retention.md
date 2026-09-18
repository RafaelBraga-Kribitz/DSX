# User Retention Cohort Analysis *AI Prompt *

Build and interpret a user retention cohort analysis. Event data: {{event_data}} (user_id, event_date, acquisition_date or cohort_date) Retention definition: {{retention_definit... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build and interpret a user retention cohort analysis.

Event data: {{event_data}} (user_id, event_date, acquisition_date or cohort_date)
Retention definition: {{retention_definition}} (e.g. any login, completed core action, purchase)
Cohort granularity: {{granularity}} (weekly / monthly)

1. Build the retention matrix:
 - Rows: cohorts defined by {{cohort_period}} of first use or acquisition
 - Columns: periods since acquisition (Period 0, 1, 2, ... N)
 - Cell value: % of cohort still active in that period
 - Period 0 = 100% by definition (the acquisition period)

2. Key retention metrics:
 - Day 1 retention: % of users returning the day after first use
 - Day 7 retention: % returning in the first week
 - Day 30 retention: % returning within the first month
 - Long-term retention: at what period does the retention curve flatten? This is the product's natural retention floor.

3. Cohort comparison:
 - Are newer cohorts retaining better or worse than older ones?
 - Which cohort has the best Day 30 retention? What was happening during that acquisition period?
 - Plot cohort curves on the same chart: diverging curves indicate improving or worsening product health

4. Retention curve shape interpretation:
 - Sharp early drop then flat: high initial churn but strong core user base
 - Gradual continuous decline: no engaged user base, product is not habit-forming
 - Bump at specific period: seasonal return or notification-driven re-engagement

5. Retention by acquisition channel:
 - Which acquisition channels produce the highest Day 30 retention?
 - Are there channels bringing volume but low retention? (Wasted acquisition spend)

6. Recommendations:
 - At which period does the biggest retention drop occur? What is the likely cause?
 - What single change would most improve the retention curve shape?

Return: retention matrix, key metrics table, cohort comparison chart description, curve interpretation, and top recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin retention analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Retention Analysis or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Build the retention matrix:, Rows: cohorts defined by {{cohort_period}} of first use or acquisition, Columns: periods since acquisition (Period 0, 1, 2, ... N). The final answer should stay clear, actionable, and easy to review inside a retention analysis workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Retention Analysis.
