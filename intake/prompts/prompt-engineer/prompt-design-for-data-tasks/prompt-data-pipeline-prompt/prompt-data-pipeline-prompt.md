# Multi-Step Data Pipeline Prompt *AI Prompt *

Design a prompt chain that guides an LLM through a multi-step data transformation task — equivalent to a mini ETL pipeline. Transformation task: {{transformation_task}} (e.g. 'n... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt chain that guides an LLM through a multi-step data transformation task — equivalent to a mini ETL pipeline.

Transformation task: {{transformation_task}} (e.g. 'normalize and deduplicate a customer list from 3 different source formats')

1. Why a single prompt fails for complex transformations:
 - Complex transformations require multiple dependent reasoning steps
 - A single prompt producing the final result skips intermediate validation steps
 - Errors in early steps propagate invisibly to the output
 - A prompt chain surfaces intermediate results for inspection and debugging

2. Pipeline prompt design pattern:

 Step 1 prompt — Schema analysis:
 - Input: raw data
 - Task: 'Analyze the structure of this data. For each column, identify: name, inferred type, example values, and potential quality issues.'
 - Output: structured schema analysis (JSON)

 Step 2 prompt — Transformation plan:
 - Input: schema analysis from Step 1 + transformation goal
 - Task: 'Based on this schema analysis, write a step-by-step transformation plan. Each step should specify: what to transform, how, and why.'
 - Output: numbered transformation plan

 Step 3 prompt — Transformation execution:
 - Input: raw data + transformation plan from Step 2
 - Task: 'Execute the transformation plan exactly as specified. Apply each step in order. For each step, show the result.'
 - Output: transformed data

 Step 4 prompt — Quality validation:
 - Input: original data + transformed data
 - Task: 'Compare the original and transformed data. Check: (1) row count preserved or changes explained, (2) no data was lost unintentionally, (3) transformations were applied correctly. Flag any issues.'
 - Output: validation report

3. Error recovery design:
 - Each step prompt should include: 'If you encounter an error or ambiguity, stop and output: ERROR: [description] rather than proceeding with an assumption.'
 - This surfaces problems early rather than propagating bad data through the chain

4. Prompt chain orchestration:
 - Show how to chain these prompts programmatically: feed output of step N as input to step N+1
 - Include JSON schema validation between steps to catch format errors before they propagate

Return: all 4 step prompts, a Python orchestration script, and a test case with expected intermediate outputs. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt design for data tasks work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Design for Data Tasks or the wider Prompt Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why a single prompt fails for complex transformations:, Complex transformations require multiple dependent reasoning steps, A single prompt producing the final result skips intermediate validation steps. The final answer should stay clear, actionable, and easy to review inside a prompt design for data tasks workflow for prompt engineer work. 

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
