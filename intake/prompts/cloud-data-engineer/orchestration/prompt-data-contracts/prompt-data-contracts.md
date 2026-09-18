# Data Contracts and SLA Management *AI Prompt *

Implement data contracts and SLA management for data products in this cloud platform. Data producers: {{producers}} Data consumers: {{consumers}} Current issues: {{issues}} (sch... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement data contracts and SLA management for data products in this cloud platform.

Data producers: {{producers}}
Data consumers: {{consumers}}
Current issues: {{issues}} (schema breaking changes, missed SLAs, undocumented changes)

1. What is a data contract:
 A data contract is a formal agreement between a data producer (team that writes the data) and data consumers (teams that read it). It specifies:
 - Schema: column names, types, and semantic meaning
 - Quality: expected null rates, value distributions, referential integrity
 - SLA: freshness (max hours since last update), availability (uptime %)
 - Versioning: how schema changes are communicated and backward compatibility

2. Data contract specification (YAML):
 apiVersion: v1
 kind: DataContract
 id: orders.v1
 producer: payments-team
 owner: payments-data@company.com
 schema:
 - name: order_id
 type: bigint
 nullable: false
 unique: true
 - name: amount_usd
 type: numeric(10,2)
 nullable: false
 minimum: 0
 sla:
 freshness_hours: 2
 availability_percent: 99.5
 versioning:
 current: 1.2.0
 breaking_change_policy: 30-day notice required

3. Tooling:
 - Data Contract CLI (open-source): validate data against contracts, publish to catalog
 - Soda Core: run quality checks defined in contracts
 - dbt + Elementary: enforce schema contracts via model contracts; test quality via tests

4. SLA monitoring:
 - Freshness check: query MAX(updated_at) per table; alert if > SLA threshold
 - Availability: monitor pipeline success rate; alert on consecutive failures
 - Quality score: % of tests passing per data product; publish in the catalog
 - SLA breach report: weekly report of SLA breaches per team, with trend

5. Governance process:
 - Contract registration: new data products must register a contract before GA
 - Breaking change process: 30-day notice + migration guide for all consumers
 - Deprecation: deprecated products sunset after 90 days with active consumer notification

Return: data contract YAML schema, tooling recommendation, SLA monitoring implementation, and governance process. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin orchestration work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Orchestration or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What is a data contract:, Schema: column names, types, and semantic meaning, Quality: expected null rates, value distributions, referential integrity. The final answer should stay clear, actionable, and easy to review inside a orchestration workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Orchestration.
