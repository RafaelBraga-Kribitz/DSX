# Reporting and Communication *AI Prompts *

3 Healthcare Data Analyst prompts in Reporting and Communication. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 1 single prompt · 1 chain · 1 template. 

## AI prompts in Reporting and Communication 
3 prompts Beginner Single prompt 01 
### Clinical Executive Summary 

This prompt is designed to translate complex hospital performance data into a concise executive narrative for senior leaders. It forces prioritization across volume, quality, and operational efficiency while keeping the language accessible to a mixed leadership audience. It is useful for monthly reviews, board packets, and leadership huddles where clarity and brevity matter. 
Prompt text Write a clinical performance executive summary based on this dataset for a hospital leadership audience.

The summary should cover exactly 4 sections:

1. Patient Volume & Mix (2–3 sentences)
 - Total admissions, ED visits, and outpatient encounters for the period
 - Key payer mix highlights and any significant shifts vs prior period

2. Quality & Safety Performance (2–3 sentences)
 - 30-day readmission rate vs target and national benchmark
 - Mortality rate and HAC rate vs benchmark
 - Highlight one quality win and one quality concern

3. Operational Efficiency (2–3 sentences)
 - Average LOS vs geometric mean benchmark
 - ED throughput metrics and any capacity concerns
 - Case mix index vs prior period

4. Priority Actions (3 bullet points)
 - Three specific, data-driven recommendations based on the analysis
 - Each bullet: what to do, why (cite a specific number), and who should own it

Tone: concise, direct, evidence-based. No clinical jargon — write for a CFO and CMO audience. Maximum 300 words. Copy prompt Open prompt details Advanced Chain 02 
### Population Health Report Chain 

This chain prompt structures a population health report from population definition through risk segmentation, utilization, care gaps, and PMPM cost. It is designed for value-based care and payer-provider settings where clinical quality and cost must be viewed together. It is most useful when preparing strategic reports for population health leaders, ACO teams, or medical management programs. 
Prompt text Step 1: Define the population — total attributed patients, demographics breakdown, payer mix, and geographic distribution.
Step 2: Stratify by risk — use available risk scores (HCC RAF score, LACE, or a custom risk model) to classify patients into low, moderate, high, and very high risk tiers. Show size and cost of each tier.
Step 3: Analyze utilization patterns — ED visit rate, hospitalization rate, and preventable admission rate (ACSC conditions) per 1,000 patients for each risk tier.
Step 4: Identify care gaps — for chronic disease patients, what % are meeting evidence-based care standards? (e.g. HbA1c tested in last 12 months for diabetics, annual eye exam, statin prescribed for CAD patients)
Step 5: Calculate total cost of care — PMPM (per member per month) cost by risk tier, broken down by inpatient, ED, outpatient, pharmacy.
Step 6: Write a population health summary report: population profile, risk stratification results, top 5 care gaps with prevalence rates, cost drivers, and three priority interventions with estimated ROI. Copy prompt Open prompt details Intermediate Template 03 
### Quality Measure Report 

This prompt creates a formal quality measure report suitable for a committee or governance setting. It combines measure specification, current performance, stratified results, and an action plan so the output is not just descriptive but operationally useful. It is especially helpful for reporting on CMS, Joint Commission, or internally governed quality metrics. 
Prompt text Generate a quality measure performance report for {{measure_name}} for the period {{reporting_period}}.

The report must include:

1. Measure definition
 - Full measure name and steward (e.g. CMS, TJC, NQF)
 - Numerator definition: {{numerator_definition}}
 - Denominator definition: {{denominator_definition}}
 - Exclusions: {{exclusions}}

2. Performance results
 - Numerator count, denominator count, and measure rate
 - Performance vs target: {{target_rate}}
 - Performance vs national benchmark (50th and 90th percentile)
 - Trend: rate for the current period vs the prior 4 periods

3. Stratification
 - Rate broken down by: service line, payer, age group, and race/ethnicity (for health equity analysis)
 - Flag any subgroup performing more than 10 percentage points below the overall rate

4. Root cause and action plan
 - Top 3 contributing factors to any gap from target
 - Specific improvement actions with owner and due date

Format as a structured report suitable for submission to a quality committee. Copy prompt Open prompt details 
## Recommended Reporting and Communication workflow 
1 
### Clinical Executive Summary 

Start with a focused prompt in Reporting and Communication so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Population Health Report Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Quality Measure Report 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
