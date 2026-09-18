# Memory Optimization *AI Prompt *

This prompt applies practical GPU memory optimization techniques in escalating order of complexity, from AMP and optimizer choices to checkpointing and parameter-efficient fine-tuning. It is intended to help models fit on constrained hardware with minimal guesswork. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize GPU memory usage for this model to fit a larger batch size or a bigger model on available hardware.

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

Return: memory optimization implementation ordered by complexity, expected savings per technique, and memory profiling code. 
```

## When to use this prompt 
Use case 01 
when a model or batch size does not fit into available VRAM 
Use case 02 
when you need a prioritized list of memory-saving techniques 
Use case 03 
when memory profiling should guide what to optimize next 
Use case 04 
when gradient accumulation or checkpointing may unlock larger workloads 

## What the AI should return 

An ordered memory optimization plan with implementation guidance, expected savings per technique, and profiling code to measure impact. 

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
