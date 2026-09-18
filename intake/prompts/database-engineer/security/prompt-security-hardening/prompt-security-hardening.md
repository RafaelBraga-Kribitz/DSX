# Database Security Hardening *AI Prompt *

Harden this database deployment against common security threats. Database: {{database}} Environment: {{environment}} (cloud, on-premise, containerized) Compliance: {{compliance}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Harden this database deployment against common security threats.

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

Return: pg_hba.conf config, role hierarchy DDL, network security rules, encryption approach, and audit log configuration. 
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

The AI should return a structured result that covers the main requested outputs, such as Authentication:, Disable password authentication over TCP; use certificate-based or IAM authentication, PostgreSQL: configure pg_hba.conf to require scram-sha-256 (not md5) for all connections. The final answer should stay clear, actionable, and easy to review inside a security workflow for database engineer work. 

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
