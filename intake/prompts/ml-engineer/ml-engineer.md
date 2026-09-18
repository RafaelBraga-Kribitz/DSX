# ML Engineer *AI Prompts *

ML Engineer AI prompt library with 42 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse ML Engineer prompt categories 
5 categories 
### Training Pipelines 

AI prompts for machine learning training pipelines, reproducibility, automation, and scalable model training systems. 
10 prompts Custom Loss Function Dataset Pipeline Builder → 
### Model Deployment 

AI prompts for model deployment, serving strategies, rollout planning, scalability, and production environment setup. 
9 prompts A/B Deployment Pattern Batch Inference Pipeline → 
### Optimization 

AI prompts for optimization, improving model performance, reducing latency, resource efficiency, and training speed tuning. 
9 prompts DataLoader Optimization Flash Attention Integration → 
### MLOps and CI/CD 

AI prompts for MLOps and CI/CD workflows, including model lifecycle automation, validation pipelines, release orchestration, and operational reliability. 
7 prompts Automated Retraining Trigger CI/CD for ML Pipeline → 
### Model Compression 

AI prompts for model compression techniques, pruning, quantization, distillation, and optimizing models for faster inference. 
7 prompts Compression Pipeline Chain Knowledge Distillation → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 42 Training Pipelines 10 Model Deployment 9 Optimization 9 MLOps and CI/CD 7 Model Compression 7 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **42 **of 42 prompts 
## Training Pipelines 
10 prompt s Training Pipelines Advanced Prompt 01 
### Custom Loss Function 
Implement a custom loss function for this problem with full PyTorch autograd compatibility.

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

Return: loss implementation, unit tests, gradient check, and integration example in a training loop. Copy prompt View page Show more ↓ Training Pipelines Beginner Prompt 02 
### Dataset Pipeline Builder 
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

Return: complete Dataset and DataLoader code with comments explaining each design decision. Copy prompt View page Show more ↓ Training Pipelines Intermediate Prompt 03 
### Distributed Training Setup 
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

Return: full DDP training script with a torchrun launch command example. Copy prompt View page Show more ↓ Training Pipelines Intermediate Prompt 04 
### Experiment Tracking Setup 
Set up comprehensive experiment tracking for this ML training pipeline.

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

Return: tracking setup code integrated into the training loop, and a run naming convention guide. Copy prompt View page Show more ↓ Training Pipelines Intermediate Prompt 05 
### Gradient Accumulation 
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

Return: complete gradient accumulation training loop with DDP and mixed precision support. Copy prompt View page Show more ↓ Training Pipelines Intermediate Prompt 06 
### Learning Rate Finder 
Implement a learning rate range test (LR finder) to find the optimal learning rate for this model.

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

Return: LR finder code, plot code, and 1-cycle scheduler setup using the found optimal LR. Copy prompt View page Show more ↓ Training Pipelines Advanced Prompt 07 
### Multi-Task Training 
Implement a multi-task learning training setup for a model that simultaneously optimizes {{task_1}} and {{task_2}}.

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

Return: multi-task model code, loss combination implementations, and training loop with per-task logging. Copy prompt View page Show more ↓ Training Pipelines Beginner Prompt 08 
### Training Loop Template 
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

Return: complete training loop code with type hints and docstrings. Copy prompt View page Show more ↓ Training Pipelines Advanced Chain 09 
### Training Pipeline Hardening Chain 
Step 1: Reproducibility audit — verify all random seeds are set (Python, NumPy, PyTorch, CUDA). Run training twice with identical config and confirm loss curves are bit-for-bit identical.
Step 2: Data pipeline profiling — profile the DataLoader to identify if training is GPU-bound or I/O-bound. Optimize num_workers, prefetch_factor, and caching strategy based on findings.
Step 3: Numerical stability check — enable torch.autograd.detect_anomaly() for one epoch to catch NaN/Inf in forward/backward passes. Fix any instabilities found.
Step 4: Memory optimization — run with torch.cuda.memory_summary() after each epoch. Identify memory leaks (steadily increasing memory usage). Ensure .detach() is called on all logged tensors.
Step 5: Checkpoint validation — verify that loading a checkpoint and resuming training produces identical results to uninterrupted training for the next 10 steps.
Step 6: Gradient health check — log gradient norms for each layer group per epoch. Flag layers with vanishing (<1e-7) or exploding (>100) gradients. Adjust initialization or add gradient clipping.
Step 7: End-to-end smoke test — write a test that runs 2 epochs on a tiny dataset (32 samples) and asserts: loss decreases, metrics are computed, checkpoint saved, no CUDA errors, no memory leaks. Copy prompt View page Show more ↓ Training Pipelines Beginner Prompt 10 
### Training Script Audit 
Audit this ML training script for correctness and best practices.

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

Return: issue list with severity, line references where possible, and fix recommendations. Copy prompt View page Show more ↓ 
## Model Deployment 
9 prompt s Model Deployment Intermediate Prompt 01 
### A/B Deployment Pattern 
Implement an A/B model deployment pattern to safely roll out a new model version alongside the current production model.

1. Traffic splitting:
 - Route {{traffic_split}}% of requests to the new model (challenger) and the remainder to the current model (champion)
 - Ensure consistent assignment: the same user/request_id always gets the same model using hash-based routing
 - Support instant traffic shift without redeployment (feature flag or config-based)

2. Request routing implementation:
 - Routing middleware in the serving layer
 - Log which model version served each request: model_version, variant (champion/challenger), request_id

3. Metrics collection:
 - Tag all prediction logs with the model variant
 - Track per-variant: p50/p95/p99 latency, error rate, throughput
 - Track per-variant business metrics: conversion rate, click-through, or other downstream outcome

4. Statistical comparison:
 - Run two-sample t-test or z-test on business metrics per variant
 - Automated alerting if challenger has significantly worse latency or error rate than champion

5. Rollout automation:
 - If challenger is statistically better after {{min_samples}} requests: automatically increase traffic to 100%
 - If challenger is significantly worse: automatically roll back to 0% traffic
 - Otherwise: hold and wait for more data

6. Shadow mode (optional first step):
 - Send all requests to champion for production responses
 - Mirror all requests to challenger for comparison only (no response returned)

Return: routing middleware, metrics logging, statistical comparison, and automated rollout/rollback logic. Copy prompt View page Show more ↓ Model Deployment Intermediate Prompt 02 
### Batch Inference Pipeline 
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

Return: complete batch inference script with progress tracking and fault tolerance. Copy prompt View page Show more ↓ Model Deployment Advanced Chain 03 
### Deployment Readiness Chain 
Step 1: Model validation — run the model on a fixed golden dataset and assert outputs match expected values to ±1e-5. Confirm model size, latency on target hardware (p50/p95/p99), and memory footprint meet requirements.
Step 2: API contract verification — test all endpoints with valid inputs, invalid inputs, edge cases (empty batch, max size batch), and concurrent requests. Verify error codes and messages match the API spec.
Step 3: Load testing — run a 5-minute load test at 2× expected peak traffic using Locust or k6. Confirm p99 latency stays within SLA, error rate < 0.1%, and no memory leaks (memory usage stable).
Step 4: Rollback plan — document the exact steps to roll back to the previous model version within 5 minutes. Verify the rollback procedure works in staging before deploying to production.
Step 5: Monitoring setup — confirm all dashboards are in place: request rate, error rate, p50/p95/p99 latency, prediction distribution, feature drift, and GPU/CPU utilization. Verify alerts are firing correctly.
Step 6: Runbook — write a deployment runbook covering: deployment steps, expected log messages, how to verify success, known issues and their fixes, and escalation path if something goes wrong.
Step 7: Go / no-go checklist — create a final checklist with sign-off required from: ML engineer (model quality), SRE (infrastructure), and product (business metrics). Block deployment until all sign off. Copy prompt View page Show more ↓ Model Deployment Beginner Prompt 04 
### Docker Container for ML 
Write an optimized Dockerfile for deploying this ML model serving application.

Requirements:
- Base image: appropriate CUDA + Python base for GPU, or slim Python for CPU
- Framework: {{framework}} (PyTorch / TensorFlow / ONNX Runtime)

1. Multi-stage build:
 - Builder stage: install build dependencies, compile any C extensions
 - Runtime stage: copy only what is needed for serving (no build tools, no test files)

2. Dependency installation:
 - Copy requirements.txt first, install dependencies before copying code (layer caching)
 - Pin all dependency versions
 - Use --no-cache-dir to reduce image size
 - Install only inference dependencies, not training ones

3. Security best practices:
 - Run as non-root user (create appuser)
 - Read-only filesystem where possible
 - No secrets in the image — use environment variables or mounted secrets

4. Model artifact handling:
 - Bake model weights into image for simplicity (smaller models <500MB)
 - OR load from object storage at startup using environment variable for path

5. Health check:
 - HEALTHCHECK instruction hitting the /health endpoint

6. Image size optimization:
 - Remove pip cache, apt cache, and __pycache__ directories
 - Use .dockerignore to exclude notebooks, tests, data, and .git

7. Runtime configuration:
 - ENV variables for: model path, port, log level, num workers
 - ENTRYPOINT with CMD for override flexibility

Return: Dockerfile, .dockerignore, and docker-compose.yml for local testing. Copy prompt View page Show more ↓ Model Deployment Beginner Prompt 05 
### FastAPI Serving Endpoint 
Build a production-ready FastAPI model serving endpoint for {{model_name}}.

1. Application structure:
 - Lifespan context manager for model loading at startup (not per-request)
 - Global model object stored in app state, not as a module-level global
 - Separate router for model endpoints

2. Request/response schemas (Pydantic v2):
 - Input schema: {{input_schema}} with field validators and example values
 - Response schema: prediction, confidence, model_version, latency_ms, request_id
 - Error response schema with error code and message

3. Inference endpoint POST /predict:
 - Input validation via Pydantic
 - Preprocessing: replicate exactly the training preprocessing pipeline
 - Inference with torch.no_grad() and model.eval()
 - Postprocessing: convert model output to human-readable format
 - Response with latency measurement

4. Health and readiness:
 - GET /health: returns 200 if service is up
 - GET /ready: returns 200 only if model is loaded and warm
 - GET /metrics: prediction count, p50/p95/p99 latency, error rate

5. Robustness:
 - Input size limits to prevent memory exhaustion
 - Timeout on inference (configurable)
 - Graceful error handling — never return a stack trace to the client

6. Concurrency:
 - For CPU models: use thread pool executor with asyncio.run_in_executor
 - For GPU models: serialize inference with asyncio.Lock or use a request queue

Return: complete FastAPI application code with Dockerfile. Copy prompt View page Show more ↓ Model Deployment Advanced Prompt 06 
### Feature Store Integration 
Design the integration between this ML model serving system and a feature store (Feast / Tecton / Hopsworks).

1. Feature retrieval at inference time:
 - Online store lookup: retrieve pre-computed features for entity_id in < 5ms
 - Handle missing entities: define fallback values or reject the request
 - Batch feature lookup for batch inference: use get_online_features with list of entity IDs

2. Feature freshness:
 - Define the maximum acceptable feature age for each feature group
 - Add feature timestamp to the inference request response for debugging
 - Alert if feature freshness degrades beyond threshold

3. Training-serving skew prevention:
 - Use the exact same feature definitions for both training (offline store) and serving (online store)
 - Log features served at inference time to a feature log table
 - Compare feature distributions in the log vs training data to detect skew

4. Point-in-time correct training data:
 - Use feature store's point-in-time join to generate training data
 - Ensure no future feature values leak into training features

5. Feature store client configuration:
 - Initialize client with retry logic and connection pooling
 - Circuit breaker: if feature store is unavailable, fall back to default features with a flag in the response

6. Monitoring:
 - Log feature store latency per request
 - Alert on feature store connection errors

Return: feature retrieval code, training data generation script, skew detection setup, and circuit breaker implementation. Copy prompt View page Show more ↓ Model Deployment Advanced Prompt 07 
### Kubernetes Deployment 
Write Kubernetes manifests for deploying this ML model serving application at production scale.

1. Deployment manifest:
 - Replicas: {{min_replicas}} initial
 - Resource requests and limits:
 - CPU: request={{cpu_request}}, limit={{cpu_limit}}
 - Memory: request={{memory_request}}, limit={{memory_limit}}
 - GPU: nvidia.com/gpu: 1 (if GPU-based)
 - Rolling update strategy: maxUnavailable=0, maxSurge=1 (zero-downtime deploys)
 - Liveness probe: GET /health every 10s, failure threshold 3
 - Readiness probe: GET /ready every 5s (only route traffic when model is loaded)
 - Startup probe: GET /ready with longer timeout for slow model loading

2. Horizontal Pod Autoscaler (HPA):
 - Scale based on: CPU utilization target {{cpu_target}}% or custom metric (requests per second)
 - Min replicas: {{min_replicas}}, max replicas: {{max_replicas}}
 - Scale-down stabilization: 5 minutes to prevent thrashing

3. Service and Ingress:
 - ClusterIP Service for internal traffic
 - Ingress with TLS termination, rate limiting, and timeout settings

4. ConfigMap and Secret management:
 - Non-sensitive config in ConfigMap (model path, log level, batch size)
 - Sensitive config in Secrets (API keys, database credentials)
 - Mount secrets as environment variables, not files

5. Pod disruption budget:
 - minAvailable: {{min_available}} to prevent all pods being evicted simultaneously

6. Namespace and RBAC:
 - Dedicated namespace for ML serving
 - ServiceAccount with minimal permissions

Return: Deployment, HPA, Service, Ingress, ConfigMap, and PodDisruptionBudget manifests. Copy prompt View page Show more ↓ Model Deployment Intermediate Prompt 08 
### Latency Optimization 
Optimize inference latency for this model serving endpoint to meet a p99 latency target of {{latency_target_ms}}ms.

Current p99 latency: {{current_latency_ms}}ms

Work through these optimizations in order of impact:

1. Profile first:
 - Break down request latency into: network, preprocessing, model inference, postprocessing
 - Identify which component dominates

2. Model-level optimizations:
 - Convert to TorchScript (torch.jit.trace or torch.jit.script)
 - Export to ONNX and run with ONNX Runtime (often 2–5× faster than PyTorch for inference)
 - Enable ONNX Runtime execution providers: CUDAExecutionProvider for GPU, TensorRT for maximum speed

3. Batching optimizations:
 - Implement dynamic batching: collect requests for {{batch_wait_ms}}ms, then process as a batch
 - Find optimal batch size: benchmark batch sizes 1, 2, 4, 8, 16, 32 and plot throughput vs latency tradeoff

4. Hardware optimizations:
 - Warm up the model at startup with dummy forward passes to trigger JIT compilation
 - Pin model to a specific GPU with CUDA_VISIBLE_DEVICES
 - Use CUDA streams to overlap data transfer and computation

5. Application-level optimizations:
 - Response caching for repeated identical inputs (LRU cache with size limit)
 - Connection pooling and keep-alive for HTTP
 - Reduce serialization overhead: use MessagePack or protobuf instead of JSON for high-throughput

Return: profiling methodology, optimization checklist with estimated gains, and benchmark code. Copy prompt View page Show more ↓ Model Deployment Intermediate Prompt 09 
### Model Versioning and Registry 
Design and implement a model versioning and registry system using MLflow Model Registry.

1. Model registration:
 - Log model with mlflow.pytorch.log_model (or sklearn/tensorflow)
 - Include: model signature (input/output schema), input example, pip requirements
 - Auto-register to registry after training if val metric exceeds threshold
 - Tag with: git_commit, training_run_id, dataset_version, framework_version

2. Model stages lifecycle:
 - Staging: newly registered models under evaluation
 - Production: models approved for serving
 - Archived: deprecated models (never delete, keep for audit)
 - Implement promotion workflow: Staging → Production requires approval + performance check

3. Model loading for inference:
 - Load by stage (always load 'Production') not by version number
 - Implement a model loader class with caching: reload only when registry version changes
 - Graceful fallback: if Production model fails to load, fall back to last known good version

4. Model comparison before promotion:
 - Load challenger (Staging) and champion (Production) models
 - Evaluate both on a fixed holdout set
 - Promote challenger only if it improves primary metric by > {{threshold}}% with no guardrail degradation

5. Rollback procedure:
 - Script to demote current Production model and promote previous version
 - Alert system when a rollback is triggered

Return: registry integration code, promotion workflow script, and rollback procedure. Copy prompt View page Show more ↓ 
## Optimization 
9 prompt s Optimization Intermediate Prompt 01 
### DataLoader Optimization 
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

Return: bottleneck diagnosis procedure, optimization implementations, and benchmark comparing before vs after. Copy prompt View page Show more ↓ Optimization Advanced Prompt 02 
### Flash Attention Integration 
Integrate Flash Attention into this transformer model to reduce memory and improve speed.

1. Installation and compatibility check:
 - Install flash-attn: pip install flash-attn --no-build-isolation
 - Verify: requires GPU with compute capability ≥ 8.0 (A100, H100, 3090, 4090)
 - Check PyTorch version compatibility

2. Drop-in replacement:
 - Replace standard scaled dot-product attention with flash_attn_func or flash_attn_varlen_func
 - For HuggingFace models: set attn_implementation='flash_attention_2' in from_pretrained

3. Expected improvements:
 - Memory: O(N) instead of O(N²) in sequence length — enables much longer sequences
 - Speed: 2–4× faster than standard attention on A100
 - No approximation: exact same output as standard attention (not approximate)

4. Sequence length scaling:
 - Benchmark max sequence length with standard attention vs Flash Attention on the same GPU memory budget
 - Demonstrate quadratic vs linear memory scaling

5. Causal vs bidirectional:
 - For decoder models: set causal=True in flash_attn_func
 - For encoder models: causal=False

6. Variable-length sequences:
 - Use flash_attn_varlen_func with cu_seqlens to handle variable-length batches without padding waste
 - Compute cumulative sequence lengths from attention masks

7. Fallback:
 - Check if Flash Attention is available at runtime; fall back to scaled_dot_product_attention if not

Return: Flash Attention integration code, before/after memory and speed benchmark, and fallback implementation. Copy prompt View page Show more ↓ Optimization Advanced Chain 03 
### Full Optimization Chain 
Step 1: Baseline measurement — establish training throughput (samples/sec), inference latency (p50/p95/p99), GPU memory usage, and GPU utilization. These are the benchmarks to beat.
Step 2: Profile — use PyTorch Profiler for one training step. Identify whether the bottleneck is I/O, CPU preprocessing, GPU compute, or memory transfers.
Step 3: Quick wins — apply mixed precision (bf16/fp16) and torch.compile. Re-benchmark and record improvement.
Step 4: Memory optimization — if memory is a constraint, apply gradient checkpointing and 8-bit optimizer. Enable the largest batch size that fits in GPU memory.
Step 5: DataLoader optimization — if I/O-bound, tune num_workers, prefetch_factor, and data format. Re-benchmark until GPU utilization > 80%.
Step 6: Inference optimization — export to ONNX or TensorRT. Benchmark against torch.compile. Choose the best option for the latency target.
Step 7: Regression tests — write automated benchmark tests that run on every code change and fail if throughput drops > 5% or latency increases > 10% vs baseline. Copy prompt View page Show more ↓ Optimization Beginner Prompt 04 
### GPU Profiling 
Profile this PyTorch model training run to identify performance bottlenecks.

1. PyTorch Profiler setup:
 - Profile with activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA]
 - Use schedule: wait=1, warmup=1, active=3, repeat=2 (avoid profiling warmup iterations)
 - Record shapes=True to see tensor sizes
 - With_stack=True for Python call stacks
 - Export to Chrome trace and TensorBoard

2. Key metrics to analyze:
 - GPU utilization: target > 80% during forward/backward
 - GPU memory bandwidth utilization
 - Kernel execution time: which CUDA kernels take the most time?
 - CPU↔GPU data transfer time: flag if >10% of step time
 - Idle time between operations (synchronization overhead)

3. Identify specific bottlenecks:
 - Is training I/O-bound? (DataLoader consuming >20% of step time)
 - Is training compute-bound? (GPU utilization high, no idle time)
 - Are there unnecessary CPU↔GPU copies? (check .cpu() or .numpy() calls in hot path)
 - Are there redundant operations in the model forward pass?

4. NVIDIA profiling tools:
 - Run nsys profile to get a system-wide trace
 - Run ncu on the top 3 kernels to get roofline analysis

5. Interpret and prioritize findings:
 - List bottlenecks ranked by time cost
 - For each: root cause and specific optimization to apply

Return: profiling setup code, interpretation guide, and prioritized optimization recommendations. Copy prompt View page Show more ↓ Optimization Intermediate Prompt 05 
### Inference Caching Strategy 
Design and implement an inference caching strategy to reduce redundant computations and improve throughput.

1. Request-level caching:
 - Identify if this model is likely to receive repeated identical inputs (recommender systems, classification of common queries)
 - Implement LRU cache with maximum {{cache_size}} entries
 - Cache key: SHA256 hash of the serialized input tensor
 - Cache hit/miss rate monitoring: log and alert if hit rate drops below expected

2. KV cache (for transformer/autoregressive models):
 - Implement key-value cache for incremental generation
 - Pre-allocate KV cache to avoid dynamic memory allocation during generation
 - Cache eviction policy for long-context scenarios

3. Embedding cache:
 - If the model has a lookup-table style embedding layer for entity IDs, cache frequently accessed embeddings in a dict
 - Warm up the embedding cache with the top {{topk}} most frequent entity IDs at startup

4. Preprocessing cache:
 - Cache the result of expensive preprocessing steps (tokenization, feature extraction) keyed by raw input
 - Use Redis for distributed caching across multiple serving replicas

5. Cache invalidation:
 - When a new model version is deployed, invalidate the entire cache
 - Version the cache key with the model version string

6. Staleness handling:
 - Set TTL (time-to-live) per cache tier based on how frequently inputs change

Return: caching implementation, Redis integration, cache warming script, and monitoring setup. Copy prompt View page Show more ↓ Optimization Intermediate Prompt 06 
### Memory Optimization 
Optimize GPU memory usage for this model to fit a larger batch size or a bigger model on available hardware.

Target: fit on {{gpu_vram}}GB GPU with maximum batch size.

Apply these techniques in order of implementation complexity:

1. Immediate wins (< 1 hour to implement):
 - Enable mixed precision (fp16/bf16) — saves 40–50% memory
 - Set optimizer to use 8-bit Adam (bitsandbytes) — saves optimizer state memory (~75% of optimizer memory)
 - Use set_to_none=True in optimizer.zero_grad()
 - Detach intermediate tensors not needed for backprop
 - Delete unused variables and call torch.cuda.empty_cache() at epoch end

2. Gradient techniques:
 - Gradient accumulation — simulate larger batches with smaller physical batch
 - Gradient checkpointing (activation checkpointing) — recompute activations during backward pass instead of storing them. Trade compute for memory (~30–40% memory reduction, ~20% slower)

3. Model architecture changes:
 - Replace nn.Linear with nn.Linear in 8-bit (bitsandbytes) for inference
 - Use flash attention instead of standard attention (for transformer models)
 - Reduce model width or depth if memory is the primary constraint

4. Advanced: Parameter-Efficient Fine-Tuning:
 - LoRA: train only low-rank adapter matrices (< 1% of parameters)
 - Prefix tuning or prompt tuning for large language models

5. Memory profiling:
 - torch.cuda.memory_summary() after each forward/backward
 - Record peak memory: torch.cuda.max_memory_allocated()
 - Identify which layer consumes the most memory

Return: memory optimization implementation ordered by complexity, expected savings per technique, and memory profiling code. Copy prompt View page Show more ↓ Optimization Beginner Prompt 07 
### Mixed Precision Training 
Implement mixed precision training to reduce memory usage and increase training speed.

1. Automatic Mixed Precision (AMP) with torch.cuda.amp:
 - torch.autocast context manager for the forward pass: dtype=torch.float16 (Volta/Turing) or torch.bfloat16 (Ampere+)
 - GradScaler for loss scaling to prevent fp16 underflow
 - Correct placement: autocast wraps only forward pass, not optimizer step

2. bf16 vs fp16 choice:
 - fp16: faster on Volta/Turing (V100, T4), but requires loss scaling, more numerically unstable
 - bf16: preferred on Ampere+ (A100, H100, 4090), no loss scaling needed, same dynamic range as fp32
 - Recommendation: use bf16 if GPU supports it, fp16 otherwise

3. Operations to keep in fp32:
 - Batch normalization running statistics
 - Loss computation (especially with log operations)
 - Softmax outputs used as probabilities
 - torch.nn.functional.cross_entropy computes in fp32 internally by default

4. GradScaler best practices:
 - Initial scale: 2^16 (default)
 - scaler.step() replaces optimizer.step() — skips update if gradients have Inf/NaN
 - scaler.update() adjusts scale dynamically
 - Check scaler.get_scale() to monitor — if it drops continuously, model has instability issues

5. Expected gains:
 - Memory reduction: ~40–50% for fp16
 - Speed improvement: 1.5–3× on Tensor Core GPUs
 - Verify: run 1 epoch with and without AMP and compare loss curves

Return: complete AMP training loop with GradScaler, bf16/fp16 selection logic, and before/after benchmark code. Copy prompt View page Show more ↓ Optimization Intermediate Prompt 08 
### Throughput Benchmark 
Build a systematic benchmarking harness to measure and optimize training and inference throughput.

1. Training throughput benchmark:
 - Measure samples/second at batch sizes: 8, 16, 32, 64, 128, 256
 - Run 10 warmup steps, then measure over 100 steps
 - Record: batch size, samples/sec, GPU memory used, GPU utilization %
 - Find the optimal batch size (highest samples/sec while staying within GPU memory budget)

2. Inference throughput benchmark:
 - Measure latency (mean, p50, p95, p99) at batch sizes: 1, 2, 4, 8, 16, 32
 - 100 warmup runs, then 1000 measured runs using torch.cuda.synchronize() for accurate GPU timing
 - Plot: latency vs batch size, throughput vs batch size
 - Find the latency-throughput Pareto frontier

3. Comparison matrix:
 - Benchmark the same model in: PyTorch eager, TorchScript, ONNX Runtime, TensorRT
 - For each: p99 latency and throughput at batch_size=1 and batch_size=32

4. Hardware utilization:
 - Use pynvml to monitor GPU utilization and memory bandwidth utilization during benchmarks
 - Flag if GPU utilization < 70% — indicates compute is not the bottleneck

5. Regression testing:
 - Save benchmark results to a JSON file
 - Compare against baseline: flag if throughput drops > 10% between runs

Return: benchmark harness code, results table, and regression detection script. Copy prompt View page Show more ↓ Optimization Advanced Prompt 09 
### torch.compile Optimization 
Apply torch.compile to optimize this PyTorch model for both training and inference.

1. Basic compilation:
 - Apply torch.compile(model) with default settings
 - Measure speedup: run 50 warmup steps, then benchmark 200 steps
 - Expected speedup: 1.5–3× for well-supported models, less for models with dynamic shapes

2. Compilation modes — benchmark and recommend:
 - 'default': balanced compile time and runtime performance
 - 'reduce-overhead': minimize Python overhead, best for small batches
 - 'max-autotune': exhaustive kernel search, longest compile but best runtime
 - 'max-autotune-no-cudagraphs': use if CUDA graphs cause issues with dynamic shapes

3. Backend selection:
 - 'inductor' (default): best general performance
 - 'cudagraphs': lowest latency for fixed-size inputs
 - 'onnxrt': for ONNX-compatible subgraphs

4. Dynamic shapes:
 - Use dynamic=True if input shapes vary at runtime
 - Use torch._dynamo.mark_dynamic(tensor, dim) for specific dynamic dimensions
 - Static shapes (default) produce faster code but recompile on shape changes

5. Debugging compilation issues:
 - torch._dynamo.explain(model)(input) to see why a graph break occurs
 - Set TORCH_LOGS=recompiles to monitor recompilation events
 - Use torch._dynamo.disable decorator to exclude problematic submodules

6. Training vs inference:
 - Compile the model before wrapping with DDP
 - Compile the loss function separately if it is a significant cost

Return: compilation setup, mode comparison benchmark, dynamic shape handling, and debugging guide. Copy prompt View page Show more ↓ 
## MLOps and CI/CD 
7 prompt s MLOps and CI/CD Intermediate Prompt 01 
### Automated Retraining Trigger 
Design an automated model retraining system that triggers based on monitored signals.

1. Retraining trigger conditions (any one is sufficient):
 - Performance degradation: model accuracy on recent data drops below {{performance_threshold}}
 - Data drift: PSI > 0.2 for any top-10 feature by importance
 - Prediction drift: KS test p-value < 0.05 on prediction distribution vs baseline
 - Scheduled: time-based trigger every {{retrain_schedule}} (e.g. weekly, monthly)
 - New data volume: {{new_data_threshold}} new labeled samples available since last training

2. Trigger detection pipeline:
 - Run drift checks daily as a scheduled job
 - Log trigger signals to a monitoring database
 - When a trigger fires: log which signal, the metric value, and the threshold exceeded

3. Retraining execution:
 - Submit training job to compute cluster (Kubernetes Job, Airflow DAG, or SageMaker Pipeline)
 - Use the latest full dataset (not just new data) with a sliding window if dataset grows unbounded
 - Run with the same config as the current production model to enable fair comparison

4. Model promotion gate:
 - New model must beat current production model on a fixed evaluation set by > {{min_improvement}}%
 - If gate passes: automatically promote to staging, trigger deployment pipeline
 - If gate fails: alert the ML team, do not auto-promote

5. Human-in-the-loop option:
 - For high-stakes models: require human approval before any promotion, even if gate passes

Return: drift detection script, trigger condition implementation, retraining job submission code, and promotion gate logic. Copy prompt View page Show more ↓ MLOps and CI/CD Intermediate Prompt 02 
### CI/CD for ML Pipeline 
Design and implement a CI/CD pipeline for this ML project using GitHub Actions.

1. On every pull request — fast checks (< 5 minutes):
 - Code quality: ruff lint, black format check, mypy type checking
 - Unit tests: test data preprocessing, loss functions, metrics, and model architecture
 - Smoke test: train for 2 epochs on 100 samples, assert loss decreases and model saves
 - No data leakage check: run automated leakage detection tests

2. On merge to main — extended checks (< 30 minutes):
 - Integration test: full training run on a small held-out dataset
 - Model performance gate: assert validation metric > {{min_metric_threshold}}
 - Inference test: run the exported model through the serving stack
 - Benchmark: run throughput/latency benchmark and compare to baseline

3. On new model registration — deployment checks:
 - Champion vs challenger comparison on fixed holdout set
 - Deploy to staging if challenger beats champion by > {{improvement_threshold}}%
 - Run smoke test in staging environment
 - Manual approval gate before production deployment

4. GitHub Actions workflow structure:
 - Separate workflow files for each stage
 - Cache: pip dependencies, pre-downloaded datasets for tests
 - Secrets: model registry credentials, cloud storage keys via GitHub Secrets

5. Failure handling:
 - Notify Slack channel on pipeline failure with the failing step and logs link
 - Auto-revert deployment if post-deployment canary metrics degrade

Return: GitHub Actions YAML files for each pipeline stage and a workflow diagram. Copy prompt View page Show more ↓ MLOps and CI/CD Advanced Prompt 03 
### Data Versioning with DVC 
Set up data versioning and pipeline tracking for this ML project using DVC.

1. DVC initialization:
 - dvc init in the Git repository
 - Configure remote storage: S3, GCS, or Azure Blob
 - .dvcignore file for files to exclude

2. Data versioning:
 - Track large data files and directories: dvc add data/raw/
 - Commit .dvc files to Git, push data to remote: dvc push
 - Retrieve a specific data version: git checkout {commit} && dvc pull
 - List data versions and their Git commits for audit trail

3. DVC pipeline definition (dvc.yaml):
 - Define pipeline stages: preprocess → train → evaluate
 - For each stage: deps (inputs), outs (outputs), params (config values), metrics (metrics.json)
 - Cache: DVC caches stage outputs — skips re-running unchanged stages
 - Run the pipeline: dvc repro

4. Experiment tracking:
 - dvc exp run for tracking experiments with different params
 - dvc exp show to compare experiments in a table
 - dvc exp branch to create a Git branch from a promising experiment

5. Metrics and params tracking:
 - Save metrics as JSON: accuracy, loss, etc.
 - dvc metrics show, dvc metrics diff to compare across commits
 - dvc params diff to see which params changed between runs

6. CI/CD integration:
 - dvc pull in CI before running tests
 - dvc repro in CI to re-run the pipeline if deps changed
 - dvc push in CI to save new data artifacts after processing

Return: dvc.yaml pipeline definition, Git workflow for data versioning, and CI/CD integration. Copy prompt View page Show more ↓ MLOps and CI/CD Advanced Chain 04 
### MLOps Platform Chain 
Step 1: Assess current state — inventory existing tools for: experiment tracking, model registry, data versioning, serving, and monitoring. Identify the biggest gaps causing friction for the ML team.
Step 2: Define the platform requirements — number of ML engineers, models in production, deployment frequency, latency requirements, on-prem vs cloud. These drive the tool selection.
Step 3: Design the stack — select and justify tools for each layer: orchestration (Airflow/Kubeflow/Prefect), experiment tracking (MLflow/W&B), model registry (MLflow/SageMaker), serving (TorchServe/Triton/BentoML), monitoring (Evidently/WhyLabs).
Step 4: Define the ML lifecycle workflow — document the exact steps from idea to production: experiment → training run → model registration → evaluation → staging → production → monitoring → retraining trigger.
Step 5: Implement the golden path — build a template project that uses all platform components. An engineer starting a new project should be able to use this template and have full MLOps support from day one.
Step 6: Write the runbook — document how to: deploy a new model, roll back a model, investigate a prediction incident, and trigger retraining. Each runbook should be executable by an on-call engineer without ML expertise.
Step 7: Define success metrics for the platform: deployment frequency, time-from-experiment-to-production, MTTR (mean time to recover from a model incident), and % of models with active drift monitoring. Copy prompt View page Show more ↓ MLOps and CI/CD Advanced Prompt 05 
### Model Incident Response 
Write a model incident response playbook for production ML systems.

1. Incident classification:
 - P0 (Critical): model returning errors for >5% of requests, or predictions are completely wrong (e.g. all same class)
 - P1 (High): model latency > 2× SLA, silent accuracy degradation detected, feature drift alarm
 - P2 (Medium): single-segment performance degradation, prediction distribution shift detected
 - P3 (Low): data freshness lag, minor accuracy regression within acceptable bounds

2. Detection and alerting:
 - Define the monitoring signals that trigger each severity level
 - Alerting chain: PagerDuty → on-call ML engineer → ML team lead → CTO (for P0 only)
 - Initial acknowledgment SLA: P0=5 min, P1=15 min, P2=1 hour, P3=next business day

3. Immediate triage checklist (first 15 minutes for P0/P1):
 - Is this a model issue or an infrastructure issue? (Check serving logs, Kubernetes pod status)
 - Did a deployment happen recently? (Check deployment log)
 - Is the input data correct? (Check feature store freshness, pipeline health)
 - Is the error rate growing or stable?

4. Rollback procedure:
 - Trigger: error rate > 5% AND confirmed model issue
 - Steps: promote previous Production model version in registry → trigger rolling restart → verify error rate drops
 - Target: rollback complete within 10 minutes of decision to rollback

5. Post-incident review:
 - Timeline of events
 - Root cause analysis
 - Customer or business impact
 - What monitoring would have detected this earlier?
 - Action items with owners and deadlines

Return: complete incident response playbook with classification matrix, triage checklist, rollback procedure, and post-mortem template. Copy prompt View page Show more ↓ MLOps and CI/CD Intermediate Prompt 06 
### Model Monitoring Setup 
Set up a comprehensive production model monitoring system.

1. Prediction logging:
 - Log every prediction to a structured store: timestamp, request_id, model_version, input_features, prediction, confidence, latency_ms
 - Use async logging to avoid adding latency to the serving path
 - Rotate logs daily and archive to object storage after 7 days

2. Service-level monitoring (Prometheus + Grafana):
 - Metrics to track: requests/sec, error rate (4xx, 5xx), p50/p95/p99 latency, queue depth
 - Alerts: error rate > 1%, p99 latency > {{latency_sla_ms}}, model load failure
 - Dashboard: request volume, latency percentiles, error rate, model version deployed

3. Model-level monitoring:
 - Prediction distribution: compare daily prediction distribution to training distribution (PSI)
 - Confidence distribution: alert if mean confidence drops significantly (model is uncertain)
 - Output drift: KS test on prediction scores between current week vs baseline week

4. Feature/data drift monitoring:
 - For each of the top 10 features: compute PSI weekly
 - PSI < 0.1: no significant change
 - PSI 0.1–0.2: moderate drift, investigate
 - PSI > 0.2: significant drift, trigger retraining evaluation

5. Ground truth feedback loop:
 - If labels become available with a delay (e.g. churn labels available after 30 days): join predictions to outcomes and compute actual model accuracy over time
 - Alert if rolling 30-day accuracy drops below {{accuracy_threshold}}

Return: prediction logging implementation, Prometheus metrics setup, drift monitoring scripts, and Grafana dashboard spec. Copy prompt View page Show more ↓ MLOps and CI/CD Beginner Prompt 07 
### Training Pipeline as Code 
Refactor this ad-hoc training script into a reproducible, configurable ML pipeline.

1. Configuration management:
 - Move all hyperparameters and paths to a config file (YAML or JSON)
 - Use OmegaConf or Hydra for hierarchical config with command-line overrides
 - Never hardcode paths — all paths are config variables with sensible defaults
 - Log the full resolved config at the start of every run

2. Pipeline stages as separate functions or classes:
 - data_preprocessing(): validate, clean, and split data
 - train(): train model with given config
 - evaluate(): evaluate on test set and return metrics dict
 - export(): save model in deployment format
 - Each stage is independently runnable and testable

3. Artifact management:
 - Every run saves to a versioned output directory: outputs/{run_id}/
 - Artifacts: model checkpoint, config copy, metrics JSON, training plots
 - Symlink outputs/latest → most recent run for convenience

4. CLI interface:
 - python train.py --config configs/base.yaml --overrides learning_rate=1e-4
 - Subcommands: train, evaluate, export, full (all stages)

5. Dependency management:
 - requirements.txt with pinned versions
 - Optional: pyproject.toml with extras for training vs inference

6. Entry point guard:
 - All DataLoader workers require if __name__ == '__main__': guard on Windows

Return: refactored pipeline structure, Hydra config setup, and CLI interface. Copy prompt View page Show more ↓ 
## Model Compression 
7 prompt s Model Compression Advanced Chain 01 
### Compression Pipeline Chain 
Step 1: Establish the baseline — measure the uncompressed model: size (MB), FLOPs, p50/p95/p99 inference latency at batch_size=1 and batch_size=32, and accuracy on the full validation set.
Step 2: Pruning — apply structured pruning at 30%, 50%, and 70% sparsity. Fine-tune after each level. Record accuracy, size, and latency at each sparsity level.
Step 3: Quantization — apply INT8 post-training quantization to the pruned model. If accuracy drops > 1%, apply QAT. Record accuracy, size, and latency.
Step 4: Distillation (optional) — if the compressed model still underperforms targets, use the original uncompressed model as a teacher to recover accuracy via knowledge distillation.
Step 5: ONNX export and TensorRT optimization — export the compressed model to TensorRT FP16. Verify numerical correctness. Record final latency and throughput.
Step 6: Accuracy vs efficiency Pareto analysis — plot all tested configurations on an accuracy vs latency scatter plot. Identify the Pareto-optimal point that meets the deployment requirements.
Step 7: Write a compression report: original vs final model comparison (size, latency, FLOPs, accuracy), techniques applied, any accuracy recovery steps taken, and recommendation for production deployment. Copy prompt View page Show more ↓ Model Compression Intermediate Prompt 02 
### Knowledge Distillation 
Implement knowledge distillation to train a smaller student model to match a larger teacher model.

Teacher model: {{teacher_model}} (large, high-accuracy, slow)
Student model: {{student_model}} (small, faster, to be trained)

1. Soft target distillation (Hinton et al. 2015):
 - Get teacher soft probabilities: softmax(teacher_logits / temperature)
 - Student loss = α × KL_divergence(student_soft, teacher_soft) + (1-α) × CrossEntropy(student, hard_labels)
 - Temperature T: higher T produces softer distributions (try T=3, T=5, T=10)
 - α: weight between distillation loss and task loss (try α=0.7)

2. Intermediate layer distillation (better for deep networks):
 - Match intermediate feature maps between teacher and student layers
 - Use an adapter layer if teacher and student have different hidden dimensions
 - Feature distillation loss: MSE(student_features, teacher_features)

3. Training procedure:
 - Freeze teacher model (no gradients)
 - Train student with combined loss
 - Use a slightly higher learning rate than training from scratch
 - Run for same number of epochs as training student from scratch

4. Evaluation:
 - Student accuracy vs teacher accuracy
 - Student accuracy vs same architecture trained from scratch (distillation should outperform)
 - Student inference latency vs teacher inference latency

5. Self-distillation variant:
 - If no pre-trained teacher exists: use the model's own earlier epochs as the teacher

Return: distillation training loop, temperature sweep results, student vs teacher benchmark, and comparison to training from scratch. Copy prompt View page Show more ↓ Model Compression Intermediate Prompt 03 
### ONNX Export and Validation 
Export this PyTorch model to ONNX format and validate correctness and performance.

1. Export to ONNX:
 - Use torch.onnx.export with opset_version=17 (latest stable)
 - Define input_names, output_names, and dynamic_axes for variable batch size and sequence length
 - Set do_constant_folding=True for graph optimization
 - Use dynamo=True (torch.onnx.dynamo_export) for newer models with control flow

2. ONNX graph validation:
 - onnx.checker.check_model(model) for structural validity
 - onnxsim (onnx-simplifier): simplify the graph and remove redundant nodes
 - Visualize with Netron to inspect the computation graph

3. Numerical correctness check:
 - Run inference with identical inputs through PyTorch and ONNX Runtime
 - Assert all outputs match to within rtol=1e-3, atol=1e-5
 - Test with multiple batch sizes and sequence lengths if dynamic axes are used

4. ONNX Runtime inference:
 - Create InferenceSession with providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
 - Optimize with ort.SessionOptions: graph_optimization_level=ORT_ENABLE_ALL
 - Enable io_binding for zero-copy GPU inference

5. Performance benchmark:
 - Compare p50/p95/p99 latency: PyTorch vs ONNX Runtime
 - Compare throughput at batch sizes 1, 8, 32
 - Typical improvement: 1.5–4× speedup on CPU, 1.2–2× on GPU

6. Common export issues and fixes:
 - Control flow (if/else in forward): use torch.jit.script first
 - Custom ops: register custom ONNX op or rewrite using supported ops
 - Dynamic shapes: test with min, typical, and max shapes

Return: export script, validation code, numerical correctness tests, and benchmark results. Copy prompt View page Show more ↓ Model Compression Beginner Prompt 04 
### Post-Training Quantization 
Apply post-training quantization (PTQ) to reduce model size and inference latency.

1. INT8 static quantization (PyTorch):
 - Prepare model: torch.quantization.prepare with a QConfig
 - Calibrate on a representative dataset (100–1000 samples): run forward passes to collect activation statistics
 - Convert: torch.quantization.convert to replace float ops with int8 ops
 - Save and measure: model size before vs after, inference latency before vs after

2. INT8 dynamic quantization:
 - torch.quantization.quantize_dynamic for models where activation ranges vary greatly
 - Suitable for: LSTMs, linear layers in NLP models
 - No calibration step needed

3. Quantization-aware training (QAT) if accuracy drops > 1%:
 - Insert fake quantization nodes during training
 - Fine-tune for {{qat_epochs}} epochs at a lower learning rate
 - Convert to fully quantized model after training

4. Accuracy validation:
 - Evaluate quantized model on the full validation set
 - Acceptable accuracy drop: < 1% for most production use cases
 - If accuracy drops significantly: try QAT, or quantize only the later layers

5. ONNX + ONNX Runtime INT8:
 - Export to ONNX, then apply ONNXRuntime quantization
 - ort.quantization.quantize_dynamic or quantize_static
 - Often faster than PyTorch native quantization on CPU

Return: PTQ implementation, QAT setup, accuracy comparison table, and latency/size improvement metrics. Copy prompt View page Show more ↓ Model Compression Intermediate Prompt 05 
### Structured Pruning 
Apply structured pruning to reduce this model's size and inference cost.

Unstructured pruning (individual weight zeroing) does not improve real-world latency without sparse hardware. Structured pruning removes entire filters, channels, or layers for actual speedup.

1. Sensitivity analysis:
 - For each layer, measure accuracy impact of removing that layer entirely
 - Rank layers from least to most sensitive
 - Layers early in the network and the last classification layer are typically most sensitive

2. Filter/channel pruning (for CNNs):
 - Score filters by L1-norm of weights (smaller norm = less important)
 - Remove the bottom {{prune_ratio}}% of filters in each prunable layer
 - Handle channel dimension changes: update the next layer's input channels accordingly
 - Re-run BN calibration after pruning

3. Attention head pruning (for transformers):
 - Score attention heads by mean attention entropy or gradient-based importance
 - Remove the {{num_heads_to_prune}} least important heads per layer
 - Adjust head projection dimensions accordingly

4. Iterative pruning and fine-tuning:
 - Prune → fine-tune → prune → fine-tune (gradual pruning is better than one-shot)
 - Use a cosine pruning schedule that increases sparsity gradually
 - Target sparsity: {{target_sparsity}}%

5. Results measurement:
 - FLOPs reduction
 - Parameter reduction
 - Inference latency reduction (must measure on real hardware, not estimate)
 - Accuracy change vs unpruned model

Return: sensitivity analysis, pruning implementation, fine-tuning loop, and results table. Copy prompt View page Show more ↓ Model Compression Advanced Prompt 06 
### TensorRT Optimization 
Optimize this model for NVIDIA GPU inference using TensorRT.

1. Conversion path: PyTorch → ONNX → TensorRT engine
 - Export to ONNX (opset 17, dynamic axes for batch)
 - Build TensorRT engine using trtexec or the TensorRT Python API

2. Precision selection:
 - FP32: baseline, no accuracy loss
 - FP16: enable with builder_config.set_flag(trt.BuilderFlag.FP16) — typically 2× speedup, minimal accuracy loss
 - INT8: requires calibration dataset for activation range statistics. Use IInt8EntropyCalibrator2. Up to 4× speedup, requires validation.

3. Engine build configuration:
 - Set optimization profiles for dynamic shape engines: min, optimal, and max input shapes
 - workspace size: 4GB (larger allows TensorRT to try more kernel alternatives)
 - Enable timing cache for faster re-builds

4. INT8 calibration:
 - Provide 100–500 representative calibration samples (not validation set)
 - Run calibration and save calibration table for reuse
 - Validate accuracy: if accuracy drops > 1%, use layer-wise precision override for sensitive layers

5. Layer-wise precision override:
 - Keep the first and last layers in FP32
 - Mark softmax and normalization layers as FP32
 - Use FP16 or INT8 for the bulk of the network

6. Performance measurement:
 - Use trtexec --percentile=99 for accurate p99 latency
 - Compare: PyTorch eager, TorchScript, ONNX Runtime, TensorRT FP16, TensorRT INT8

7. Engine serialization and loading:
 - Serialize engine to disk — engines are GPU-specific, not portable
 - Load at inference time and bind input/output buffers

Return: full TensorRT conversion pipeline, INT8 calibration code, precision comparison table, and engine serving wrapper. Copy prompt View page Show more ↓ Model Compression Advanced Prompt 07 
### Weight Sharing and Low-Rank Decomposition 
Apply low-rank matrix decomposition to compress the large weight matrices in this model.

1. Identify compression targets:
 - Profile all weight matrices by parameter count and FLOPs contribution
 - Focus on large linear layers (embedding, feed-forward, projection layers)
 - Attention QKV matrices and output projections in transformers are primary targets

2. SVD-based decomposition:
 - For weight matrix W (m × n), compute SVD: W = U × S × Vt
 - Keep only top-k singular values: W ≈ U_k × S_k × Vt_k
 - Rank k selection: sweep k values and measure accuracy vs compression tradeoff
 - Replace original layer with two consecutive smaller layers: Linear(in, k) + Linear(k, out)
 - Break-even rank: k < (m × n) / (m + n) reduces parameter count

3. LoRA (Low-Rank Adaptation) for fine-tuning:
 - Freeze base model weights
 - Add trainable low-rank matrices A (d × r) and B (r × k) in parallel with frozen weights
 - Output = Wx + BAx × (alpha/r)
 - Typical ranks: r=4, r=8, r=16, r=64
 - Merge LoRA weights back into base model for inference: W_new = W + B × A

4. Accuracy evaluation:
 - Measure accuracy at compression ratios: 25%, 50%, 75% parameter reduction
 - Plot accuracy vs compression ratio curve
 - Find the Pareto-optimal point

5. Mixed-rank strategy:
 - Apply higher compression to less sensitive layers, lower compression to sensitive ones
 - Use gradient-based layer sensitivity to guide rank assignment

Return: SVD decomposition code, LoRA implementation, compression curve, and mixed-rank strategy. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
