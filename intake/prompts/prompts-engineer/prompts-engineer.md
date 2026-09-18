# Prompts Engineer *AI Prompts *

Prompts Engineer AI prompt library with 18 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Prompts Engineer prompt categories 
5 categories 
### Prompt Design for Data Tasks 

AI prompts for designing reliable prompts for data extraction, cleaning, SQL generation, and multi-step data workflows. 
5 prompts Anomaly Explanation Prompt Data Cleaning Instruction Prompt → 
### Chain-of-Thought for Analysis 

AI prompts for structured reasoning patterns in data analysis, comparative evaluation, root-cause analysis, and self-critique workflows. 
4 prompts Comparative Analysis CoT Data Analysis CoT Prompt → 
### Output Formatting and Extraction 

AI prompts for strict output formatting, schema enforcement, table parsing, and robust extraction pipelines at scale. 
4 prompts Batch Extraction at Scale Reliable JSON Output Prompt → 
### Prompt Testing and Evaluation 

AI prompts for prompt testing and evaluation, including quality criteria, benchmark scenarios, regression checks, and improvement loops. 
3 prompts LLM-as-Judge Evaluation Prompt Evaluation Dataset Builder → 
### Meta-Prompting 

AI prompts for meta-prompting, including prompt critique, iteration strategies, and reusable prompt design patterns for better model behavior. 
2 prompts Few-Shot Example Builder Chain Prompt Optimizer → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 18 Prompt Design for Data Tasks 5 Chain-of-Thought for Analysis 4 Output Formatting and Extraction 4 Prompt Testing and Evaluation 3 Meta-Prompting 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **18 **of 18 prompts 
## Prompt Design for Data Tasks 
5 prompt s Prompt Design for Data Tasks Intermediate Prompt 01 
### Anomaly Explanation Prompt 
Design a prompt that takes a detected data anomaly and produces a clear, business-friendly explanation with hypotheses.

Context: anomaly detection systems generate alerts, but data teams spend significant time translating statistical findings into actionable business language. This prompt automates that translation.

1. Anomaly context input structure:
 Define the inputs the prompt receives:
 - metric_name: the metric that anomalized
 - current_value: the observed value
 - expected_value: the baseline or predicted value
 - deviation_pct: percentage deviation from expected
 - time_period: when the anomaly occurred
 - segment_breakdown: how the anomaly distributes across dimensions (region, product, channel)
 - related_metrics: other metrics that moved at the same time
 - recent_events: known business events in the same time window (promotions, deployments, holidays)

2. Prompt instructions:
 - 'You are a senior data analyst. Explain this data anomaly to a business audience.'
 - 'Do not use statistical terminology. Replace with plain business language.'
 - 'Do not speculate beyond what the data supports. Distinguish between confirmed facts and hypotheses.'

3. Output structure (enforce with the prompt):
 - What happened: 1–2 sentences describing the anomaly in plain English
 - Where it is concentrated: which segments, regions, or dimensions account for most of the deviation
 - Likely causes: 2–3 hypotheses ranked by likelihood, each with supporting evidence from the data
 - What is needed to confirm: what additional data or investigation would confirm the top hypothesis
 - Recommended action: a specific next step for the business team

4. Tone calibration:
 - For a 5% deviation: 'A moderate shift worth monitoring'
 - For a 20% deviation: 'A significant change that warrants investigation'
 - For a 50%+ deviation: 'An extreme anomaly requiring immediate attention'
 - Instruct the model to match tone to deviation magnitude

5. Few-shot examples:
 - Provide 2 example anomalies with full context and the ideal explanation output
 - Include one where the cause is known (holiday effect) and one where it is unknown

Return: the complete anomaly explanation prompt, 2 few-shot examples, and a rubric for evaluating explanation quality (accuracy, clarity, actionability). Copy prompt View page Show more ↓ Prompt Design for Data Tasks Beginner Prompt 02 
### Data Cleaning Instruction Prompt 
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

Return: single-record cleaning prompt, batch cleaning prompt, test set of 20 messy values, and expected normalized outputs. Copy prompt View page Show more ↓ Prompt Design for Data Tasks Advanced Prompt 03 
### Multi-Step Data Pipeline Prompt 
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

Return: all 4 step prompts, a Python orchestration script, and a test case with expected intermediate outputs. Copy prompt View page Show more ↓ Prompt Design for Data Tasks Intermediate Prompt 04 
### SQL Generation Prompt 
Design a prompt that reliably generates correct SQL from natural language questions about a specific database schema.

Database schema: {{schema_definition}}
SQL dialect: {{dialect}} (PostgreSQL / BigQuery / Snowflake / DuckDB)
Target user: {{user_type}} (data analyst / business user / developer)

1. Schema context injection:
 - Include the full DDL for all relevant tables in the prompt
 - Add a brief description above each table: what it represents and its grain
 - Add a brief description of each column that is not self-explanatory
 - Include sample data (3 rows per table) to help the model understand value formats
 - Specify relationships: 'orders.customer_id is a foreign key to customers.id'

2. Dialect-specific instructions:
 - List the dialect-specific functions to use: 'Use DATE_TRUNC for date truncation, not TRUNC'
 - Specify quoting conventions: 'Quote identifiers with double quotes'
 - Specify NULL handling conventions relevant to this dialect

3. SQL style guidelines (for readable, consistent output):
 - SELECT clause: one column per line, aligned
 - Use CTEs (WITH clauses) for multi-step logic, not nested subqueries
 - Always use explicit JOIN syntax, never implicit comma joins
 - Always qualify column names with table aliases when joining multiple tables
 - Add a comment above each CTE explaining what it computes

4. Ambiguity resolution rules:
 - 'When the question is ambiguous about date range, default to the last 30 days'
 - 'When the question asks for top N without specifying N, use 10'
 - 'When a metric could be calculated multiple ways, choose the simplest correct interpretation and add a SQL comment noting the assumption'

5. Error prevention instructions:
 - 'Never use SELECT * in the final output'
 - 'Always add a LIMIT clause when the question does not specify a row count'
 - 'For aggregations, always include GROUP BY for all non-aggregated columns'

6. Output format:
 - Return only the SQL query
 - No explanation unless explicitly asked
 - Add inline SQL comments for any non-obvious logic

Return: the complete SQL generation prompt, 5 test questions ranging from simple to complex, the correct SQL for each, and a rubric for evaluating SQL correctness. Copy prompt View page Show more ↓ Prompt Design for Data Tasks Beginner Prompt 05 
### Structured Data Extraction Prompt 
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

Return: the complete extraction prompt, a test with 3 sample inputs (clean, messy, and edge case), and expected outputs for each. Copy prompt View page Show more ↓ 
## Chain-of-Thought for Analysis 
4 prompt s Chain-of-Thought for Analysis Intermediate Prompt 01 
### Comparative Analysis CoT 
Design a chain-of-thought prompt for rigorous comparative analysis — comparing two or more entities, time periods, or segments in data.

Comparative questions ('is A better than B?', 'what changed between Q1 and Q2?') are prone to cherry-picking evidence and confirmation bias without structured reasoning.

1. Comparative analysis CoT structure:

 Step 1 — Define what is being compared:
 'State explicitly: what are the entities being compared (A and B)? Over what time period? On what metrics?'

 Step 2 — Establish the comparison framework:
 'Before looking at the numbers, list all the metrics relevant to this comparison. This prevents cherry-picking only favorable metrics.'

 Step 3 — Gather facts for each metric:
 'For each metric: state the value for A, the value for B, the absolute difference, and the percentage difference. No interpretation yet — just facts.'

 Step 4 — Context and normalization:
 'Are the metrics comparable as-is, or do they need normalization? (e.g. revenue needs to be adjusted for market size, conversion rate needs same traffic source)'

 Step 5 — Statistical significance check:
 'For each difference: is the sample size large enough to be confident in this difference? State if sample sizes are too small to draw conclusions.'

 Step 6 — Balanced interpretation:
 'Where does A outperform B? Where does B outperform A? Are there metrics where they are effectively equal?'

 Step 7 — Synthesis:
 'Given the complete picture, what is the overall conclusion? On balance, which is better and why? What are the conditions under which this conclusion might reverse?'

2. Common mistakes to guard against (include in the prompt):
 - 'Do not declare an overall winner based on only 1–2 metrics while ignoring others.'
 - 'Do not interpret noise as signal. Differences smaller than X% on samples smaller than N should be treated as inconclusive.'
 - 'Do not use relative changes that obscure absolute differences. Always state both.'

3. Output format:
 - Comparison table: metric | A value | B value | difference | significance | winner
 - Written summary: balanced narrative, 2–3 paragraphs
 - Bottom line: one sentence conclusion with appropriate caveats

Return: the comparative analysis CoT prompt, a sample comparison scenario with data, expected CoT reasoning, and the comparison table output. Copy prompt View page Show more ↓ Chain-of-Thought for Analysis Beginner Prompt 02 
### Data Analysis CoT Prompt 
Design a chain-of-thought (CoT) prompt that guides an LLM to analyze a dataset systematically rather than jumping to conclusions.

Without CoT, LLMs often pattern-match to the most likely answer rather than reasoning through the data. CoT forces step-by-step reasoning that catches more errors and produces more reliable analysis.

1. The CoT trigger phrase:
 - End your analysis instruction with: 'Think through this step by step before giving your final answer.'
 - Alternative: 'Before answering, work through your reasoning in a <scratchpad> block.'
 - The scratchpad approach separates reasoning from the final answer, making the output cleaner

2. Analysis CoT structure to enforce:

 Instruct the model to reason through these steps explicitly:

 Step 1 — Understand the question:
 'Restate the analysis question in your own words. What exactly is being asked?'

 Step 2 — Identify what data is needed:
 'What columns, filters, or aggregations are needed to answer this question?'

 Step 3 — Check for data quality issues:
 'Before computing, scan for: missing values in key columns, outliers that could skew results, date range coverage.'

 Step 4 — Compute:
 'Perform the calculation. Show intermediate steps for any non-trivial computation.'

 Step 5 — Sanity check the result:
 'Does this result make intuitive sense? Is it in the expected order of magnitude? If it seems surprising, explain why.'

 Step 6 — Answer the question:
 'State the answer clearly in one sentence. Include the key number and appropriate context.'

3. When to use CoT vs direct prompting:
 - Use CoT for: multi-step calculations, comparisons across multiple groups, trend analysis, root cause questions
 - Use direct prompting for: simple lookups, single-step aggregations, formatting tasks
 - CoT adds tokens (cost and latency) — only use it when reasoning quality matters

4. Zero-shot CoT vs few-shot CoT:
 - Zero-shot: just add 'Think step by step' — works surprisingly well for moderate complexity
 - Few-shot: provide 2–3 complete reasoning examples — significantly better for complex or domain-specific analysis

Return: a zero-shot CoT data analysis prompt, a few-shot version with 2 complete reasoning examples, and a comparison of outputs with and without CoT on a sample analysis question. Copy prompt View page Show more ↓ Chain-of-Thought for Analysis Intermediate Prompt 03 
### Root Cause CoT Prompt 
Design a chain-of-thought prompt that guides an LLM through a data-driven root cause analysis.

Context: given a metric deviation and supporting data, the LLM must reason through possible causes systematically rather than anchoring on the first plausible explanation.

1. The anchoring bias problem:
 - Without explicit CoT, LLMs tend to latch onto the first plausible cause and construct evidence to support it
 - The prompt must force the model to generate and evaluate multiple hypotheses before selecting one

2. Root cause CoT structure:

 Phase 1 — Problem characterization:
 'Before investigating causes, fully characterize the problem:
 - What changed? (metric, direction, magnitude)
 - When did it change? (onset, duration, pattern: sudden vs gradual)
 - Where is it concentrated? (which segments, regions, or products account for the most deviation)
 - What did NOT change? (other metrics that are stable, ruling out systemic causes)'

 Phase 2 — Hypothesis generation (before looking at evidence):
 'Generate 5 possible causes for this deviation WITHOUT evaluating likelihood yet.
 Force yourself to consider: seasonal effects, data pipeline issues, product changes, external events, and measurement errors.'

 Phase 3 — Evidence evaluation:
 'For each hypothesis, evaluate the evidence FOR and AGAINST it from the provided data.
 Be explicit about what evidence would be needed to confirm or rule out each hypothesis.'

 Phase 4 — Hypothesis ranking:
 'Rank the 5 hypotheses from most to least likely. Justify each ranking with specific evidence.'

 Phase 5 — Conclusion:
 'State the most likely root cause. State your confidence level (High/Medium/Low). State the key assumption that, if wrong, would change your conclusion.'

3. Anti-hallucination guardrails:
 - 'Do not cite data that was not provided in the input. If you need data you do not have, say so.'
 - 'If the available data is insufficient to determine the root cause, say so explicitly rather than speculating.'

4. Structured output:
 - The scratchpad contains the full CoT reasoning
 - The final answer is a concise summary: root cause, confidence, key evidence, and next diagnostic step

Return: the root cause CoT prompt, 2 test cases with complete data inputs, expected reasoning chains, and evaluation rubric. Copy prompt View page Show more ↓ Chain-of-Thought for Analysis Advanced Prompt 04 
### Self-Critique Analysis Prompt 
Design a self-critique prompt pattern where the LLM generates an initial data analysis and then critiques and improves its own output.

Self-critique significantly improves analysis quality by catching errors, unsupported conclusions, and missing context that the initial generation missed.

1. The two-pass pattern:

 Pass 1 — Initial analysis:
 Use a standard analysis prompt to generate an initial response.
 Do not add self-critique instructions yet — let the model generate its natural first response.

 Pass 2 — Self-critique (separate prompt call):
 Feed the initial analysis back to the model with this critique prompt:

 'Review the following data analysis. Critique it on these specific dimensions:

 1. Factual accuracy: Are all numbers and statistics correctly stated? Check each claim against the source data.
 2. Unsupported claims: Are any conclusions drawn that go beyond what the data supports? Flag each one.
 3. Missing context: What important context was omitted that would change the interpretation?
 4. Confounding factors: What alternative explanations were not considered?
 5. Misleading framing: Is any language used that could lead a reader to a wrong conclusion?
 6. Precision: Are confidence levels stated where appropriate? Is uncertainty acknowledged?

 For each issue found: quote the problematic text, explain the issue, and provide the corrected version.'

 Pass 3 — Revised analysis:
 'Now write a revised version of the analysis that incorporates all the corrections from your critique.'

2. When self-critique is most valuable:
 - High-stakes analyses that will be presented to leadership
 - Analyses that will inform a significant business decision
 - Any analysis containing causal claims (correlation ≠ causation)
 - Analyses where the conclusion is surprising — surprising results deserve extra scrutiny

3. Efficiency tip:
 - For most analyses, the two-pass pattern (initial + critique) is sufficient
 - Three passes (initial + critique + revised) adds quality but also cost and latency
 - Use three passes only when the stakes are high enough to justify it

4. Automated critique checklist integration:
 - Convert the critique dimensions into a checklist that runs automatically after every analysis
 - Flag outputs that trigger any checklist item for human review before distribution

Return: the three-pass prompt sequence, a test case showing how critique improved a flawed initial analysis, and a decision guide for when to use 2 vs 3 passes. Copy prompt View page Show more ↓ 
## Output Formatting and Extraction 
4 prompt s Output Formatting and Extraction Advanced Prompt 01 
### Batch Extraction at Scale 
Design a prompt and system for efficiently extracting structured data from thousands of documents using LLMs at scale.

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

Return: system prompt for batch extraction, batching implementation, chunking strategy, tier routing logic, and cost monitoring dashboard spec. Copy prompt View page Show more ↓ Output Formatting and Extraction Beginner Prompt 02 
### Reliable JSON Output Prompt 
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

Return: the reliable JSON prompt template, extraction code, schema validation code, retry logic, and a test harness that measures JSON parse success rate across 100 calls. Copy prompt View page Show more ↓ Output Formatting and Extraction Intermediate Prompt 03 
### Schema Enforcement Prompt 
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

Return: schema enforcement prompt template, JSON Schema definition pattern, client validation code, retry-on-failure logic, and test cases for ambiguous inputs. Copy prompt View page Show more ↓ Output Formatting and Extraction Intermediate Prompt 04 
### Table Parsing Prompt 
Design prompts that extract structured data from tables in various formats — HTML, Markdown, PDF text, and ASCII.

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

Return: parsing prompts for each format, a test with a complex table (merged cells, footnotes), expected JSON output, and validation code. Copy prompt View page Show more ↓ 
## Prompt Testing and Evaluation 
3 prompt s Prompt Testing and Evaluation Advanced Prompt 01 
### LLM-as-Judge Evaluation 
Design a reliable LLM-as-judge system to evaluate the quality of data analysis outputs at scale.

Human evaluation is the gold standard but does not scale. LLM-as-judge enables automated quality evaluation across thousands of outputs — if done correctly.

1. When LLM-as-judge is appropriate:
 - When human evaluation is too expensive or slow to run at scale
 - For outputs where correctness has a nuanced, rubric-based definition
 - As a first-pass filter before human review of borderline cases
 - NOT appropriate as a sole quality gate for high-stakes outputs

2. Judge prompt design (critical — garbage in, garbage out):

 a. Role and task:
 'You are an expert data analyst evaluating the quality of an AI-generated data analysis. Your evaluation must be objective and based only on the criteria below.'

 b. Evaluation rubric (specific dimensions with clear descriptions):
 'Score the analysis on each dimension from 1 to 5:
 - Factual accuracy (1–5): Are all numbers and statistics correctly stated? Does the analysis accurately describe the data?
 - Logical reasoning (1–5): Does the analysis reason correctly from data to conclusions? Are any logical leaps unjustified?
 - Completeness (1–5): Does the analysis address the question fully? Are important insights missing?
 - Clarity (1–5): Is the analysis clearly written and easy for a business audience to understand?
 - Actionability (1–5): Does the analysis lead to a clear, specific recommended action?'

 c. Output format:
 'Return a JSON object: {"factual_accuracy": N, "logical_reasoning": N, "completeness": N, "clarity": N, "actionability": N, "overall": N, "key_issues": ["issue 1", "issue 2"], "strengths": ["strength 1"]}'

3. Reliability safeguards:
 - Reference answer: provide the correct answer alongside the candidate output so the judge can compare
 - Position bias mitigation: if comparing two outputs, run the judge twice with A/B order swapped; average the scores
 - Calibration: measure judge agreement with human evaluators on 50 calibration examples; adjust if disagreement > 20%

4. Judge validation:
 - Test the judge on known good outputs (should score > 4 on all dimensions)
 - Test on known bad outputs (should score < 2 on accuracy when factual errors are present)
 - Measure consistency: run the same input through the judge 5 times and check score variance (should be < 0.5 std)

Return: judge prompt, calibration procedure, consistency test, and a dashboard for tracking judge-assessed quality over time. Copy prompt View page Show more ↓ Prompt Testing and Evaluation Intermediate Prompt 02 
### Prompt Evaluation Dataset Builder 
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

Return: dataset construction procedure, annotation guide, inter-annotator agreement calculation, metric implementations per task type, and dataset versioning schema. Copy prompt View page Show more ↓ Prompt Testing and Evaluation Intermediate Prompt 03 
### Prompt Regression Test Suite 
Build a regression test suite to detect when prompt changes break existing behavior.

Prompts are code. When you change a prompt, you need to verify that all previously working cases still work — just like software regression testing.

1. Test case structure:
 Each test case has:
 - test_id: unique identifier
 - description: what this test verifies
 - input: the exact input to the prompt
 - expected_output: the exact expected output (for exact match tests) OR
 - expected_properties: properties the output must satisfy (for semantic tests)
 - tags: categories for running subsets (e.g. 'edge_case', 'high_priority', 'numeric')

2. Test types for data prompts:

 a. Exact match tests:
 - For deterministic outputs (extraction, formatting, SQL generation with temperature=0)
 - output == expected_output
 - Run with temperature=0 for reproducibility

 b. Schema validation tests:
 - Output must conform to the expected JSON schema
 - Use jsonschema.validate()

 c. Semantic equivalence tests:
 - For analysis outputs where wording may vary but meaning must be the same
 - Use a judge LLM: 'Does this output convey the same information as the expected output? Answer yes or no and explain.'
 - Or use sentence similarity (cosine similarity of embeddings > 0.9)

 d. Property tests:
 - Check specific properties: 'revenue value is a positive number', 'date is in ISO 8601 format', 'no fields are missing'
 - More robust than exact match for outputs with variability

3. Test execution:
 - Run the full suite before every prompt change is deployed
 - Track pass rate over time — a declining pass rate indicates prompt drift
 - Run with multiple seeds (temperature > 0) for stochastic tests to measure variance

4. Building the initial test set:
 - Start with 20–30 representative cases covering the main input patterns
 - Add an edge case test every time a bug is found and fixed
 - Prioritize: 5 critical tests that must always pass (core functionality), 20 standard tests, N edge case tests

5. CI/CD integration:
 - Run critical tests on every PR that touches the prompt
 - Run the full suite before every production deployment
 - Block deployment if critical test pass rate < 100% or overall pass rate < 90%

Return: test case schema, test runner implementation, judge LLM integration for semantic tests, and CI/CD configuration. Copy prompt View page Show more ↓ 
## Meta-Prompting 
2 prompt s Meta-Prompting Advanced Chain 01 
### Few-Shot Example Builder Chain 
Step 1: Define the task and failure modes — describe the extraction or analysis task precisely. List the 5 most common ways the model currently fails on this task (wrong format, wrong field, missed edge case, wrong inference, etc.).
Step 2: Identify example coverage needs — for each failure mode, determine what kind of example would teach the model to handle it correctly. The example set should cover: a clean/easy case, a hard/ambiguous case, an edge case for each common failure mode, and a 'correct refusal' case where the answer is null or unknown.
Step 3: Draft examples — write input-output pairs for each required example type. For each example: choose the simplest input that demonstrates the pattern (complex examples obscure the lesson), write the exact correct output in the target format, and add a brief comment explaining what this example teaches (this comment is for you, not the model).
Step 4: Order the examples — order them from simplest to most complex. Studies show that example order affects LLM performance. The first example anchors the model's interpretation of the task; make it the clearest, most typical case.
Step 5: Test individual examples — before assembling into a full prompt, test each example by asking the model to predict the output without seeing the answer. If the model gets it right without the example, the example may not be needed. If the model gets it wrong, the example is teaching something valuable.
Step 6: Assemble and evaluate — combine the examples into the prompt and run the full evaluation suite. Compare performance with 0, 2, 4, 6, and 8 examples to find the optimal number. More is not always better — irrelevant examples add noise.
Step 7: Document the example set — for each example, record: why it was included, what failure mode it addresses, and when it should be updated. Treat examples as code: version-controlled, with change history and rationale. Copy prompt View page Show more ↓ Meta-Prompting Advanced Prompt 02 
### Prompt Optimizer 
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

Return: the failure analysis meta-prompt, optimization loop implementation, candidate evaluation framework, and a worked example showing 3 iterations of improvement on a real extraction prompt. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
