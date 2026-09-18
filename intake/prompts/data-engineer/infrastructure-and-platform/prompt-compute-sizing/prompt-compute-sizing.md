# Compute Sizing Guide *AI Prompt *

This prompt determines an appropriate compute footprint for data engineering workloads by tying runtime targets and data volume to cluster design. It is useful when teams need a starting configuration plus a benchmarking method instead of guessing node sizes. The answer should reflect workload shape, not just generic sizing heuristics. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Determine the right compute configuration for this data engineering workload.

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

Return: sizing recommendation, benchmark procedure, spot instance configuration, and cost estimate. 
```

## When to use this prompt 
Use case 01 
When provisioning Spark or similar compute for a new workload. 
Use case 02 
When jobs miss runtime SLAs and cluster sizing must be revisited. 
Use case 03 
When budget constraints require careful performance-cost trade-offs. 
Use case 04 
When benchmarking and spot-instance strategy are part of the decision. 

## What the AI should return 

Return a sizing recommendation with assumptions, scaling guidance, benchmarking procedure, spot-instance advice, and cost estimate. Explain whether the workload is likely CPU-, memory-, or I/O-bound and how that affects the recommended shape. The response should give a practical baseline cluster and a path to validate it. 

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

Once you have the first result, continue deeper with related prompts in Infrastructure and Platform.
