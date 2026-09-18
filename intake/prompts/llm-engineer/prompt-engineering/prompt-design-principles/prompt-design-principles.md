# Prompt Design Principles *AI Prompt *

Apply structured prompt design principles to improve the reliability and quality of LLM outputs for this task. Task: {{task_description}} Model: {{model}} (GPT-4, Claude, Llama,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply structured prompt design principles to improve the reliability and quality of LLM outputs for this task.

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

Return: revised system prompt, user prompt template, output format specification, and test plan. 
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

The AI should return a structured result that covers the main requested outputs, such as Anatomy of an effective prompt:, State the role: 'You are an expert {{domain}} analyst.', State the task clearly: what should the model do?. The final answer should stay clear, actionable, and easy to review inside a prompt engineering workflow for llm engineer work. 

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
