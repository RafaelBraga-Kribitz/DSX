# Code Review for Reproducibility *AI Prompt *

Review my analysis code for reproducibility and identify problems that would prevent another researcher from replicating my results. Code: {{analysis_code}} Language: {{language... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Review my analysis code for reproducibility and identify problems that would prevent another researcher from replicating my results.

Code: {{analysis_code}}
Language: {{language}}

Check for each category of reproducibility problem:

1. Environment problems (code may run differently on another machine):
 - Absolute paths: any path starting with /Users/ or C:\Users\ will fail on another machine. Replace with relative paths from the project root.
 - Missing package/library declarations: list all library() or import statements at the top of the script.
 - Undeclared package versions: are package versions recorded? Different versions may produce different results.
 - System-specific code: any code that depends on OS-specific behavior.
 - Missing random seeds: any analysis using randomization must set a seed for reproducibility.

2. Ordering problems (code must run from top to bottom without manual steps):
 - Objects used before they are defined: will cause errors if run sequentially.
 - External file dependencies not created by earlier code: scripts that depend on files that another analyst must manually provide.
 - Hidden state: code that relies on objects in the global environment from a previous session.
 - Manual steps: any step that requires human intervention (e.g. 'run this block first, then that block').

3. Data provenance problems:
 - Raw data modified in place: raw data files should never be overwritten.
 - Missing data source documentation: where did the raw data come from? How was it obtained?
 - Undocumented exclusions: data filtered or excluded without comment explaining why.

4. Documentation problems:
 - Uncommented analytical decisions: if a choice was made (which covariates to include, how to handle outliers), a comment should explain why.
 - Variable names that require knowledge of the project: use descriptive variable names.
 - No description of what the script does at the top.

5. Output stability:
 - Does the code produce the same output when run twice with the same inputs?
 - Are intermediate results saved so the full pipeline does not need to re-run to get the final results?

For each problem found:
- Line number or code section
- Description of the problem
- Corrected code

Return: annotated code review, corrected code, and a reproducibility score (0–100) with justification. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin reproducibility and open science work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Reproducibility and Open Science or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Environment problems (code may run differently on another machine):, Absolute paths: any path starting with /Users/ or C:\Users\ will fail on another machine. Replace with relative paths from the project root., Missing package/library declarations: list all library() or import statements at the top of the script.. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Reproducibility and Open Science.
