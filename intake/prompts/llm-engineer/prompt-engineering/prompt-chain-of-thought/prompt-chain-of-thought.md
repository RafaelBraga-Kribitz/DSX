# Chain-of-Thought and Reasoning Prompts *AI Prompt *

Design chain-of-thought (CoT) and structured reasoning prompts for complex tasks. Task type: {{task_type}} (math, logic, multi-step analysis, classification with rationale) Mode... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design chain-of-thought (CoT) and structured reasoning prompts for complex tasks.

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

Return: CoT prompt template for this task, few-shot examples, self-consistency implementation plan, and reasoning format specification. 
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

The AI should return a structured result that covers the main requested outputs, such as Zero-shot chain-of-thought:, Identify the key information given, Determine what needs to be found. The final answer should stay clear, actionable, and easy to review inside a prompt engineering workflow for llm engineer work. 

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
