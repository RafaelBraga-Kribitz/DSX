# Pipeline Dependency Management *AI Prompt *

Design a robust dependency management system for interconnected data pipelines. Pipelines: {{pipeline_list}} Dependency graph: {{dependencies}} (which pipelines consume outputs... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a robust dependency management system for interconnected data pipelines.

Pipelines: {{pipeline_list}}
Dependency graph: {{dependencies}} (which pipelines consume outputs of others)
Orchestrator: {{orchestrator}}

1. Dependency types:
 - Direct data dependency: pipeline B reads from a table written by pipeline A → A must complete before B
 - Time dependency: pipeline B runs after pipeline A completes on the same execution date
 - External dependency: pipeline B requires a file to arrive in S3 from an external system

2. Airflow dependency patterns:

 Within a DAG:
 extract_task >> transform_task >> load_task

 Across DAGs (ExternalTaskSensor):
 ExternalTaskSensor(
 task_id='wait_for_upstream',
 external_dag_id='upstream_pipeline',
 external_task_id='final_task',
 timeout=7200, # 2 hours max wait
 poke_interval=60
 )

 Data-aware scheduling (Airflow 2.4+):
 @dag(schedule=[Dataset('s3://bucket/orders/latest')])
 def downstream_pipeline():
 ...
 # Triggers when the upstream pipeline updates the dataset

3. External file arrival:
 S3KeySensor(
 task_id='wait_for_file',
 bucket_name='uploads',
 bucket_key='daily_report_{{ ds }}.csv',
 timeout=3600
 )

4. SLA-aware dependencies:
 - If upstream is late: should downstream wait or run with available data?
 - Decision: for time-critical downstream (exec dashboard): wait up to 2 hours then alert
 - Decision: for non-critical downstream: run with available data; log a warning

5. Dependency documentation:
 - Maintain a dependency registry: each pipeline lists its upstream and downstream dependencies
 - Visualize with Airflow's DAG graph view or a data lineage tool (DataHub, Atlan)
 - Impact analysis: before changing any pipeline, check: 'which downstream pipelines depend on this output?'

Return: dependency wiring code, sensor configuration, data-aware scheduling setup, SLA handling policy, and dependency registry format. 
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

The AI should return a structured result that covers the main requested outputs, such as Dependency types:, Direct data dependency: pipeline B reads from a table written by pipeline A → A must complete before B, Time dependency: pipeline B runs after pipeline A completes on the same execution date. The final answer should stay clear, actionable, and easy to review inside a pipeline reliability workflow for dataops engineer work. 

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
