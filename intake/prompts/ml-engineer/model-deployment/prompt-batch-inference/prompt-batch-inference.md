# Batch Inference Pipeline *AI Prompt *

This prompt designs a scalable batch inference pipeline for large datasets with streaming reads, mixed precision inference, chunked writes, progress tracking, and resume support. It is built for offline scoring workloads where throughput and fault tolerance matter. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an efficient batch inference pipeline for running predictions on {{dataset_size}} records.

1. Data loading strategy:
 - Stream from source (S3, database, or file) without loading all into memory
 - Use a DataLoader with appropriate batch size for maximum GPU utilization
 - Parallelize I/O with prefetching: load next batch while GPU processes current

2. Inference optimization:
 - model.eval() and torch.no_grad()
 - Mixed precision inference with torch.autocast
 - Disable gradient computation globally: torch.set_grad_enabled(False)
 - TorchScript or ONNX export for faster inference if model is compatible

3. Output handling:
 - Buffer predictions in memory and write to output in chunks (avoid one write per sample)
 - Write to Parquet for efficient downstream use
 - Include input ID and model version in output for traceability

4. Fault tolerance:
 - Checkpoint progress: track which batches are complete
 - Resume from last successful batch on failure
 - Handle individual batch errors without killing the whole pipeline

5. Throughput optimization:
 - Profile to find the bottleneck: I/O, CPU preprocessing, or GPU inference
 - Dynamic batching: collect samples until batch is full or timeout is reached
 - Multi-process inference for CPU-only models

6. Monitoring:
 - Log throughput (samples/sec) and ETA every 100 batches
 - Log GPU memory usage and utilization
 - Alert if error rate exceeds 1%

Return: complete batch inference script with progress tracking and fault tolerance. 
```

## When to use this prompt 
Use case 01 
when scoring millions or billions of records offline 
Use case 02 
when predictions must be written incrementally without loading all data into memory 
Use case 03 
when failures should not require restarting from the beginning 
Use case 04 
when throughput, ETA, and GPU utilization need to be monitored 

## What the AI should return 

A complete batch inference script with streaming input, optimized batching, progress checkpoints, error handling, and chunked output writing. 

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

Once you have the first result, continue deeper with related prompts in Model Deployment.
