# Reporting and Dashboards *AI Prompts *

8 Business Analyst prompts in Reporting and Dashboards. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain · 1 template. 

## AI prompts in Reporting and Dashboards 
8 prompts Intermediate Single prompt 01 
### Anomaly Narrative Writer 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It explains an unusual movement in business terms so leaders understand what happened and what to do. 
Prompt text Write a clear narrative explanation of this data anomaly for a non-technical business audience.

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

Return: 200-word narrative suitable for a Slack message or email to leadership. Copy prompt Open prompt details Intermediate Template 02 
### Board-Level Report 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It frames performance at a strategic level for board discussion, focusing on outcomes, risks, and decisions. 
Prompt text Write a board-level performance report for {{company_name}} for {{period}}.

Board-level reports have specific requirements:
- Strategic, not operational: focus on business outcomes, not activity
- Every number cited must be compared to a target or prior period
- Recommendations must be specific and actionable
- Maximum 2 pages of text

Structure:

1. Performance against strategic KPIs (table):
 - 4–6 strategic metrics only: revenue, growth rate, NPS, market share, or equivalent
 - Each: actual | target | vs target | trend

2. Strategic highlights (3 bullets max):
 - Major milestones achieved this period

3. Risks and challenges (3 bullets max):
 - Significant risks to the strategy with current mitigation status

4. Decisions required (if any):
 - Clearly state what decision is being asked of the board and by when
 - Provide the option set and a recommended option with rationale

5. Outlook:
 - Full-year forecast vs target
 - Top 2 tailwinds and headwinds going into next quarter

Tone: confident, precise, no jargon. Use active voice. Every paragraph should answer 'so what?' Copy prompt Open prompt details Beginner Single prompt 03 
### Dashboard Specification 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It creates a handoff-ready specification for building a dashboard with the right metrics, layout, and governance. 
Prompt text Write a dashboard specification document for a {{dashboard_name}} dashboard for {{audience}}.

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

Return: complete dashboard specification document. Copy prompt Open prompt details Advanced Single prompt 04 
### Metric Discrepancy Investigation 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It helps diagnose why two reports disagree on the same metric and how to align them. 
Prompt text Investigate why two reports are showing different values for the same metric: {{metric_name}}

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

Return: investigation log, root cause finding, and recommended fix to align both reports. Copy prompt Open prompt details Beginner Single prompt 05 
### Monthly Business Report 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It turns monthly performance data into a fuller management narrative with wins, misses, and outlook. 
Prompt text Write a monthly business performance report based on the data provided.

Structure:

1. Month in review (2–3 sentences): overall performance summary — was it a good month or a challenging one, and why?

2. Key metrics summary (table):
 - Each metric: this month | last month | MoM % | this month last year | YoY % | vs annual target (% complete)

3. Top 3 wins: specific achievements with numbers. What drove them?

4. Top 3 misses or concerns: what fell short of expectations? What is the root cause?

5. Deep dive (1 topic):
 - Choose the most important story in the data this month
 - 2–3 paragraphs with charts described in text
 - What is happening, why, and what should we do about it?

6. Forecast update:
 - Based on current month performance, update the full-year forecast
 - Are we on track, ahead, or behind the annual target?

7. Next month priorities: 3 focus areas with owner and measurable goal

Length: 600–800 words. Tone: professional but direct. No bullet soup — use paragraphs for the narrative sections. Copy prompt Open prompt details Advanced Chain 06 
### Reporting Strategy Chain 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It creates a full reporting model, including audit, hierarchy, calendar, governance, and glossary. 
Prompt text Step 1: Audit current reports — inventory all existing reports and dashboards. For each: audience, frequency, purpose, time to produce, and last known use date. Identify reports that are never used.
Step 2: Define reporting needs by audience tier — board (monthly, strategic), leadership (weekly, operational), team (daily, tactical). Define the right format, length, and metrics for each tier.
Step 3: Design the reporting hierarchy — create a single reporting framework where every metric rolls up consistently from team level to board level with no conflicting definitions.
Step 4: Retire redundant reports — list reports to discontinue. Draft a communication plan so stakeholders are not left without information.
Step 5: Build the reporting calendar — schedule all recurring reports with owners, data cut-off times, review deadlines, and distribution lists.
Step 6: Define the data glossary — for the top 20 metrics in the reporting suite, write agreed definitions, formulas, and data sources so there is one version of the truth.
Step 7: Write a reporting strategy document: current state assessment, proposed future state, transition plan, and governance model. Copy prompt Open prompt details Intermediate Single prompt 07 
### Self-Serve Analytics Spec 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It designs a self-serve analytics approach so a business team can answer common questions independently. 
Prompt text Design a self-serve analytics solution for {{business_team}} to answer their most common data questions without needing analyst support.

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

Return: question audit table, self-serve design spec, training plan, and governance rules. Copy prompt Open prompt details Beginner Single prompt 08 
### Weekly Business Review 

This prompt helps turn business data into reports, dashboards, and reporting systems that support decisions. It is best used when you need a clear reporting structure, an audience-specific narrative, or a specification that can be handed to analysts, BI developers, or leadership. It emphasizes clarity, consistency, and usefulness over raw data dumps. It produces a concise weekly narrative with scorecard, highlights, concerns, and next actions. 
Prompt text Generate a weekly business review report based on this data.

The report should follow this structure:

1. Executive headline (1 sentence): the single most important thing that happened this week

2. Scorecard (table format):
 - Each KPI: current week value | prior week value | WoW change % | vs target | status (🟢/🟡/🔴)

3. Highlights (3 bullet points):
 - What went well this week? Cite specific numbers.

4. Concerns (2–3 bullet points):
 - What needs attention? Cite specific numbers and why it matters.

5. Context:
 - Any external events, seasonality, or one-time factors that explain unusual movements

6. Actions:
 - 2–3 specific actions for next week with an owner and due date for each

7. Next week outlook:
 - What are we expecting? Any events or decisions coming up that will affect the metrics?

Tone: factual, direct, no jargon. Written for a general management audience. Maximum 400 words excluding the scorecard. Copy prompt Open prompt details 
## Recommended Reporting and Dashboards workflow 
1 
### Anomaly Narrative Writer 

Start with a focused prompt in Reporting and Dashboards so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Board-Level Report 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Dashboard Specification 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Metric Discrepancy Investigation 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
