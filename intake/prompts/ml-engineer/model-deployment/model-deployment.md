# Model Deployment *AI Prompts *

9 ML Engineer prompts in Model Deployment. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 8 single prompts · 1 chain. 

## AI prompts in Model Deployment 
9 prompts Intermediate Single prompt 01 
### A/B Deployment Pattern 

This prompt implements an A/B deployment pattern for serving a challenger model alongside a champion model, with deterministic routing, per-variant metrics, and rollout or rollback automation. It is useful for safe online model experimentation in production. 
Prompt text Implement an A/B model deployment pattern to safely roll out a new model version alongside the current production model.

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

Return: routing middleware, metrics logging, statistical comparison, and automated rollout/rollback logic. Copy prompt Open prompt details Intermediate Single prompt 02 
### Batch Inference Pipeline 

This prompt designs a scalable batch inference pipeline for large datasets with streaming reads, mixed precision inference, chunked writes, progress tracking, and resume support. It is built for offline scoring workloads where throughput and fault tolerance matter. 
Prompt text Build an efficient batch inference pipeline for running predictions on {{dataset_size}} records.

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

Return: complete batch inference script with progress tracking and fault tolerance. Copy prompt Open prompt details Advanced Chain 03 
### Deployment Readiness Chain 

This chain assesses whether a model service is truly ready for production by verifying model outputs, API behavior, load performance, rollback readiness, monitoring, runbooks, and sign-off gates. It is meant to reduce surprises during launch. 
Prompt text Step 1: Model validation — run the model on a fixed golden dataset and assert outputs match expected values to ±1e-5. Confirm model size, latency on target hardware (p50/p95/p99), and memory footprint meet requirements.
Step 2: API contract verification — test all endpoints with valid inputs, invalid inputs, edge cases (empty batch, max size batch), and concurrent requests. Verify error codes and messages match the API spec.
Step 3: Load testing — run a 5-minute load test at 2× expected peak traffic using Locust or k6. Confirm p99 latency stays within SLA, error rate < 0.1%, and no memory leaks (memory usage stable).
Step 4: Rollback plan — document the exact steps to roll back to the previous model version within 5 minutes. Verify the rollback procedure works in staging before deploying to production.
Step 5: Monitoring setup — confirm all dashboards are in place: request rate, error rate, p50/p95/p99 latency, prediction distribution, feature drift, and GPU/CPU utilization. Verify alerts are firing correctly.
Step 6: Runbook — write a deployment runbook covering: deployment steps, expected log messages, how to verify success, known issues and their fixes, and escalation path if something goes wrong.
Step 7: Go / no-go checklist — create a final checklist with sign-off required from: ML engineer (model quality), SRE (infrastructure), and product (business metrics). Block deployment until all sign off. Copy prompt Open prompt details Beginner Single prompt 04 
### Docker Container for ML 

This prompt produces an optimized Docker packaging setup for a model serving application, including a multi-stage Dockerfile, .dockerignore, and docker-compose example. It emphasizes secure and minimal runtime images, pinned dependencies, health checks, and configurable runtime behavior. 
Prompt text Write an optimized Dockerfile for deploying this ML model serving application.

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

Return: Dockerfile, .dockerignore, and docker-compose.yml for local testing. Copy prompt Open prompt details Beginner Single prompt 05 
### FastAPI Serving Endpoint 

This prompt builds a production-oriented FastAPI inference service for an ML model, including request validation, startup model loading, health endpoints, error handling, latency reporting, and concurrency controls. It is intended for real serving environments rather than quick demos. 
Prompt text Build a production-ready FastAPI model serving endpoint for {{model_name}}.

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

Return: complete FastAPI application code with Dockerfile. Copy prompt Open prompt details Advanced Single prompt 06 
### Feature Store Integration 

This prompt integrates a model serving system with a feature store and addresses online lookup speed, freshness, training-serving skew prevention, point-in-time training correctness, and failure fallback behavior. It is useful in feature-rich production inference systems. 
Prompt text Design the integration between this ML model serving system and a feature store (Feast / Tecton / Hopsworks).

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

Return: feature retrieval code, training data generation script, skew detection setup, and circuit breaker implementation. Copy prompt Open prompt details Advanced Single prompt 07 
### Kubernetes Deployment 

This prompt writes Kubernetes manifests for running an ML serving service at production scale, including Deployment, HPA, Service, Ingress, ConfigMap, and PodDisruptionBudget. It focuses on safe rollout behavior, readiness, autoscaling, and operational resilience. 
Prompt text Write Kubernetes manifests for deploying this ML model serving application at production scale.

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

Return: Deployment, HPA, Service, Ingress, ConfigMap, and PodDisruptionBudget manifests. Copy prompt Open prompt details Intermediate Single prompt 08 
### Latency Optimization 

This prompt works through inference latency optimization in a structured order, starting with profiling and then addressing model, batching, hardware, and application-level bottlenecks. It is meant to help an endpoint meet a concrete p99 latency target. 
Prompt text Optimize inference latency for this model serving endpoint to meet a p99 latency target of {{latency_target_ms}}ms.

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

Return: profiling methodology, optimization checklist with estimated gains, and benchmark code. Copy prompt Open prompt details Intermediate Single prompt 09 
### Model Versioning and Registry 

This prompt designs a model versioning and governance workflow around MLflow Model Registry. It covers model registration, lifecycle stages, production loading by stage, promotion checks, and rollback procedures for safer model operations. 
Prompt text Design and implement a model versioning and registry system using MLflow Model Registry.

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

Return: registry integration code, promotion workflow script, and rollback procedure. Copy prompt Open prompt details 
## Recommended Model Deployment workflow 
1 
### A/B Deployment Pattern 

Start with a focused prompt in Model Deployment so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Batch Inference Pipeline 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Deployment Readiness Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Docker Container for ML 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
