# Operational Analytics *AI Prompts *

4 Healthcare Data Analyst prompts in Operational Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Operational Analytics 
4 prompts Intermediate Single prompt 01 
### Bed Utilization and Capacity 

This prompt evaluates whether inpatient capacity is being used efficiently and whether certain units are operating in chronic scarcity or chronic underuse. It connects census, occupancy, turnover, and boarding into one operational view, then extends the analysis into forecasting and scenario modeling. It is useful for bed management, service line planning, and hospital operations leadership. 
Prompt text Analyze inpatient bed utilization and capacity in this dataset.

1. Calculate daily census for each unit or service line: total occupied beds per day
2. Calculate occupancy rate: (occupied beds / staffed beds) × 100
 - Target range: 80–85% for most acute care units
 - Flag any unit consistently above 90% (capacity crisis) or below 70% (inefficiency)
3. Analyze bed turnover ratio: admissions / average daily census — higher is more efficient
4. Identify peak demand periods:
 - Hour of day with highest census
 - Day of week with highest occupancy
 - Seasonal patterns (flu season, summer vs winter)
5. Calculate boarding hours: time admitted patients spend in the ED waiting for an inpatient bed
6. Model: what occupancy rate reduction is needed to eliminate boarding waits of >4 hours?
7. Forecast: based on current admission trends, when will average occupancy exceed 90%?

Return: occupancy dashboard by unit, peak demand heatmap, and capacity forecast chart. Copy prompt Open prompt details Intermediate Single prompt 02 
### Discharge Timing Analysis 

This prompt examines when discharges actually happen and quantifies the operational consequences of late discharge patterns. It links discharge timing to occupancy pressure and ED boarding, making it useful for hospitals trying to improve patient flow without adding beds. It also highlights physicians or services with better discharge timing practices that may be reproducible elsewhere. 
Prompt text Analyze discharge timing patterns and their operational impact.

1. Plot the distribution of actual discharge times by hour of day — when do most discharges happen?
2. Calculate the % of discharges that occur before noon vs after noon
 - Target: ≥30% of discharges before noon (industry best practice)
3. Analyze the relationship between discharge timing and:
 - ED boarding time (do early discharges reduce ED waits?)
 - Occupancy rate by hour (does morning discharge free capacity?)
4. Break down discharge timing by:
 - Service line / attending physician
 - Day of week
 - Discharge disposition (home discharges vs SNF vs other)
5. Identify which physicians or units have the best early discharge rates
6. Calculate the estimated impact: if early discharge rate improved from current to 30%, how many additional bed-hours would be freed per day?

Return: discharge timing histogram, early discharge rate by service and physician, and capacity impact estimate. Copy prompt Open prompt details Beginner Single prompt 03 
### ED Throughput Analysis 

This prompt analyzes emergency department throughput across the full patient journey from arrival to departure. It identifies timing distributions, compares performance to external targets, and reveals where flow breaks down by hour, acuity, or disposition. It is especially helpful for ED operations teams trying to reduce waiting, crowding, and left-without-being-seen rates. 
Prompt text Analyze Emergency Department throughput and flow in this dataset.

1. Calculate key ED flow metrics:
 - Door-to-triage time: arrival to first nursing assessment
 - Door-to-physician time: arrival to first physician contact
 - Door-to-disposition time: arrival to admit/discharge decision
 - Door-to-departure time: total ED LOS
 - Left without being seen (LWBS) rate
 - Left against medical advice (AMA) rate
2. Show 50th, 75th, 90th, and 95th percentile for each time metric
3. Compare to CMS and Joint Commission benchmarks:
 - Door-to-physician: target ≤ 60 minutes (median)
 - Admitted patient ED LOS: target ≤ 360 minutes
4. Break down all metrics by:
 - Hour of day and day of week (heatmap format)
 - ESI triage level (1–5)
 - Admit vs discharge patients
5. Identify the top 3 bottlenecks in the ED flow based on where time is most lost

Return a throughput dashboard with benchmark comparisons and bottleneck analysis. Copy prompt Open prompt details Advanced Chain 04 
### Staffing Efficiency Chain 

This chain prompt assesses staffing efficiency by connecting labor inputs, patient volume, quality outcomes, and cost. It does more than describe staffing levels; it looks for under- and over-staffing signals, overtime dependency, and the potential financial effect of schedule redesign. It is useful for nursing leadership, finance, and operations teams evaluating workforce optimization. 
Prompt text Step 1: Calculate nursing hours per patient day (NHPPD) for each unit by dividing total nursing hours worked by total patient days. Compare to target NHPPD by unit type (ICU: 12–24, Med/Surg: 6–8, Telemetry: 8–10).
Step 2: Identify units with NHPPD significantly above or below target. Above target may indicate overstaffing or high patient acuity; below target may indicate understaffing risk.
Step 3: Analyze overtime usage: what % of total nursing hours are overtime? High overtime (>5%) increases cost and may indicate staffing shortages.
Step 4: Correlate staffing levels with patient outcomes: is there a statistically significant relationship between NHPPD and falls, pressure injuries, or 30-day readmissions on each unit?
Step 5: Identify peak demand hours where actual staffing consistently falls below target nurse-to-patient ratios.
Step 6: Model the cost impact: calculate the cost per patient day at current staffing vs optimized staffing, and the potential savings from better shift scheduling. Copy prompt Open prompt details 
## Recommended Operational Analytics workflow 
1 
### Bed Utilization and Capacity 

Start with a focused prompt in Operational Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Discharge Timing Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### ED Throughput Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Staffing Efficiency Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
