# Post-Training Quantization *AI Prompt *

This prompt applies post-training quantization and, if needed, quantization-aware training to reduce model size and improve inference speed. It includes validation steps so compression gains can be weighed against accuracy loss. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: PTQ implementation, QAT setup, accuracy comparison table, and latency/size improvement metrics. 
```

## When to use this prompt 
Use case 01 
when a trained model must be smaller or faster at inference time 
Use case 02 
when evaluating static or dynamic INT8 quantization in PyTorch or ONNX Runtime 
Use case 03 
when calibration and accuracy validation are required 
Use case 04 
when QAT is a fallback if PTQ reduces accuracy too much 

## What the AI should return 

PTQ implementation, optional QAT setup, and a comparison of accuracy, model size, and inference latency before and after quantization. 

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
