# Spark Job Optimization *AI Prompt *

This prompt focuses on improving Spark jobs by diagnosing the real bottleneck before suggesting tuning changes. It helps teams reason about partitioning, skew, joins, caching, shuffle behavior, and cluster configuration in a disciplined way. The goal is not random tuning tips, but an optimization plan tied to runtime and cost impact. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize this Spark job for performance, cost, and reliability.

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

Return: diagnosis procedure, optimization implementations with estimated impact, and configuration recommendations. 
```

## When to use this prompt 
Use case 01 
When a Spark job is slow, expensive, or unstable. 
Use case 02 
When analyzing Spark UI evidence after repeated job failures or long runtimes. 
Use case 03 
When preparing a performance tuning plan for a critical batch workflow. 
Use case 04 
When you need concrete Spark code and configuration changes with expected impact. 

## What the AI should return 

Return a diagnosis-first optimization plan, not just a list of best practices. Identify the likely bottlenecks, then recommend specific changes to partitioning, joins, skew handling, caching, and configuration. For each recommendation, include why it helps, how to implement it, and the estimated runtime or cost benefit. 

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
