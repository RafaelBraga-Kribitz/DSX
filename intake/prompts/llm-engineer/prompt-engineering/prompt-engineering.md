# Prompt Engineering *AI Prompts *

4 LLM Engineer prompts in Prompt Engineering. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Prompt Engineering 
4 prompts Intermediate Single prompt 01 
### Chain-of-Thought and Reasoning Prompts 

Design chain-of-thought (CoT) and structured reasoning prompts for complex tasks. Task type: {{task_type}} (math, logic, multi-step analysis, classification with rationale) Mode... 
Prompt text Design chain-of-thought (CoT) and structured reasoning prompts for complex tasks.

Task type: {{task_type}} (math, logic, multi-step analysis, classification with rationale)
Model: {{model}}
Accuracy requirement: {{accuracy}} (standard or high-stakes)

1. Zero-shot chain-of-thought:
 Simply adding 'Let's think step by step.' to the prompt dramatically improves accuracy on multi-step reasoning tasks.

 Template:
 'Solve this problem: {{problem}}
 Let's think step by step. Show your reasoning before giving the final answer.'

 For even more structure:
 'Work through this problem systematically:
 1. Identify the key information given
 2. Determine what needs to be found
 3. Apply the relevant principles step by step
 4. State the final answer clearly

 Problem: {{problem}}'

2. Few-shot CoT:
 Provide 2-3 worked examples before the target problem.
 Each example shows: input → reasoning steps → output

 Format:
 'Q: [example problem]
 A: Let me think step by step.
 Step 1: ...
 Step 2: ...
 Therefore: [answer]

 Q: [target problem]
 A: Let me think step by step.'

 Example quality: examples should cover different reasoning patterns, not just the same type repeated.

3. Self-consistency:
 - Generate N independent responses to the same question (different random seeds / temperature > 0)
 - Aggregate by majority vote on the final answer
 - Empirically improves accuracy by 5-10% on reasoning benchmarks
 - Practical implementation: run the prompt 5 times, take the most common answer

4. ReAct (Reasoning + Acting):
 - Interleave: Thought → Action → Observation loops
 - The model reasons about what to do, takes an action (tool call), observes the result, repeats
 - Use for: tasks requiring external tool use, multi-step information retrieval, code execution

 Format:
 'Thought: I need to find the current population of France.
 Action: search("France population 2024")
 Observation: France has a population of approximately 68 million.
 Thought: Now I can answer the question.
 Answer: France's population is approximately 68 million.'

5. Least-to-most prompting:
 - Decompose the hard question into simpler sub-questions
 - Solve each sub-question sequentially, feeding prior answers as context
 - Use for: compositional tasks, multi-hop questions

Return: CoT prompt template for this task, few-shot examples, self-consistency implementation plan, and reasoning format specification. Copy prompt Open prompt details Beginner Single prompt 02 
### Prompt Design Principles 

Apply structured prompt design principles to improve the reliability and quality of LLM outputs for this task. Task: {{task_description}} Model: {{model}} (GPT-4, Claude, Llama,... 
Prompt text Apply structured prompt design principles to improve the reliability and quality of LLM outputs for this task.

Task: {{task_description}}
Model: {{model}} (GPT-4, Claude, Llama, Mistral, etc.)
Output format required: {{output_format}}
Current prompt: {{current_prompt}} (if exists)

1. Anatomy of an effective prompt:

 System prompt (instruction context):
 - State the role: 'You are an expert {{domain}} analyst.'
 - State the task clearly: what should the model do?
 - State the constraints: what should the model NOT do?
 - State the output format explicitly: 'Return a JSON object with fields...'
 - Keep the system prompt focused: one role, one task type per system prompt

 User prompt (the input):
 - Provide the specific input to process
 - Separate instructions from data: use XML tags, triple backticks, or markdown headings
 - Be specific: avoid vague instructions like 'summarize well' — say 'summarize in 3 bullet points, each < 20 words'

2. Clarity and specificity:
 - Vague: 'Analyze this text'
 - Better: 'Identify the main argument, list 3 supporting claims, and note any logical fallacies. Return as JSON: {main_argument: str, supporting_claims: [str], fallacies: [str]}'
 - Always specify: length, format, level of detail, target audience, and any constraints

3. Context and role-setting:
 - Assigning a role improves domain-specific outputs: 'You are a board-certified cardiologist...'
 - Providing context reduces hallucination: tell the model what it needs to know
 - Grounding: 'Based only on the following document:' prevents the model from using outside knowledge

4. Output format specification:
 - For structured data: always specify JSON schema with field names, types, and descriptions
 - For text: specify structure (e.g., 'Use H2 headings for each section, bullet points under each')
 - Use few-shot examples for complex or non-standard formats
 - Add: 'Return only the JSON object and nothing else, no preamble or explanation'

5. Negative instructions:
 - 'Do not include any information not present in the source text'
 - 'Do not use the phrase "In conclusion"'
 - 'Do not make assumptions about data not provided'

6. Iterative refinement:
 - Test the prompt on 10-20 diverse examples before finalizing
 - Review failures: which examples fail and why?
 - Add a clarifying sentence to the system prompt for each failure category

Return: revised system prompt, user prompt template, output format specification, and test plan. Copy prompt Open prompt details Advanced Single prompt 03 
### Prompt Evaluation and Testing 

Build a systematic evaluation framework for testing and improving LLM prompts. Task: {{task}} Prompt: {{prompt}} Success criteria: {{success_criteria}} Evaluation budget: {{budg... 
Prompt text Build a systematic evaluation framework for testing and improving LLM prompts.

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

Return: eval dataset construction plan, metric selection, LLM-judge prompt, regression test protocol, and failure analysis procedure. Copy prompt Open prompt details Intermediate Single prompt 04 
### Structured Output Extraction 

Design prompts that reliably extract structured data from LLM outputs. Input type: {{input_type}} (free text, documents, conversations, web content) Required output schema: {{sc... 
Prompt text Design prompts that reliably extract structured data from LLM outputs.

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

Return: extraction prompt template, schema specification, compliance enforcement approach, retry logic, and hallucination prevention rules. Copy prompt Open prompt details 
## Recommended Prompt Engineering workflow 
1 
### Chain-of-Thought and Reasoning Prompts 

Start with a focused prompt in Prompt Engineering so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Prompt Design Principles 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Prompt Evaluation and Testing 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Structured Output Extraction 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
