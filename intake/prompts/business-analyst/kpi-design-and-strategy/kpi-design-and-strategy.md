# KPI Design and Strategy *AI Prompts *

9 Business Analyst prompts in KPI Design and Strategy. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain · 1 template. 

## AI prompts in KPI Design and Strategy 
9 prompts Beginner Single prompt 01 
### KPI Framework Builder 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It helps build a hierarchy of outcome, driver, and activity metrics tied to a strategic objective. 
Prompt text Design a KPI framework for {{business_area}} aligned to the strategic objective: {{strategic_objective}}

1. Define the measurement hierarchy:
 - Outcome KPIs (2–3): the ultimate business results we want to achieve
 - Driver KPIs (4–6): the leading indicators that predict and drive the outcomes
 - Activity metrics (6–8): the operational inputs we control directly

2. For each KPI define:
 - Name and plain-English definition
 - Formula or calculation method
 - Data source: where does the data come from?
 - Measurement frequency: daily / weekly / monthly
 - Owner: who is accountable?
 - Current baseline value (if known)
 - Target value and timeframe
 - Direction of improvement: higher is better / lower is better

3. Map the causal relationships: draw a simple KPI tree showing how activity metrics drive driver KPIs which drive outcome KPIs

4. Flag any KPI that cannot currently be measured (data gaps)

Return: KPI framework table, KPI tree diagram (text-based), and a data gap report. Copy prompt Open prompt details Advanced Chain 02 
### KPI Strategy Chain 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It creates a full measurement strategy from strategic goals through targets, owners, and reporting cadence. 
Prompt text Step 1: Align to strategy — map the business's stated strategic objectives to measurable outcomes. What does success look like in 12 months?
Step 2: Define the North Star Metric — identify the single metric that best captures customer value and predicts long-term business health.
Step 3: Build the metric tree — decompose the North Star into driver metrics and then into actionable input metrics. Map ownership at each level.
Step 4: Audit current metrics — review the existing KPI set against the new framework. Classify each as keep, modify, or retire.
Step 5: Fill gaps — identify business dimensions with no metric coverage. Propose new metrics with data source, owner, and measurement method.
Step 6: Set targets — for each metric in the final framework, set a baseline, a 12-month target, and an interim 90-day milestone.
Step 7: Write the KPI strategy document: one page covering — strategic alignment, NSM, metric framework summary, ownership table, targets, and reporting cadence. Copy prompt Open prompt details Intermediate Template 03 
### KPI Target Setting 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It compares multiple target-setting methods so teams can choose a realistic but ambitious KPI target. 
Prompt text Help set data-driven targets for the KPI: {{kpi_name}} for {{time_period}}.

Current performance data is provided. Use these four approaches and compare:

1. Historical trend extrapolation:
 - Fit a trend line to the last 12 months of data
 - Project forward to {{time_period}} end
 - Suggested target: trend projection + {{stretch_factor}}% improvement

2. Benchmarking:
 - Compare current performance to industry benchmarks (provide if known, otherwise note as assumption)
 - Target: close the gap to the industry median by 50% within {{time_period}}

3. Bottom-up driver modeling:
 - Identify the 2–3 key drivers of this KPI
 - Model the KPI impact of realistic improvements in each driver
 - Suggested target: sum of driver improvements

4. Top-down from business goal:
 - Start from the business revenue or growth target for {{time_period}}
 - Work backwards: what level of {{kpi_name}} is needed to achieve that goal?

Compare all four targets. Recommend a final target with rationale.
Return: target comparison table, recommended target, and confidence level (High / Medium / Low). Copy prompt Open prompt details Advanced Single prompt 04 
### Leading vs Lagging Indicators 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It helps balance predictive and outcome metrics so teams can act earlier, not just report after the fact. 
Prompt text Classify and balance the KPI set for {{business_area}} into leading and lagging indicators.

KPI list: {{kpi_list}}

Definitions:
- Lagging indicator: measures what has already happened (outcome). Reliable but too late to act on. Example: monthly revenue, customer churn rate.
- Leading indicator: predicts what will happen (predictor). Actionable now but harder to measure. Example: NPS, pipeline coverage ratio, trial activation rate.

For each KPI:
1. Classify: Leading / Lagging / Mixed
2. Time lag: how far in advance does this metric predict or reflect business performance?
3. Reliability: how strongly correlated is this metric with the business outcome it's supposed to predict?

Then:
4. Assess balance: most teams over-index on lagging metrics. Is this set balanced?
5. For each lagging KPI, suggest a corresponding leading indicator
6. Identify the 2 leading indicators with the strongest predictive relationship to the most important outcome metric

Return: classification table, balance assessment, and leading/lagging pairs. Copy prompt Open prompt details Advanced Single prompt 05 
### Metric Decomposition Tree 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It breaks a top-level KPI into the smaller levers that teams can understand and influence. 
Prompt text Build a full metric decomposition tree for the top-level metric: {{top_metric}}

A decomposition tree breaks a top-level metric into its component parts, making it possible to diagnose exactly which lever to pull when the metric moves.

1. Level 1 decomposition: break {{top_metric}} into its arithmetic components
 - Example: Revenue = Users × Conversion Rate × Average Order Value
2. Level 2 decomposition: break each Level 1 component further
 - Example: Users = New Users + Returning Users
3. Level 3 decomposition where meaningful
4. For each leaf node in the tree:
 - Current value (if available)
 - Which team or person owns it
 - How quickly it can realistically change
 - What specific actions move it
5. Identify which leaf nodes have the highest leverage — a 10% improvement in which node would move the top metric the most?
6. Identify which leaf nodes are currently unmeasured

Return: full decomposition tree (text format), leverage analysis table, and measurement gap list. Copy prompt Open prompt details Intermediate Single prompt 06 
### Metric Health Check 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It audits whether existing KPIs are still relevant, actionable, and worth keeping. 
Prompt text Audit the existing KPI set for {{business_area}} and assess its health.

Existing KPIs: {{kpi_list}}

For each KPI, evaluate:
1. Relevance: does it still align to current business strategy? (Yes / Partially / No)
2. Actionability: if this metric moves, does the team know what to do? (High / Medium / Low)
3. Measurability: is it reliably measured with good data quality? (High / Medium / Low)
4. Frequency: is it measured and reviewed frequently enough to drive action?
5. Gaming risk: can someone make this metric look good without creating real value? (High / Medium / Low)
6. Overlap: is it redundant with another metric in the set?

After auditing each KPI:
- Recommend which KPIs to keep, modify, retire, or replace
- Identify any important business dimensions that have no KPI coverage
- Suggest the ideal total number of KPIs for this team (rule of thumb: 5–8 for a team, 3–5 for an individual)

Return: KPI health scorecard, recommended actions per KPI, and gaps in metric coverage. Copy prompt Open prompt details Beginner Single prompt 07 
### North Star Metric Definition 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It helps teams identify the one metric that best captures customer value and long-term business progress. 
Prompt text Help define the North Star Metric (NSM) for this business or product: {{business_description}}

1. Explain what makes a good North Star Metric:
 - It measures value delivered to customers, not just revenue
 - It is a leading indicator of long-term growth
 - The whole company can influence it
 - It is a single number everyone understands

2. Propose 3 candidate North Star Metrics for this business, with for each:
 - Metric name and definition
 - Why it captures customer value
 - How it connects to revenue
 - How measurable it is today
 - Potential gaming risks (can it be gamed without delivering real value?)

3. Recommend the best candidate with a clear rationale

4. Define the input metrics (3–5) that the teams would manage to move the NSM

5. Write a one-paragraph NSM narrative: 'We grow revenue by doing X, which creates value for customers by Y, and our North Star Metric captures this by measuring Z.'

Return: candidate comparison table, recommended NSM, input metrics, and NSM narrative. Copy prompt Open prompt details Intermediate Single prompt 08 
### OKR Design 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It structures objectives and measurable key results so a team can align execution with strategy. 
Prompt text Design a set of OKRs (Objectives and Key Results) for {{team_or_department}} for {{time_period}}.

Context: {{strategic_context}}

For each OKR:
1. Write the Objective: inspiring, qualitative, direction-setting. It should answer 'where do we want to go?'
2. Write 3–4 Key Results per objective:
 - Quantitative and measurable: must include a specific number
 - Outcome-focused, not activity-focused: 'Increase NPS from 32 to 45' not 'Run 10 customer surveys'
 - Ambitious but achievable: 70% achievement should feel like success
 - Time-bound: achievable within the OKR period
3. For each Key Result:
 - Current baseline value
 - Target value
 - Measurement method
 - Owner
4. Check OKR quality:
 - Do the Key Results, if all achieved, guarantee the Objective is met?
 - Are any Key Results actually activities or outputs rather than outcomes?
 - Do they connect to the company-level OKRs?

Return: formatted OKR set, quality check assessment, and an alignment map showing how these OKRs ladder up to company goals. Copy prompt Open prompt details Intermediate Single prompt 09 
### Vanity vs Actionable Metrics 

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It helps separate impressive-looking metrics from the ones that actually guide action and performance. 
Prompt text Review this list of metrics and classify each as a vanity metric or an actionable metric: {{metrics_list}}

Definitions:
- Vanity metric: looks impressive, grows over time, but doesn't tell you what to do or predict business success (e.g. total registered users, page views, app downloads)
- Actionable metric: directly tied to business outcomes, tells you what to do when it changes, and can be influenced by specific team actions (e.g. activation rate, revenue per user, week-2 retention)

For each metric:
1. Classification: Vanity / Actionable / Context-dependent
2. Why: one sentence explanation
3. If vanity: suggest the actionable version (e.g. replace 'registered users' with 'weekly active users')
4. If actionable: confirm which team owns it and what actions move it

Then:
5. Identify the 3 most important actionable metrics from the list
6. Flag any critical business dimension (revenue, retention, acquisition, engagement) with no actionable metric coverage

Return: classification table, recommended replacements, and coverage gaps. Copy prompt Open prompt details 
## Recommended KPI Design and Strategy workflow 
1 
### KPI Framework Builder 

Start with a focused prompt in KPI Design and Strategy so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### KPI Strategy Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### KPI Target Setting 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Leading vs Lagging Indicators 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
