# Schema Enforcement Prompt *AI Prompt *

Design a prompt pattern that enforces strict output schema adherence even when the input data is ambiguous or incomplete. The challenge: when input data is messy, LLMs tend to i... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt pattern that enforces strict output schema adherence even when the input data is ambiguous or incomplete.

The challenge: when input data is messy, LLMs tend to improvise — inventing field names, changing types, or nesting structures differently than specified. Schema enforcement prevents this.

1. Hard schema specification:
 - Include the schema as a JSON Schema definition, not just a description
 - Specify for each field: type, required/optional, allowed values, format constraints
 - Example:
 ```json
 {
 "type": "object",
 "required": ["entity_id", "entity_type", "confidence"],
 "properties": {
 "entity_id": {"type": "string"},
 "entity_type": {"type": "string", "enum": ["person", "organization", "location"]},
 "confidence": {"type": "number", "minimum": 0, "maximum": 1}
 },
 "additionalProperties": false
 }
 ```
 - The `additionalProperties: false` is critical — prevents the model from adding extra fields

2. Ambiguity resolution rules (included in the prompt):
 - 'If a value cannot be determined: set required fields to null, omit optional fields entirely'
 - 'Never invent a value for a field. If the value is not in the input, it is null or omitted.'
 - 'If a value does not match the allowed enum values, map it to the closest matching enum value. If no mapping is appropriate, set to null.'

3. Type coercion instructions:
 - 'Numbers that appear as strings must be converted to numeric type: "42" → 42'
 - 'Boolean values may appear as: yes/no, true/false, 1/0 — normalize to boolean'
 - 'Dates must be converted to ISO 8601 format regardless of input format'

4. Client-side schema validation as the final safety net:
 ```python
 from jsonschema import validate, ValidationError
 def validate_output(output, schema):
 try:
 validate(instance=output, schema=schema)
 return output
 except ValidationError as e:
 # Re-prompt with the validation error
 return retry_with_correction(output, e.message)
 ```

5. Schema versioning:
 - Include a schema_version field in the prompt and in the expected output
 - When the schema changes, increment the version — this prevents old cached responses from being used

Return: schema enforcement prompt template, JSON Schema definition pattern, client validation code, retry-on-failure logic, and test cases for ambiguous inputs. 
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

The AI should return a structured result that covers the main requested outputs, such as Hard schema specification:, Include the schema as a JSON Schema definition, not just a description, Specify for each field: type, required/optional, allowed values, format constraints. The final answer should stay clear, actionable, and easy to review inside a output formatting and extraction workflow for prompts engineer work. 

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
