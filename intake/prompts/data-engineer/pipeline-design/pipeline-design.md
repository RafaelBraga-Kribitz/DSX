# Pipeline Design *AI Prompts *

10 Data Engineer prompts in Pipeline Design. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 9 single prompts · 1 chain. 

## AI prompts in Pipeline Design 
10 prompts Advanced Single prompt 01 
### Backfill Strategy 

This prompt designs a controlled backfill process that minimizes risk to production tables, source systems, and downstream consumers. It is especially useful for correcting historical logic, replaying missed data, or reprocessing after a bug fix. The prompt emphasizes isolation, checkpointing, validation, and rollback readiness. 
Prompt text Design a safe, efficient backfill strategy for re-processing historical data in this pipeline.

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

Return: backfill execution script, validation checks, downstream notification template, and rollback procedure. Copy prompt Open prompt details Beginner Single prompt 02 
### DAG Design for Airflow 

This prompt is for designing an Airflow DAG that follows solid orchestration practices instead of becoming a fragile collection of tasks. It pushes for clear task boundaries, safe reruns, operational alerting, and maintainable code structure. It is best used when you want both a design and executable starter code. 
Prompt text Design and implement an Airflow DAG for this pipeline.

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

Return: complete DAG code with all operators, dependencies, and alerting. Copy prompt Open prompt details Intermediate Single prompt 03 
### dbt Project Structure 

This prompt defines how to structure a dbt project so that models remain understandable, testable, and maintainable as the warehouse grows. It is useful for teams that want consistent naming, layer separation, materialization choices, testing, and CI rules from the start. It encourages a scalable project layout rather than ad hoc model sprawl. 
Prompt text Design the dbt project structure for a data warehouse with {{num_source_systems}} source systems.

1. Directory structure:
```
models/
 staging/ # 1:1 with source tables, light cleaning only
 source_a/
 source_b/
 intermediate/ # Business logic, joining staging models
 marts/
 core/ # Shared dimension and fact tables
 finance/ # Domain-specific marts
 marketing/
tests/
 generic/ # Custom generic tests
 singular/ # One-off data quality tests
macros/
seeds/
snapshots/
```

2. Model naming conventions:
 - Staging: stg_{source}__{entity} (e.g. stg_salesforce__accounts)
 - Intermediate: int_{entity}_{verb} (e.g. int_orders_pivoted)
 - Marts: {entity} or dim_{entity} / fct_{entity}

3. Materialization strategy:
 - Staging: view (always fresh, no storage cost)
 - Intermediate: ephemeral or table depending on complexity
 - Marts: table or incremental depending on size and freshness requirements

4. Sources configuration (sources.yml):
 - Define all source tables with freshness checks
 - freshness: warn_after: {count: 12, period: hour}, error_after: {count: 24, period: hour}

5. Model configuration (schema.yml):
 - Document every model and column
 - Apply generic tests: unique, not_null, accepted_values, relationships

6. Incremental models:
 - Use unique_key for merge strategy
 - Filter with is_incremental() macro: WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
 - Handle late-arriving data with a lookback window

7. CI/CD integration:
 - dbt build --select state:modified+ on PRs (only changed models and their downstream)
 - dbt test --select source:* for source freshness checks

Return: directory structure, naming convention guide, materialization decision matrix, and CI/CD integration config. Copy prompt Open prompt details Intermediate Single prompt 04 
### Incremental Load Design 

This prompt designs a dependable incremental loading strategy with explicit handling for watermarks, upserts, deletes, replay, and schema drift. It is aimed at pipelines that must run repeatedly without duplicates, data loss, or hard-to-debug edge cases. The output should emphasize deterministic windows and operational safety. 
Prompt text Design a robust incremental data load pattern for this source table.

Source: {{source_table}} in {{source_db}}
Target: {{target_table}} in {{target_db}}
Update pattern: {{update_pattern}} (append-only / append-and-update / full CRUD)

1. Watermark management:
 - Store the last successful watermark (max updated_at or max id) in a dedicated metadata table
 - Watermark must be committed only after successful write to target — never before
 - Handle clock skew: use watermark = max(updated_at) - safety_margin (e.g. 5 minutes) to catch late-arriving rows

2. Incremental query:
 - SELECT * FROM source WHERE updated_at > {{last_watermark}} AND updated_at <= {{current_run_time}}
 - Use a closed upper bound (current run time) to make the window deterministic and replayable
 - Add an ORDER BY to ensure consistent extraction order

3. Merge/upsert to target:
 - Use MERGE statement (or equivalent) matching on primary key
 - Handle inserts (new rows), updates (changed rows), and optionally soft deletes (is_deleted flag)
 - Never use INSERT blindly — always upsert to maintain idempotency

4. Hard delete handling:
 - If source supports deletes and CDC is not available: run a full key scan periodically (e.g. daily) and soft-delete rows absent from source
 - Add deleted_at and is_current columns to target table

5. Backfill procedure:
 - To re-process a date range: set watermark back to range start and re-run
 - Ensure the merge logic is idempotent so backfill does not create duplicates

6. Schema change handling:
 - Before each run, compare source schema to last known schema
 - Alert on new, removed, or type-changed columns before proceeding

Return: watermark table DDL, incremental query, merge statement, delete handling, and backfill procedure. Copy prompt Open prompt details Beginner Single prompt 05 
### Ingestion Pattern Selector 

This prompt helps choose the right ingestion pattern for a source based on latency, volume, change behavior, and source-system constraints. It avoids the common mistake of defaulting to full loads or CDC without checking whether the source and business requirements justify that choice. The result should balance simplicity, correctness, source impact, and future scalability. 
Prompt text Recommend the right data ingestion pattern for this source system.

Source system: {{source_system}}
Data characteristics: {{data_characteristics}}
Latency requirement: {{latency_requirement}}
Volume: {{volume}}

Evaluate and recommend from these patterns:

1. Full load:
 - Re-ingest the entire source table on every run
 - When to use: small tables (<1M rows), no reliable change tracking, sources that cannot support incremental queries
 - Drawbacks: expensive, slow, high source system load

2. Incremental load (timestamp-based):
 - Query rows where updated_at > last_watermark
 - When to use: source has a reliable updated_at column, append-and-update workloads
 - Drawbacks: misses hard deletes, requires reliable timestamp column

3. Change Data Capture (CDC):
 - Read from database transaction log (Debezium, AWS DMS, Fivetran)
 - When to use: need to capture deletes, near-real-time latency, high-volume OLTP source
 - Drawbacks: requires log access, more complex infrastructure

4. Event streaming:
 - Source publishes events to Kafka/Kinesis, pipeline consumes
 - When to use: event-driven architecture already exists, sub-minute latency needed
 - Drawbacks: requires event producer instrumentation

5. API polling:
 - Call REST/GraphQL API on schedule
 - When to use: no database access, SaaS sources (Salesforce, HubSpot)
 - Drawbacks: rate limits, pagination, no deletes

Return: recommended pattern with rationale, drawbacks to be aware of, and implementation checklist. Copy prompt Open prompt details Advanced Single prompt 06 
### Lambda vs Kappa Architecture 

This prompt compares Lambda and Kappa architectures for use cases that combine historical processing with low-latency needs. It helps teams avoid choosing an architecture based on buzzwords rather than processing logic, replay needs, and operational complexity. The answer should clearly apply the trade-offs to the specific use case. 
Prompt text Evaluate whether this use case calls for a Lambda architecture or a Kappa architecture.

Use case: {{use_case_description}}
Latency requirements: {{latency}}
Historical reprocessing need: {{reprocessing_need}}
Team size and complexity tolerance: {{team_constraints}}

1. Lambda architecture:
 - Two separate pipelines: batch (accurate, slow) and speed (fast, approximate)
 - Serving layer merges batch and speed views
 - Pros: handles historical reprocessing naturally, speed layer can be simpler
 - Cons: two codebases for the same logic (duplication and drift risk), higher operational complexity
 - When to choose: if batch and streaming have genuinely different business logic, or if batch accuracy is non-negotiable and streaming is additive

2. Kappa architecture:
 - Single streaming pipeline for everything
 - Reprocessing = replay from beginning of the message log with a new consumer group
 - Pros: single codebase, simpler operations, no view merging
 - Cons: requires a long-retention message log, streaming system must handle batch-scale replay, stateful processing is more complex
 - When to choose: when batch and streaming logic are identical, team wants to minimize operational surface area

3. Decision framework:
 - Is the processing logic identical for batch and streaming? → Kappa
 - Do you need to reprocess years of history frequently? → Check if Kappa replay is cost-effective
 - Is your team small? → Kappa (less to maintain)
 - Do you have complex, different historical vs real-time logic? → Lambda
 - Is latency requirement < 1 minute AND accuracy is critical? → Lambda with micro-batch

4. Recommended architecture for this use case:
 - State the recommendation clearly with rationale
 - Identify the top 2 risks of the chosen approach and mitigations

Return: architecture comparison, decision framework applied to this use case, recommendation, and risk register. Copy prompt Open prompt details Beginner Single prompt 07 
### Pipeline Architecture Review 

This prompt reviews a pipeline design as a production system rather than just a diagram. It helps uncover reliability, idempotency, observability, scalability, and maintainability risks before they become outages or expensive rebuilds. It is especially useful when a team has a proposed architecture but needs a structured technical critique. 
Prompt text Review this data pipeline architecture and identify weaknesses.

Pipeline description: {{pipeline_description}}

Evaluate across these dimensions and flag each as Critical / Warning / Info:

1. Reliability:
 - Is there a single point of failure? What happens if any one component goes down?
 - Are retries implemented with exponential backoff and jitter?
 - Is there a dead-letter queue or error sink for failed records?
 - Are downstream consumers protected from upstream failures (circuit breaker)?

2. Idempotency:
 - Can the pipeline be safely re-run without producing duplicate data?
 - Is the write operation upsert/merge rather than append-only?
 - If append-only, is there a deduplication step downstream?

3. Observability:
 - Are row counts logged at every stage (source, after transformation, at sink)?
 - Is there alerting on pipeline failure, SLA breach, and anomalous record counts?
 - Can you trace a single record from source to destination?

4. Scalability:
 - Will the design hold at 10× current data volume?
 - Are there any sequential bottlenecks that cannot be parallelized?

5. Maintainability:
 - Is business logic separated from infrastructure concerns?
 - Are transformations testable in isolation?

Return: issue list with severity, impact, and specific remediation for each finding. Copy prompt Open prompt details Advanced Chain 08 
### Pipeline Design Chain 

This prompt chains together the full data pipeline design process from requirements to architecture document. It is meant for larger designs where ingestion, storage, processing, orchestration, and monitoring all need to fit together coherently. It works best when you want a system-level blueprint instead of isolated recommendations. 
Prompt text Step 1: Requirements gathering — define: source systems and their characteristics (volume, velocity, format, update pattern), latency SLA (batch/micro-batch/real-time), downstream consumers and their needs, and any compliance or data residency constraints.
Step 2: Ingestion pattern selection — for each source, select the appropriate ingestion pattern (full load, incremental, CDC, streaming, API polling) with rationale. Identify which sources need CDC and what infrastructure that requires.
Step 3: Processing layer design — choose the processing technology (dbt, Spark, Flink, SQL) for each transformation layer. Define the medallion layers (Bronze/Silver/Gold or equivalent) and what transformations happen at each layer.
Step 4: Storage and partitioning — design the storage layout for each layer. Define partitioning strategy, file format (Parquet/Delta/Iceberg), and retention policy. Estimate storage cost.
Step 5: Orchestration design — design the DAG structure. Define dependencies between pipelines, scheduling strategy, SLA per pipeline, retry policy, and alerting.
Step 6: Reliability and observability — define: row count reconciliation checks, data freshness monitoring, lineage tracking, alerting thresholds, and incident response procedure.
Step 7: Write the pipeline design document: architecture diagram (text), technology choices with rationale, data flow description, SLA commitments, known risks, and estimated build timeline. Copy prompt Open prompt details Intermediate Single prompt 09 
### Spark Job Optimization 

This prompt focuses on improving Spark jobs by diagnosing the real bottleneck before suggesting tuning changes. It helps teams reason about partitioning, skew, joins, caching, shuffle behavior, and cluster configuration in a disciplined way. The goal is not random tuning tips, but an optimization plan tied to runtime and cost impact. 
Prompt text Optimize this Spark job for performance, cost, and reliability.

Current job: {{job_description}}
Current runtime: {{current_runtime}}
Current cost: {{current_cost}}

1. Diagnose first with Spark UI:
 - Identify stages with the longest duration
 - Check for data skew: are some partitions processing 10× more data than others?
 - Check for shuffle volume: large shuffles are the most common performance killer
 - Check for spill: memory spill to disk indicates insufficient executor memory

2. Partitioning optimization:
 - Repartition before a join or aggregation to the right number of partitions: num_partitions = total_data_size_GB × 128 (for 128MB partitions)
 - Use repartition(n, key_column) to co-locate related records and reduce shuffle
 - Use coalesce() to reduce partition count before writing (avoids full shuffle)

3. Join optimization:
 - Broadcast join: use for any table < {{broadcast_threshold_mb}}MB — eliminates shuffle entirely
 - Sort-merge join (default): ensure both sides are partitioned and sorted on the join key
 - Skew join: handle skewed keys by salting (append a random prefix to the key)

4. Data skew handling:
 - Identify skewed keys: GROUP BY join_key ORDER BY COUNT DESC LIMIT 20
 - Salt skewed keys: join_key_salted = concat(join_key, '_', floor(rand() * N))
 - Process skewed keys separately and union with normal results

5. Caching strategy:
 - cache() / persist() DataFrames used more than once in the same job
 - Use MEMORY_AND_DISK_SER for large DataFrames that don't fit in memory
 - Unpersist cached DataFrames when no longer needed

6. Configuration tuning:
 - spark.sql.adaptive.enabled=true (AQE): enables runtime partition coalescing and join strategy switching
 - spark.sql.adaptive.skewJoin.enabled=true: automatically handles skewed joins
 - Executor memory = (node_memory - overhead) / executors_per_node

Return: diagnosis procedure, optimization implementations with estimated impact, and configuration recommendations. Copy prompt Open prompt details Intermediate Single prompt 10 
### Streaming Pipeline Design 

This prompt is for designing a streaming pipeline that can meet strict throughput and latency requirements while remaining replayable and observable. It covers broker setup, consumer behavior, stateful processing, exactly-once considerations, DLQ handling, and monitoring. It is useful when the team needs an end-to-end real-time design, not just code snippets. 
Prompt text Design a streaming data pipeline for processing {{event_type}} events from {{source}} to {{destination}}.

Throughput requirement: {{throughput}} events/sec
Latency requirement: end-to-end < {{latency_target}}

1. Message broker configuration (Kafka / Kinesis):
 - Topic partitioning: number of partitions = max_throughput / throughput_per_partition
 - Partition key: choose a key that distributes load evenly AND ensures ordering where required
 - Retention: set to at least 7 days to allow replay from any point in the last week
 - Replication factor: 3 for production (tolerates 2 broker failures)

2. Consumer design:
 - Consumer group: one per logical pipeline to enable independent replay
 - Offset commit strategy: commit after successful write to destination (at-least-once delivery)
 - Idempotent consumer: handle duplicate messages at the destination with deduplication on event_id
 - Backpressure: limit consumer fetch size and processing batch to control memory usage

3. Stream processing (Flink / Spark Structured Streaming / Kafka Streams):
 - Windowing: tumbling window of {{window_size}} for aggregations
 - Watermark: allow late events up to {{late_arrival_tolerance}} before closing window
 - State management: use checkpointing every 60 seconds for fault tolerance

4. Exactly-once semantics:
 - Kafka transactions + idempotent producers for source-to-broker
 - Transactional writes to destination (or idempotent upserts)
 - Checkpoint-based recovery to avoid reprocessing

5. Dead letter queue:
 - Route unparseable or schema-invalid messages to a DLQ topic
 - Alert on DLQ growth rate > {{dlq_threshold}} messages/min

6. Monitoring:
 - Consumer lag per partition (alert if lag > {{lag_threshold}})
 - Processing latency (time from event timestamp to destination write)
 - Throughput (events/sec in and out)

Return: architecture diagram (text), configuration recommendations, processing code skeleton, and monitoring setup. Copy prompt Open prompt details 
## Recommended Pipeline Design workflow 
1 
### Backfill Strategy 

Start with a focused prompt in Pipeline Design so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### DAG Design for Airflow 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### dbt Project Structure 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Incremental Load Design 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
