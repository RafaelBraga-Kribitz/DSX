# Infrastructure and Platform *AI Prompts *

4 Data Engineer prompts in Infrastructure and Platform. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Infrastructure and Platform 
4 prompts Intermediate Single prompt 01 
### Compute Sizing Guide 

This prompt determines an appropriate compute footprint for data engineering workloads by tying runtime targets and data volume to cluster design. It is useful when teams need a starting configuration plus a benchmarking method instead of guessing node sizes. The answer should reflect workload shape, not just generic sizing heuristics. 
Prompt text Determine the right compute configuration for this data engineering workload.

Workload: {{workload_description}}
Data volume: {{data_volume}}
Runtime requirement: {{runtime_sla}}
Budget constraint: {{budget}}

1. Spark cluster sizing:
 - Driver: 1 node with 4–8 cores and 16–32GB RAM (driver is a coordinator, not a worker)
 - Executor memory rule: executor_memory = (node_memory × 0.75) / executors_per_node
 - Executor cores: 4–5 per executor (sweet spot — too many causes context switching, too few underutilizes memory parallelism)
 - Number of executors: total_data_size_GB / (executor_memory × compression_ratio) as a starting point
 - For shuffle-heavy jobs: more executors with less memory each (shuffle writes to local disk)
 - For memory-heavy joins: fewer executors with more memory each

2. Scaling strategy:
 - Start with a cluster that fits the data comfortably in memory
 - Profile first: identify if job is CPU-bound, memory-bound, or I/O-bound before scaling
 - CPU-bound: add more cores (more executors)
 - Memory-bound: add more RAM per executor (increase executor memory)
 - I/O-bound: add more storage bandwidth (use instance storage types like i3 on AWS)

3. Spot/preemptible instances:
 - Use spot for worker nodes (can tolerate eviction + checkpoint recovery)
 - Use on-demand for driver (eviction kills the entire job)
 - Savings: 60–80% cost reduction vs on-demand

4. Autoscaling:
 - Enable autoscaling for interactive and variable workloads
 - Disable for scheduled batch jobs with predictable volume (autoscaling overhead not worth it)

5. Benchmark procedure:
 - Run the job at 1×, 2×, 4× the baseline cluster size
 - Plot runtime vs cost: find the point of diminishing returns

Return: sizing recommendation, benchmark procedure, spot instance configuration, and cost estimate. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Lake File Format Selection 

This prompt helps select the right file and table formats for a lake or lakehouse based on workloads, engines, and update requirements. It is especially valuable when teams need to choose between plain file formats and ACID table formats for different layers. The response should clearly separate storage format from table-management capabilities. 
Prompt text Select the right file format and table format for each layer of this data lake.

Workloads: {{workloads}} (batch analytics, streaming, ML feature engineering, etc.)
Platform: {{compute_engines}} (Spark, Trino, Dremio, BigQuery, etc.)

1. File format comparison:

 Parquet:
 - Columnar, splittable, highly compressed
 - Best for: analytical reads, column-selective queries, broad engine support
 - Limitations: no ACID transactions, no efficient row-level updates, schema evolution is limited
 - Choose when: read-heavy analytics, stable schemas, no need for row-level changes

 ORC:
 - Similar to Parquet, marginally better for Hive workloads
 - Choose when: primary engine is Hive or Hive-compatible

 Avro:
 - Row-based, schema embedded in file, excellent schema evolution support
 - Best for: streaming ingestion, schema-registry integration, write-heavy workloads
 - Choose when: Kafka → data lake ingestion, schema evolution is frequent

 Delta Lake / Apache Iceberg / Apache Hudi (table formats):
 - ACID transactions, time travel, schema evolution, row-level deletes
 - Delta: tightest Spark integration, best for Databricks
 - Iceberg: broadest engine support (Spark, Trino, Flink, Dremio, BigQuery), best for multi-engine lakes
 - Hudi: streaming-optimized, best for CDC and near-real-time use cases

2. Recommendation by layer:
 - Bronze (raw ingest): Parquet or Avro depending on source
 - Silver (cleansed): Delta or Iceberg (need row-level updates for SCD)
 - Gold (marts): Delta or Iceberg (need ACID for concurrent writes)

3. Compression codec recommendation:
 - Snappy: fast compression/decompression, moderate compression ratio (default)
 - Zstd: better compression ratio than Snappy at similar speed (preferred for cold storage)
 - Gzip: maximum compression, slow decompression (use only for archival)

Return: format selection matrix, recommendation per layer, and compression codec guide. Copy prompt Open prompt details Advanced Chain 03 
### Platform Evaluation Chain 

This prompt structures a full platform selection process from requirements through proof of concept, TCO, risk, and final recommendation. It is designed for decisions that are expensive to reverse and need evidence across technology, cost, operations, and team fit. The output should resemble a platform evaluation dossier rather than a quick opinion. 
Prompt text Step 1: Requirements gathering — document the platform requirements: data volume (current and 3-year projection), workload types (batch ETL, streaming, ad-hoc SQL, ML), latency SLAs, team size and SQL vs code preference, compliance requirements (data residency, SOC2, HIPAA), and budget range.
Step 2: Candidate selection — identify 3 candidate platforms based on the requirements. Typical candidates: Snowflake vs Databricks vs BigQuery, or Airflow vs Prefect vs Dagster. Eliminate options that fail hard requirements immediately.
Step 3: Evaluation criteria scoring — score each candidate on: performance (benchmark on representative workloads), total cost of ownership (compute + storage + egress + seats), developer experience (ease of use for the team), ecosystem (integrations with existing tools), operational burden (managed vs self-hosted), and vendor risk.
Step 4: Proof of concept — run a 2-week PoC for the top 2 candidates. Use a representative subset of actual workloads. Measure: query performance, pipeline development speed, operational effort, and cost.
Step 5: TCO modeling — build a 3-year TCO model for each finalist: compute, storage, licensing, personnel, migration, and training costs. Include the cost of not choosing this platform (opportunity cost).
Step 6: Risk assessment — for each finalist: vendor lock-in risk, migration complexity, scaling limits, support quality, and financial stability of the vendor.
Step 7: Write the platform recommendation document: requirements summary, evaluation matrix, PoC results, TCO comparison, risk assessment, final recommendation with rationale, migration plan, and success metrics. Copy prompt Open prompt details Beginner Single prompt 04 
### Warehouse Cost Optimization 

This prompt examines warehouse spend and turns cost into concrete optimization opportunities across compute, storage, governance, and user behavior. It is useful when teams need to reduce cloud warehouse cost without blindly cutting performance or access. The answer should connect savings ideas to measurable spend drivers. 
Prompt text Analyze and optimize the cost of this cloud data warehouse.

Platform: {{platform}} (Snowflake / BigQuery / Redshift / Databricks)
Current monthly cost: {{current_cost}}
Target reduction: {{target_reduction}}

1. Cost breakdown analysis:
 - Identify the top 10 most expensive queries by compute cost
 - Identify the top 10 most expensive users/teams by spend
 - Break down storage cost: active storage vs time-travel vs fail-safe
 - Identify tables that have not been queried in the last 90 days (zombie tables)

2. Compute optimizations:
 - Auto-suspend: set warehouse auto-suspend to 1–2 minutes (not the default 10)
 - Auto-scale: use multi-cluster warehouses only for concurrent workloads, not sequential ones
 - Query optimization: the top 3 most expensive queries — can they be rewritten to scan less data?
 - Result caching: are users re-running identical queries? Enable result cache.
 - Materialization: for frequently run expensive aggregations, create a pre-aggregated table

3. Storage optimizations:
 - Reduce time-travel retention from 90 days to 7 days for non-critical tables (Snowflake)
 - Set partition expiration for old data that is no longer needed (BigQuery)
 - Compress and archive historical data to cheaper storage tiers
 - Delete zombie tables after confirming with owners

4. Governance:
 - Set per-user and per-team cost budgets with alerts at 80% and 100% of budget
 - Require query cost estimates before running full-table scans over {{threshold_gb}}GB
 - Tag queries with cost center for chargeback reporting

Return: cost breakdown analysis queries, top optimizations with estimated savings each, and governance policy. Copy prompt Open prompt details 
## Recommended Infrastructure and Platform workflow 
1 
### Compute Sizing Guide 

Start with a focused prompt in Infrastructure and Platform so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Lake File Format Selection 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Platform Evaluation Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Warehouse Cost Optimization 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
