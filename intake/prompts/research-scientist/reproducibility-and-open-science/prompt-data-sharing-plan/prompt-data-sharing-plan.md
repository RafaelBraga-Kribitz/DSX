# Data Sharing Plan *AI Prompt *

Help me create a data sharing plan that maximizes openness while addressing legal, ethical, and practical constraints. Data type: {{data_type}} Participant population: {{populat... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me create a data sharing plan that maximizes openness while addressing legal, ethical, and practical constraints.

Data type: {{data_type}}
Participant population: {{population}}
Funder requirements: {{funder}} (e.g. NIH, NSF, Wellcome Trust, EU Horizon)
Journal requirements: {{journal}}

1. Determine the appropriate level of data sharing:

 Fully open (preferred when possible):
 - Data deposited in a public repository with no access controls
 - Appropriate when: data contains no identifying information and poses no re-identification risk
 - Repositories: OSF, Zenodo, Figshare, domain-specific repositories (ICPSR, UKDA, GenBank, etc.)

 Restricted access:
 - Data available to qualified researchers upon request or through an application process
 - Appropriate when: data contains sensitive information but de-identification is not sufficient
 - Repositories: UKDA, ICSPR Restricted Access, institutional data repository

 Available on request:
 - Data available by contacting the authors
 - Least preferred: frequently data becomes unavailable after author changes institution
 - Appropriate only when: repository deposit is genuinely not possible

 Not shared:
 - Appropriate only when: legal or ethical prohibitions exist (classified data, legally protected patient records)
 - Must provide a clear statement of why data cannot be shared

2. De-identification requirements:
 - Apply Safe Harbor method (HIPAA): remove the 18 specified identifiers
 - Apply Expert Determination: a qualified expert certifies re-identification risk is very small
 - For small or unusual populations: even 'de-identified' data may be re-identifiable — consider restricted access
 - Synthetic data: generate synthetic data that preserves statistical properties without individual records

3. Metadata and documentation:
 - Data without documentation is nearly unusable
 - Provide: a codebook for every variable (name, label, values, missing codes), a data collection instrument, and a processing log describing all transformations from raw to analysis-ready data

4. Consent language (for future studies):
 - Consent forms should include explicit language about data sharing
 - Recommended language: 'De-identified data from this study may be shared with other researchers via a secure repository to enable verification of results and future research.'

5. Funder-specific requirements:
 - NIH: Data Management and Sharing Plan required for all funded studies
 - NSF: similar requirements, check program-specific guidance
 - EU Horizon: 'open by default' requirement with possibility of exceptions
 Write the data management plan text appropriate for {{funder}}.

Return: data sharing recommendation, de-identification procedure, repository selection, metadata checklist, and data management plan text for the funder. 
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

The AI should return a structured result that covers the main requested outputs, such as Determine the appropriate level of data sharing:, Data deposited in a public repository with no access controls, Appropriate when: data contains no identifying information and poses no re-identification risk. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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
