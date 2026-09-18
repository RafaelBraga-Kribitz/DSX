# Structured Data Extraction Prompt *AI Prompt *

Write a prompt that reliably extracts structured data from unstructured text. Source text type: {{text_type}} (e.g. customer support tickets, invoice PDFs, clinical notes, news... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a prompt that reliably extracts structured data from unstructured text.

Source text type: {{text_type}} (e.g. customer support tickets, invoice PDFs, clinical notes, news articles)
Target schema: {{target_schema}} (the fields you want to extract)

Apply these prompt engineering principles for data extraction:

1. Schema-first instruction:
 - Define the output schema explicitly before showing any examples
 - Name every field, its type, and what to do when it is missing (null vs omit vs default value)
 - Example: 'Extract the following fields. If a field is not present in the text, return null for that field.'

2. Constraint specification:
 - State the output format unambiguously: 'Return ONLY a JSON object. No explanation, no markdown, no preamble.'
 - Specify value formats: 'Dates must be in ISO 8601 format (YYYY-MM-DD)', 'Monetary values as numbers without currency symbols'
 - Specify enumeration constraints: 'status must be one of: [open, closed, pending]'

3. Ambiguity resolution rules:
 - What should the model do when a field is ambiguous? Provide explicit tie-breaking rules.
 - Example: 'If multiple dates appear, extract the most recent one as order_date'
 - Example: 'If the customer name appears in multiple formats, use the version that includes both first and last name'

4. Negative examples:
 - Show what NOT to include: 'Do not extract dates from headers or footers'
 - Show what NOT to infer: 'Do not infer fields that are not explicitly stated in the text'

5. Robustness to messy input:
 - Instruct the model to handle OCR errors, typos, and inconsistent formatting gracefully
 - 'If a field contains obvious OCR artifacts (e.g. 0 vs O), normalize to the most likely intended value'

Return: the complete extraction prompt, a test with 3 sample inputs (clean, messy, and edge case), and expected outputs for each. 
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

The AI should return a structured result that covers the main requested outputs, such as Schema-first instruction:, Define the output schema explicitly before showing any examples, Name every field, its type, and what to do when it is missing (null vs omit vs default value). The final answer should stay clear, actionable, and easy to review inside a prompt design for data tasks workflow for prompts engineer work. 

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
