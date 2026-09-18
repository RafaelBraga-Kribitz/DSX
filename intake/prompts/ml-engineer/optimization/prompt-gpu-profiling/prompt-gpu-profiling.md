# GPU Profiling *AI Prompt *

This prompt sets up PyTorch and NVIDIA profiling to identify where training time is being spent across CPU, CUDA kernels, data loading, and transfers. It is designed to move from vague performance complaints to ranked, evidence-based bottlenecks. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: profiling setup code, interpretation guide, and prioritized optimization recommendations. 
```

## When to use this prompt 
Use case 01 
when a training run is slower than expected and you need root-cause analysis 
Use case 02 
when DataLoader, kernel execution, or CPU↔GPU transfer overhead is suspected 
Use case 03 
when you want PyTorch Profiler plus nsys and ncu guidance 
Use case 04 
when optimizations should be prioritized by actual time cost 

## What the AI should return 

Profiling setup code, an interpretation guide for key profiler outputs, and prioritized optimization recommendations with likely root causes. 

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
