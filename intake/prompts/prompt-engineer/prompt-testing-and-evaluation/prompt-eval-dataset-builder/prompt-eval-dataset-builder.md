# Prompt Evaluation Dataset Builder *AI Prompt *

Build a systematic evaluation dataset for measuring the quality of a data-focused LLM prompt. A good eval dataset is the foundation of prompt engineering — without it, you are g... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a systematic evaluation dataset for measuring the quality of a data-focused LLM prompt.

A good eval dataset is the foundation of prompt engineering — without it, you are guessing whether your prompt improvements are real.

1. Evaluation dataset requirements:
 - Minimum size: 50–200 examples (fewer → high variance in measurements, more → diminishing returns)
 - Distribution: representative of real production inputs, not just easy cases
 - Coverage: includes rare but important edge cases
 - Ground truth: each example has a verified correct output (human-labeled or programmatically verifiable)

2. Dataset construction methods:

 a. Sample from production (best for real-world relevance):
 - Sample 200 recent production inputs randomly
 - Stratify by input complexity: simple / medium / complex
 - Have domain experts label the expected output for each

 b. Programmatic generation (best for edge cases):
 - Generate inputs algorithmically to cover specific scenarios
 - Example for an extraction prompt: generate documents with 0 fields, 1 field, all fields, conflicting fields, malformed values
 - Use a template + parameter grid to generate all combinations

 c. Adversarial examples (best for robustness):
 - Inputs designed to trigger failure modes: very long text, unusual formatting, ambiguous cases
 - Include examples where the correct output is 'no information found' rather than a value

3. Ground truth creation:
 - For extraction tasks: human annotators label expected fields and values
 - Inter-annotator agreement: have 2 annotators label the same 20% of examples; measure agreement; resolve disagreements
 - For SQL generation: execute the SQL and compare results to expected results
 - For analysis tasks: define a rubric and have domain experts score outputs 1–5

4. Eval metrics per task type:
 - Extraction: field-level precision and recall
 - Classification: accuracy, F1 per class
 - SQL generation: execution accuracy (does the SQL run and return correct results?)
 - Analysis: rubric score (factual accuracy, clarity, completeness)

5. Dataset maintenance:
 - Add 5 new examples per month from production failures
 - Re-label examples when the ground truth definition changes
 - Track dataset version alongside prompt version

Return: dataset construction procedure, annotation guide, inter-annotator agreement calculation, metric implementations per task type, and dataset versioning schema. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt testing and evaluation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Testing and Evaluation or the wider Prompt Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Evaluation dataset requirements:, Minimum size: 50–200 examples (fewer → high variance in measurements, more → diminishing returns), Distribution: representative of real production inputs, not just easy cases. The final answer should stay clear, actionable, and easy to review inside a prompt testing and evaluation workflow for prompt engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Testing and Evaluation.
