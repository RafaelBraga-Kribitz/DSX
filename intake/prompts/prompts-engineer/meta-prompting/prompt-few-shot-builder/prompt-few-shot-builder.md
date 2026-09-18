# Few-Shot Example Builder Chain *AI Prompt *

Step 1: Define the task and failure modes — describe the extraction or analysis task precisely. List the 5 most common ways the model currently fails on this task (wrong format,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define the task and failure modes — describe the extraction or analysis task precisely. List the 5 most common ways the model currently fails on this task (wrong format, wrong field, missed edge case, wrong inference, etc.).
Step 2: Identify example coverage needs — for each failure mode, determine what kind of example would teach the model to handle it correctly. The example set should cover: a clean/easy case, a hard/ambiguous case, an edge case for each common failure mode, and a 'correct refusal' case where the answer is null or unknown.
Step 3: Draft examples — write input-output pairs for each required example type. For each example: choose the simplest input that demonstrates the pattern (complex examples obscure the lesson), write the exact correct output in the target format, and add a brief comment explaining what this example teaches (this comment is for you, not the model).
Step 4: Order the examples — order them from simplest to most complex. Studies show that example order affects LLM performance. The first example anchors the model's interpretation of the task; make it the clearest, most typical case.
Step 5: Test individual examples — before assembling into a full prompt, test each example by asking the model to predict the output without seeing the answer. If the model gets it right without the example, the example may not be needed. If the model gets it wrong, the example is teaching something valuable.
Step 6: Assemble and evaluate — combine the examples into the prompt and run the full evaluation suite. Compare performance with 0, 2, 4, 6, and 8 examples to find the optimal number. More is not always better — irrelevant examples add noise.
Step 7: Document the example set — for each example, record: why it was included, what failure mode it addresses, and when it should be updated. Treat examples as code: version-controlled, with change history and rationale. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin meta-prompting work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Meta-Prompting or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a meta-prompting workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Meta-Prompting.
