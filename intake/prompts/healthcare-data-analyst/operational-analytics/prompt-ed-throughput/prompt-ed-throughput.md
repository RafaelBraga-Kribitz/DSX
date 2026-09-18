# ED Throughput Analysis *AI Prompt *

This prompt analyzes emergency department throughput across the full patient journey from arrival to departure. It identifies timing distributions, compares performance to external targets, and reveals where flow breaks down by hour, acuity, or disposition. It is especially helpful for ED operations teams trying to reduce waiting, crowding, and left-without-being-seen rates. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze Emergency Department throughput and flow in this dataset.

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

Return a throughput dashboard with benchmark comparisons and bottleneck analysis. 
```

## When to use this prompt 
Use case 01 
when ED crowding, LWBS, or long waits are operational priorities 
Use case 02 
when you need percentile-based turnaround times rather than just averages 
Use case 03 
when you want to see how throughput varies by acuity, hour, or disposition 
Use case 04 
when leadership asks where the biggest ED bottlenecks are 

## What the AI should return 

An ED throughput dashboard with percentile-based turnaround metrics, benchmark comparisons, hourly and weekday breakdowns, and a short bottleneck analysis pointing to where time is lost. 

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

Once you have the first result, continue deeper with related prompts in Operational Analytics.
