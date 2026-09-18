# Fine-tuning *AI Prompts *

4 LLM Engineer prompts in Fine-tuning. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in Fine-tuning 
4 prompts Advanced Single prompt 01 
### Fine-tuning Data Preparation 

Prepare and quality-check a fine-tuning dataset for this LLM task. Task: {{task}} Data sources: {{data_sources}} Base model format: {{format}} (Alpaca, ChatML, ShareGPT, custom)... 
Prompt text Prepare and quality-check a fine-tuning dataset for this LLM task.

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

Return: data collection plan, format specification, quality filtering pipeline, distribution analysis, and train/val/test split strategy. Copy prompt Open prompt details Intermediate Single prompt 02 
### Fine-tuning Evaluation 

Evaluate a fine-tuned LLM model against the base model and identify regression risks. Fine-tuned model: {{fine_tuned_model}} Base model: {{base_model}} Fine-tuning task: {{task}... 
Prompt text Evaluate a fine-tuned LLM model against the base model and identify regression risks.

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

Return: evaluation protocol, catastrophic forgetting checks, safety regression tests, human evaluation plan, and deployment decision criteria. Copy prompt Open prompt details Intermediate Single prompt 03 
### Fine-tuning Strategy Selection 

Select and design the appropriate fine-tuning approach for this LLM adaptation task. Base model: {{base_model}} Task: {{task}} Available labeled examples: {{n_examples}} Compute... 
Prompt text Select and design the appropriate fine-tuning approach for this LLM adaptation task.

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

Return: fine-tuning vs prompting recommendation, approach selection (LoRA/QLoRA/full), dataset requirements, and training configuration. Copy prompt Open prompt details Advanced Single prompt 04 
### RLHF and Alignment Techniques 

Design an alignment fine-tuning pipeline to improve helpfulness, harmlessness, and honesty. Base model: {{base_model}} (already instruction-tuned or raw) Alignment goal: {{goal}... 
Prompt text Design an alignment fine-tuning pipeline to improve helpfulness, harmlessness, and honesty.

Base model: {{base_model}} (already instruction-tuned or raw)
Alignment goal: {{goal}} (reduce refusals, improve helpfulness, enforce tone, reduce hallucination)
Resources: {{resources}} (GPU count, annotation budget)

1. The alignment pipeline overview:

 Stage 1 — Supervised Fine-Tuning (SFT):
 - Fine-tune on high-quality human demonstrations of the desired behavior
 - Creates the 'SFT model' — a good baseline for the target behavior

 Stage 2 — Reward Model Training:
 - Collect human preference data: show pairs of responses to the same prompt, ask which is better
 - Train a reward model to predict human preferences
 - The RM maps (prompt, response) → a scalar reward score

 Stage 3 — RLHF (PPO or similar):
 - Use the reward model to optimize the SFT model via reinforcement learning
 - PPO (Proximal Policy Optimization): standard RL algorithm for LLM fine-tuning
 - KL penalty: prevent the model from deviating too far from the SFT model (avoids reward hacking)

2. DPO (Direct Preference Optimization) — simplified alternative to RLHF:
 - Requires: preference dataset of (prompt, chosen_response, rejected_response) pairs
 - Directly optimizes the policy using a classification-style loss — no separate reward model needed
 - Much simpler to implement than PPO-based RLHF
 - Quality: competitive with PPO for most alignment tasks
 - Loss: L_DPO = -log sigmoid(beta * (log π(chosen|x) / π_ref(chosen|x) - log π(rejected|x) / π_ref(rejected|x)))
 - beta: temperature controlling strength of preference learning (default 0.1-0.5)

3. Preference data collection:
 - Red teaming prompts: adversarial inputs designed to elicit unwanted behavior
 - Helpful task prompts: standard task inputs where response quality varies
 - For each prompt: collect 2-4 model responses, have annotators rank or choose the best
 - Annotator guidelines: define precisely what 'better' means (more helpful? less harmful? more accurate?)

4. ORPO (Odds Ratio Preference Optimization):
 - Combines SFT and preference optimization in a single training stage
 - Simpler than the SFT → DPO two-stage pipeline
 - Good default for limited compute budgets

5. Constitutional AI (CAI) approach:
 - Specify a set of principles ('constitution') that the model should follow
 - Use the model itself to critique and revise its own responses against the constitution
 - Reduces dependence on human preference annotation

Return: alignment pipeline selection (full RLHF vs DPO vs ORPO), preference data collection plan, training configuration, and evaluation approach. Copy prompt Open prompt details 
## Recommended Fine-tuning workflow 
1 
### Fine-tuning Data Preparation 

Start with a focused prompt in Fine-tuning so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Fine-tuning Evaluation 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Fine-tuning Strategy Selection 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### RLHF and Alignment Techniques 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
