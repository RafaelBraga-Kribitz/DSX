# Pipeline Design Chain *AI Prompt *

This prompt chains together the full data pipeline design process from requirements to architecture document. It is meant for larger designs where ingestion, storage, processing, orchestration, and monitoring all need to fit together coherently. It works best when you want a system-level blueprint instead of isolated recommendations. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Requirements gathering — define: source systems and their characteristics (volume, velocity, format, update pattern), latency SLA (batch/micro-batch/real-time), downstream consumers and their needs, and any compliance or data residency constraints.
Step 2: Ingestion pattern selection — for each source, select the appropriate ingestion pattern (full load, incremental, CDC, streaming, API polling) with rationale. Identify which sources need CDC and what infrastructure that requires.
Step 3: Processing layer design — choose the processing technology (dbt, Spark, Flink, SQL) for each transformation layer. Define the medallion layers (Bronze/Silver/Gold or equivalent) and what transformations happen at each layer.
Step 4: Storage and partitioning — design the storage layout for each layer. Define partitioning strategy, file format (Parquet/Delta/Iceberg), and retention policy. Estimate storage cost.
Step 5: Orchestration design — design the DAG structure. Define dependencies between pipelines, scheduling strategy, SLA per pipeline, retry policy, and alerting.
Step 6: Reliability and observability — define: row count reconciliation checks, data freshness monitoring, lineage tracking, alerting thresholds, and incident response procedure.
Step 7: Write the pipeline design document: architecture diagram (text), technology choices with rationale, data flow description, SLA commitments, known risks, and estimated build timeline. 
```

## When to use this prompt 
Use case 01 
When designing a new platform or major pipeline family from scratch. 
Use case 02 
When creating a technical design document for review or approval. 
Use case 03 
When multiple source types and SLAs must be handled consistently. 
Use case 04 
When you need one prompt to cover architecture, operations, and governance together. 

## What the AI should return 

Return a phased design document covering requirements, ingestion choices, processing layers, storage layout, orchestration, and observability. Include architecture decisions with rationale, a text diagram, SLAs, risks, and an estimated build sequence or timeline. The output should feel like a draft technical design package. 

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
