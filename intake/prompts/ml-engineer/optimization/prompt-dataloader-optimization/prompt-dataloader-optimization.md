# DataLoader Optimization *AI Prompt *

This prompt diagnoses whether the DataLoader is the training bottleneck and then tunes worker count, prefetching, pinning, and data format choices to improve utilization. It is aimed at eliminating input pipeline stalls that starve the GPU. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and optimize the DataLoader to eliminate I/O bottlenecks in this training pipeline.

1. Diagnose if I/O is the bottleneck:
 - Run training with an all-random dataset (no disk I/O): if GPU utilization increases significantly, DataLoader is the bottleneck
 - Profile DataLoader: measure time spent in __getitem__ vs training step

2. num_workers tuning:
 - Rule of thumb: start with num_workers = number of CPU cores / 2
 - Benchmark num_workers = 0, 2, 4, 8, 16: find the value that maximizes GPU utilization
 - Note: too many workers increases memory usage and can cause shared memory errors

3. Prefetching:
 - prefetch_factor=2 (default): each worker prefetches 2 batches ahead
 - Increase to 4 if GPU is fast relative to I/O
 - persistent_workers=True: avoids worker restart overhead each epoch

4. Data format optimization:
 - Convert images to WebDataset (tar-based streaming) if reading many small files
 - Use Parquet + PyArrow for tabular data with columnar reads
 - Memory-mapped files (np.memmap) for large arrays that fit in RAM
 - Store preprocessed tensors as .pt files to skip preprocessing in __getitem__

5. Memory pinning:
 - pin_memory=True: pinned (page-locked) memory enables faster CPU→GPU transfers
 - Use non_blocking=True in .to(device) calls

6. On-GPU preprocessing:
 - Move augmentation to GPU using Kornia or torchvision transforms v2 on CUDA tensors
 - Reduces per-worker CPU load

Return: bottleneck diagnosis procedure, optimization implementations, and benchmark comparing before vs after. 
```

## When to use this prompt 
Use case 01 
when GPU utilization is low and input loading may be the bottleneck 
Use case 02 
when tuning num_workers, prefetch_factor, or persistent_workers 
Use case 03 
when storage format changes could improve throughput 
Use case 04 
when you need before-versus-after benchmarking of the data pipeline 

## What the AI should return 

A DataLoader diagnosis procedure, concrete optimization implementations, and benchmark results showing the impact of the improvements. 

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

Once you have the first result, continue deeper with related prompts in Optimization.
