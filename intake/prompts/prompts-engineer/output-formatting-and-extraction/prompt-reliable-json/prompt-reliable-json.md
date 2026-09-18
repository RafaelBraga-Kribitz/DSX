# Reliable JSON Output Prompt *AI Prompt *

Design prompts and parsing strategies to get reliable, parseable JSON from LLMs every time. Unreliable JSON is one of the most common LLM integration failure modes — the model a... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design prompts and parsing strategies to get reliable, parseable JSON from LLMs every time.

Unreliable JSON is one of the most common LLM integration failure modes — the model adds markdown fences, explanatory text, trailing commas, or truncates the output mid-JSON.

1. Prompt instructions for reliable JSON:

 Instruction 1 — Format command:
 'Return ONLY a JSON object. Do not include any explanation, markdown formatting, or code blocks.'

 Instruction 2 — Schema specification:
 'The JSON must match this exact schema: {{json_schema}}'
 Include a JSON Schema definition or a clear field-by-field description with types.

 Instruction 3 — Null handling:
 'If a field cannot be determined from the input, set it to null. Do not omit fields.'

 Instruction 4 — No truncation:
 'Return the complete JSON object. Never truncate. If the output would be very long, summarize field values rather than cutting off.'

 Instruction 5 — Validation example:
 Append a valid example at the end of the prompt: 'Your output should look like this: {{example_json}}'

2. Engineering safeguards (client-side):

 Safeguard 1 — JSON extraction from messy output:
 Even with good prompts, models sometimes add preamble. Use regex to extract JSON:
 ```python
 import re, json
 def extract_json(text):
 match = re.search(r'\{[\s\S]*\}', text)
 if match:
 return json.loads(match.group())
 raise ValueError('No JSON found in output')
 ```

 Safeguard 2 — Schema validation:
 After extraction, validate against the expected schema using jsonschema or Pydantic.

 Safeguard 3 — Retry with correction:
 If JSON parsing fails: re-call the model with: 'Your previous response was not valid JSON. The error was: {{error}}. Return only the corrected JSON object.'

 Safeguard 4 — Structured output APIs:
 Use model APIs that enforce JSON output natively (OpenAI response_format, Anthropic tool use, Instructor library).

3. Model-specific tips:
 - Add 'Your response:' followed by '{' at the end of the prompt to prime the model to start with JSON
 - For long JSON objects: request the model output one section at a time and merge

Return: the reliable JSON prompt template, extraction code, schema validation code, retry logic, and a test harness that measures JSON parse success rate across 100 calls. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin output formatting and extraction work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Output Formatting and Extraction or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Prompt instructions for reliable JSON:, Engineering safeguards (client-side):, Model-specific tips:. The final answer should stay clear, actionable, and easy to review inside a output formatting and extraction workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Output Formatting and Extraction.
