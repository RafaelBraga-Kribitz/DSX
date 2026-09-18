# Business Insights *AI Prompts *

8 Data Analyst prompts in Business Insights. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain · 1 template. 

## AI prompts in Business Insights 
8 prompts Beginner Single prompt 01 
### 5 Key Findings 

5 Key Findings is a beginner prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Analyze this dataset and return exactly 5 key findings, ordered from most to least important.

For each finding:
- A bold one-sentence headline stating the finding
- Two to three supporting sentences with specific numbers from the data
- One sentence on the business implication

Rules:
- No filler or vague statements. Every sentence must contain a specific number or comparison.
- Findings must be distinct — no overlapping insights.
- Use plain language a non-analyst could understand.

End with one sentence: 'The finding that most urgently requires action is [finding N] because [reason].' Copy prompt Open prompt details Advanced Single prompt 02 
### Churn Risk Analysis 

Churn Risk Analysis is a advanced prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Identify customers or users at risk of churning based on behavioral signals in this dataset:

1. Define churn signals from the available columns (e.g. declining purchase frequency, reduced engagement, support ticket spikes, payment failures)
2. Score each customer on a churn risk scale of 1–10 based on the strength of signals present
3. Identify the top 20 highest-risk customers with their risk score and primary churn signal
4. Segment at-risk customers by reason: price sensitivity, product dissatisfaction, competitive alternative, inactivity
5. Recommend one targeted retention action per segment

Return a churn risk table and a 2-sentence executive summary of the overall churn risk level. Copy prompt Open prompt details Advanced Chain 03 
### Data Storytelling Chain 

Data Storytelling Chain is a advanced chain for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Identify the single most important insight in this dataset. State it in one sentence, as if telling a non-technical colleague.
Step 2: Find exactly 3 data points that serve as compelling evidence for this insight. For each: state the number, what it means, and why it matters.
Step 3: Find one counterintuitive or surprising finding that adds nuance and prevents oversimplification.
Step 4: Identify the top 2 questions this data cannot answer — what additional data would you need to be fully confident in your recommendation?
Step 5: Write a complete data narrative: opening hook, central insight with evidence, nuance, data gap acknowledgement, and a clear call to action. Copy prompt Open prompt details Beginner Single prompt 04 
### Executive Summary 

Executive Summary is a beginner prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Analyze this dataset and write a concise executive summary in exactly 3 paragraphs:

Paragraph 1 — Situation: What does this data describe? What is the main trend over the period shown?
Paragraph 2 — Complication: What is the most significant risk, anomaly, or missed opportunity hidden in the data? Cite at least two specific numbers.
Paragraph 3 — Recommendation: What is the single most important action to take, who should own it, and by when?

Tone: direct, data-driven, no jargon. Max 200 words total. Write as if presenting to a C-suite audience. Copy prompt Open prompt details Intermediate Template 05 
### KPI Status Report 

KPI Status Report is a intermediate template for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Generate a KPI status report for {{reporting_period}} using the data provided.

For each key metric:
- Current value and target (source: {{target_source}})
- Absolute and percentage change vs {{comparison_period}}
- Status label: ✅ On Track / ⚠️ At Risk / 🔴 Off Track
- One-sentence explanation of the primary driver behind the change
- If Off Track: one specific recommended corrective action

Format: a clean table with one KPI per row.
At the bottom, add a 2-sentence overall summary: is the business trending in the right direction, and what is the most urgent issue to address? Copy prompt Open prompt details Intermediate Single prompt 06 
### Opportunity Sizing 

Opportunity Sizing is a intermediate prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Use this dataset to size the biggest business opportunity available:

1. Identify the metric that has the largest gap between current performance and best-in-class performance (either internal top performer or industry benchmark if known)
2. Calculate the revenue or metric impact of closing 25%, 50%, and 100% of that gap
3. Identify which segment, region, or cohort offers the fastest path to closing the gap
4. Estimate the effort level: is this gap likely due to a process issue (fixable quickly) or a structural issue (requires longer investment)?
5. Write a one-paragraph opportunity statement suitable for an internal business case Copy prompt Open prompt details Intermediate Single prompt 07 
### Pricing Analysis 

Pricing Analysis is a intermediate prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Analyze pricing patterns and their relationship to business outcomes in this dataset:

1. Show the distribution of prices across products, tiers, or regions
2. Identify any price clustering (common price points that appear frequently)
3. Calculate the correlation between price and volume/quantity — is there a clear demand elasticity signal?
4. Find the price point with the highest total revenue contribution (price × quantity)
5. Identify any products or segments where price and margin seem misaligned
6. Recommend 2–3 pricing adjustments based on the data, with estimated revenue impact of each Copy prompt Open prompt details Intermediate Single prompt 08 
### Segment Performance Breakdown 

Segment Performance Breakdown is a intermediate prompt for business insights. This prompt is designed to turn analysis into decisions. It helps the AI extract the most important findings from the data, explain why they matter, and frame actions in business language rather than technical language. Use it when the audience cares more about implications and next steps than methodology. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Analyze the performance of every segment in this dataset.

For each segment, compute:
- Size (row count and % of total)
- Mean and median of the primary metric
- Growth rate vs the prior period
- Share of total metric contribution

Then:
- Rank segments from highest to lowest performing
- Flag any segment with an unusual growth rate (more than 2 standard deviations from the average segment growth)
- Identify the segment with the highest untapped potential
- Write 3 concrete strategic recommendations based on the segment findings Copy prompt Open prompt details 
## Recommended Business Insights workflow 
1 
### 5 Key Findings 

Start with a focused prompt in Business Insights so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Churn Risk Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Storytelling Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Executive Summary 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
