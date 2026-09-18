# Latency Optimization *AI Prompt *

This prompt works through inference latency optimization in a structured order, starting with profiling and then addressing model, batching, hardware, and application-level bottlenecks. It is meant to help an endpoint meet a concrete p99 latency target. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: profiling methodology, optimization checklist with estimated gains, and benchmark code. 
```

## When to use this prompt 
Use case 01 
when an ML endpoint must hit a strict p99 latency SLA 
Use case 02 
when you need to profile and separate preprocessing, inference, and networking costs 
Use case 03 
when dynamic batching or export to ONNX Runtime may help 
Use case 04 
when you want benchmark code and an optimization checklist 

## What the AI should return 

A profiling methodology, ordered optimization plan with estimated gains, and benchmark code for testing latency and throughput improvements. 

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

Once you have the first result, continue deeper with related prompts in Model Deployment.
