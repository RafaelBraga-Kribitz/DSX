# Self-Service Analytics *AI Prompts *

3 Citizen Data Scientist prompts in Self-Service Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 3 single prompts. 

## AI prompts in Self-Service Analytics 
3 prompts Intermediate Single prompt 01 
### Automate My Recurring Report 

Help me automate a report I currently produce manually so it runs itself and I can focus on analysis instead of assembly. Report I produce manually: {{report_description}} How l... 
Prompt text Help me automate a report I currently produce manually so it runs itself and I can focus on analysis instead of assembly.

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

Return: automation approach for my specific tools, quality check implementation, commentary template, and estimated time savings. Copy prompt Open prompt details Beginner Single prompt 02 
### Reusable Analysis Template 

Help me create a reusable analysis template so I can repeat this analysis quickly each week or month without starting from scratch. Analysis I do repeatedly: {{analysis_descript... 
Prompt text Help me create a reusable analysis template so I can repeat this analysis quickly each week or month without starting from scratch.

Analysis I do repeatedly: {{analysis_description}}
Data source: {{data_source}}
Outputs needed: {{outputs}}

1. Template structure:
 Design a template that:
 - Has clearly labeled sections I fill in each time (date range, filter criteria, comparison period)
 - Has fixed sections that stay the same every time (the formulas, the chart types, the table structure)
 - Is easy to use for someone who did not create it (my colleague should be able to run this without asking me how)

2. What to parameterize (make easy to change):
 - Date range: make it a single cell reference that all other cells use — change it once, everything updates
 - Comparison period: prior period, same period last year, target
 - Filters: which region, product, or segment to include
 For each parameter: where to put it, how to label it, and what the default value should be

3. What to standardize (keep the same every time):
 - Column names and order
 - Chart types and formatting
 - Metric definitions — write them out once so future-me and colleagues use the same definition
 - The commentary structure (this forces you to answer the same questions every time, which makes period-over-period comparison easier)

4. Documentation to include in the template:
 - A brief description of what this template does
 - Where the data comes from and when it was last refreshed
 - Definitions of each metric
 - Known limitations or caveats
 - Who to contact if something looks wrong

5. The 'can a colleague use this?' test:
 - Could someone with similar skills use this template without any instructions from you?
 - What is the most likely point of confusion? Add a note there.

Return: a step-by-step template design with all the above elements. Copy prompt Open prompt details Intermediate Single prompt 03 
### Team Dashboard Design 

Help me design a simple dashboard that my team can use independently to monitor performance without needing my help. Team: {{team_description}} Key questions they need to answer... 
Prompt text Help me design a simple dashboard that my team can use independently to monitor performance without needing my help.

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

Return: dashboard wireframe (described in text), metric definitions, color coding rules, and a 30-minute walkthrough plan for the team. Copy prompt Open prompt details 
## Recommended Self-Service Analytics workflow 
1 
### Automate My Recurring Report 

Start with a focused prompt in Self-Service Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Reusable Analysis Template 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Team Dashboard Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
