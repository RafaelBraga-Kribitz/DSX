# Redshift Architecture and Tuning *AI Prompt *

Design and optimize a Redshift deployment for this workload. Workload: {{workload}} Data volume: {{volume}} Query patterns: {{query_patterns}} Cluster type: {{cluster_type}} (pr... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and optimize a Redshift deployment for this workload.

Workload: {{workload}}
Data volume: {{volume}}
Query patterns: {{query_patterns}}
Cluster type: {{cluster_type}} (provisioned vs Serverless)

1. Redshift Serverless vs Provisioned:
 Serverless: auto-scales, pay per compute-second, no cluster management
 - Use for: unpredictable workloads, intermittent usage, cost optimization
 Provisioned: fixed cluster, predictable performance and cost
 - Use for: consistent heavy workloads, >$500/month sustained use

2. Table design:
 Distribution styles:
 - DISTSTYLE KEY (column): rows with the same key on the same slice — use for large JOIN tables
 - DISTSTYLE EVEN: round-robin — use for large tables with no clear join key
 - DISTSTYLE ALL: copy to every slice — use for small dimension tables (< 1M rows)

 Sort keys:
 - COMPOUND SORTKEY (col1, col2): range scan optimization on ordered columns (date)
 - INTERLEAVED SORTKEY: equal weight to all sort key columns — use for multiple filter patterns

3. COPY command for loading:
 COPY orders FROM 's3://bucket/data/orders/'
 IAM_ROLE 'arn:aws:iam::123456789:role/RedshiftRole'
 FORMAT AS PARQUET;
 - Use PARQUET (fastest) or CSV with GZIP compression
 - Parallel loading: split files into 1× number of slices for maximum parallelism

4. Vacuuming:
 VACUUM orders TO 100 PERCENT BOOST;
 -- Reclaims space from deleted rows and re-sorts unsorted rows
 -- Schedule weekly; automatic vacuum may not keep up with high-write tables

5. WLM (Workload Management):
 - Define query queues by user group or query group
 - Short query acceleration (SQA): auto-routes short queries to a fast lane
 - Concurrency scaling: auto-adds read capacity during peak periods

Return: distribution and sort key design, COPY command, vacuum schedule, and WLM configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud warehouse work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Warehouse or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Redshift Serverless vs Provisioned:, Use for: unpredictable workloads, intermittent usage, cost optimization, Use for: consistent heavy workloads, >$500/month sustained use. The final answer should stay clear, actionable, and easy to review inside a cloud warehouse workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Warehouse.
