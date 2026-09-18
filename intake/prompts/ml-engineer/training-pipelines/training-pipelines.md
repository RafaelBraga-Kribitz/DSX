# Training Pipelines *AI Prompts *

10 ML Engineer prompts in Training Pipelines. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 9 single prompts · 1 chain. 

## AI prompts in Training Pipelines 
10 prompts Advanced Single prompt 01 
### Custom Loss Function 

This prompt builds a custom PyTorch loss function that is differentiable, numerically stable, and testable. It includes unit tests, gradient checks, reduction modes, and edge-case handling so the loss can be trusted in real training workloads. 
Prompt text Implement a custom loss function for this problem with full PyTorch autograd compatibility.

Problem: {{problem_description}}
Loss requirements: {{loss_requirements}}

1. Implementation requirements:
 - Subclass torch.nn.Module or implement as a function
 - Fully differentiable — use only PyTorch tensor operations, no NumPy inside forward()
 - Support batched inputs of arbitrary batch size
 - Handle edge cases: empty batches, all-same-class batches, NaN/Inf inputs

2. For composite losses (combining multiple terms):
 - Implement each term as a separate method for testability
 - Use learnable or fixed weighting between terms
 - Log each term's contribution separately during training

3. Numerical stability:
 - Use log-sum-exp trick for log probabilities
 - Apply clipping to prevent log(0) or division by zero
 - Test with fp16 — ensure no overflow with half precision

4. Testing the loss:
 - Unit test: verify loss = 0 for perfect predictions
 - Unit test: verify loss > 0 for wrong predictions
 - Gradient check: torch.autograd.gradcheck to verify analytical gradients match numerical approximation
 - Verify loss is lower for better predictions (sanity check)

5. Reduction modes: support 'mean', 'sum', and 'none' as in standard PyTorch losses

Return: loss implementation, unit tests, gradient check, and integration example in a training loop. Copy prompt Open prompt details Beginner Single prompt 02 
### Dataset Pipeline Builder 

This prompt generates a production-quality PyTorch Dataset and DataLoader pipeline tailored to a model type and data format. It emphasizes lazy loading, worker tuning, augmentation placement, caching, and deterministic seeding so that the input pipeline is scalable, reproducible, and memory efficient. 
Prompt text Build a production-quality data loading pipeline for training a {{model_type}} model on {{data_format}} data.

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

Return: complete Dataset and DataLoader code with comments explaining each design decision. Copy prompt Open prompt details Intermediate Single prompt 03 
### Distributed Training Setup 

This prompt converts a single-GPU PyTorch script into a distributed training setup using DistributedDataParallel. It covers launch configuration, process group initialization, model wrapping, distributed sampling, checkpointing, and rank-aware logging for scalable multi-GPU or multi-node training. 
Prompt text Convert this single-GPU training script to distributed training using PyTorch DDP (DistributedDataParallel).

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

Return: full DDP training script with a torchrun launch command example. Copy prompt Open prompt details Intermediate Single prompt 04 
### Experiment Tracking Setup 

This prompt integrates experiment tracking into an ML training pipeline using MLflow, Weights & Biases, or Neptune. It focuses on consistent run naming, hyperparameter logging, metric logging, artifact capture, and reproducibility metadata so experiments are easy to compare and audit. 
Prompt text Set up comprehensive experiment tracking for this ML training pipeline.

Use {{tracking_tool}} (MLflow / Weights & Biases / Neptune).

1. Run initialization:
 - Create a run with a descriptive name including: model architecture, dataset version, timestamp
 - Tag run with: git commit hash, environment (dev/staging/prod), dataset version

2. Hyperparameter logging:
 - Log all hyperparameters at run start: learning rate, batch size, epochs, optimizer, scheduler, architecture config
 - Log data config: train/val split, augmentations, preprocessing steps

3. Metric logging per epoch:
 - Training: loss, primary metric, learning rate, gradient norm
 - Validation: loss, primary metric, all secondary metrics
 - System: GPU memory used, step time, throughput (samples/sec)

4. Artifact logging:
 - Best model checkpoint
 - Final model checkpoint
 - Confusion matrix or prediction plots at end of training
 - Feature importance if applicable

5. Run comparison:
 - Show how to use the tracking UI to compare runs by val metric
 - Show how to retrieve the best run programmatically

6. Reproducibility:
 - Log environment: requirements.txt or conda env YAML
 - Log random seeds

Return: tracking setup code integrated into the training loop, and a run naming convention guide. Copy prompt Open prompt details Intermediate Single prompt 05 
### Gradient Accumulation 

This prompt implements gradient accumulation to simulate a larger effective batch size when GPU memory is limited. It handles accumulation math, AMP compatibility, DDP synchronization behavior, and scheduler stepping so the loop behaves like large-batch training without fitting the full batch at once. 
Prompt text Implement gradient accumulation to simulate a larger effective batch size on limited GPU memory.

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

Return: complete gradient accumulation training loop with DDP and mixed precision support. Copy prompt Open prompt details Intermediate Single prompt 06 
### Learning Rate Finder 

This prompt implements a learning rate range test and uses its results to configure an effective learning rate schedule, including a 1-cycle policy. It is meant to replace guesswork with a data-driven way to pick a stable and performant learning rate. 
Prompt text Implement a learning rate range test (LR finder) to find the optimal learning rate for this model.

Based on the Smith (2017) cyclical learning rate paper approach:

1. LR range test implementation:
 - Start with a very small LR (1e-7) and exponentially increase to a large LR (10) over 100–200 iterations
 - Log loss at each step
 - Stop early if loss explodes (> 4× minimum loss)

2. Plot the LR finder curve:
 - x-axis: learning rate (log scale)
 - y-axis: smoothed loss (EMA smoothing factor=0.05)
 - Annotate: the point of steepest descent (best LR), the point where loss starts diverging (max LR)

3. Recommended LR selection rules:
 - For standard training: use the LR at steepest loss descent ÷ 10
 - For 1-cycle policy: use the LR at steepest descent as max_lr, and max_lr ÷ 10 as initial_lr

4. Implement 1-cycle LR scheduler using the found LR:
 - Warmup: linear increase from max_lr/10 to max_lr over 30% of training
 - Decay: cosine anneal from max_lr to max_lr/10000 over remaining 70%

5. Reset model weights after the LR finder (do not use weights from the search)

Return: LR finder code, plot code, and 1-cycle scheduler setup using the found optimal LR. Copy prompt Open prompt details Advanced Single prompt 07 
### Multi-Task Training 

This prompt creates a multi-task learning setup with a shared backbone, task-specific heads, multiple loss-weighting strategies, and gradient conflict mitigation. It is useful when one model must optimize more than one objective without one task overwhelming the other. 
Prompt text Implement a multi-task learning training setup for a model that simultaneously optimizes {{task_1}} and {{task_2}}.

1. Model architecture:
 - Shared backbone: {{backbone}} that extracts shared representations
 - Task-specific heads: separate output heads for each task
 - Gradient isolation: ensure gradients from one task head do not corrupt features needed by another

2. Loss combination strategies — implement and compare:
 a. Fixed weighting: total_loss = w1 × loss_1 + w2 × loss_2
 b. Uncertainty weighting (Kendall et al. 2018): learn task weights as trainable parameters based on homoscedastic uncertainty
 c. GradNorm (Chen et al. 2018): dynamically adjust weights based on relative gradient magnitudes

3. Task imbalance handling:
 - Normalize each task loss to similar scale before combining
 - Monitor per-task gradient norms — large imbalance indicates weighting issues

4. Training strategy:
 - Option A: alternate between tasks each batch
 - Option B: sample tasks proportionally by dataset size
 - Option C: train all tasks simultaneously in each batch

5. Evaluation:
 - Log per-task metrics separately during validation
 - Use a combined score (e.g. average of normalized per-task metrics) to select the best checkpoint

6. Gradient surgery: implement PCGrad to project conflicting gradients to prevent task interference

Return: multi-task model code, loss combination implementations, and training loop with per-task logging. Copy prompt Open prompt details Beginner Single prompt 08 
### Training Loop Template 

This prompt produces a robust PyTorch training loop template with mixed precision, gradient clipping, validation, checkpointing, early stopping, and logging. It is meant for engineers who need a reliable baseline loop that can be reused across experiments and extended for production workloads. 
Prompt text Write a production-quality PyTorch training loop with all essential components.

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

Return: complete training loop code with type hints and docstrings. Copy prompt Open prompt details Advanced Chain 09 
### Training Pipeline Hardening Chain 

This chain hardens a training pipeline end to end by auditing reproducibility, profiling the data pipeline, checking numerical stability, validating checkpoint resume behavior, monitoring gradients, and finishing with a smoke test. It is designed for teams preparing training code for repeated reliable use. 
Prompt text Step 1: Reproducibility audit — verify all random seeds are set (Python, NumPy, PyTorch, CUDA). Run training twice with identical config and confirm loss curves are bit-for-bit identical.
Step 2: Data pipeline profiling — profile the DataLoader to identify if training is GPU-bound or I/O-bound. Optimize num_workers, prefetch_factor, and caching strategy based on findings.
Step 3: Numerical stability check — enable torch.autograd.detect_anomaly() for one epoch to catch NaN/Inf in forward/backward passes. Fix any instabilities found.
Step 4: Memory optimization — run with torch.cuda.memory_summary() after each epoch. Identify memory leaks (steadily increasing memory usage). Ensure .detach() is called on all logged tensors.
Step 5: Checkpoint validation — verify that loading a checkpoint and resuming training produces identical results to uninterrupted training for the next 10 steps.
Step 6: Gradient health check — log gradient norms for each layer group per epoch. Flag layers with vanishing (<1e-7) or exploding (>100) gradients. Adjust initialization or add gradient clipping.
Step 7: End-to-end smoke test — write a test that runs 2 epochs on a tiny dataset (32 samples) and asserts: loss decreases, metrics are computed, checkpoint saved, no CUDA errors, no memory leaks. Copy prompt Open prompt details Beginner Single prompt 10 
### Training Script Audit 

This prompt reviews an ML training script for correctness, reproducibility, evaluation integrity, and operational training hygiene. It is useful for catching common but costly issues such as data leakage, nondeterministic splits, weak validation setup, and inefficient training defaults before a model is trusted or scaled. 
Prompt text Audit this ML training script for correctness and best practices.

Check for the following issues and flag each as Critical / Warning / Info:

1. Data leakage:
 - Is preprocessing (scaling, encoding, imputation) fitted on training data only, then applied to val/test?
 - Are any features derived from the target variable?
 - For time series: is there any forward-looking data in the features?

2. Reproducibility:
 - Are random seeds set for: Python random, NumPy, PyTorch/TensorFlow, and CUDA?
 - Is the dataset split deterministic?

3. Evaluation correctness:
 - Is the evaluation metric appropriate for the problem type and class imbalance?
 - Is evaluation done on a truly held-out set, never used during training or tuning?

4. Training hygiene:
 - Is learning rate scheduling used?
 - Is gradient clipping applied for RNNs or transformers?
 - Are validation metrics logged per epoch, not just at the end?

5. Resource efficiency:
 - Is DataLoader using num_workers > 0 and pin_memory=True?
 - Is mixed precision (torch.cuda.amp) enabled?
 - Are unused tensors detached from the computation graph during validation?

Return: issue list with severity, line references where possible, and fix recommendations. Copy prompt Open prompt details 
## Recommended Training Pipelines workflow 
1 
### Custom Loss Function 

Start with a focused prompt in Training Pipelines so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Dataset Pipeline Builder 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Distributed Training Setup 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Experiment Tracking Setup 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
