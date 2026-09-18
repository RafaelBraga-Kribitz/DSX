# torch.compile Optimization *AI Prompt *

This prompt applies torch.compile to a PyTorch model for training or inference, benchmarks compilation modes, and explains how to handle graph breaks and dynamic shapes. It is useful when you want modern compiler-based speedups without rewriting the model. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: compilation setup, mode comparison benchmark, dynamic shape handling, and debugging guide. 
```

## When to use this prompt 
Use case 01 
when optimizing PyTorch training or inference with torch.compile 
Use case 02 
when you want to compare compilation modes and backends 
Use case 03 
when dynamic shapes or graph breaks need debugging guidance 
Use case 04 
when benchmarking compiled versus eager execution 

## What the AI should return 

Compilation setup code, benchmark comparisons across modes, dynamic shape handling examples, and a debugging guide for common compile issues. 

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
