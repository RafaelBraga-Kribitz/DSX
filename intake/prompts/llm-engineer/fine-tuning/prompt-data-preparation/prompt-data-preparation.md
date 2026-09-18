# Fine-tuning Data Preparation *AI Prompt *

Prepare and quality-check a fine-tuning dataset for this LLM task. Task: {{task}} Data sources: {{data_sources}} Base model format: {{format}} (Alpaca, ChatML, ShareGPT, custom)... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Prepare and quality-check a fine-tuning dataset for this LLM task.

Task: {{task}}
Data sources: {{data_sources}}
Base model format: {{format}} (Alpaca, ChatML, ShareGPT, custom)
Target examples: {{n_target}}

1. Data collection strategies:

 From existing outputs:
 - Collect successful model outputs (from prompt engineering or user logs)
 - Clean and filter: remove low-quality, harmful, or off-topic examples

 Human labeling:
 - Write instructions + create input → have labelers produce ideal outputs
 - Gold standard: 100-500 high-quality expert examples

 LLM-assisted generation (distillation):
 - Use GPT-4 / Claude to generate instruction-response pairs on topic
 - Verify quality: run LLM judge on generated examples before including
 - Risk: if the student model trains on teacher outputs, it is bounded by the teacher's quality

2. Data format:

 Alpaca format:
 {"instruction": "...", "input": "...", "output": "..."}
 - Instruction: what should the model do?
 - Input: the specific content to process (can be empty)
 - Output: the ideal response

 ChatML format (for chat models):
 {"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}

 Multi-turn conversation: include the full conversation history leading to each ideal response

3. Quality filtering:
 - Length filter: remove outputs < 10 tokens (too short) or > 2000 tokens (may dilute training)
 - Deduplication: remove near-duplicate examples (hash or embedding similarity)
 - Consistency filter: flag examples where similar inputs lead to very different outputs
 - Toxicity / safety filter: remove harmful or inappropriate content
 - LLM quality judge: score each example for: instruction clarity, response quality, factual accuracy
 Keep only examples scoring >= 4/5

4. Distribution analysis:
 - Topic coverage: are all task-relevant topics represented in the dataset?
 - Length distribution: ensure a mix of short and long responses
 - Instruction diversity: use embedding clustering to ensure diverse instructions (avoid repetitive examples)
 - Negative examples: do NOT include examples of undesired behavior (the model will learn to produce them)

5. Train / validation split:
 - Hold out 10% as a validation set for loss monitoring during training
 - Ensure validation set is drawn from the same distribution as training data
 - Create a separate, held-out test set (not used during training) for final evaluation

Return: data collection plan, format specification, quality filtering pipeline, distribution analysis, and train/val/test split strategy. 
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

The AI should return a structured result that covers the main requested outputs, such as Data collection strategies:, Collect successful model outputs (from prompt engineering or user logs), Clean and filter: remove low-quality, harmful, or off-topic examples. The final answer should stay clear, actionable, and easy to review inside a fine-tuning workflow for llm engineer work. 

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
