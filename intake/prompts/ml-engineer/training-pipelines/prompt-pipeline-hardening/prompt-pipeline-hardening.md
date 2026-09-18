# Training Pipeline Hardening Chain *AI Prompt *

This chain hardens a training pipeline end to end by auditing reproducibility, profiling the data pipeline, checking numerical stability, validating checkpoint resume behavior, monitoring gradients, and finishing with a smoke test. It is designed for teams preparing training code for repeated reliable use. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Reproducibility audit — verify all random seeds are set (Python, NumPy, PyTorch, CUDA). Run training twice with identical config and confirm loss curves are bit-for-bit identical.
Step 2: Data pipeline profiling — profile the DataLoader to identify if training is GPU-bound or I/O-bound. Optimize num_workers, prefetch_factor, and caching strategy based on findings.
Step 3: Numerical stability check — enable torch.autograd.detect_anomaly() for one epoch to catch NaN/Inf in forward/backward passes. Fix any instabilities found.
Step 4: Memory optimization — run with torch.cuda.memory_summary() after each epoch. Identify memory leaks (steadily increasing memory usage). Ensure .detach() is called on all logged tensors.
Step 5: Checkpoint validation — verify that loading a checkpoint and resuming training produces identical results to uninterrupted training for the next 10 steps.
Step 6: Gradient health check — log gradient norms for each layer group per epoch. Flag layers with vanishing (<1e-7) or exploding (>100) gradients. Adjust initialization or add gradient clipping.
Step 7: End-to-end smoke test — write a test that runs 2 epochs on a tiny dataset (32 samples) and asserts: loss decreases, metrics are computed, checkpoint saved, no CUDA errors, no memory leaks. 
```

## When to use this prompt 
Use case 01 
when a training pipeline must be hardened before wider team use or production 
Use case 02 
when intermittent bugs, NaNs, or resume inconsistencies need systematic diagnosis 
Use case 03 
when you want a structured sequence of validation and stability checks 
Use case 04 
when you need a final smoke test covering metrics, checkpoints, and memory behavior 

## What the AI should return 

A hardening checklist and implementation plan covering reproducibility, profiling, anomaly detection, memory health, checkpoint validation, gradient diagnostics, and smoke testing. 

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

Once you have the first result, continue deeper with related prompts in Training Pipelines.
