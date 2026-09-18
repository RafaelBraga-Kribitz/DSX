# Multi-Tenancy Patterns *AI Prompt *

Design a multi-tenancy data isolation strategy for this SaaS application. Isolation requirement: {{isolation}} (full isolation / logical isolation / row-level) Expected tenants:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a multi-tenancy data isolation strategy for this SaaS application.

Isolation requirement: {{isolation}} (full isolation / logical isolation / row-level)
Expected tenants: {{tenant_count}}
Tenant size variation: {{size_variation}} (all small / some enterprise / highly variable)
Database: {{database}}

1. Multi-tenancy patterns:

 Pattern A — Separate database per tenant:
 - Maximum isolation: each tenant has their own database instance
 - Pros: complete data isolation, independent backups, custom configurations per tenant
 - Cons: expensive (one DB instance per tenant), complex management at scale
 - Use for: high-compliance tenants (financial, healthcare), large enterprise customers

 Pattern B — Separate schema per tenant:
 - Each tenant gets a PostgreSQL schema within a shared database
 - Each schema has identical table structures
 - search_path = tenant_xyz_schema; routes queries to the right schema
 - Pros: strong logical isolation, easy schema-level backup, easier to customize per tenant
 - Cons: schema proliferation beyond ~1000 schemas becomes slow

 Pattern C — Row-level security (shared tables):
 - All tenants share the same tables; a tenant_id column identifies rows
 - PostgreSQL Row Level Security enforces isolation at the database level
 - Pros: simple schema, scales to millions of tenants, efficient
 - Cons: a bug in the RLS policy could expose cross-tenant data

2. Row-Level Security implementation:
 ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

 CREATE POLICY tenant_isolation ON orders
 USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

 -- Set in the application before every query:
 SET app.current_tenant_id = 'tenant-uuid-here';

3. Hybrid approach:
 - Free tier / SMB: shared tables with RLS (Pattern C)
 - Enterprise / high-compliance: dedicated schema or database (Pattern A or B)
 - Migrate enterprise tenants to dedicated instances on request

4. Index strategy for shared tables:
 - Always include tenant_id as the first column of every index
 - CREATE INDEX ON orders (tenant_id, created_at);
 - Without this, queries for one tenant scan all tenants' data

Return: pattern recommendation, RLS policy DDL, index strategy, and hybrid architecture for mixed tenant tiers. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin schema design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Schema Design or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Multi-tenancy patterns:, Maximum isolation: each tenant has their own database instance, Pros: complete data isolation, independent backups, custom configurations per tenant. The final answer should stay clear, actionable, and easy to review inside a schema design workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Schema Design.
