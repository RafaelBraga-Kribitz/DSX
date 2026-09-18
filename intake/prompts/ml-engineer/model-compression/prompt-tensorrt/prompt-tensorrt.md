# TensorRT Optimization *AI Prompt *

This prompt optimizes NVIDIA GPU inference with TensorRT through an ONNX-based pipeline, optional FP16 or INT8 precision, calibration, and engine serialization. It is meant for teams chasing the lowest possible latency on supported NVIDIA hardware. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: full TensorRT conversion pipeline, INT8 calibration code, precision comparison table, and engine serving wrapper. 
```

## When to use this prompt 
Use case 01 
when GPU inference needs to be faster than PyTorch or ONNX Runtime alone 
Use case 02 
when TensorRT FP16 or INT8 optimization is under consideration 
Use case 03 
when calibration and layer-wise precision control are needed 
Use case 04 
when you need a reusable serialized engine and serving wrapper 

## What the AI should return 

A TensorRT conversion pipeline, calibration code for INT8 if needed, precision comparison results, and engine loading or serving code. 

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
