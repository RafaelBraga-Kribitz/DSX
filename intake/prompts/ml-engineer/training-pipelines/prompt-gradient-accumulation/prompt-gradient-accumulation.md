# Gradient Accumulation *AI Prompt *

This prompt implements gradient accumulation to simulate a larger effective batch size when GPU memory is limited. It handles accumulation math, AMP compatibility, DDP synchronization behavior, and scheduler stepping so the loop behaves like large-batch training without fitting the full batch at once. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement gradient accumulation to simulate a larger effective batch size on limited GPU memory.

Target effective batch size: {{effective_batch_size}}
Physical batch size that fits in GPU memory: {{physical_batch_size}}
Accumulation steps: effective_batch_size / physical_batch_size

1. Basic gradient accumulation loop:
 - Accumulate gradients for N steps before calling optimizer.step()
 - Divide loss by accumulation steps to maintain consistent gradient scale
 - Zero gradients only after optimizer.step(), not every batch

2. Mixed precision compatibility:
 - Use GradScaler correctly with accumulation — only call scaler.update() after optimizer.step()
 - Correct scaler.scale(loss) placement

3. DDP compatibility:
 - Use model.no_sync() context manager for accumulation steps to prevent premature gradient sync
 - Only sync on the last accumulation step

4. Learning rate adjustment:
 - Learning rate should be tuned for the effective batch size, not physical batch size
 - Linear scaling rule: lr = base_lr × (effective_batch_size / reference_batch_size)

5. Scheduler compatibility:
 - Step scheduler based on optimizer steps (after accumulation), not raw batches

6. Verification:
 - Show how to verify that accumulation of N small batches produces identical gradients to 1 large batch

Return: complete gradient accumulation training loop with DDP and mixed precision support. 
```

## When to use this prompt 
Use case 01 
when GPU memory limits the physical batch size 
Use case 02 
when you need large-batch behavior without changing the model 
Use case 03 
when mixed precision or DDP must work correctly with accumulation 
Use case 04 
when scheduler and learning rate logic should follow optimizer steps 

## What the AI should return 

A complete gradient accumulation training loop with AMP and DDP support, learning rate guidance, and a method to verify gradient equivalence. 

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
