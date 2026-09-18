# Agentic System Design *AI Prompt *

Design a reliable LLM agent system that uses tools to complete multi-step tasks. Agent task: {{task}} Available tools: {{tools}} (web search, code execution, database query, API... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a reliable LLM agent system that uses tools to complete multi-step tasks.

Agent task: {{task}}
Available tools: {{tools}} (web search, code execution, database query, API calls, file operations)
Reliability requirement: {{reliability}} (best-effort or guaranteed completion)
Human-in-the-loop: {{hitl}} (yes/no — is human approval required for certain actions?)

1. Agent architecture:

 ReAct loop (Reasoning + Acting):
 - Thought: the agent reasons about what to do next
 - Action: the agent selects and calls a tool
 - Observation: the agent receives the tool result
 - Repeat until the agent decides the task is complete

 Plan-and-execute (more reliable for complex tasks):
 - Planning step: decompose the task into a sequence of sub-tasks
 - Execution: execute each sub-task sequentially (or in parallel where possible)
 - Re-planning: if a step fails, re-plan from the current state

2. Tool design:
 - Each tool has: name, description (the agent reads this to decide when to use it), input schema, output schema
 - Tools must be: idempotent where possible (safe to retry), fast (< 5s for most tools), well-scoped (do one thing well)
 - Tool description quality is critical: the agent's tool selection depends entirely on the description
 - Validation: validate tool outputs before passing to the next step

3. Error handling and retries:
 - Transient failures: retry the tool call up to 3 times with backoff
 - Persistent failures: skip the step and log; reroute to a fallback tool if available
 - Maximum iterations: set a hard limit (e.g., 20 steps) to prevent infinite loops
 - Checkpoint saving: save the agent's state after each completed step; resume from the last checkpoint on failure

4. Safety for agentic systems:
 - Minimal footprint: request only the permissions needed for the current task
 - Human approval gates: require human confirmation before irreversible actions (sending emails, deleting data, making payments)
 - Sandboxed execution: run code in an isolated container (e.g., E2B sandbox)
 - Audit log: log every action the agent takes, every tool it calls, and every decision it makes

5. Frameworks:
 - LangGraph: production-grade graph-based agent framework with state management
 - LlamaIndex Agents: strong for RAG-augmented agents
 - AutoGen (Microsoft): multi-agent conversation framework
 - Pydantic AI: type-safe agent framework with validation
 - Anthropic's computer use: for agents that interact with GUIs

Return: agent architecture selection, tool specification schema, error handling strategy, safety controls, and framework recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin llm infrastructure work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in LLM Infrastructure or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Agent architecture:, Thought: the agent reasons about what to do next, Action: the agent selects and calls a tool. The final answer should stay clear, actionable, and easy to review inside a llm infrastructure workflow for llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in LLM Infrastructure.
