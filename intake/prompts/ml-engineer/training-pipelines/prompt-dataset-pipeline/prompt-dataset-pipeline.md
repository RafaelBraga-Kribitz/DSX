# Dataset Pipeline Builder *AI Prompt *

This prompt generates a production-quality PyTorch Dataset and DataLoader pipeline tailored to a model type and data format. It emphasizes lazy loading, worker tuning, augmentation placement, caching, and deterministic seeding so that the input pipeline is scalable, reproducible, and memory efficient. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a production-quality data loading pipeline for training a {{model_type}} model on {{data_format}} data.

Requirements:
1. PyTorch Dataset class:
 - __len__ and __getitem__ methods
 - Lazy loading (load from disk per item, not all into memory)
 - Caching strategy for expensive preprocessing steps

2. DataLoader configuration:
 - num_workers: calculate optimal value based on CPU cores
 - pin_memory: True if using GPU
 - prefetch_factor: 2 (default) or higher if I/O bound
 - persistent_workers: True to avoid worker restart overhead
 - Appropriate batch size for available GPU memory

3. Data augmentation pipeline:
 - Training augmentations: {{augmentations}}
 - Validation augmentations: normalization only (no random augmentations)
 - Augmentations applied on CPU in workers, not on GPU

4. Memory efficiency:
 - Use memory-mapped files for large datasets if applicable
 - Stream from object storage (S3/GCS) without downloading fully if remote

5. Determinism:
 - Worker seed function to ensure reproducibility across runs

Return: complete Dataset and DataLoader code with comments explaining each design decision. 
```

## When to use this prompt 
Use case 01 
when building a new PyTorch data pipeline from scratch 
Use case 02 
when large datasets require lazy loading or memory-mapped access 
Use case 03 
when you need reproducible worker seeding and efficient DataLoader settings 
Use case 04 
when augmentations and batching must be production ready 

## What the AI should return 

Complete Dataset and DataLoader code with comments explaining lazy loading, caching, augmentation design, worker settings, and reproducibility choices. 

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

Once you have the first result, continue deeper with related prompts in Training Pipelines.
