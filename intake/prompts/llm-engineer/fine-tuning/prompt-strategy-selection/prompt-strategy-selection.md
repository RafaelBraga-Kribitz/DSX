# Fine-tuning Strategy Selection *AI Prompt *

Select and design the appropriate fine-tuning approach for this LLM adaptation task. Base model: {{base_model}} Task: {{task}} Available labeled examples: {{n_examples}} Compute... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Select and design the appropriate fine-tuning approach for this LLM adaptation task.

Base model: {{base_model}}
Task: {{task}}
Available labeled examples: {{n_examples}}
Compute budget: {{compute_budget}}
Goal: {{goal}} (task adaptation, domain adaptation, style / format adaptation, instruction following)

1. Should you fine-tune at all?
 First, try prompt engineering. Fine-tuning is only justified when:
 - The task requires capabilities not achievable via prompting (specialized domain knowledge, consistent format, speed)
 - Latency requirements cannot be met by a large model
 - Cost per query is too high with a large model
 - Privacy: data cannot be sent to external APIs

2. Fine-tuning approaches:

 Full fine-tuning:
 - Update all model weights on the task dataset
 - Requires: large compute (multiple GPUs), large dataset (10K+ examples)
 - Risk: catastrophic forgetting of general capabilities if not carefully regularized
 - Use when: maximum task performance is needed and resources are available

 LoRA (Low-Rank Adaptation):
 - Freeze the pre-trained weights; add small trainable low-rank matrices to attention layers
 - Trainable parameters: only 0.1-1% of full model parameters
 - Memory efficient: can fine-tune 7B model on a single consumer GPU
 - Quality: often matches full fine-tuning on task-specific benchmarks
 - Recommended default for most fine-tuning tasks

 QLoRA:
 - Load the base model in 4-bit quantization, apply LoRA adapters in full precision
 - Memory: fine-tune 65B parameter model on 48GB of GPU memory
 - Slight quality degradation vs LoRA at full precision; acceptable for most tasks

 Prefix tuning / Prompt tuning:
 - Learn soft prompt tokens prepended to the input; base model frozen
 - Very parameter-efficient but less expressive than LoRA
 - Best for: many tasks from the same base model (swap only the prompt tokens)

3. Dataset requirements:
 - Minimum effective: 500-1000 high-quality examples
 - Optimal: 3,000-10,000 examples for most tasks
 - Quality > quantity: 500 excellent examples outperform 5,000 mediocre ones
 - Format: instruction-input-output triplets (Alpaca format) or conversation format (ChatML)

4. Training configuration for LoRA:
 - r (rank): 8-64 (higher rank = more expressiveness, more compute)
 - alpha: typically 2x rank
 - Target modules: all attention projections (q_proj, k_proj, v_proj, o_proj)
 - Learning rate: 2e-4 with cosine schedule, lower than standard fine-tuning
 - Epochs: 3-5 (more epochs on small datasets risks overfitting)

Return: fine-tuning vs prompting recommendation, approach selection (LoRA/QLoRA/full), dataset requirements, and training configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin fine-tuning work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Fine-tuning or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Should you fine-tune at all?, The task requires capabilities not achievable via prompting (specialized domain knowledge, consistent format, speed), Latency requirements cannot be met by a large model. The final answer should stay clear, actionable, and easy to review inside a fine-tuning workflow for llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in Fine-tuning.
