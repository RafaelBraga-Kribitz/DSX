# Weight Sharing and Low-Rank Decomposition *AI Prompt *

This prompt compresses large weight matrices using low-rank decomposition or LoRA-style adaptations, with rank sweeps and mixed-rank strategies guided by sensitivity. It is useful when large linear layers dominate parameter count and compute cost. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply low-rank matrix decomposition to compress the large weight matrices in this model.

1. Identify compression targets:
 - Profile all weight matrices by parameter count and FLOPs contribution
 - Focus on large linear layers (embedding, feed-forward, projection layers)
 - Attention QKV matrices and output projections in transformers are primary targets

2. SVD-based decomposition:
 - For weight matrix W (m × n), compute SVD: W = U × S × Vt
 - Keep only top-k singular values: W ≈ U_k × S_k × Vt_k
 - Rank k selection: sweep k values and measure accuracy vs compression tradeoff
 - Replace original layer with two consecutive smaller layers: Linear(in, k) + Linear(k, out)
 - Break-even rank: k < (m × n) / (m + n) reduces parameter count

3. LoRA (Low-Rank Adaptation) for fine-tuning:
 - Freeze base model weights
 - Add trainable low-rank matrices A (d × r) and B (r × k) in parallel with frozen weights
 - Output = Wx + BAx × (alpha/r)
 - Typical ranks: r=4, r=8, r=16, r=64
 - Merge LoRA weights back into base model for inference: W_new = W + B × A

4. Accuracy evaluation:
 - Measure accuracy at compression ratios: 25%, 50%, 75% parameter reduction
 - Plot accuracy vs compression ratio curve
 - Find the Pareto-optimal point

5. Mixed-rank strategy:
 - Apply higher compression to less sensitive layers, lower compression to sensitive ones
 - Use gradient-based layer sensitivity to guide rank assignment

Return: SVD decomposition code, LoRA implementation, compression curve, and mixed-rank strategy. 
```

## When to use this prompt 
Use case 01 
when large dense matrices are the main source of model size or FLOPs 
Use case 02 
when exploring SVD compression or LoRA-based fine-tuning 
Use case 03 
when you need accuracy-versus-compression tradeoff curves 
Use case 04 
when different layers should use different target ranks 

## What the AI should return 

SVD decomposition code, LoRA implementation, compression analysis, and recommendations for rank choices or mixed-rank strategies. 

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
