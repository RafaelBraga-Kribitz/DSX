# Process Analysis *AI Prompts *

9 Business Analyst prompts in Process Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 8 single prompts · 1 chain. 

## AI prompts in Process Analysis 
9 prompts Intermediate Single prompt 01 
### Automation Opportunity Scan 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It evaluates which process steps are the best candidates for automation and why. 
Prompt text Scan this process for automation opportunities and build an automation prioritization plan.

Process description and step data provided.

For each process step, evaluate automation potential:
1. Rule-based: is the logic clear, consistent, and documentable? (High automation potential)
2. Volume: how many times per day/week is this step executed? (Higher volume = higher ROI)
3. Frequency of exceptions: how often does the step require human judgment? (High exceptions = lower automation potential)
4. Data availability: is the input data digital and structured? (Yes = automatable, No = requires data capture first)
5. Regulatory risk: are there compliance reasons a human must be in the loop?

Score each step: Automation Potential (High/Medium/Low) and Automation ROI (High/Medium/Low)

For high-potential steps, specify:
- Recommended automation type: RPA, workflow automation, API integration, ML model, or full end-to-end BPA
- Estimated time savings per week
- Implementation effort in person-days
- Payback period

Return: automation opportunity matrix, prioritized automation roadmap, and estimated total time savings. Copy prompt Open prompt details Beginner Single prompt 02 
### Bottleneck Identification 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It finds the process step that most constrains flow and prioritizes fixes based on business impact. 
Prompt text Identify and prioritize the bottlenecks in this business process using the data provided.

A bottleneck is a step where work accumulates, throughput is constrained, or cycle time is disproportionately long.

1. For each process step, analyze:
 - Average cycle time (how long does this step take?)
 - Wait time before this step (how long does work sit waiting to be processed?)
 - Volume (how many units pass through this step per day/week?)
 - Error rate and rework rate at this step
 - Utilization rate of the resource at this step (% of time actively working)

2. Calculate total cycle time vs total value-add time: what % of end-to-end time actually adds value?

3. Apply the Theory of Constraints: identify the single biggest constraint. Everything else is secondary until this is resolved.

4. For each bottleneck identified:
 - Root cause: is it a people, process, system, or data problem?
 - Business impact: what is the cost of this bottleneck in time, money, or customer experience?
 - Recommended fix: quick win vs longer-term solution

Return: bottleneck analysis table, constraint identification, and prioritized improvement actions. Copy prompt Open prompt details Advanced Chain 03 
### Process Improvement Chain 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It links process documentation, measurement, diagnosis, redesign, and business case into one improvement package. 
Prompt text Step 1: Document the current state — map the as-is process, capturing every step, actor, system, cycle time, and handoff.
Step 2: Measure performance — quantify the current process: total lead time, value-add percentage, error rate, cost per unit, and customer satisfaction score if available.
Step 3: Analyze waste and bottlenecks — identify the top 3 waste categories (Lean 8 wastes) and the single biggest bottleneck using Theory of Constraints.
Step 4: Root cause analysis — for each major bottleneck and waste source, apply Five Whys to identify the underlying root cause.
Step 5: Design the future state — propose a redesigned process that eliminates identified waste. Calculate the new expected performance metrics.
Step 6: Build the business case — quantify the value of the improvement: cost savings, time savings, error reduction, and customer impact. Calculate ROI.
Step 7: Write the improvement proposal: executive summary, current vs future state comparison, business case, implementation plan, risks, and success metrics. Copy prompt Open prompt details Beginner Single prompt 04 
### Process Map 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It documents a business process in a structured, role-based format that is easy to review and improve. 
Prompt text Create a structured process map for: {{process_name}}

Based on the provided process description or interview notes:

1. Document the process in a standard swim-lane format:
 - Identify the actors/roles involved (each gets a swim lane)
 - List each step in sequence
 - Show decision points (diamonds) with Yes/No branches
 - Show where inputs enter and outputs leave the process
 - Show system touchpoints at each step

2. Since this is text-based, represent the process map as:
 - A numbered step list with the actor, action, system, and decision/output for each step
 - Indented sub-steps for branches

3. Add metadata per step:
 - Average time to complete
 - Who is responsible (RACI: Responsible, Accountable, Consulted, Informed)
 - System or tool used
 - Common errors or exceptions

4. Summarize: total end-to-end time, total number of handoffs, and total number of decision points

Return: structured process map, step metadata table, and summary statistics. Copy prompt Open prompt details Advanced Single prompt 05 
### Process Redesign Proposal 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It proposes a future-state process that reduces waste, time, cost, or errors within real constraints. 
Prompt text Design a redesigned future-state version of this process based on the pain points identified.

Current process summary: {{current_process}}
Key pain points: {{pain_points}}
Design constraints: {{constraints}}

1. Define the redesign objectives:
 - Target cycle time reduction: X%
 - Target error rate reduction: X%
 - Target cost reduction: X%
 - Any regulatory or compliance constraints to maintain

2. Apply redesign principles:
 - Eliminate: which steps add no value and can be removed entirely?
 - Automate: which steps are repetitive, rules-based, and suitable for automation?
 - Simplify: which steps can be condensed or combined?
 - Parallelize: which sequential steps could run simultaneously?
 - Empower: where could decisions be pushed down to reduce handoffs?

3. Document the redesigned process:
 - Step-by-step description of the future state
 - New cycle time and wait time estimates per step
 - New process efficiency calculation

4. Implementation plan:
 - Quick wins (implement in <2 weeks)
 - Medium-term changes (1–3 months)
 - Long-term changes (3–12 months, may require technology)

5. Risk assessment: what could go wrong with this redesign?

Return: future state process map, efficiency comparison table, and phased implementation plan. Copy prompt Open prompt details Intermediate Single prompt 06 
### RACI Matrix Builder 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It clarifies who does the work, who owns the result, and where accountability gaps exist. 
Prompt text Build a RACI matrix for the process or project: {{process_or_project}}

RACI definitions:
- R (Responsible): does the work
- A (Accountable): owns the outcome, approves deliverables. Only one A per task.
- C (Consulted): provides input before the task is done
- I (Informed): notified after the task is done

1. List all tasks or decisions in the process as rows
2. List all roles (not people) involved as columns
3. For each task × role intersection, assign R, A, C, I, or blank

4. Check for RACI anti-patterns and flag:
 - Multiple A for a single task: accountability ambiguity — assign one owner
 - No R for a task: who is actually doing this work?
 - R without A: work with no accountability — add an owner
 - Too many C or I on one task: decision-making will be slow — trim the list
 - A role with no tasks: are they needed?

5. Highlight the top 3 process risks revealed by the RACI analysis

Return: formatted RACI matrix, anti-pattern flags with recommended fixes, and process risk summary. Copy prompt Open prompt details Intermediate Single prompt 07 
### Root Cause Analysis 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It uses proven problem-solving methods to move from symptoms to a changeable root cause. 
Prompt text Conduct a structured root cause analysis (RCA) for this problem: {{problem_statement}}

Use the following structured approach:

1. Problem definition:
 - What exactly happened? (Specific, measurable)
 - When did it start? Is it recurring?
 - What is the business impact? (Quantify: cost, time, customer impact)

2. Five Whys analysis:
 - Why did the problem occur? [Answer 1]
 - Why did [Answer 1] occur? [Answer 2]
 - Continue until you reach the root cause (usually 4–6 levels deep)
 - Stop when the answer is a system, process, or policy that can be changed

3. Fishbone (Ishikawa) analysis:
 - Categorize potential causes under: People, Process, Technology, Data, Environment
 - For each category, list 2–3 contributing factors
 - Mark which are confirmed, suspected, or ruled out

4. Root cause confirmation:
 - Which cause, if fixed, would prevent the problem from recurring?
 - What evidence supports this as the root cause?

5. Corrective actions:
 - Immediate containment: stop the bleeding now
 - Root cause fix: prevent recurrence
 - Systemic improvement: prevent similar problems elsewhere

Return: Five Whys chain, fishbone diagram (text format), confirmed root cause, and action plan. Copy prompt Open prompt details Intermediate Single prompt 08 
### SLA Compliance Analysis 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It shows whether service targets are being met, where breaches cluster, and what the business impact is. 
Prompt text Analyze SLA (Service Level Agreement) compliance for this process or service using the data provided.

1. Define the SLAs being measured:
 - SLA name, target threshold, measurement method, and business impact of breach

2. Calculate compliance rates:
 - Overall SLA compliance %
 - Compliance trend: is it improving or deteriorating over time?
 - Compliance by: time period, team, region, request type, priority level

3. Analyze breaches:
 - How many SLA breaches occurred?
 - Average and maximum breach duration
 - Distribution of breach severity (minor: <10% over SLA, moderate: 10–50%, severe: >50%)

4. Identify breach patterns:
 - What day of week or time of day do breaches cluster?
 - Are certain request types or teams responsible for the majority of breaches?
 - Is there a correlation between request volume and breach rate?

5. Root cause the top 3 breach drivers

6. Calculate the business impact of non-compliance:
 - Penalty costs if applicable
 - Customer satisfaction impact
 - Estimated revenue at risk

Return: compliance dashboard, breach analysis, pattern analysis, and improvement recommendations. Copy prompt Open prompt details Intermediate Single prompt 09 
### Value Stream Mapping 

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It separates value-adding work from waste so the team can redesign the process around flow and efficiency. 
Prompt text Create a value stream map for the process: {{process_name}}

Value stream mapping distinguishes between value-adding and non-value-adding steps to identify waste.

1. Map the current state:
 - List every step from trigger to final output
 - For each step, classify:
 - Value-adding (VA): customer would pay for this step
 - Non-value-adding but necessary (NNVA): required by regulation, system constraint, etc.
 - Pure waste (NVA): adds no value and can be eliminated
 - Record cycle time and wait time per step

2. Calculate waste metrics:
 - Total lead time (end-to-end)
 - Total value-adding time
 - Process efficiency = VA time / Total lead time × 100%
 - Typical processes are 5–15% efficient — how does this one compare?

3. Identify the 8 Lean wastes present:
 Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra-processing

4. Design the future state:
 - Eliminate or reduce the top 3 waste categories
 - What would the process look like without those wastes?
 - What would the new process efficiency be?

Return: current state VSM table, waste inventory, process efficiency metrics, and future state design. Copy prompt Open prompt details 
## Recommended Process Analysis workflow 
1 
### Automation Opportunity Scan 

Start with a focused prompt in Process Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Bottleneck Identification 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Process Improvement Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Process Map 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
