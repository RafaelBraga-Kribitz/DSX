# Dashboard Performance Optimization *AI Prompt *

Diagnose and fix slow dashboard performance. Dashboard tool: {{tool}} Current load time: {{load_time}} Data size: {{data_size}} User complaint: {{complaint}} 1. Diagnose the bot... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and fix slow dashboard performance.

Dashboard tool: {{tool}}
Current load time: {{load_time}}
Data size: {{data_size}}
User complaint: {{complaint}}

1. Diagnose the bottleneck:

 Data query bottleneck:
 - Is the slow part the query or the rendering?
 - Enable query profiling in the tool — how long does each query take?
 - Are queries running on a large uncached dataset?
 - Are there multiple queries running sequentially that could run in parallel?

 Rendering bottleneck:
 - Too many data points in a single chart (scatter plot with 1M points)
 - Too many charts on a single page requesting data simultaneously
 - Heavy chart types (maps, network graphs) with large geometries

 Filter bottleneck:
 - Every filter change triggers a full database query
 - Cascading filters that trigger multiple queries in sequence

2. Data-layer optimizations:

 Pre-aggregation:
 - Move aggregations from dashboard query time to ETL time
 - Create summary tables at the grain the dashboard needs (daily totals, not individual transactions)
 - Expected improvement: 10–100× faster queries

 Materialized views / extracts:
 - Tableau: extract to .hyper file instead of live connection
 - Power BI: import mode instead of DirectQuery for non-real-time data
 - Looker: persistent derived tables (PDTs)
 - When to use live connection: only when data must be real-time (< 15-minute latency required)

 Caching:
 - Enable dashboard-level query caching
 - Set cache refresh to match data update frequency (no point refreshing every minute if data updates hourly)
 - User-level vs shared cache: shared cache serves the same query result to all users

 Query optimization:
 - Add indexes on filter columns (date, region, product category)
 - Partition tables by date for time-filtered queries
 - Push filters to the query level (not post-query in the viz layer)

3. Dashboard-layer optimizations:

 Reduce chart count:
 - Each chart = one or more queries
 - Remove or consolidate charts that answer the same question
 - Move supporting detail to a second page / click-through

 Lazy loading:
 - Load above-the-fold charts first, load below-the-fold on scroll
 - Show a loading spinner per chart rather than blocking the whole page

 Limit data points per chart:
 - Time series: aggregate to a coarser granularity (weekly instead of daily if trend is what matters)
 - Scatter plots: sample or bin large datasets
 - Tables: paginate or limit to top N rows with a 'load more' option

4. Benchmarks:
 - Target load time: < 3 seconds for first meaningful paint
 - Filter response: < 2 seconds for filter changes
 - Table pagination: < 1 second per page load

Return: bottleneck diagnosis, prioritized optimization list with estimated improvement per action, and implementation steps for the tool specified. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dashboard architecture work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Dashboard Architecture or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Diagnose the bottleneck:, Is the slow part the query or the rendering?, Enable query profiling in the tool — how long does each query take?. The final answer should stay clear, actionable, and easy to review inside a dashboard architecture workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Dashboard Architecture.
