# Mixed Precision Training *AI Prompt *

This prompt adds mixed precision training to a PyTorch workflow using AMP, including bf16 or fp16 selection, GradScaler usage, and simple benchmark comparisons. It focuses on achieving speed and memory gains without destabilizing training. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: complete AMP training loop with GradScaler, bf16/fp16 selection logic, and before/after benchmark code. 
```

## When to use this prompt 
Use case 01 
when training must fit in less GPU memory or run faster 
Use case 02 
when you want a correct AMP implementation with bf16 or fp16 logic 
Use case 03 
when GradScaler behavior and safe fp32 exceptions matter 
Use case 04 
when you need before-and-after speed and memory comparisons 

## What the AI should return 

A complete AMP-enabled training loop with precision selection logic, GradScaler integration, and benchmark code comparing AMP against full precision. 

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
