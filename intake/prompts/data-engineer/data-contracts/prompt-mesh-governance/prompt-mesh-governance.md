# Data Mesh Contract Governance *AI Prompt *

This prompt designs governance for data contracts in a data mesh where many domain teams publish their own data products. It helps define ownership, standards, enforcement, discoverability, and dispute handling without creating a central bottleneck. The answer should balance autonomy with enough consistency to keep the ecosystem reliable. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a data contract governance model for a data mesh architecture with {{num_domains}} domain teams.

In a data mesh, domain teams own and publish their own data products. Contracts are the mechanism that makes data products reliable and trustworthy.

1. Contract ownership model:
 - Producer team: responsible for defining the contract, meeting the commitments, and handling breaking changes
 - Consumer teams: responsible for registering as consumers and migrating when notified
 - Data platform team: responsible for tooling, enforcement, and governance process
 - No central team should approve every contract — this creates bottlenecks

2. Contract registry:
 - Centralized catalog of all published contracts (not a bottleneck — just a registry)
 - Each contract: schema, SLA, consumers, version history, compliance status
 - Automatic registration when a producer publishes a new dataset

3. Automated enforcement:
 - CI/CD check: new data publication must include a valid contract
 - Automated compatibility check: new schema version must be compatible with current contract
 - Consumer registration: consumers must register in the contract registry to receive change notifications
 - SLA monitoring: automated checks run against every published contract

4. Cross-domain standards (things that must be consistent across all domains):
 - Common entity IDs (customer_id must mean the same thing everywhere)
 - Standard date/time formats and timezone
 - PII classification and handling
 - Minimum required fields in every contract

5. Dispute resolution:
 - Process for when a producer cannot meet a consumer's requirements
 - Escalation path for unresolved contract disputes
 - SLA breach accountability and remediation

6. Discoverability:
 - Data product catalog: searchable, showing all published contracts, quality scores, and consumer counts
 - Quality score per data product: based on SLA compliance, test pass rate, consumer satisfaction

Return: governance model document, contract registry schema, enforcement automation design, and cross-domain standards. 
```

## When to use this prompt 
Use case 01 
When implementing contract governance across many domain teams. 
Use case 02 
When building a data mesh operating model. 
Use case 03 
When producer and consumer responsibilities need formal definition. 
Use case 04 
When automated enforcement and catalog discoverability are required. 

## What the AI should return 

Return a governance model document, registry schema, automation design, and cross-domain standards. Explain ownership for producer teams, consumer registration, and platform enforcement responsibilities. Include dispute-resolution and discoverability mechanisms so the response can serve as a governance blueprint. 

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

Once you have the first result, continue deeper with related prompts in Data Contracts.
