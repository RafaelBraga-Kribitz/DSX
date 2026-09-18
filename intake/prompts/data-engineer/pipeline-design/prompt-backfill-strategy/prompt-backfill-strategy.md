# Backfill Strategy *AI Prompt *

This prompt designs a controlled backfill process that minimizes risk to production tables, source systems, and downstream consumers. It is especially useful for correcting historical logic, replaying missed data, or reprocessing after a bug fix. The prompt emphasizes isolation, checkpointing, validation, and rollback readiness. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a safe, efficient backfill strategy for re-processing historical data in this pipeline.

Pipeline: {{pipeline_description}}
Data range to backfill: {{date_range}}
Estimated data volume: {{volume}}
Downstream dependencies: {{downstream_tables}}

1. Backfill isolation:
 - Never write backfill output to the production table directly during processing
 - Write to a staging table or partition-isolated location first
 - Swap into production atomically after validation

2. Partitioned backfill approach:
 - Process one date partition at a time to limit blast radius
 - Use a date loop: for each date in the range, submit an independent job
 - Parallelism: how many partitions can safely run in parallel without overloading the source system or cluster?
 - Checkpoint completed partitions: re-running the backfill skips already-completed dates

3. Source system protection:
 - Throttle extraction queries to avoid overwhelming the source (use LIMIT/offset pagination or time-boxed micro-batches)
 - Schedule backfill during low-traffic hours if source is OLTP
 - Use read replicas if available

4. Downstream impact management:
 - Notify downstream consumers before starting the backfill
 - If downstream tables are materialized from this table, suspend their refresh until backfill is complete
 - After backfill: re-run downstream tables in dependency order

5. Validation before cutover:
 - Row count: does the backfilled output match expected counts?
 - Key uniqueness: no duplicate primary keys in the output
 - Metric spot check: compare aggregated metrics for a sample of dates to the source system

6. Rollback plan:
 - If validation fails: what is the procedure to restore the previous state?

Return: backfill execution script, validation checks, downstream notification template, and rollback procedure. 
```

## When to use this prompt 
Use case 01 
When historical data must be reprocessed safely. 
Use case 02 
When fixing logic bugs that affected past partitions. 
Use case 03 
When planning a large replay that could affect downstream consumers. 
Use case 04 
When you need a cutover and rollback process, not just extraction code. 

## What the AI should return 

Return an end-to-end backfill plan with execution steps, partition strategy, source protection controls, validation checks, and rollback procedure. Include example scripts or pseudocode for checkpointing and cutover. Also provide a downstream communication template and post-backfill dependency refresh order. 

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
