# Output Formatting and Extraction *AI Prompts *

4 Prompts Engineer prompts in Output Formatting and Extraction. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Output Formatting and Extraction 
4 prompts Advanced Single prompt 01 
### Batch Extraction at Scale 

Design a prompt and system for efficiently extracting structured data from thousands of documents using LLMs at scale. Target: extract {{schema}} from {{num_documents}} document... 
Prompt text Design a prompt and system for efficiently extracting structured data from thousands of documents using LLMs at scale.

Target: extract {{schema}} from {{num_documents}} documents at a cost of < {{target_cost_per_doc}} per document.

1. Prompt efficiency for batch workloads:

 a. Minimize token count:
 - System prompt: put stable instructions (schema, rules) in the system prompt — reused across calls without re-tokenizing
 - User prompt: only the document text and a minimal task reminder
 - Omit examples from the user prompt (they are in the system prompt)
 - Compress the schema: use a compact field list instead of verbose JSON Schema

 b. Multi-document batching:
 - Process multiple short documents in a single API call by separating them with delimiters
 - 'Below are N documents separated by ---DOCUMENT_BREAK---. Extract the schema from each and return a JSON array with one object per document in the same order.'
 - Optimal batch size: experiment with 3–10 documents per call; larger batches reduce API overhead but increase error blast radius

 c. Document chunking for long documents:
 - If a document exceeds the context window: split into overlapping chunks
 - Extract from each chunk independently
 - Merge: for each field, take the value from whichever chunk had the clearest signal

2. Quality vs cost tradeoffs:
 - Tier 1 (high importance documents): full prompt + self-critique + validation = highest quality, highest cost
 - Tier 2 (standard documents): full prompt + schema validation = balanced
 - Tier 3 (bulk/archival): compact prompt + spot-check validation = lowest cost

3. Error handling at scale:
 - Track parse failure rate per batch
 - If failure rate > 5%: halt and investigate prompt or input quality
 - Retry failures with a longer, more explicit prompt before flagging for human review
 - Log every failure with the input document and error for post-hoc analysis

4. Cost monitoring:
 - Track tokens in and out per document type
 - Alert if cost per document exceeds budget
 - Identify document types that are disproportionately expensive (too long, too complex)

Return: system prompt for batch extraction, batching implementation, chunking strategy, tier routing logic, and cost monitoring dashboard spec. Copy prompt Open prompt details Beginner Single prompt 02 
### Reliable JSON Output Prompt 

Design prompts and parsing strategies to get reliable, parseable JSON from LLMs every time. Unreliable JSON is one of the most common LLM integration failure modes — the model a... 
Prompt text Design prompts and parsing strategies to get reliable, parseable JSON from LLMs every time.

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

Return: the reliable JSON prompt template, extraction code, schema validation code, retry logic, and a test harness that measures JSON parse success rate across 100 calls. Copy prompt Open prompt details Intermediate Single prompt 03 
### Schema Enforcement Prompt 

Design a prompt pattern that enforces strict output schema adherence even when the input data is ambiguous or incomplete. The challenge: when input data is messy, LLMs tend to i... 
Prompt text Design a prompt pattern that enforces strict output schema adherence even when the input data is ambiguous or incomplete.

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

Return: schema enforcement prompt template, JSON Schema definition pattern, client validation code, retry-on-failure logic, and test cases for ambiguous inputs. Copy prompt Open prompt details Intermediate Single prompt 04 
### Table Parsing Prompt 

Design prompts that extract structured data from tables in various formats — HTML, Markdown, PDF text, and ASCII. Tables from documents are often the richest data source but are... 
Prompt text Design prompts that extract structured data from tables in various formats — HTML, Markdown, PDF text, and ASCII.

Tables from documents are often the richest data source but are structurally complex. LLMs can parse them, but need explicit instructions to do so reliably.

1. Table parsing challenges:
 - Multi-row headers (the column meaning is in 2 rows, not 1)
 - Merged cells (a cell spans multiple rows or columns)
 - Implicit structure (blank cells mean 'same as above')
 - Footnotes that modify cell values (values marked with * have different meaning)
 - Mixed data types in the same column

2. Table parsing prompt structure:

 Step 1 — Table understanding:
 'First, describe the structure of this table: how many rows and columns, what the headers mean, and any structural complexity (merged cells, multi-row headers, footnotes).'

 Step 2 — Header normalization:
 'List the column headers as they will appear in the output. If headers span multiple rows, combine them into a single descriptive name. Example: a table with "Revenue" in row 1 and "Q1 | Q2 | Q3" in row 2 produces columns: revenue_q1, revenue_q2, revenue_q3.'

 Step 3 — Row extraction:
 'Extract each data row as a JSON object. Resolve all implicit structure: fill in blank cells with the value from the cell above. Handle footnotes: if a cell has a footnote marker, include a footnote_[column] field with the footnote text.'

 Step 4 — Output:
 'Return a JSON array of objects, one per data row (excluding headers). Column names must match Step 2.'

3. Format-specific instructions:

 HTML tables:
 'Parse the <table> element. Handle colspan and rowspan attributes to correctly assign values to cells.'

 Markdown tables:
 'Parse the pipe-delimited table. The first row after |---|---| is the header. Each subsequent row is a data row.'

 PDF extracted text (hardest):
 'The table has been extracted from a PDF and may have alignment artifacts. Use column position context to assign values to the correct column even if whitespace is irregular.'

4. Validation:
 - After extraction: 'Verify that the number of values in each row matches the number of headers. Flag any row with a mismatch.'

Return: parsing prompts for each format, a test with a complex table (merged cells, footnotes), expected JSON output, and validation code. Copy prompt Open prompt details 
## Recommended Output Formatting and Extraction workflow 
1 
### Batch Extraction at Scale 

Start with a focused prompt in Output Formatting and Extraction so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Reliable JSON Output Prompt 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Schema Enforcement Prompt 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Table Parsing Prompt 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
