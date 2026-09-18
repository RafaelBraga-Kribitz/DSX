# Self-Healing Pipeline Patterns *AI Prompt *

Design self-healing mechanisms for this data pipeline that automatically detect and recover from common failures. Pipeline: {{pipeline}} Common failure modes: {{failure_modes}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design self-healing mechanisms for this data pipeline that automatically detect and recover from common failures.

Pipeline: {{pipeline}}
Common failure modes: {{failure_modes}}
Recovery SLA: {{recovery_sla}}

1. Automatic retry with backoff:
 - Retry transient failures: network timeouts, API rate limits, temporary resource unavailability
 - Exponential backoff: 1s → 2s → 4s → 8s (max 3 retries)
 - Circuit breaker: after 3 consecutive failures, stop retrying and alert humans
 - Idempotent design: retries require idempotent operations (UPSERT, not INSERT)

2. Automatic data quality remediation:
 - If a source file has schema drift: route to a quarantine path; send an alert; process the rest
 - If row count is 0 (source empty): skip the run; do not overwrite the target with empty data
 - If a critical DQ test fails: pause downstream pipelines; alert; wait for human sign-off

3. Backfill automation:
 - Detect gaps: query the output table for missing date partitions
 - Auto-trigger backfill: if a gap is detected, automatically trigger a backfill run for the missing partition
 - Airflow implementation: a 'gap detection' DAG runs daily; if gaps found, it triggers the backfill DAG

4. Stale data prevention:
 - Before overwriting a table with a new run, compare: does the new data have >= the expected row count?
 - If new data is suspiciously small (< 50% of yesterday): abort the write; alert

5. Fallback data:
 - For non-critical data: if the fresh run fails, serve the last known good data with a staleness warning
 - Maintain a 'last_successful_run' timestamp per table for staleness calculations
 - Never serve data older than {{max_staleness}} without an explicit staleness flag for consumers

Return: retry and backoff configuration, quality remediation rules, gap detection and backfill automation, stale data prevention, and fallback data strategy. 
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

The AI should return a structured result that covers the main requested outputs, such as Automatic retry with backoff:, Retry transient failures: network timeouts, API rate limits, temporary resource unavailability, Exponential backoff: 1s → 2s → 4s → 8s (max 3 retries). The final answer should stay clear, actionable, and easy to review inside a pipeline reliability workflow for dataops engineer work. 

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
