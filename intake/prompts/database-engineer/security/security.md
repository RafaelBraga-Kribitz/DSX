# Security *AI Prompts *

2 Database Engineer prompts in Security. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Security 
2 prompts Intermediate Single prompt 01 
### Database Security Hardening 

Harden this database deployment against common security threats. Database: {{database}} Environment: {{environment}} (cloud, on-premise, containerized) Compliance: {{compliance}... 
Prompt text Harden this database deployment against common security threats.

Database: {{database}}
Environment: {{environment}} (cloud, on-premise, containerized)
Compliance: {{compliance}} (SOC 2, HIPAA, PCI-DSS, GDPR)

1. Authentication:
 - Disable password authentication over TCP; use certificate-based or IAM authentication
 - PostgreSQL: configure pg_hba.conf to require scram-sha-256 (not md5) for all connections
 - Require TLS for all connections: ssl = on; ssl_cert_file; ssl_key_file
 - Rotate database passwords on a schedule (90 days maximum)

2. Least-privilege role model:
 - Application user: SELECT/INSERT/UPDATE/DELETE on specific schemas only; no DDL
 - Read-only user: SELECT only on production tables (for reporting tools)
 - Migration user: DDL rights only during deployment windows; revoke after
 - DBA user: full access; requires MFA; every action logged

 CREATE ROLE app_user LOGIN PASSWORD '...';
 GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
 REVOKE ALL ON ALL TABLES IN SCHEMA pg_catalog FROM app_user;

3. Network security:
 - Database not reachable from the public internet: place in a private subnet
 - Firewall rule: only application servers and VPN hosts can reach the database port
 - VPC/network-level isolation: separate database VPC from web tier

4. Encryption:
 - In-transit: TLS required for all connections (no cleartext allowed)
 - At-rest: OS-level encryption (dm-crypt/LUKS, cloud-provider disk encryption)
 - Column-level: for PII columns, consider pgcrypto or application-level encryption
 pgp_sym_encrypt(ssn::text, key) AS encrypted_ssn

5. Audit logging:
 - pgaudit extension: logs all DDL and DML at the statement level
 - log_statement = 'ddl': log all DDL even without pgaudit
 - Ship logs to SIEM (Splunk, Elastic) for anomaly detection
 - Alert on: login failures, privilege escalation, bulk SELECT on sensitive tables

6. SQL injection prevention:
 - Always use parameterized queries in the application — never string interpolation
 - Row-level security (RLS): enforce multi-tenant data isolation at the database level

Return: pg_hba.conf config, role hierarchy DDL, network security rules, encryption approach, and audit log configuration. Copy prompt Open prompt details Advanced Single prompt 02 
### Row-Level Security and Data Access Control 

Implement row-level security (RLS) and fine-grained data access control for this multi-tenant or sensitive data use case. Use case: {{use_case}} (multi-tenant SaaS, per-departme... 
Prompt text Implement row-level security (RLS) and fine-grained data access control for this multi-tenant or sensitive data use case.

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

Return: RLS policy DDL for each role and use case, column masking approach, index requirements, and performance validation queries. Copy prompt Open prompt details 
## Recommended Security workflow 
1 
### Database Security Hardening 

Start with a focused prompt in Security so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Row-Level Security and Data Access Control 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
