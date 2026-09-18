# Full Optimization Chain *AI Prompt *

This chain performs a full optimization pass on a training and inference stack, moving from baseline measurement and profiling to quick wins, memory work, DataLoader tuning, inference export, and regression testing. It is intended for systematic performance hardening rather than one-off tweaks. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Baseline measurement — establish training throughput (samples/sec), inference latency (p50/p95/p99), GPU memory usage, and GPU utilization. These are the benchmarks to beat.
Step 2: Profile — use PyTorch Profiler for one training step. Identify whether the bottleneck is I/O, CPU preprocessing, GPU compute, or memory transfers.
Step 3: Quick wins — apply mixed precision (bf16/fp16) and torch.compile. Re-benchmark and record improvement.
Step 4: Memory optimization — if memory is a constraint, apply gradient checkpointing and 8-bit optimizer. Enable the largest batch size that fits in GPU memory.
Step 5: DataLoader optimization — if I/O-bound, tune num_workers, prefetch_factor, and data format. Re-benchmark until GPU utilization > 80%.
Step 6: Inference optimization — export to ONNX or TensorRT. Benchmark against torch.compile. Choose the best option for the latency target.
Step 7: Regression tests — write automated benchmark tests that run on every code change and fail if throughput drops > 5% or latency increases > 10% vs baseline. 
```

## When to use this prompt 
Use case 01 
when you want an end-to-end optimization workflow instead of isolated tuning 
Use case 02 
when throughput, latency, memory, and utilization must all improve together 
Use case 03 
when you need a sequence that starts with measurement and ends with regression guards 
Use case 04 
when production performance has to be documented and repeatable 

## What the AI should return 

A structured optimization plan with baseline metrics, profiling findings, applied optimizations, re-benchmarks, and automated regression test criteria. 

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
