# Training Loop Template *AI Prompt *

This prompt produces a robust PyTorch training loop template with mixed precision, gradient clipping, validation, checkpointing, early stopping, and logging. It is meant for engineers who need a reliable baseline loop that can be reused across experiments and extended for production workloads. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a production-quality PyTorch training loop with all essential components.

Include:

1. Epoch loop with tqdm progress bar showing live loss and metric

2. Forward pass:
 - Mixed precision with torch.autocast (fp16 for GPU, bf16 for Ampere+)
 - Gradient scaling with GradScaler for fp16 stability

3. Backward pass:
 - Zero gradients (set_to_none=True for memory efficiency)
 - Loss scaling
 - Gradient clipping: torch.nn.utils.clip_grad_norm_ with max_norm=1.0
 - Optimizer step
 - Scheduler step

4. Validation loop:
 - torch.no_grad() context
 - model.eval() / model.train() switching
 - Accumulate metrics across batches, compute at epoch end

5. Checkpointing:
 - Save on validation metric improvement: model state, optimizer state, scheduler state, epoch, best metric
 - Load checkpoint function for resuming interrupted training

6. Early stopping:
 - Patience-based: stop if no improvement after N epochs
 - Save best model separately from last checkpoint

7. Logging:
 - Log train loss, val loss, and primary metric per epoch
 - Optional: Weights & Biases or MLflow integration

Return: complete training loop code with type hints and docstrings. 
```

## When to use this prompt 
Use case 01 
when you need a clean production-grade PyTorch training loop 
Use case 02 
when starting a new training project and want all essential loop components included 
Use case 03 
when checkpointing, early stopping, and validation logging must be built in 
Use case 04 
when mixed precision and scheduler support are required 

## What the AI should return 

Complete PyTorch training loop code with type hints, docstrings, training and validation steps, checkpoint utilities, early stopping, and logging hooks. 

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
