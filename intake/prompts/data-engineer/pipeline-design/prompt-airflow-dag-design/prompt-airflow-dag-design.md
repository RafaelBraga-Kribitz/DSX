# DAG Design for Airflow *AI Prompt *

This prompt is for designing an Airflow DAG that follows solid orchestration practices instead of becoming a fragile collection of tasks. It pushes for clear task boundaries, safe reruns, operational alerting, and maintainable code structure. It is best used when you want both a design and executable starter code. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement an Airflow DAG for this pipeline.

Pipeline requirements: {{pipeline_requirements}}
Schedule: {{schedule}}
Dependencies: {{upstream_dependencies}}

1. DAG structure best practices:
 - Use @dag decorator with explicit schedule, catchup=False, and max_active_runs=1
 - Set meaningful dag_id, description, and tags
 - Define default_args with retries=3, retry_delay=timedelta(minutes=5), retry_exponential_backoff=True
 - Set execution_timeout per task to prevent hung tasks from blocking slots

2. Task design:
 - Keep tasks small and single-responsibility (one logical operation per task)
 - Use TaskFlow API (@task decorator) for Python tasks — cleaner than PythonOperator
 - Use KubernetesPodOperator for heavy workloads — isolates dependencies and resources
 - Avoid pulling large datasets into Airflow worker memory — use Spark/dbt/SQL for heavy transforms

3. Dependencies and branching:
 - Define task dependencies with >> and << operators
 - Use BranchPythonOperator for conditional logic
 - Use TriggerDagRunOperator for cross-DAG dependencies (prefer sensors for blocking waits)

4. Idempotency:
 - All tasks must be safely re-runnable
 - Use execution_date in file paths and table partition filters to scope each run

5. Alerting:
 - on_failure_callback: send Slack alert with DAG name, task, execution_date, and log URL
 - SLA miss callback: alert if DAG does not complete within SLA

6. Testing:
 - Unit test task logic separately from the DAG
 - Use airflow dags test dag_id execution_date for local DAG runs

Return: complete DAG code with all operators, dependencies, and alerting. 
```

## When to use this prompt 
Use case 01 
When creating a new Airflow pipeline from requirements. 
Use case 02 
When refactoring a messy DAG into a cleaner design. 
Use case 03 
When standardizing DAG conventions across a data engineering team. 
Use case 04 
When you need production-ready orchestration code with alerting and retries. 

## What the AI should return 

Return complete Airflow DAG code plus a short explanation of the task structure, dependencies, and idempotency strategy. Include retry behavior, failure callbacks, SLA handling, and notes on where heavy processing should live outside Airflow. The response should be directly usable as a starting point in a repo. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Design.
