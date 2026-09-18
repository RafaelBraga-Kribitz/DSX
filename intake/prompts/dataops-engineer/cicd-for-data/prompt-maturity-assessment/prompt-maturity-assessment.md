# DataOps Maturity Assessment *AI Prompt *

Conduct a DataOps maturity assessment for this data team and create an improvement roadmap. Team: {{team_description}} Current practices: {{current_practices}} Pain points: {{pa... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a DataOps maturity assessment for this data team and create an improvement roadmap.

Team: {{team_description}}
Current practices: {{current_practices}}
Pain points: {{pain_points}}
Goals: {{goals}}

1. Maturity dimensions to assess (score 1-5 each):

 Version control:
 1: No version control; SQL in spreadsheets / ad-hoc scripts
 3: All code in git; PRs required for changes
 5: All code, config, and DDL in git; automated linting and formatting

 Automated testing:
 1: No automated tests; manual QA before deployment
 3: Unit tests for transformations; basic schema tests
 5: Full test pyramid; contract tests; automated regression testing

 CI/CD:
 1: Manual deployments; no CI
 3: CI runs on PR; deployment is semi-automated with a manual step
 5: Fully automated CI/CD; canary deployments; automated rollback

 Monitoring and alerting:
 1: Consumers notice data issues before the data team
 3: Pipeline success/failure alerts; basic freshness monitoring
 5: Comprehensive quality monitoring; anomaly detection; SLA tracking per table

 Documentation:
 1: No documentation; knowledge in people's heads
 3: Key models documented in the catalog; ownership assigned
 5: All assets documented; auto-updated catalog; data contracts for all public data products

 Incident management:
 1: Ad-hoc response; no runbooks
 3: Runbooks for common failures; post-mortems for major incidents
 5: Automated incident detection; auto-remediation for known failure patterns; blameless post-mortems

2. Current state scoring:
 Score each dimension for the current team.
 Identify: the two lowest-scoring dimensions (highest improvement opportunity).

3. 90-day improvement roadmap:
 Based on the lowest scores, propose 3 high-impact initiatives for the next 90 days.
 Each initiative: title, current state, target state, actions, owner, success metric.

4. Quick wins (< 2 weeks each):
 Identify 3 changes that can be made immediately with high visibility impact.

Return: maturity scorecard for each dimension, gap analysis, 90-day roadmap, and quick wins. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin ci/cd for data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in CI/CD for Data or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Maturity dimensions to assess (score 1-5 each):, Current state scoring:, 90-day improvement roadmap:. The final answer should stay clear, actionable, and easy to review inside a ci/cd for data workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for Data.
