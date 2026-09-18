# Prompt Optimizer *AI Prompt *

Design a meta-prompt that uses an LLM to automatically improve a data extraction or analysis prompt based on observed failures. Manual prompt tuning is iterative and intuition-d... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a meta-prompt that uses an LLM to automatically improve a data extraction or analysis prompt based on observed failures.

Manual prompt tuning is iterative and intuition-driven. Automated prompt optimization uses the model's own reasoning to generate improvements systematically.

1. The optimization loop:

 Step 1 — Failure collection:
 Run the current prompt on the evaluation dataset. Collect all cases where the output failed (wrong extraction, schema violation, incorrect analysis).

 Step 2 — Failure analysis meta-prompt:
 'You are a prompt engineer. Here is a prompt that is failing on certain inputs:

 [CURRENT PROMPT]

 Here are the inputs where it failed and what the correct output should have been:
 [FAILURE CASES WITH EXPECTED OUTPUTS]

 Analyze the failure pattern:
 1. What is the common characteristic of all failing inputs?
 2. What aspect of the prompt is causing these failures? (unclear instruction, missing edge case handling, wrong example, etc.)
 3. Propose a specific, minimal change to the prompt that would fix these failures without breaking passing cases.'

 Step 3 — Candidate prompt generation:
 Generate 3–5 candidate improvements based on the failure analysis.

 Step 4 — Candidate evaluation:
 Run each candidate prompt on the full evaluation dataset. Select the prompt with the highest overall pass rate that does not regress previously passing cases.

 Step 5 — Iterate:
 Repeat steps 1–4 until pass rate plateaus or meets the target.

2. Guardrails for automated optimization:
 - Require human review before deploying any auto-optimized prompt to production
 - Never optimize on the same dataset used for evaluation (overfitting risk)
 - Track prompt version history: keep all previous versions and their eval scores
 - Limit prompt length growth: if the optimized prompt is > 50% longer than the original, require human review

3. What automated optimization cannot do:
 - It cannot fix failures caused by genuinely ambiguous instructions without human clarification
 - It cannot improve performance beyond the model's capability ceiling
 - It is not a substitute for a well-curated evaluation dataset

Return: the failure analysis meta-prompt, optimization loop implementation, candidate evaluation framework, and a worked example showing 3 iterations of improvement on a real extraction prompt. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin meta-prompting work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Meta-Prompting or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The optimization loop:, What is the common characteristic of all failing inputs?, What aspect of the prompt is causing these failures? (unclear instruction, missing edge case handling, wrong example, etc.). The final answer should stay clear, actionable, and easy to review inside a meta-prompting workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Meta-Prompting.
