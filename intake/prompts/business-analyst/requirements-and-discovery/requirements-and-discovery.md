# Requirements and Discovery *AI Prompts *

8 Business Analyst prompts in Requirements and Discovery. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain. 

## AI prompts in Requirements and Discovery 
8 prompts Intermediate Single prompt 01 
### As-Is Process Interview Guide 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It creates a practical interview script for uncovering how a process really works, including pain points and volume questions. 
Prompt text Create a structured interview guide for a business process discovery session.

Process to document: {{process_name}}
Interviewee role: {{role}}

The guide should include:

1. Opening questions (context setting):
 - What is your role in this process?
 - How long have you been doing this? Has the process changed?

2. Process flow questions:
 - Walk me through each step from start to finish
 - What triggers this process to begin?
 - What inputs do you need before you can start?
 - What systems, tools, or data do you use at each step?
 - Who else is involved and at what points?
 - What is the output or outcome at the end?

3. Pain point questions:
 - Where does this process slow down or get stuck?
 - What steps feel unnecessary or repetitive?
 - What errors or exceptions happen most often?
 - What would you change if you could?

4. Volume and frequency questions:
 - How many times per day/week does this process run?
 - How long does each step take?
 - Are there peak periods?

5. Wrap-up:
 - Who else should I speak with about this process?
 - Is there documentation I should review?

Return the full interview guide formatted as a printable document with space for notes after each question. Copy prompt Open prompt details Advanced Single prompt 02 
### Business Rules Extraction 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It surfaces the rules, policies, and constraints hidden in documents, datasets, or existing processes. 
Prompt text Extract and catalog all business rules from this dataset, document, or process description: {{source}}

A business rule is a specific, actionable constraint, condition, or policy that governs business behavior.

1. Identify and classify each rule by type:
 - Constraint rules: 'A customer must have an active account to place an order'
 - Derivation rules: 'Loyalty tier is Gold if annual spend > $5,000'
 - Inference rules: 'If a customer has 3 late payments, flag account for review'
 - Timing rules: 'Invoices must be paid within 30 days of issue'

2. For each rule write:
 - Rule ID (BR-001)
 - Rule statement in plain English
 - Rule type
 - Source (policy document, legal requirement, historical practice)
 - Current enforcement method (manual check, system validation, not enforced)
 - Business impact if rule is violated
 - Exceptions to the rule

3. Flag rules that are ambiguous, conflicting, or out of date
4. Identify rules that should be automated but are currently manual

Return: business rules catalog and a list of automation candidates. Copy prompt Open prompt details Intermediate Single prompt 03 
### Feasibility Assessment 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It gives a balanced view of whether an initiative is realistic across technical, operational, financial, and timeline dimensions. 
Prompt text Assess the feasibility of the proposed solution or initiative: {{initiative_description}}

Evaluate across four dimensions:

1. Technical feasibility:
 - Does the required technology exist and is it mature?
 - Can existing systems support this, or is new infrastructure needed?
 - What are the technical risks and unknowns?

2. Operational feasibility:
 - Does the organization have the skills and capacity to implement and run this?
 - What change management or training is required?
 - How disruptive is this to existing operations?

3. Financial feasibility:
 - Estimate the order-of-magnitude cost (implementation, licensing, ongoing)
 - Estimate the expected benefit (revenue increase, cost reduction, risk reduction)
 - Simple ROI: (benefit - cost) / cost × 100 — is it positive within {{timeframe}}?

4. Schedule feasibility:
 - Is the proposed timeline realistic given scope and resources?
 - What are the critical path items?
 - What is the risk of delay?

Return: feasibility scorecard (Red / Amber / Green per dimension), overall feasibility verdict, top 3 risks, and recommended next steps. Copy prompt Open prompt details Advanced Chain 04 
### Full Discovery Chain 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It combines the main discovery activities into one end-to-end workflow, from stakeholder analysis through requirements and summary. 
Prompt text Step 1: Stakeholder analysis — identify all stakeholders, their influence/interest levels, primary concerns, and engagement strategy.
Step 2: Current state documentation — describe the as-is process, systems, data flows, and pain points based on the provided inputs.
Step 3: Future state vision — define the desired outcomes, success criteria, and high-level capabilities needed.
Step 4: Gap analysis — identify the gaps between current and future state, scored by impact and effort.
Step 5: Requirements extraction — convert gaps and stakeholder needs into structured business and functional requirements with MoSCoW priorities.
Step 6: Risks and assumptions — list the top 5 risks to successful delivery and the key assumptions being made. For each risk: likelihood, impact, and mitigation strategy.
Step 7: Discovery summary — write a 1-page discovery report: problem statement, proposed solution direction, requirements summary, open questions, and recommended next steps. Copy prompt Open prompt details Intermediate Single prompt 05 
### Gap Analysis 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It compares current capabilities with a desired future state so teams can see what must change and what can wait. 
Prompt text Conduct a gap analysis between the current state and the desired future state.

Current state: {{current_state_description}}
Desired future state: {{future_state_description}}

1. Map the current capabilities, processes, and systems in a structured list
2. Map the required capabilities, processes, and systems for the future state
3. Identify gaps: what is missing, inadequate, or needs replacement?
4. For each gap:
 - Gap description
 - Business impact if gap is not closed (High / Medium / Low)
 - Effort to close (High / Medium / Low)
 - Options to close it: build, buy, partner, or process change
 - Recommended approach with rationale
5. Create a gap prioritization matrix: plot gaps by impact vs effort
6. Identify quick wins: high impact, low effort gaps that can be closed immediately

Return: current vs future state comparison table, gap register, prioritization matrix, and recommended sequencing. Copy prompt Open prompt details Beginner Single prompt 06 
### Requirements Extraction 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It is especially useful for turning raw notes into traceable requirements with priorities, sources, and open questions. 
Prompt text Extract and structure the business requirements from the following input: {{input}} (meeting notes, email thread, or stakeholder interview transcript).

1. Identify and separate:
 - Business requirements: what the business needs to achieve (outcomes)
 - Functional requirements: what the system or process must do
 - Non-functional requirements: performance, security, compliance constraints
 - Out of scope: what was explicitly excluded

2. For each requirement write:
 - Unique ID (BR-001, FR-001, etc.)
 - Clear one-sentence statement in the format: 'The system/process shall [action] so that [business outcome]'
 - Priority: Must Have / Should Have / Nice to Have (MoSCoW)
 - Source: who requested it
 - Open questions that need clarification before this requirement can be finalized

3. Flag any conflicting requirements between stakeholders

Return a structured requirements table and a list of open questions to resolve in the next session. Copy prompt Open prompt details Beginner Single prompt 07 
### Stakeholder Mapping 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It helps reveal who matters most, what they care about, and how they should be engaged throughout delivery. 
Prompt text Create a stakeholder map for this project or initiative based on the context provided.

1. Identify all stakeholders mentioned or implied, including:
 - Internal: business units, leadership, IT, operations, finance, legal, compliance
 - External: customers, regulators, vendors, partners

2. For each stakeholder, define:
 - Name / role / department
 - Level of influence on the project (High / Medium / Low)
 - Level of interest in the project (High / Medium / Low)
 - Primary concern or motivation
 - Preferred communication style and frequency
 - Potential objections or resistance

3. Place stakeholders into the classic 2×2 grid:
 - Manage closely (High influence, High interest)
 - Keep satisfied (High influence, Low interest)
 - Keep informed (Low influence, High interest)
 - Monitor (Low influence, Low interest)

4. Recommend an engagement strategy for the top 5 most critical stakeholders

Return the stakeholder table, grid placement, and engagement recommendations. Copy prompt Open prompt details Beginner Single prompt 08 
### User Story Writer 

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It converts broad requirements into delivery-ready user stories with acceptance criteria, dependencies, and sizing. 
Prompt text Convert these business requirements into well-formed user stories with acceptance criteria.

Requirements input: {{requirements}}

For each user story:
1. Write in standard format: 'As a [user type], I want [action] so that [benefit]'
2. Add a clear, specific title (5 words max)
3. Write 3–5 acceptance criteria in Given-When-Then (GWT) format:
 - Given [context/precondition]
 - When [action is taken]
 - Then [expected outcome]
4. Assign a story point estimate using Fibonacci scale (1, 2, 3, 5, 8, 13) based on complexity
5. Flag any story that is too large to complete in one sprint (>8 points) and suggest how to split it
6. Identify dependencies between stories

Return: formatted user story cards, dependency map, and a prioritized backlog order based on business value and dependencies. Copy prompt Open prompt details 
## Recommended Requirements and Discovery workflow 
1 
### As-Is Process Interview Guide 

Start with a focused prompt in Requirements and Discovery so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Business Rules Extraction 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Feasibility Assessment 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Full Discovery Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
