# Structured Output Extraction *AI Prompt *

Design prompts that reliably extract structured data from LLM outputs. Input type: {{input_type}} (free text, documents, conversations, web content) Required output schema: {{sc... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design prompts that reliably extract structured data from LLM outputs.

Input type: {{input_type}} (free text, documents, conversations, web content)
Required output schema: {{schema}}
Model: {{model}}
Failure tolerance: {{failure_tolerance}} (best effort vs guaranteed schema compliance)

1. JSON output prompting:
 Explicit schema specification:
 'Extract the following information from the text and return ONLY a valid JSON object with no additional text, markdown formatting, or code blocks.

 Required fields:
 - name (string): full name of the person
 - date (string, ISO 8601 format YYYY-MM-DD or null if not found)
 - amount (number or null): monetary amount in USD
 - sentiment (string, one of: "positive", "neutral", "negative")

 If a field is not found in the text, return null for that field.
 Do not invent information not present in the text.

 Text to extract from:
 {{text}}'

2. Enforcing schema compliance:

 OpenAI Structured Outputs:
 - Provide a JSON schema in the API request; the model is constrained to produce valid output
 - response_format={"type": "json_schema", "json_schema": {"name": "...", "schema": {...}}}
 - Requires: careful schema design (all required fields specified, correct types)

 Instructor library (Python):
 - Define a Pydantic model as the expected output
 - Instructor wraps the LLM call and retries if the output fails Pydantic validation
 - Handles retries automatically (typically 1-3 retries resolves most failures)

 Outlines / Guidance:
 - Force the model to follow a grammar or regex pattern at the token level
 - Guaranteed valid output; some quality tradeoff for very constrained grammars

3. Extraction failure handling:
 - Parse the output; if parsing fails: retry with additional instructions
 - Retry prompt addition: 'Your previous response could not be parsed as JSON. Please return only valid JSON with no other text.'
 - After 3 retries: log as extraction failure and route for manual review

4. Nested and array schemas:
 - For arrays: 'Return a JSON array of objects, each with fields: ...'
 - For nested objects: define the nested schema explicitly
 - Limit nesting depth to 3 levels for reliable extraction

5. Hallucination prevention for extraction:
 - Always add: 'Only extract information explicitly stated in the text'
 - For optional fields: 'If the field is not clearly mentioned, return null — do not infer or guess'
 - Post-extraction validation: verify extracted values are actually present in the source text

Return: extraction prompt template, schema specification, compliance enforcement approach, retry logic, and hallucination prevention rules. 
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

The AI should return a structured result that covers the main requested outputs, such as JSON output prompting:, name (string): full name of the person, date (string, ISO 8601 format YYYY-MM-DD or null if not found). The final answer should stay clear, actionable, and easy to review inside a prompt engineering workflow for llm engineer work. 

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
