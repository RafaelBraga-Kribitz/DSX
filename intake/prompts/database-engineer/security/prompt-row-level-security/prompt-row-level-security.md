# Row-Level Security and Data Access Control *AI Prompt *

Implement row-level security (RLS) and fine-grained data access control for this multi-tenant or sensitive data use case. Use case: {{use_case}} (multi-tenant SaaS, per-departme... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement row-level security (RLS) and fine-grained data access control for this multi-tenant or sensitive data use case.

Use case: {{use_case}} (multi-tenant SaaS, per-department data, financial data with role-based access)
Database: {{database}}
Roles needed: {{roles}}

1. Enable and create RLS policies:
 ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
 ALTER TABLE orders FORCE ROW LEVEL SECURITY; -- applies to table owners too

 Tenant isolation policy:
 CREATE POLICY tenant_isolation ON orders
 FOR ALL
 TO app_user
 USING (tenant_id = current_setting('app.current_tenant')::UUID)
 WITH CHECK (tenant_id = current_setting('app.current_tenant')::UUID);

 USING: controls SELECT/UPDATE/DELETE visibility
 WITH CHECK: controls INSERT/UPDATE values (prevents writing to wrong tenant)

2. Role-based policies:
 -- Managers can see all orders; staff can only see their own
 CREATE POLICY manager_access ON orders
 FOR SELECT TO manager_role
 USING (TRUE);

 CREATE POLICY staff_access ON orders
 FOR SELECT TO staff_role
 USING (assigned_rep_id = current_user);

3. Sensitive column masking (alternative: column privileges):
 REVOKE SELECT ON employees FROM analyst_role;
 CREATE VIEW employees_masked AS
 SELECT employee_id, name, department,
 LEFT(salary::text, 2) || '***' AS salary_masked
 FROM employees;
 GRANT SELECT ON employees_masked TO analyst_role;

4. Audit logging with RLS:
 -- Log when RLS blocks a query (for compliance)
 CREATE EXTENSION IF NOT EXISTS pgaudit;
 SET pgaudit.log = 'read,write';

5. Performance impact:
 - RLS adds a predicate to every query (effectively a WHERE clause)
 - The predicate must use indexed columns to avoid full table scans
 - Always: CREATE INDEX ON orders (tenant_id) before enabling RLS
 - Test: verify EXPLAIN shows Index Scan with the RLS predicate applied

Return: RLS policy DDL for each role and use case, column masking approach, index requirements, and performance validation queries. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin security work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Security or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Enable and create RLS policies:, Role-based policies:, Sensitive column masking (alternative: column privileges):. The final answer should stay clear, actionable, and easy to review inside a security workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Security.
