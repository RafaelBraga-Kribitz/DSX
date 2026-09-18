# Optimization *AI Prompts *

9 ML Engineer prompts in Optimization. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 8 single prompts · 1 chain. 

## AI prompts in Optimization 
9 prompts Intermediate Single prompt 01 
### DataLoader Optimization 

This prompt diagnoses whether the DataLoader is the training bottleneck and then tunes worker count, prefetching, pinning, and data format choices to improve utilization. It is aimed at eliminating input pipeline stalls that starve the GPU. 
Prompt text Diagnose and optimize the DataLoader to eliminate I/O bottlenecks in this training pipeline.

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

Return: bottleneck diagnosis procedure, optimization implementations, and benchmark comparing before vs after. Copy prompt Open prompt details Advanced Single prompt 02 
### Flash Attention Integration 

This prompt integrates Flash Attention into a transformer model, including compatibility checks, drop-in replacements, variable-length support, and fallback behavior. It is useful for reducing memory use and speeding up attention-heavy workloads on supported GPUs. 
Prompt text Integrate Flash Attention into this transformer model to reduce memory and improve speed.

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

Return: Flash Attention integration code, before/after memory and speed benchmark, and fallback implementation. Copy prompt Open prompt details Advanced Chain 03 
### Full Optimization Chain 

This chain performs a full optimization pass on a training and inference stack, moving from baseline measurement and profiling to quick wins, memory work, DataLoader tuning, inference export, and regression testing. It is intended for systematic performance hardening rather than one-off tweaks. 
Prompt text Step 1: Baseline measurement — establish training throughput (samples/sec), inference latency (p50/p95/p99), GPU memory usage, and GPU utilization. These are the benchmarks to beat.
Step 2: Profile — use PyTorch Profiler for one training step. Identify whether the bottleneck is I/O, CPU preprocessing, GPU compute, or memory transfers.
Step 3: Quick wins — apply mixed precision (bf16/fp16) and torch.compile. Re-benchmark and record improvement.
Step 4: Memory optimization — if memory is a constraint, apply gradient checkpointing and 8-bit optimizer. Enable the largest batch size that fits in GPU memory.
Step 5: DataLoader optimization — if I/O-bound, tune num_workers, prefetch_factor, and data format. Re-benchmark until GPU utilization > 80%.
Step 6: Inference optimization — export to ONNX or TensorRT. Benchmark against torch.compile. Choose the best option for the latency target.
Step 7: Regression tests — write automated benchmark tests that run on every code change and fail if throughput drops > 5% or latency increases > 10% vs baseline. Copy prompt Open prompt details Beginner Single prompt 04 
### GPU Profiling 

This prompt sets up PyTorch and NVIDIA profiling to identify where training time is being spent across CPU, CUDA kernels, data loading, and transfers. It is designed to move from vague performance complaints to ranked, evidence-based bottlenecks. 
Prompt text Profile this PyTorch model training run to identify performance bottlenecks.

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

Return: profiling setup code, interpretation guide, and prioritized optimization recommendations. Copy prompt Open prompt details Intermediate Single prompt 05 
### Inference Caching Strategy 

This prompt designs an inference caching strategy covering request-level caching, transformer KV caching, embedding caches, preprocessing caches, invalidation, and monitoring. It is best for services that see repeated or incrementally related inputs and can benefit from avoiding redundant computation. 
Prompt text Design and implement an inference caching strategy to reduce redundant computations and improve throughput.

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

Return: caching implementation, Redis integration, cache warming script, and monitoring setup. Copy prompt Open prompt details Intermediate Single prompt 06 
### Memory Optimization 

This prompt applies practical GPU memory optimization techniques in escalating order of complexity, from AMP and optimizer choices to checkpointing and parameter-efficient fine-tuning. It is intended to help models fit on constrained hardware with minimal guesswork. 
Prompt text Optimize GPU memory usage for this model to fit a larger batch size or a bigger model on available hardware.

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

Return: memory optimization implementation ordered by complexity, expected savings per technique, and memory profiling code. Copy prompt Open prompt details Beginner Single prompt 07 
### Mixed Precision Training 

This prompt adds mixed precision training to a PyTorch workflow using AMP, including bf16 or fp16 selection, GradScaler usage, and simple benchmark comparisons. It focuses on achieving speed and memory gains without destabilizing training. 
Prompt text Implement mixed precision training to reduce memory usage and increase training speed.

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

Return: complete AMP training loop with GradScaler, bf16/fp16 selection logic, and before/after benchmark code. Copy prompt Open prompt details Intermediate Single prompt 08 
### Throughput Benchmark 

This prompt builds a benchmark harness for training and inference throughput, including warmup, repeated measurements, GPU monitoring, latency percentiles, and regression detection. It is useful for establishing performance baselines and catching slowdowns over time. 
Prompt text Build a systematic benchmarking harness to measure and optimize training and inference throughput.

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

Return: benchmark harness code, results table, and regression detection script. Copy prompt Open prompt details Advanced Single prompt 09 
### torch.compile Optimization 

This prompt applies torch.compile to a PyTorch model for training or inference, benchmarks compilation modes, and explains how to handle graph breaks and dynamic shapes. It is useful when you want modern compiler-based speedups without rewriting the model. 
Prompt text Apply torch.compile to optimize this PyTorch model for both training and inference.

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

Return: compilation setup, mode comparison benchmark, dynamic shape handling, and debugging guide. Copy prompt Open prompt details 
## Recommended Optimization workflow 
1 
### DataLoader Optimization 

Start with a focused prompt in Optimization so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Flash Attention Integration 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full Optimization Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### GPU Profiling 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
