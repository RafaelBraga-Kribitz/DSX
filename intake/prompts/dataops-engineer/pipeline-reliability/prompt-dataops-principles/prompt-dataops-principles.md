# DataOps Principles and Practices *AI Prompt *

Apply DataOps principles to improve the reliability and speed of this data pipeline. Current pipeline: {{pipeline_description}} Pain points: {{pain_points}} (long release cycles... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply DataOps principles to improve the reliability and speed of this data pipeline.

Current pipeline: {{pipeline_description}}
Pain points: {{pain_points}} (long release cycles, data quality issues, slow debugging, etc.)
Team: {{team}}

1. DataOps core principles:
 - Automated testing: every data transformation is tested before it reaches production
 - Continuous delivery: pipeline changes deploy frequently with automated validation
 - Monitoring: every pipeline has health metrics and alerts
 - Version control: all pipeline code, configurations, and SQL are in git
 - Collaboration: data engineers and data consumers work together in the feedback loop

2. DataOps maturity model:
 Level 1 (manual): ad-hoc pipelines, no tests, deployments are manual and infrequent
 Level 2 (repeatable): pipelines in version control, some tests, scheduled deployments
 Level 3 (defined): automated CI/CD, comprehensive tests, monitoring with alerting
 Level 4 (managed): data contracts, SLA tracking, automated anomaly detection
 Level 5 (optimizing): self-healing pipelines, automated root cause analysis

3. Quick wins (Level 1 → Level 3 in 4 weeks):
 Week 1: Move all pipeline code to git; add README.md for each pipeline
 Week 2: Add smoke tests and schema validation to CI
 Week 3: Set up monitoring (freshness alerts, row count tracking)
 Week 4: Automate deployment; require PR reviews before merging

4. Pipeline contract:
 Every pipeline should define and publish:
 - Input schema and freshness SLA
 - Output schema and freshness SLA
 - Owner and on-call rotation
 - Known failure modes and recovery procedure

5. Feedback loops:
 - Development feedback: tests run in < 10 minutes in CI
 - Production feedback: monitoring alerts within 15 minutes of a failure
 - Consumer feedback: data quality issues reported via a defined channel

Return: maturity assessment, quick win roadmap, pipeline contract template, and feedback loop design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pipeline reliability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Pipeline Reliability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as DataOps core principles:, Automated testing: every data transformation is tested before it reaches production, Continuous delivery: pipeline changes deploy frequently with automated validation. The final answer should stay clear, actionable, and easy to review inside a pipeline reliability workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Reliability.
