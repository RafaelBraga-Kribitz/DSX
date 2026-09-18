# Fine-tuning Evaluation *AI Prompt *

Evaluate a fine-tuned LLM model against the base model and identify regression risks. Fine-tuned model: {{fine_tuned_model}} Base model: {{base_model}} Fine-tuning task: {{task}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Evaluate a fine-tuned LLM model against the base model and identify regression risks.

Fine-tuned model: {{fine_tuned_model}}
Base model: {{base_model}}
Fine-tuning task: {{task}}
Evaluation dataset: {{eval_dataset}}

1. Task-specific performance:
 - Compute the primary metric on the held-out test set: accuracy, F1, ROUGE, BLEU, or custom metric
 - Compare fine-tuned vs base model vs SFT baseline (if exists)
 - Minimum success threshold: fine-tuned model must beat the base model by > 10% on the primary metric

2. Catastrophic forgetting assessment:
 Fine-tuning on a specific task can degrade general capabilities.
 Check these general capability benchmarks:
 - MMLU (general knowledge): did score drop > 5%?
 - HellaSwag (common sense): did score drop > 5%?
 - HumanEval (coding): did score drop > 5% if coding was not part of fine-tuning?
 If any drop > 10%: the fine-tuning process is too aggressive — reduce epochs, add general data, or use LoRA with lower rank

3. Instruction following:
 - Test: does the fine-tuned model still follow system prompt instructions correctly?
 - Test: does it respect output format requirements?
 - Test: does it appropriately decline harmful requests?
 - If any of these regress: the alignment of the base model has been partially eroded

4. Safety regression:
 - Run the fine-tuned model against the safety test set used for the base model
 - Harmful content rate must not increase vs the base model
 - Over-refusal rate: does the fine-tuned model refuse more legitimate requests? (Fine-tuning can sometimes increase refusals on benign inputs)

5. Output quality assessment:
 - Human evaluation: 100 paired comparisons (base vs fine-tuned) rated by annotators
 - LLM judge: use GPT-4 to compare pairs; report win/tie/loss rates

6. Decision criteria:
 - Deploy if: task metric > threshold AND no general capability drop > 10% AND safety metrics maintained
 - Revise if: task metric is good but capability regression detected → reduce fine-tuning intensity
 - Reject if: safety regression detected — do not deploy, investigate fine-tuning data

Return: evaluation protocol, catastrophic forgetting checks, safety regression tests, human evaluation plan, and deployment decision criteria. 
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

The AI should return a structured result that covers the main requested outputs, such as Task-specific performance:, Compute the primary metric on the held-out test set: accuracy, F1, ROUGE, BLEU, or custom metric, Compare fine-tuned vs base model vs SFT baseline (if exists). The final answer should stay clear, actionable, and easy to review inside a fine-tuning workflow for llm engineer work. 

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
