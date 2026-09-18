# Flash Attention Integration *AI Prompt *

This prompt integrates Flash Attention into a transformer model, including compatibility checks, drop-in replacements, variable-length support, and fallback behavior. It is useful for reducing memory use and speeding up attention-heavy workloads on supported GPUs. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Integrate Flash Attention into this transformer model to reduce memory and improve speed.

1. Installation and compatibility check:
 - Install flash-attn: pip install flash-attn --no-build-isolation
 - Verify: requires GPU with compute capability ≥ 8.0 (A100, H100, 3090, 4090)
 - Check PyTorch version compatibility

2. Drop-in replacement:
 - Replace standard scaled dot-product attention with flash_attn_func or flash_attn_varlen_func
 - For HuggingFace models: set attn_implementation='flash_attention_2' in from_pretrained

3. Expected improvements:
 - Memory: O(N) instead of O(N²) in sequence length — enables much longer sequences
 - Speed: 2–4× faster than standard attention on A100
 - No approximation: exact same output as standard attention (not approximate)

4. Sequence length scaling:
 - Benchmark max sequence length with standard attention vs Flash Attention on the same GPU memory budget
 - Demonstrate quadratic vs linear memory scaling

5. Causal vs bidirectional:
 - For decoder models: set causal=True in flash_attn_func
 - For encoder models: causal=False

6. Variable-length sequences:
 - Use flash_attn_varlen_func with cu_seqlens to handle variable-length batches without padding waste
 - Compute cumulative sequence lengths from attention masks

7. Fallback:
 - Check if Flash Attention is available at runtime; fall back to scaled_dot_product_attention if not

Return: Flash Attention integration code, before/after memory and speed benchmark, and fallback implementation. 
```

## When to use this prompt 
Use case 01 
when transformer attention is the main memory or speed bottleneck 
Use case 02 
when running on GPUs that support Flash Attention 
Use case 03 
when long-sequence training or inference must fit within memory limits 
Use case 04 
when you need before-and-after benchmarks and a safe fallback path 

## What the AI should return 

Flash Attention integration code, runtime compatibility checks, fallback logic, and benchmark comparisons for memory and speed. 

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
