# Data Vault Design *AI Prompt *

This prompt designs a Data Vault 2.0 model for integrating multiple source systems while preserving history and supporting scalable loading. It is useful when the integration problem is complex, source systems are heterogeneous, and auditability matters. The output should clearly separate Hubs, Links, Satellites, and optional Business Vault structures. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a Data Vault 2.0 model for integrating {{num_sources}} source systems on the entity: {{core_entity}}.

1. Hub table:
 - One Hub per core business entity (Customer, Product, Order, etc.)
 - Columns: hash_key (PK, SHA-256 of business key), business_key, load_date, record_source
 - No descriptive attributes — Hubs contain only the business key
 - Business key: the natural identifier used by the business (customer_id, order_number)
 - Hash key: deterministic hash of the business key — enables parallel loading without sequences

2. Satellite tables:
 - One or more Satellites per Hub, each containing descriptive attributes from one source
 - Columns: hash_key (FK to Hub), load_date, load_end_date (NULL = current), record_source, + descriptive columns
 - Split Satellites by: rate of change (fast-changing vs slow-changing attributes separate), source system, sensitivity level
 - load_end_date pattern: NULL for current record, populated when a new record supersedes it

3. Link tables:
 - Represent many-to-many relationships between Hubs
 - Columns: link_hash_key (PK), hash_key_hub_a (FK), hash_key_hub_b (FK), load_date, record_source
 - Never delete from Links — relationships are historical facts

4. Business Vault:
 - Computed Satellites: derived business rules applied on top of raw Vault
 - Bridge tables: pre-joined structures for performance
 - Point-in-time (PIT) tables: snapshot of active satellite records at each date — avoids complex timestamp joins in queries

5. Loading patterns:
 - Hubs: INSERT new business keys only (never update)
 - Satellites: INSERT new records; close previous record by setting load_end_date
 - Links: INSERT new relationships only
 - All loads are insert-only — no updates, no deletes

Return: Hub, Satellite, and Link DDLs, loading SQL for each component, and PIT table design. 
```

## When to use this prompt 
Use case 01 
When integrating multiple operational systems into a historical raw model. 
Use case 02 
When auditability and insert-only patterns are important. 
Use case 03 
When a Data Vault approach is being evaluated or implemented. 
Use case 04 
When you need DDL plus loading logic for Hubs, Links, and Satellites. 

## What the AI should return 

Return DDLs for Hubs, Satellites, and Links, along with loading SQL patterns and PIT-table design guidance. Explain how hash keys are created, how descriptive history is stored, and how relationships are modeled over time. Include practical notes on splitting satellites and supporting downstream query performance. 

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

Once you have the first result, continue deeper with related prompts in Data Warehouse Patterns.
