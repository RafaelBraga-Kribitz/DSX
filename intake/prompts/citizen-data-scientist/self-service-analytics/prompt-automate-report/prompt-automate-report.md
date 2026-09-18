# Automate My Recurring Report *AI Prompt *

Help me automate a report I currently produce manually so it runs itself and I can focus on analysis instead of assembly. Report I produce manually: {{report_description}} How l... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me automate a report I currently produce manually so it runs itself and I can focus on analysis instead of assembly.

Report I produce manually: {{report_description}}
How long it takes me currently: {{time_spent}}
Tool I have access to: {{available_tools}}
Audience and delivery method: {{audience_and_delivery}}

1. Identify what can be automated vs what requires human judgment:
 Go through the report and classify each step:
 - Fully automatable: data pulling, number calculation, chart generation, formatting
 - Partially automatable: anomaly flagging (automate the detection, human writes the explanation)
 - Requires human judgment: context, implications, recommendations
 The goal is to automate the assembly so I can spend my time on interpretation.

2. Automation approach for my tools:

 If using Excel / Google Sheets:
 - Data connection: link directly to the data source so the file refreshes automatically
 - Scheduled refresh: configure the data connection to refresh on a schedule
 - Email distribution: use a simple script or Zapier to email the report automatically

 If using Python (low-code approach):
 - Use pandas to pull and process the data
 - Use openpyxl or xlsxwriter to generate a formatted Excel report
 - Schedule with cron (Mac/Linux) or Task Scheduler (Windows)
 - Send via smtplib or a Slack bot

 If using a BI tool (Tableau, Power BI, Looker, Metabase):
 - Set the data source to auto-refresh
 - Use the built-in subscription feature to email a PDF snapshot on a schedule

3. Build in quality checks:
 - Before the automated report sends: check that the data was refreshed (compare last update timestamp to expected update time)
 - Check that key metrics are within a plausible range (alert me if revenue is 0 or 10× normal — likely a data error)
 - If checks fail: send an alert to me instead of the report to the audience

4. The commentary problem:
 - Automated reports without commentary are just data dumps
 - Build a commentary template with fill-in-the-blank sections that I complete in 10 minutes
 - The template prompts me: 'Key trend this week:', 'Biggest deviation from expectations:', 'Recommended action:'

Return: automation approach for my specific tools, quality check implementation, commentary template, and estimated time savings. 
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

The AI should return a structured result that covers the main requested outputs, such as Identify what can be automated vs what requires human judgment:, Fully automatable: data pulling, number calculation, chart generation, formatting, Partially automatable: anomaly flagging (automate the detection, human writes the explanation). The final answer should stay clear, actionable, and easy to review inside a self-service analytics workflow for citizen data scientist work. 

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
