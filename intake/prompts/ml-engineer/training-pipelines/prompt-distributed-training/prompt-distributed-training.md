# Distributed Training Setup *AI Prompt *

This prompt converts a single-GPU PyTorch script into a distributed training setup using DistributedDataParallel. It covers launch configuration, process group initialization, model wrapping, distributed sampling, checkpointing, and rank-aware logging for scalable multi-GPU or multi-node training. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Convert this single-GPU training script to distributed training using PyTorch DDP (DistributedDataParallel).

1. Launcher setup:
 - Use torchrun (not deprecated torch.distributed.launch)
 - Support both single-node multi-GPU and multi-node setups
 - Environment variable initialization (MASTER_ADDR, MASTER_PORT, RANK, WORLD_SIZE)

2. Process group initialization:
 - dist.init_process_group with nccl backend (GPU) or gloo (CPU)
 - Set device based on LOCAL_RANK

3. Model wrapping:
 - Move model to device before wrapping with DDP
 - Use find_unused_parameters=False if possible (faster)
 - Sync BatchNorm: convert_sync_batchnorm if using BatchNorm layers

4. DataLoader modifications:
 - DistributedSampler with shuffle=True for training, shuffle=False for val
 - Set sampler.set_epoch(epoch) each epoch for proper shuffling
 - Divide effective batch size by world_size

5. Gradient synchronization:
 - Gradients automatically synced by DDP — do not manually all_reduce
 - Use model.no_sync() context manager for gradient accumulation

6. Checkpointing:
 - Save/load only on rank 0
 - Unwrap model with model.module before saving state_dict

7. Logging:
 - Only log on rank 0 to avoid duplicate output

Return: full DDP training script with a torchrun launch command example. 
```

## When to use this prompt 
Use case 01 
when moving from single-GPU to multi-GPU PyTorch training 
Use case 02 
when you need a correct torchrun-based DDP template 
Use case 03 
when training must scale across nodes with proper samplers and rank handling 
Use case 04 
when checkpointing and logging should only happen on rank 0 

## What the AI should return 

A full DDP training script with launcher assumptions, distributed samplers, checkpoint logic, and an example torchrun command. 

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
