# Data Quality Framework Chain *AI Prompt *

This prompt assembles a full data quality operating model, not just individual checks. It covers critical-table selection, testing, severity, routing, scorecards, incidents, and continuous feedback. It is best used when an organization wants a formal DQ framework with ownership and response expectations. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: DQ requirements — identify the top 10 most critical tables in the platform. For each, define: the business impact of bad data, the acceptable error rate, and the SLA for detecting and resolving issues.
Step 2: Test implementation — for each critical table, implement the full test suite: schema, freshness, row count reconciliation, business rule validation, and statistical anomaly detection.
Step 3: Severity and routing — classify each test by severity (blocking vs warning) and define the alert routing: who gets notified, by which channel, and within what time window.
Step 4: DQ scorecard — build a daily DQ scorecard: overall pass rate, test pass rate per table, trend over time, and highlight tables with declining quality.
Step 5: Incident workflow — define the incident workflow for DQ failures: detection → acknowledgment → investigation → root cause → fix → post-mortem. Define SLAs per severity.
Step 6: Feedback loop — create a mechanism for analysts to report suspected data quality issues. Triage reported issues, trace to root cause, and update tests to prevent recurrence.
Step 7: Write the DQ framework document: test inventory, severity matrix, alert routing, SLAs, incident workflow, and the governance process for adding new tests. 
```

## When to use this prompt 
Use case 01 
When creating a platform-wide data quality program. 
Use case 02 
When critical tables need differentiated SLAs and alerting. 
Use case 03 
When incidents must be managed consistently across teams. 
Use case 04 
When you want a DQ framework document, not only test code. 

## What the AI should return 

Return a full framework covering table prioritization, test inventory, severity matrix, routing rules, scorecard design, incident workflow, and governance. Include how issues are reported, triaged, fixed, and prevented from recurring. The result should read like a data quality operating model for the organization. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
