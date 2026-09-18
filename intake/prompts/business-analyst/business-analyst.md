# Business Analyst *AI Prompts *

Business Analyst AI prompt library with 50 prompts in 7 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 7 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Business Analyst prompt categories 
7 categories 
### KPI Design and Strategy 

AI prompts for KPI design, metric selection, performance tracking, goal alignment, and business strategy measurement. 
9 prompts KPI Framework Builder KPI Strategy Chain → 
### Process Analysis 

AI prompts for process analysis, identifying bottlenecks, workflow optimization, and improving operational efficiency. 
9 prompts Automation Opportunity Scan Bottleneck Identification → 
### AB Testing and Experimentation 

AI prompts for A/B testing, experiment design, hypothesis validation, statistical analysis, and interpreting results with business impact. 
8 prompts A/B Test Design Brief A/B Test Results Analysis → 
### Reporting and Dashboards 

AI prompts for dashboards, business reporting, executive summaries, visualization design, and recurring performance tracking. 
8 prompts Anomaly Narrative Writer Board-Level Report → 
### Requirements and Discovery 

AI prompts for requirements gathering, stakeholder interviews, scope definition, and problem discovery in data projects. 
8 prompts As-Is Process Interview Guide Business Rules Extraction → 
### Stakeholder Communication 

AI prompts for stakeholder communication, presenting insights, framing tradeoffs, and tailoring messages to different audiences. 
5 prompts Data Literacy Translation Difficult Data Conversation → 
### Business Case and Prioritization 

AI prompts for business case development, impact estimation, opportunity sizing, prioritization frameworks, and decision-making support. 
3 prompts Full Business Case Chain Prioritization Framework → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 50 KPI Design and Strategy 9 Process Analysis 9 AB Testing and Experimentation 8 Reporting and Dashboards 8 Requirements and Discovery 8 Stakeholder Communication 5 Business Case and Prioritization 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **50 **of 50 prompts 
## KPI Design and Strategy 
9 prompt s KPI Design and Strategy Beginner Prompt 01 
### KPI Framework Builder 
Design a KPI framework for {{business_area}} aligned to the strategic objective: {{strategic_objective}}

1. Define the measurement hierarchy:
 - Outcome KPIs (2–3): the ultimate business results we want to achieve
 - Driver KPIs (4–6): the leading indicators that predict and drive the outcomes
 - Activity metrics (6–8): the operational inputs we control directly

2. For each KPI define:
 - Name and plain-English definition
 - Formula or calculation method
 - Data source: where does the data come from?
 - Measurement frequency: daily / weekly / monthly
 - Owner: who is accountable?
 - Current baseline value (if known)
 - Target value and timeframe
 - Direction of improvement: higher is better / lower is better

3. Map the causal relationships: draw a simple KPI tree showing how activity metrics drive driver KPIs which drive outcome KPIs

4. Flag any KPI that cannot currently be measured (data gaps)

Return: KPI framework table, KPI tree diagram (text-based), and a data gap report. Copy prompt View page Show more ↓ KPI Design and Strategy Advanced Chain 02 
### KPI Strategy Chain 
Step 1: Align to strategy — map the business's stated strategic objectives to measurable outcomes. What does success look like in 12 months?
Step 2: Define the North Star Metric — identify the single metric that best captures customer value and predicts long-term business health.
Step 3: Build the metric tree — decompose the North Star into driver metrics and then into actionable input metrics. Map ownership at each level.
Step 4: Audit current metrics — review the existing KPI set against the new framework. Classify each as keep, modify, or retire.
Step 5: Fill gaps — identify business dimensions with no metric coverage. Propose new metrics with data source, owner, and measurement method.
Step 6: Set targets — for each metric in the final framework, set a baseline, a 12-month target, and an interim 90-day milestone.
Step 7: Write the KPI strategy document: one page covering — strategic alignment, NSM, metric framework summary, ownership table, targets, and reporting cadence. Copy prompt View page Show more ↓ KPI Design and Strategy Intermediate Template 03 
### KPI Target Setting 
Help set data-driven targets for the KPI: {{kpi_name}} for {{time_period}}.

Current performance data is provided. Use these four approaches and compare:

1. Historical trend extrapolation:
 - Fit a trend line to the last 12 months of data
 - Project forward to {{time_period}} end
 - Suggested target: trend projection + {{stretch_factor}}% improvement

2. Benchmarking:
 - Compare current performance to industry benchmarks (provide if known, otherwise note as assumption)
 - Target: close the gap to the industry median by 50% within {{time_period}}

3. Bottom-up driver modeling:
 - Identify the 2–3 key drivers of this KPI
 - Model the KPI impact of realistic improvements in each driver
 - Suggested target: sum of driver improvements

4. Top-down from business goal:
 - Start from the business revenue or growth target for {{time_period}}
 - Work backwards: what level of {{kpi_name}} is needed to achieve that goal?

Compare all four targets. Recommend a final target with rationale.
Return: target comparison table, recommended target, and confidence level (High / Medium / Low). Copy prompt View page Show more ↓ KPI Design and Strategy Advanced Prompt 04 
### Leading vs Lagging Indicators 
Classify and balance the KPI set for {{business_area}} into leading and lagging indicators.

KPI list: {{kpi_list}}

Definitions:
- Lagging indicator: measures what has already happened (outcome). Reliable but too late to act on. Example: monthly revenue, customer churn rate.
- Leading indicator: predicts what will happen (predictor). Actionable now but harder to measure. Example: NPS, pipeline coverage ratio, trial activation rate.

For each KPI:
1. Classify: Leading / Lagging / Mixed
2. Time lag: how far in advance does this metric predict or reflect business performance?
3. Reliability: how strongly correlated is this metric with the business outcome it's supposed to predict?

Then:
4. Assess balance: most teams over-index on lagging metrics. Is this set balanced?
5. For each lagging KPI, suggest a corresponding leading indicator
6. Identify the 2 leading indicators with the strongest predictive relationship to the most important outcome metric

Return: classification table, balance assessment, and leading/lagging pairs. Copy prompt View page Show more ↓ KPI Design and Strategy Advanced Prompt 05 
### Metric Decomposition Tree 
Build a full metric decomposition tree for the top-level metric: {{top_metric}}

A decomposition tree breaks a top-level metric into its component parts, making it possible to diagnose exactly which lever to pull when the metric moves.

1. Level 1 decomposition: break {{top_metric}} into its arithmetic components
 - Example: Revenue = Users × Conversion Rate × Average Order Value
2. Level 2 decomposition: break each Level 1 component further
 - Example: Users = New Users + Returning Users
3. Level 3 decomposition where meaningful
4. For each leaf node in the tree:
 - Current value (if available)
 - Which team or person owns it
 - How quickly it can realistically change
 - What specific actions move it
5. Identify which leaf nodes have the highest leverage — a 10% improvement in which node would move the top metric the most?
6. Identify which leaf nodes are currently unmeasured

Return: full decomposition tree (text format), leverage analysis table, and measurement gap list. Copy prompt View page Show more ↓ KPI Design and Strategy Intermediate Prompt 06 
### Metric Health Check 
Audit the existing KPI set for {{business_area}} and assess its health.

Existing KPIs: {{kpi_list}}

For each KPI, evaluate:
1. Relevance: does it still align to current business strategy? (Yes / Partially / No)
2. Actionability: if this metric moves, does the team know what to do? (High / Medium / Low)
3. Measurability: is it reliably measured with good data quality? (High / Medium / Low)
4. Frequency: is it measured and reviewed frequently enough to drive action?
5. Gaming risk: can someone make this metric look good without creating real value? (High / Medium / Low)
6. Overlap: is it redundant with another metric in the set?

After auditing each KPI:
- Recommend which KPIs to keep, modify, retire, or replace
- Identify any important business dimensions that have no KPI coverage
- Suggest the ideal total number of KPIs for this team (rule of thumb: 5–8 for a team, 3–5 for an individual)

Return: KPI health scorecard, recommended actions per KPI, and gaps in metric coverage. Copy prompt View page Show more ↓ KPI Design and Strategy Beginner Prompt 07 
### North Star Metric Definition 
Help define the North Star Metric (NSM) for this business or product: {{business_description}}

1. Explain what makes a good North Star Metric:
 - It measures value delivered to customers, not just revenue
 - It is a leading indicator of long-term growth
 - The whole company can influence it
 - It is a single number everyone understands

2. Propose 3 candidate North Star Metrics for this business, with for each:
 - Metric name and definition
 - Why it captures customer value
 - How it connects to revenue
 - How measurable it is today
 - Potential gaming risks (can it be gamed without delivering real value?)

3. Recommend the best candidate with a clear rationale

4. Define the input metrics (3–5) that the teams would manage to move the NSM

5. Write a one-paragraph NSM narrative: 'We grow revenue by doing X, which creates value for customers by Y, and our North Star Metric captures this by measuring Z.'

Return: candidate comparison table, recommended NSM, input metrics, and NSM narrative. Copy prompt View page Show more ↓ KPI Design and Strategy Intermediate Prompt 08 
### OKR Design 
Design a set of OKRs (Objectives and Key Results) for {{team_or_department}} for {{time_period}}.

Context: {{strategic_context}}

For each OKR:
1. Write the Objective: inspiring, qualitative, direction-setting. It should answer 'where do we want to go?'
2. Write 3–4 Key Results per objective:
 - Quantitative and measurable: must include a specific number
 - Outcome-focused, not activity-focused: 'Increase NPS from 32 to 45' not 'Run 10 customer surveys'
 - Ambitious but achievable: 70% achievement should feel like success
 - Time-bound: achievable within the OKR period
3. For each Key Result:
 - Current baseline value
 - Target value
 - Measurement method
 - Owner
4. Check OKR quality:
 - Do the Key Results, if all achieved, guarantee the Objective is met?
 - Are any Key Results actually activities or outputs rather than outcomes?
 - Do they connect to the company-level OKRs?

Return: formatted OKR set, quality check assessment, and an alignment map showing how these OKRs ladder up to company goals. Copy prompt View page Show more ↓ KPI Design and Strategy Intermediate Prompt 09 
### Vanity vs Actionable Metrics 
Review this list of metrics and classify each as a vanity metric or an actionable metric: {{metrics_list}}

Definitions:
- Vanity metric: looks impressive, grows over time, but doesn't tell you what to do or predict business success (e.g. total registered users, page views, app downloads)
- Actionable metric: directly tied to business outcomes, tells you what to do when it changes, and can be influenced by specific team actions (e.g. activation rate, revenue per user, week-2 retention)

For each metric:
1. Classification: Vanity / Actionable / Context-dependent
2. Why: one sentence explanation
3. If vanity: suggest the actionable version (e.g. replace 'registered users' with 'weekly active users')
4. If actionable: confirm which team owns it and what actions move it

Then:
5. Identify the 3 most important actionable metrics from the list
6. Flag any critical business dimension (revenue, retention, acquisition, engagement) with no actionable metric coverage

Return: classification table, recommended replacements, and coverage gaps. Copy prompt View page Show more ↓ 
## Process Analysis 
9 prompt s Process Analysis Intermediate Prompt 01 
### Automation Opportunity Scan 
Scan this process for automation opportunities and build an automation prioritization plan.

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

Return: automation opportunity matrix, prioritized automation roadmap, and estimated total time savings. Copy prompt View page Show more ↓ Process Analysis Beginner Prompt 02 
### Bottleneck Identification 
Identify and prioritize the bottlenecks in this business process using the data provided.

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

Return: bottleneck analysis table, constraint identification, and prioritized improvement actions. Copy prompt View page Show more ↓ Process Analysis Advanced Chain 03 
### Process Improvement Chain 
Step 1: Document the current state — map the as-is process, capturing every step, actor, system, cycle time, and handoff.
Step 2: Measure performance — quantify the current process: total lead time, value-add percentage, error rate, cost per unit, and customer satisfaction score if available.
Step 3: Analyze waste and bottlenecks — identify the top 3 waste categories (Lean 8 wastes) and the single biggest bottleneck using Theory of Constraints.
Step 4: Root cause analysis — for each major bottleneck and waste source, apply Five Whys to identify the underlying root cause.
Step 5: Design the future state — propose a redesigned process that eliminates identified waste. Calculate the new expected performance metrics.
Step 6: Build the business case — quantify the value of the improvement: cost savings, time savings, error reduction, and customer impact. Calculate ROI.
Step 7: Write the improvement proposal: executive summary, current vs future state comparison, business case, implementation plan, risks, and success metrics. Copy prompt View page Show more ↓ Process Analysis Beginner Prompt 04 
### Process Map 
Create a structured process map for: {{process_name}}

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

Return: structured process map, step metadata table, and summary statistics. Copy prompt View page Show more ↓ Process Analysis Advanced Prompt 05 
### Process Redesign Proposal 
Design a redesigned future-state version of this process based on the pain points identified.

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

Return: future state process map, efficiency comparison table, and phased implementation plan. Copy prompt View page Show more ↓ Process Analysis Intermediate Prompt 06 
### RACI Matrix Builder 
Build a RACI matrix for the process or project: {{process_or_project}}

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

Return: formatted RACI matrix, anti-pattern flags with recommended fixes, and process risk summary. Copy prompt View page Show more ↓ Process Analysis Intermediate Prompt 07 
### Root Cause Analysis 
Conduct a structured root cause analysis (RCA) for this problem: {{problem_statement}}

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

Return: Five Whys chain, fishbone diagram (text format), confirmed root cause, and action plan. Copy prompt View page Show more ↓ Process Analysis Intermediate Prompt 08 
### SLA Compliance Analysis 
Analyze SLA (Service Level Agreement) compliance for this process or service using the data provided.

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

Return: compliance dashboard, breach analysis, pattern analysis, and improvement recommendations. Copy prompt View page Show more ↓ Process Analysis Intermediate Prompt 09 
### Value Stream Mapping 
Create a value stream map for the process: {{process_name}}

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

Return: current state VSM table, waste inventory, process efficiency metrics, and future state design. Copy prompt View page Show more ↓ 
## AB Testing and Experimentation 
8 prompt s AB Testing and Experimentation Beginner Prompt 01 
### A/B Test Design Brief 
Write an A/B test design brief for the following proposed change: {{change_description}}

The brief must include:

1. Hypothesis
 - We believe that [change] will cause [outcome] because [rationale]
 - Null hypothesis: the change has no effect on the primary metric

2. Primary metric: the single metric this test will be judged on
3. Secondary metrics: 2–3 supporting metrics to monitor
4. Guardrail metrics: 2–3 metrics that must not significantly degrade

5. Test setup
 - Unit of randomization: user / session / account / device
 - Traffic split: 50/50 or other (justify any deviation)
 - Targeting: all users, or a specific segment? Why?

6. Statistical parameters
 - Significance level α = 0.05 (two-tailed)
 - Minimum detectable effect (MDE): the smallest change worth detecting
 - Required statistical power: 80%
 - Required sample size per variant (calculate)
 - Required experiment duration given current daily traffic of {{daily_traffic}}

7. Risks: what could go wrong? How will you detect it?
8. Decision criteria: exactly when will you ship, iterate, or kill?

Return: the complete test brief as a shareable document. Copy prompt View page Show more ↓ AB Testing and Experimentation Intermediate Prompt 02 
### A/B Test Results Analysis 
Analyze the results of this A/B test and produce a decision-ready report.

Test data is provided. Include:

1. Pre-analysis checks:
 - Sample ratio mismatch (SRM): is the actual traffic split consistent with the planned split? Use chi-squared test.
 - Was the test run for the full planned duration?
 - Any signs of peeking (early stopping)?

2. Primary metric analysis:
 - Control vs treatment value (mean ± std or conversion rate)
 - Observed absolute and relative difference
 - Statistical test: t-test (continuous) or z-test/chi-squared (proportions)
 - p-value and 95% confidence interval for the difference
 - Is the result statistically significant at α = 0.05?

3. Secondary and guardrail metrics: repeat analysis for each

4. Practical significance: is the observed effect large enough to matter for the business? Compare to the MDE.

5. Segment analysis: break results down by key segments — does treatment work equally across all user types?

6. Decision recommendation: Ship / Do not ship / Iterate / Inconclusive — with clear justification

Return: full analysis report with all tests, segment breakdown, and decision recommendation. Copy prompt View page Show more ↓ AB Testing and Experimentation Advanced Prompt 03 
### Experiment Roadmap Builder 
Build a 90-day experimentation roadmap for {{product_area}} based on the provided business objectives and backlog of ideas.

Idea backlog: {{ideas_list}}

1. Score each experiment idea on:
 - Expected impact: how much could this move the primary metric? (1–5)
 - Confidence in hypothesis: how strong is the evidence this will work? (1–5)
 - Implementation effort: engineering days to build (1=<3 days, 5=>20 days)
 - Sample size required: how many weeks at current traffic?
 - Learning value: even if negative, what will we learn? (1–5)

2. Score each idea using ICE score: (Impact × Confidence) / Effort

3. Apply scheduling constraints:
 - Maximum 2 experiments running simultaneously on the same surface
 - Avoid overlapping experiments that share user populations
 - Schedule quick tests (high ICE) first to build velocity

4. Produce a week-by-week experiment calendar for 90 days

5. Identify the top learning that each 30-day block is designed to answer

Return: scored idea table, ICE rankings, experiment calendar, and 30-day learning objectives. Copy prompt View page Show more ↓ AB Testing and Experimentation Advanced Chain 04 
### Full Experiment Chain 
Step 1: Hypothesis — write a clear falsifiable hypothesis for the proposed change. Define primary metric, secondary metrics, and guardrail metrics.
Step 2: Sample size — calculate required sample size and test duration given baseline metric, MDE, α=0.05, and power=80%.
Step 3: Pre-experiment checks — run an AA test on historical data to verify randomization works. Check for pre-existing imbalances between groups.
Step 4: Run analysis — after experiment completion: check for SRM, run primary statistical test, apply multiple testing correction if needed, segment the results.
Step 5: Novelty and stability check — plot daily results to check for novelty effects or instability. Confirm results are consistent in the second half of the experiment.
Step 6: Business impact calculation — translate the statistical result into business impact: if this effect holds, what is the annual revenue or metric impact?
Step 7: Decision and documentation — write a 1-page experiment summary: hypothesis, method, results, decision (ship/no-ship/iterate), business impact, and lessons learned. Copy prompt View page Show more ↓ AB Testing and Experimentation Intermediate Prompt 05 
### Inconclusive Test Diagnosis 
This A/B test returned an inconclusive result (p > 0.05, no significant effect detected). Diagnose why and recommend next steps.

1. Check statistical power:
 - Was the test adequately powered? Calculate post-hoc power given observed effect size and sample size.
 - If power < 80%, the test was underpowered — this is likely a false negative, not proof of no effect.

2. Check the effect size:
 - What was the observed effect size, even if not significant?
 - Is the observed effect smaller than the MDE? If yes, the test was powered for a larger effect.

3. Check test duration:
 - Was the test run long enough to cover at least one full weekly cycle?
 - Was the test affected by external events (seasonality, promotions, product launches)?

4. Check for segment heterogeneity:
 - Does the effect appear in specific segments even if the overall result is null?
 - This could indicate the change is right for a subset of users.

5. Based on the diagnosis, recommend one of:
 - Re-run with larger sample size (provide new calculation)
 - Re-run targeting only the segment where effect appeared
 - Redesign the test with a stronger treatment
 - Accept the null — the change genuinely has no effect

Return: power analysis, effect size assessment, duration check, segment analysis, and recommendation. Copy prompt View page Show more ↓ AB Testing and Experimentation Intermediate Prompt 06 
### Multiple Testing Correction 
Apply multiple testing corrections to this experiment that tested multiple metrics or multiple variants simultaneously.

Test data provided includes {{num_metrics}} metrics and/or {{num_variants}} variants.

1. Explain the multiple testing problem:
 - With {{num_tests}} independent tests at α=0.05, the probability of at least one false positive is {{familywise_error_rate}}%
 - Without correction, we are likely to see spurious significant results

2. Apply and compare three correction methods:
 a. Bonferroni correction: α_adjusted = 0.05 / number of tests
 b. Holm-Bonferroni (step-down): less conservative than Bonferroni
 c. Benjamini-Hochberg (FDR): controls false discovery rate at 5%

3. For each metric, show: raw p-value | Bonferroni adjusted | Holm adjusted | BH adjusted | significant after each correction?

4. Recommend which correction method to use for this specific test and why

5. Re-state the decision recommendation after applying the correction — does it change?

Return: corrected p-value table, method comparison, and final decision recommendation. Copy prompt View page Show more ↓ AB Testing and Experimentation Intermediate Prompt 07 
### Novelty Effect Check 
Check whether this A/B test result is driven by a novelty effect rather than a genuine sustained improvement.

A novelty effect occurs when users behave differently simply because something is new — the effect fades over time as users habituate.

1. Plot the primary metric for treatment and control groups over time (day by day or week by week)
2. Check for the novelty effect pattern:
 - Large early treatment lift that narrows or disappears over time
 - Treatment performance converges toward control in later weeks
3. Segment analysis by user tenure:
 - Compare treatment effect for new users (first 30 days) vs established users (>90 days)
 - A novelty effect typically only appears in established users, not new ones
4. Compute the treatment effect for the first half vs second half of the experiment
 - If first-half effect is significantly larger than second-half, novelty effect is likely
5. Extrapolate: if the novelty effect is confirmed, what is the expected long-term steady-state lift?

Return: time series plot of treatment vs control, novelty effect diagnosis, user tenure breakdown, and long-term lift estimate. Copy prompt View page Show more ↓ AB Testing and Experimentation Beginner Prompt 08 
### Sample Size Calculator 
Calculate the required sample size for this A/B test.

Inputs:
- Primary metric type: {{metric_type}} (conversion rate / continuous metric)
- Baseline value: {{baseline}} (e.g. current conversion rate of 5%, or mean revenue of $42)
- Minimum detectable effect (MDE): {{mde}} (e.g. 10% relative lift, or absolute +0.5%)
- Significance level α: 0.05 (two-tailed)
- Statistical power: 80%
- Number of variants: {{variants}} (e.g. 2 = one control + one treatment)

Calculate and return:
1. Required sample size per variant
2. Total sample size across all variants
3. Required test duration given daily traffic of {{daily_traffic}} users/sessions
4. Sensitivity table: how does sample size change as MDE varies?
 - MDE at 50%, 75%, 100%, 125%, 150% of the specified MDE
5. Power curve: plot statistical power vs sample size for the specified MDE
6. Flag if the required duration exceeds 4 weeks — longer tests are vulnerable to seasonality and novelty effects

Return: sample size calculation, duration estimate, sensitivity table, and power curve. Copy prompt View page Show more ↓ 
## Reporting and Dashboards 
8 prompt s Reporting and Dashboards Intermediate Prompt 01 
### Anomaly Narrative Writer 
Write a clear narrative explanation of this data anomaly for a non-technical business audience.

Anomaly: {{anomaly_description}} (e.g. 'Revenue dropped 23% week-over-week in the EMEA region during the week of March 10')

Data provided shows the full context.

1. State the anomaly clearly in the first sentence — what happened, how large was the deviation, and when?
2. Provide immediate context: is this the largest deviation in the past 12 months? How does it compare to normal variance?
3. Diagnose the cause using the data:
 - Drill down by dimension to isolate where the anomaly is concentrated
 - Check for correlated changes in other metrics
 - Identify any known external events (holidays, outages, campaigns)
4. Assess business impact: what is the estimated financial or operational impact?
5. State whether this is:
 - A data quality issue (pipeline error, reporting lag)
 - A temporary one-off event
 - The start of a concerning trend
6. Recommend the next action: investigate further / monitor / escalate / no action needed

Return: 200-word narrative suitable for a Slack message or email to leadership. Copy prompt View page Show more ↓ Reporting and Dashboards Intermediate Template 02 
### Board-Level Report 
Write a board-level performance report for {{company_name}} for {{period}}.

Board-level reports have specific requirements:
- Strategic, not operational: focus on business outcomes, not activity
- Every number cited must be compared to a target or prior period
- Recommendations must be specific and actionable
- Maximum 2 pages of text

Structure:

1. Performance against strategic KPIs (table):
 - 4–6 strategic metrics only: revenue, growth rate, NPS, market share, or equivalent
 - Each: actual | target | vs target | trend

2. Strategic highlights (3 bullets max):
 - Major milestones achieved this period

3. Risks and challenges (3 bullets max):
 - Significant risks to the strategy with current mitigation status

4. Decisions required (if any):
 - Clearly state what decision is being asked of the board and by when
 - Provide the option set and a recommended option with rationale

5. Outlook:
 - Full-year forecast vs target
 - Top 2 tailwinds and headwinds going into next quarter

Tone: confident, precise, no jargon. Use active voice. Every paragraph should answer 'so what?' Copy prompt View page Show more ↓ Reporting and Dashboards Beginner Prompt 03 
### Dashboard Specification 
Write a dashboard specification document for a {{dashboard_name}} dashboard for {{audience}}.

The specification should include:

1. Purpose and audience:
 - What decision does this dashboard support?
 - Who are the primary users and what is their technical level?
 - How often will it be used and in what context (daily standup, weekly review, ad-hoc analysis)?

2. KPIs and metrics to display:
 - For each metric: name, definition, formula, data source, refresh frequency

3. Dashboard layout (describe each panel):
 - Panel 1: [metric name] — [chart type] — [why this chart type]
 - List all panels with their position, size, and purpose

4. Filters and interactivity:
 - Date range selector
 - Dimension filters (region, product, segment, etc.)
 - Drill-down capabilities

5. Alerts and thresholds:
 - Which metrics should trigger alerts and at what thresholds?

6. Data sources and refresh:
 - Source tables or APIs, refresh schedule, SLA for data freshness

7. Access and permissions:
 - Who can view, who can edit, any data sensitivity restrictions

Return: complete dashboard specification document. Copy prompt View page Show more ↓ Reporting and Dashboards Advanced Prompt 04 
### Metric Discrepancy Investigation 
Investigate why two reports are showing different values for the same metric: {{metric_name}}

Report A shows: {{value_a}} | Report B shows: {{value_b}} | Difference: {{difference}}

Systematically investigate each possible cause:

1. Definition differences:
 - Is the metric formula identical in both reports?
 - Are the same inclusion/exclusion filters applied?
 - Are the same business rules applied (e.g. how refunds are treated)?

2. Date range differences:
 - Are both reports using the same date range?
 - Is one using event date and the other using processing date?
 - Is one using UTC and the other using local time?

3. Data source differences:
 - Do both reports pull from the same source table?
 - If different sources, when were they last synced and could there be a lag?

4. Aggregation differences:
 - Is one report double-counting rows due to joins?
 - Is one report deduplicating differently?

5. Access differences:
 - Does one report include data the other user doesn't have access to?

For each hypothesis: confirmed / ruled out / needs investigation.

Return: investigation log, root cause finding, and recommended fix to align both reports. Copy prompt View page Show more ↓ Reporting and Dashboards Beginner Prompt 05 
### Monthly Business Report 
Write a monthly business performance report based on the data provided.

Structure:

1. Month in review (2–3 sentences): overall performance summary — was it a good month or a challenging one, and why?

2. Key metrics summary (table):
 - Each metric: this month | last month | MoM % | this month last year | YoY % | vs annual target (% complete)

3. Top 3 wins: specific achievements with numbers. What drove them?

4. Top 3 misses or concerns: what fell short of expectations? What is the root cause?

5. Deep dive (1 topic):
 - Choose the most important story in the data this month
 - 2–3 paragraphs with charts described in text
 - What is happening, why, and what should we do about it?

6. Forecast update:
 - Based on current month performance, update the full-year forecast
 - Are we on track, ahead, or behind the annual target?

7. Next month priorities: 3 focus areas with owner and measurable goal

Length: 600–800 words. Tone: professional but direct. No bullet soup — use paragraphs for the narrative sections. Copy prompt View page Show more ↓ Reporting and Dashboards Advanced Chain 06 
### Reporting Strategy Chain 
Step 1: Audit current reports — inventory all existing reports and dashboards. For each: audience, frequency, purpose, time to produce, and last known use date. Identify reports that are never used.
Step 2: Define reporting needs by audience tier — board (monthly, strategic), leadership (weekly, operational), team (daily, tactical). Define the right format, length, and metrics for each tier.
Step 3: Design the reporting hierarchy — create a single reporting framework where every metric rolls up consistently from team level to board level with no conflicting definitions.
Step 4: Retire redundant reports — list reports to discontinue. Draft a communication plan so stakeholders are not left without information.
Step 5: Build the reporting calendar — schedule all recurring reports with owners, data cut-off times, review deadlines, and distribution lists.
Step 6: Define the data glossary — for the top 20 metrics in the reporting suite, write agreed definitions, formulas, and data sources so there is one version of the truth.
Step 7: Write a reporting strategy document: current state assessment, proposed future state, transition plan, and governance model. Copy prompt View page Show more ↓ Reporting and Dashboards Intermediate Prompt 07 
### Self-Serve Analytics Spec 
Design a self-serve analytics solution for {{business_team}} to answer their most common data questions without needing analyst support.

1. Conduct a question audit:
 - List the top 10 most common questions this team asks the data team
 - Classify each: answerable with a standard report, requires ad-hoc analysis, or needs a new data source

2. Design the self-serve layer:
 - Which questions can be answered with a pre-built dashboard? Specify the dashboard.
 - Which questions need a flexible exploration tool (e.g. Looker, Metabase)? Specify the data model.
 - Which require scheduled reports? Specify format and recipients.

3. Data literacy requirements:
 - What level of data skill does this team currently have?
 - What training or documentation is needed for them to use the self-serve layer confidently?

4. Governance rules:
 - Which metrics need a single agreed definition (to prevent different people getting different answers)?
 - Who approves new metric definitions?
 - How are errors or discrepancies reported and resolved?

5. Success metric: how will you know the self-serve solution is working?

Return: question audit table, self-serve design spec, training plan, and governance rules. Copy prompt View page Show more ↓ Reporting and Dashboards Beginner Prompt 08 
### Weekly Business Review 
Generate a weekly business review report based on this data.

The report should follow this structure:

1. Executive headline (1 sentence): the single most important thing that happened this week

2. Scorecard (table format):
 - Each KPI: current week value | prior week value | WoW change % | vs target | status (🟢/🟡/🔴)

3. Highlights (3 bullet points):
 - What went well this week? Cite specific numbers.

4. Concerns (2–3 bullet points):
 - What needs attention? Cite specific numbers and why it matters.

5. Context:
 - Any external events, seasonality, or one-time factors that explain unusual movements

6. Actions:
 - 2–3 specific actions for next week with an owner and due date for each

7. Next week outlook:
 - What are we expecting? Any events or decisions coming up that will affect the metrics?

Tone: factual, direct, no jargon. Written for a general management audience. Maximum 400 words excluding the scorecard. Copy prompt View page Show more ↓ 
## Requirements and Discovery 
8 prompt s Requirements and Discovery Intermediate Prompt 01 
### As-Is Process Interview Guide 
Create a structured interview guide for a business process discovery session.

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

Return the full interview guide formatted as a printable document with space for notes after each question. Copy prompt View page Show more ↓ Requirements and Discovery Advanced Prompt 02 
### Business Rules Extraction 
Extract and catalog all business rules from this dataset, document, or process description: {{source}}

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

Return: business rules catalog and a list of automation candidates. Copy prompt View page Show more ↓ Requirements and Discovery Intermediate Prompt 03 
### Feasibility Assessment 
Assess the feasibility of the proposed solution or initiative: {{initiative_description}}

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

Return: feasibility scorecard (Red / Amber / Green per dimension), overall feasibility verdict, top 3 risks, and recommended next steps. Copy prompt View page Show more ↓ Requirements and Discovery Advanced Chain 04 
### Full Discovery Chain 
Step 1: Stakeholder analysis — identify all stakeholders, their influence/interest levels, primary concerns, and engagement strategy.
Step 2: Current state documentation — describe the as-is process, systems, data flows, and pain points based on the provided inputs.
Step 3: Future state vision — define the desired outcomes, success criteria, and high-level capabilities needed.
Step 4: Gap analysis — identify the gaps between current and future state, scored by impact and effort.
Step 5: Requirements extraction — convert gaps and stakeholder needs into structured business and functional requirements with MoSCoW priorities.
Step 6: Risks and assumptions — list the top 5 risks to successful delivery and the key assumptions being made. For each risk: likelihood, impact, and mitigation strategy.
Step 7: Discovery summary — write a 1-page discovery report: problem statement, proposed solution direction, requirements summary, open questions, and recommended next steps. Copy prompt View page Show more ↓ Requirements and Discovery Intermediate Prompt 05 
### Gap Analysis 
Conduct a gap analysis between the current state and the desired future state.

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

Return: current vs future state comparison table, gap register, prioritization matrix, and recommended sequencing. Copy prompt View page Show more ↓ Requirements and Discovery Beginner Prompt 06 
### Requirements Extraction 
Extract and structure the business requirements from the following input: {{input}} (meeting notes, email thread, or stakeholder interview transcript).

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

Return a structured requirements table and a list of open questions to resolve in the next session. Copy prompt View page Show more ↓ Requirements and Discovery Beginner Prompt 07 
### Stakeholder Mapping 
Create a stakeholder map for this project or initiative based on the context provided.

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

Return the stakeholder table, grid placement, and engagement recommendations. Copy prompt View page Show more ↓ Requirements and Discovery Beginner Prompt 08 
### User Story Writer 
Convert these business requirements into well-formed user stories with acceptance criteria.

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

Return: formatted user story cards, dependency map, and a prioritized backlog order based on business value and dependencies. Copy prompt View page Show more ↓ 
## Stakeholder Communication 
5 prompt s Stakeholder Communication Intermediate Prompt 01 
### Data Literacy Translation 
Translate this technical analysis into plain business language for {{audience}} who has no data or statistical background.

Technical analysis: {{technical_content}}

1. Remove or replace every technical term:
 - Replace statistical terms with business language
 - Example: 'statistically significant at p < 0.05' → 'we are 95% confident this is a real change, not random noise'
 - Example: 'regression coefficient of 0.42' → 'for every $1 increase in marketing spend, revenue increases by 42 cents'

2. Replace abstract numbers with concrete comparisons:
 - Instead of '15% increase', say 'that's like adding the equivalent of our entire Q3 sales team's output'
 - Use the audience's own business context for analogies

3. Connect every finding to a decision:
 - For each insight, state what it means for a decision the audience controls

4. Summarize in 3 bullet points a non-technical executive could repeat to their peers accurately

5. Identify any nuance or caveat that was lost in the translation that the audience must still know

Return: translated version, 3-bullet summary, and a list of caveats that survived translation. Copy prompt View page Show more ↓ Stakeholder Communication Advanced Prompt 02 
### Difficult Data Conversation 
Help me prepare for a difficult stakeholder conversation about underperformance shown in this data.

Situation: {{situation_description}}
Stakeholder: {{stakeholder_role}}
Data shows: {{performance_summary}}

1. Frame the conversation structure:
 - Opening: how to introduce the data without triggering defensiveness
 - Data presentation: how to show the numbers as facts, not judgments
 - Exploration: questions to understand their perspective before pushing your analysis
 - Alignment: how to agree on what the data means before discussing what to do
 - Resolution: how to get to a committed action

2. Prepare for the 3 most likely defensive reactions:
 - 'The data is wrong' → how to handle a data quality challenge
 - 'There are factors outside my control' → how to acknowledge and still move forward
 - 'This is normal for this time of year' → how to respond to a seasonality objection

3. Write an opening statement (3 sentences) that is neutral, data-grounded, and invites dialogue

4. Write 3 open questions to draw out their perspective

5. Identify what success looks like at the end of this conversation

Return: conversation guide, opening statement, prepared questions, and success definition. Copy prompt View page Show more ↓ Stakeholder Communication Beginner Prompt 03 
### Insight Communication 
Write a clear, compelling communication of this data insight for a non-technical business audience.

Insight: {{insight_description}}
Audience: {{audience}} (e.g. Sales Director, CFO, Marketing team)

1. Lead with the so-what, not the analysis:
 - First sentence: what should the audience know or do?
 - Do not start with 'The data shows...'

2. Support with evidence:
 - 2–3 specific numbers that prove the point
 - One comparison that provides context (vs last period, vs target, vs benchmark)

3. Explain the implication:
 - What does this mean for the business?
 - What is the risk of ignoring this?

4. Recommend an action:
 - Specific, feasible, and owned by someone in the audience
 - Include a suggested timeline

5. Anticipate the first objection and address it proactively

Format: max 150 words. No bullet points — write in 3 short paragraphs.
Return: the communication text and a one-sentence 'subject line' suitable for a Slack message or email. Copy prompt View page Show more ↓ Stakeholder Communication Intermediate Prompt 04 
### Objection Handling Prep 
Prepare responses to likely objections for this proposal or recommendation: {{proposal_summary}}

Audience: {{audience}}

1. Anticipate the top 7 objections this audience is likely to raise:
 - Identify objection type: factual dispute, resource concern, priority conflict, risk aversion, trust issue, or strategic disagreement

2. For each objection prepare:
 - The objection stated in the audience's own language
 - The underlying concern behind the objection (what are they really worried about?)
 - A data-backed response (1–2 sentences)
 - A follow-up question to move the conversation forward
 - Concession if appropriate: is there a legitimate version of this concern you should acknowledge?

3. Identify the 2 objections most likely to kill the proposal if not handled well

4. Prepare a pre-emptive strike: which 2 objections should you address proactively in the presentation before they are raised?

Return: objection-response guide, pre-emptive address recommendations, and a one-page cheat sheet for the meeting. Copy prompt View page Show more ↓ Stakeholder Communication Beginner Prompt 05 
### Presentation Structure Builder 
Create a structured slide-by-slide outline for a {{duration}}-minute presentation on {{topic}} for {{audience}}.

Presentation goal: by the end, the audience should {{desired_outcome}} (e.g. approve the proposal, understand the performance issue, commit to an action)

For each slide provide:
- Slide number and title (max 6 words — a statement, not a label)
- Key message: the single thing the audience must take away from this slide (1 sentence)
- Content: 2–3 data points, visuals, or arguments that support the key message
- Notes: what to say verbally that is not on the slide
- Estimated time: how many minutes to spend on this slide

Structure principles:
- Slide 1: the situation (context, why we're here)
- Slide 2–3: the complication (what's the problem or opportunity)
- Slide 4–7: the resolution (analysis, options, recommendation)
- Last slide: the ask (one clear call to action)

Return: full slide outline with titles, messages, content notes, and timing. Copy prompt View page Show more ↓ 
## Business Case and Prioritization 
3 prompt s Business Case and Prioritization Advanced Chain 01 
### Full Business Case Chain 
Step 1: Problem statement — define the business problem or opportunity with quantified impact. What is the cost of doing nothing?
Step 2: Options analysis — identify 3 solution options including a 'do nothing' baseline. For each: description, pros, cons, rough cost, and rough benefit.
Step 3: Recommended option — select the best option with a clear rationale. Why does it outperform the alternatives?
Step 4: Detailed financials — build the full ROI model for the recommended option: implementation costs, ongoing costs, benefits by category, NPV, ROI, and payback period.
Step 5: Risk assessment — identify the top 5 risks to the business case. For each: probability, impact, mitigation strategy, and residual risk.
Step 6: Implementation overview — high-level timeline, key milestones, resource requirements, and dependencies.
Step 7: Write the executive business case: one-page summary covering — problem, recommended solution, financial case (3 key numbers), key risks, and the ask (decision required, investment needed, timeline to decide). Copy prompt View page Show more ↓ Business Case and Prioritization Intermediate Prompt 02 
### Prioritization Framework 
Prioritize this backlog of initiatives or features: {{backlog_list}}

Apply three prioritization frameworks and compare:

1. RICE Score: (Reach × Impact × Confidence) / Effort
 - Reach: how many users or customers affected per period?
 - Impact: how much does it move the key metric? (1=minimal, 2=low, 3=medium, 4=high, 5=massive)
 - Confidence: how sure are we? (100%=high, 80%=medium, 50%=low)
 - Effort: person-months to implement

2. Value vs Effort matrix:
 - Plot each initiative on a 2×2: value on y-axis, effort on x-axis
 - Quadrants: Quick Wins (high value, low effort), Big Bets (high value, high effort), Fill-ins (low value, low effort), Money Pits (low value, high effort)

3. Strategic alignment score:
 - Rate each initiative 1–5 on alignment to each of the top 3 strategic objectives
 - Total score = sum of alignment ratings

After scoring with all three frameworks:
4. Identify the consensus top 5: initiatives ranked highly across all three methods
5. Flag any that appear in only one framework's top 5 — these need more discussion

Return: scoring table for all three frameworks, priority quadrant assignments, consensus top 5, and a recommended sequence. Copy prompt View page Show more ↓ Business Case and Prioritization Beginner Prompt 03 
### ROI Calculator 
Build an ROI analysis for this proposed initiative: {{initiative_description}}

1. Costs (one-time):
 - Implementation cost: technology, professional services, internal labor
 - Training and change management
 - Testing and validation

2. Costs (ongoing annual):
 - Licensing or subscription fees
 - Maintenance and support
 - Ongoing internal labor

3. Benefits (annual):
 - Revenue increase: quantify and explain the mechanism
 - Cost reduction: quantify and explain what costs are reduced
 - Risk reduction: convert risk probability × impact to expected annual cost
 - Productivity gain: hours saved × hourly cost

4. Financial summary:
 - Total 3-year cost
 - Total 3-year benefit
 - Net benefit (benefit - cost)
 - ROI = (net benefit / total cost) × 100%
 - Payback period: months to break even
 - NPV at 10% discount rate

5. Sensitivity analysis:
 - What if benefits are 25% lower than expected?
 - What if costs are 25% higher?
 - At what benefit level does ROI turn negative?

Return: ROI model table, payback calculation, NPV, and sensitivity analysis. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
