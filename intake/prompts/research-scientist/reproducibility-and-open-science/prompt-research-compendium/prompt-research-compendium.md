# Research Compendium Builder *AI Prompt *

Help me organize my research project into a reproducible research compendium that another researcher could use to replicate my findings. Project type: {{project_type}} Tools use... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me organize my research project into a reproducible research compendium that another researcher could use to replicate my findings.

Project type: {{project_type}}
Tools used: {{tools}} (R, Python, Stata, SPSS, etc.)

1. What is a research compendium:
 A research compendium is a structured collection of files that contains the data, code, and text associated with a research project, organized so that anyone can reproduce the reported results.

2. Recommended directory structure:
```
project_name/
├── README.md # Overview, how to reproduce results
├── DESCRIPTION # Dependencies and environment info
├── data/
│ ├── raw/ # Original, unmodified data (read-only)
│ ├── processed/ # Cleaned, analysis-ready data
│ └── codebook.md # Variable definitions and coding
├── code/ (or R/, scripts/)
│ ├── 00_data_cleaning.R # Data cleaning script
│ ├── 01_analysis.R # Main analysis
│ ├── 02_figures.R # Figure generation
│ └── functions/ # Custom functions used by scripts
├── output/
│ ├── figures/ # Generated figures
│ └── tables/ # Generated tables
├── paper/
│ ├── manuscript.Rmd # Paper manuscript (ideally dynamic)
│ └── references.bib # Bibliography
└── tests/ # Tests for analysis code
```

3. README content requirements:
 - Project title, authors, and contact
 - One-paragraph project description
 - How to install dependencies
 - How to reproduce the main results (step by step)
 - Brief description of each directory
 - Data availability statement
 - License

4. Dependency management:
 - R: use renv to capture package versions. Commit renv.lock.
 - Python: use a requirements.txt or conda environment.yml
 - Document the R/Python version used
 - Ideally: provide a Dockerfile or Binder link for complete environment reproducibility

5. Coding standards for reproducibility:
 - Set random seeds at the top of every script that uses randomization
 - Use relative paths (never absolute paths like /Users/YourName/...)
 - Do not modify raw data files — always create new processed versions
 - Write scripts that run from top to bottom without manual intervention
 - Comment code to explain analytical decisions, not just what the code does

6. Dynamic documents:
 - Ideal: R Markdown or Quarto document that generates the paper by running the analysis inline
 - Results in the paper update automatically when data or code changes
 - Eliminates copy-paste errors between analysis output and paper text

Return: directory structure for my project, README template, dependency setup instructions, and coding standards checklist. 
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

The AI should return a structured result that covers the main requested outputs, such as What is a research compendium:, Recommended directory structure:, README content requirements:. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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
