# Marketing Analytics Stack Audit *AI Prompt *

Audit the marketing analytics stack for this organization and identify gaps, redundancies, and improvement opportunities. Current tools: {{tools_list}} Data flows: {{data_flows}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit the marketing analytics stack for this organization and identify gaps, redundancies, and improvement opportunities.

Current tools: {{tools_list}}
Data flows: {{data_flows}}
Team capability: {{team_capability}}

1. Analytics stack layers:
 Map the current stack against these layers:
 - Data collection: (pixels, SDKs, server-side tagging, webhooks)
 - Data transport: (tag management, event streaming, APIs)
 - Data storage: (data warehouse, CDP, CRM, platform-native storage)
 - Data transformation: (dbt, Fivetran, custom ETL)
 - Analytics and reporting: (BI tool, platform dashboards, spreadsheets)
 - Activation: (email platform, ad platforms, personalization engine)

2. Data quality assessment per layer:
 - Collection: are all key events tracked? Are there data gaps?
 - Storage: is there a single source of truth or multiple conflicting sources?
 - Transformation: is business logic documented and version-controlled?
 - Reporting: do different teams use different definitions for the same metric?

3. Redundancy identification:
 - Are multiple tools doing the same job? (Two CDPs, two email platforms)
 - Can any tools be consolidated without loss of capability?
 - What is the total annual cost of the current stack?

4. Critical gaps:
 - Multi-touch attribution: is there a cross-channel attribution solution beyond platform-reported ROAS?
 - Customer identity resolution: can you link the same person across devices and channels?
 - Offline-to-online: is offline (store, call center) data connected to digital behavior?
 - Incrementality measurement: is there any program to measure true causal marketing impact?

5. Priority improvements:
 - Top 3 gaps with highest impact on marketing decision quality
 - For each: recommended solution, estimated implementation effort, expected ROI

6. Data governance:
 - Is there a marketing data dictionary? (Agreed definitions for all metrics)
 - Who owns each data source and is responsible for its quality?

Return: stack layer map, quality assessment, redundancy analysis, critical gaps, priority improvements, and governance recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin web and digital analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Web and Digital Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Analytics stack layers:, Data collection: (pixels, SDKs, server-side tagging, webhooks), Data transport: (tag management, event streaming, APIs). The final answer should stay clear, actionable, and easy to review inside a web and digital analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Web and Digital Analytics.
