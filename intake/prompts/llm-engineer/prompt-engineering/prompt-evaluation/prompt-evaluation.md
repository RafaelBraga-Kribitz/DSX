# Prompt Evaluation and Testing *AI Prompt *

Build a systematic evaluation framework for testing and improving LLM prompts. Task: {{task}} Prompt: {{prompt}} Success criteria: {{success_criteria}} Evaluation budget: {{budg... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a systematic evaluation framework for testing and improving LLM prompts.

Task: {{task}}
Prompt: {{prompt}}
Success criteria: {{success_criteria}}
Evaluation budget: {{budget}} (number of examples, cost)

1. Evaluation dataset construction:
 - Minimum viable eval set: 50-100 examples
 - Include: easy examples (should always pass), hard examples (edge cases), adversarial examples (designed to expose failures)
 - Distribution: cover the real distribution of inputs the prompt will face in production
 - Label examples with ground truth outputs (or expected output characteristics)

2. Metrics by task type:

 Exact match tasks (classification, extraction):
 - Accuracy: fraction of outputs exactly matching the expected output
 - F1 per class for multi-class problems
 - Confusion matrix: where are the systematic failures?

 Open-ended generation tasks:
 - ROUGE-1/2/L: n-gram overlap with reference outputs (weak proxy for quality)
 - BERTScore: semantic similarity using contextual embeddings (stronger than ROUGE)
 - LLM-as-judge: use a separate LLM (GPT-4) to rate quality on a 1-5 scale per criterion
 - Win rate: compare two prompt versions side-by-side using LLM judge

 JSON extraction tasks:
 - Field-level accuracy: precision and recall per extracted field
 - Schema compliance rate: % of outputs that are valid JSON with correct schema
 - Hallucination rate: % of extracted values not present in the source

3. LLM-as-judge setup:
 'You are evaluating the quality of an AI assistant's response. Rate the response on a scale of 1-5 for each criterion:
 - Accuracy (1-5): does the response correctly answer the question?
 - Completeness (1-5): are all required elements present?
 - Format compliance (1-5): does the response match the required format?
 Return only a JSON object: {"accuracy": N, "completeness": N, "format_compliance": N, "explanation": "..."}'

4. Regression testing:
 - Before deploying any prompt change: run the full eval set
 - Accept change only if: primary metric improves AND no secondary metric degrades by > 5%
 - Version all prompts in version control; link each version to its eval results

5. Failure analysis:
 - Cluster failures by type: wrong format, wrong answer, hallucination, refusal
 - For each failure cluster: add a clarifying instruction to the system prompt
 - Re-run eval after each fix to confirm improvement and check for regressions

Return: eval dataset construction plan, metric selection, LLM-judge prompt, regression test protocol, and failure analysis procedure. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt engineering work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Engineering or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Evaluation dataset construction:, Minimum viable eval set: 50-100 examples, Include: easy examples (should always pass), hard examples (edge cases), adversarial examples (designed to expose failures). The final answer should stay clear, actionable, and easy to review inside a prompt engineering workflow for llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Engineering.
