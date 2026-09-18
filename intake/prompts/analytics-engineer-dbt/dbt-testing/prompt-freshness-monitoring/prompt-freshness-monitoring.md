# dbt Data Freshness and Monitoring *AI Prompt *

Configure source freshness monitoring and anomaly detection for this dbt project. Sources: {{sources}} SLA requirements: {{sla}} (e.g. dashboard data must be < 4 hours old) Aler... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Configure source freshness monitoring and anomaly detection for this dbt project.

Sources: {{sources}}
SLA requirements: {{sla}} (e.g. dashboard data must be < 4 hours old)
Alert channel: {{alerts}} (Slack, PagerDuty, email)

1. Source freshness config in sources.yml:
 sources:
 - name: stripe
 database: raw
 schema: stripe
 loaded_at_field: _fivetran_synced
 freshness:
 warn_after: {count: 6, period: hour}
 error_after: {count: 24, period: hour}
 tables:
 - name: charges
 freshness:
 warn_after: {count: 2, period: hour}
 error_after: {count: 6, period: hour}

2. Run freshness checks:
 dbt source freshness
 - Queries each source table for the MAX of the loaded_at_field
 - Reports: pass / warn / error per source table
 - Integrate into CI: fail the pipeline if any source is in error state

3. Model-level recency test (dbt-utils):
 - name: recency
 config:
 severity: warn
 meta:
 description: 'Orders table should have records from today'
 tests:
 - dbt_utils.recency:
 datepart: hour
 field: created_at
 interval: 6

4. Row count anomaly detection:
 - dbt-expectations: expect_table_row_count_to_be_between
 min_value: 1000
 max_value: 500000
 - Or: custom singular test comparing today's row count to 7-day rolling average
 SELECT ABS(today_count - avg_7d) / avg_7d AS pct_deviation
 FROM daily_counts
 WHERE pct_deviation > 0.3

5. Elementary (open-source dbt monitoring):
 - Installs as a dbt package
 - Monitors: row count anomalies, null rate, uniqueness, distribution shifts
 - Sends Slack alerts with anomaly details and a link to the affected model
 - config: elementary_timeframe_days: 30, anomaly_sensitivity: 3

6. Alerting integration:
 - On dbt Cloud: set up job notifications to Slack on failure
 - Custom: parse dbt run results JSON and post to Slack webhook
 artifacts/run_results.json → filter status == 'error' → Slack message

Return: sources.yml freshness config, recency test configuration, row count anomaly detection SQL, Elementary setup, and alerting integration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Testing or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Source freshness config in sources.yml:, name: stripe, name: charges. The final answer should stay clear, actionable, and easy to review inside a dbt testing workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Testing.
