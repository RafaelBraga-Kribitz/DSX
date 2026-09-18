# Structured Pruning *AI Prompt *

This prompt performs structured pruning that removes whole filters, channels, or heads so real hardware speedups are possible. It includes sensitivity analysis, iterative prune-and-fine-tune cycles, and measurement of actual latency and accuracy tradeoffs. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply structured pruning to reduce this model's size and inference cost.

Unstructured pruning (individual weight zeroing) does not improve real-world latency without sparse hardware. Structured pruning removes entire filters, channels, or layers for actual speedup.

1. Sensitivity analysis:
 - For each layer, measure accuracy impact of removing that layer entirely
 - Rank layers from least to most sensitive
 - Layers early in the network and the last classification layer are typically most sensitive

2. Filter/channel pruning (for CNNs):
 - Score filters by L1-norm of weights (smaller norm = less important)
 - Remove the bottom {{prune_ratio}}% of filters in each prunable layer
 - Handle channel dimension changes: update the next layer's input channels accordingly
 - Re-run BN calibration after pruning

3. Attention head pruning (for transformers):
 - Score attention heads by mean attention entropy or gradient-based importance
 - Remove the {{num_heads_to_prune}} least important heads per layer
 - Adjust head projection dimensions accordingly

4. Iterative pruning and fine-tuning:
 - Prune → fine-tune → prune → fine-tune (gradual pruning is better than one-shot)
 - Use a cosine pruning schedule that increases sparsity gradually
 - Target sparsity: {{target_sparsity}}%

5. Results measurement:
 - FLOPs reduction
 - Parameter reduction
 - Inference latency reduction (must measure on real hardware, not estimate)
 - Accuracy change vs unpruned model

Return: sensitivity analysis, pruning implementation, fine-tuning loop, and results table. 
```

## When to use this prompt 
Use case 01 
when model compression should improve real-world inference cost, not just sparsity statistics 
Use case 02 
when pruning CNN filters or transformer attention heads 
Use case 03 
when sensitivity analysis should guide what to prune first 
Use case 04 
when you need measured FLOPs, latency, and accuracy outcomes 

## What the AI should return 

Structured pruning code, sensitivity analysis results, fine-tuning workflow, and a results table comparing size, latency, FLOPs, and accuracy. 

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
