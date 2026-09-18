# Compression Pipeline Chain *AI Prompt *

This chain walks through a full compression pipeline: baseline measurement, structured pruning, quantization, optional distillation recovery, deployment export, and Pareto analysis. It is meant for selecting a production-ready compressed model based on measured tradeoffs rather than guesswork. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Establish the baseline — measure the uncompressed model: size (MB), FLOPs, p50/p95/p99 inference latency at batch_size=1 and batch_size=32, and accuracy on the full validation set.
Step 2: Pruning — apply structured pruning at 30%, 50%, and 70% sparsity. Fine-tune after each level. Record accuracy, size, and latency at each sparsity level.
Step 3: Quantization — apply INT8 post-training quantization to the pruned model. If accuracy drops > 1%, apply QAT. Record accuracy, size, and latency.
Step 4: Distillation (optional) — if the compressed model still underperforms targets, use the original uncompressed model as a teacher to recover accuracy via knowledge distillation.
Step 5: ONNX export and TensorRT optimization — export the compressed model to TensorRT FP16. Verify numerical correctness. Record final latency and throughput.
Step 6: Accuracy vs efficiency Pareto analysis — plot all tested configurations on an accuracy vs latency scatter plot. Identify the Pareto-optimal point that meets the deployment requirements.
Step 7: Write a compression report: original vs final model comparison (size, latency, FLOPs, accuracy), techniques applied, any accuracy recovery steps taken, and recommendation for production deployment. 
```

## When to use this prompt 
Use case 01 
when compressing a model with multiple techniques in sequence 
Use case 02 
when you need to compare candidate compressed variants systematically 
Use case 03 
when deployment constraints require a balance of latency, size, and accuracy 
Use case 04 
when the final recommendation should be backed by a Pareto analysis 

## What the AI should return 

A compression workflow summary with metrics for each tested configuration, Pareto tradeoff analysis, and a final production recommendation. 

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
