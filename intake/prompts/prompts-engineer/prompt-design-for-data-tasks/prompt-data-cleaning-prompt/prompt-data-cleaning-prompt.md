# Data Cleaning Instruction Prompt *AI Prompt *

Design a prompt that instructs an LLM to clean and standardize a specific type of messy data field. Field type: {{field_type}} (e.g. company names, phone numbers, addresses, pro... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt that instructs an LLM to clean and standardize a specific type of messy data field.

Field type: {{field_type}} (e.g. company names, phone numbers, addresses, product descriptions, job titles)
Source data sample: {{data_sample}}

1. The challenge with LLM data cleaning:
 - LLMs are inconsistent without explicit rules — the same model may normalize 'IBM Corp.' differently on two calls
 - The prompt must eliminate ambiguity by providing exhaustive rules and examples

2. Prompt structure for data cleaning:

 a. Task definition (1 sentence): 'Normalize the following {{field_type}} to a standard format.'

 b. Normalization rules (numbered list, in order of priority):
 - Rule 1: [most important normalization, e.g. 'Convert to Title Case']
 - Rule 2: [second rule, e.g. 'Remove legal suffixes: LLC, Inc., Corp., Ltd.']
 - Rule 3: [third rule, e.g. 'Expand common abbreviations: St. → Street, Ave. → Avenue']
 - Continue until all cases are covered

 c. Conflict resolution: 'If two rules conflict, apply the earlier rule.'

 d. Uncertainty handling: 'If you are not confident in the correct normalization, return the input unchanged and append a [?] flag.'

 e. Output format: 'Return ONLY the normalized value. No explanation.'

3. Few-shot examples (critical for consistency):
 - Include 6–10 input → output pairs covering the most common messy patterns
 - Include at least 2 edge cases (very short, very long, non-standard characters)
 - Include 1 example where the model should return the value unchanged with [?]

4. Batch processing version:
 - Extend the prompt to clean a list of 20 values in one call
 - Output as a JSON array preserving input order
 - Include an index field so outputs can be joined back to inputs

Return: single-record cleaning prompt, batch cleaning prompt, test set of 20 messy values, and expected normalized outputs. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt design for data tasks work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Design for Data Tasks or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The challenge with LLM data cleaning:, LLMs are inconsistent without explicit rules — the same model may normalize 'IBM Corp.' differently on two calls, The prompt must eliminate ambiguity by providing exhaustive rules and examples. The final answer should stay clear, actionable, and easy to review inside a prompt design for data tasks workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Design for Data Tasks.
