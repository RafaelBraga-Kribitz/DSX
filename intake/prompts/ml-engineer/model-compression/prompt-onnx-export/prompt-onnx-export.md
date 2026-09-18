# ONNX Export and Validation *AI Prompt *

This prompt exports a PyTorch model to ONNX, validates graph correctness, compares outputs against PyTorch, and benchmarks ONNX Runtime performance. It is useful when preparing a model for portable or faster inference beyond eager PyTorch. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: export script, validation code, numerical correctness tests, and benchmark results. 
```

## When to use this prompt 
Use case 01 
when exporting PyTorch models for deployment with ONNX Runtime 
Use case 02 
when correctness between PyTorch and ONNX must be verified numerically 
Use case 03 
when dynamic batch or sequence dimensions are needed 
Use case 04 
when you want benchmark evidence before switching runtimes 

## What the AI should return 

ONNX export code, validation and numerical correctness tests, and benchmark comparisons between PyTorch and ONNX Runtime. 

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

Once you have the first result, continue deeper with related prompts in Model Compression.
