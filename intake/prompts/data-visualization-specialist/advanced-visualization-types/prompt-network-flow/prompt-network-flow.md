# Network and Flow Visualization *AI Prompt *

Design a visualization for network or flow data. Data type: {{data_type}} (customer journey, supply chain, relationship network, conversion funnel, Sankey flow) Nodes: {{nodes}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a visualization for network or flow data.

Data type: {{data_type}} (customer journey, supply chain, relationship network, conversion funnel, Sankey flow)
Nodes: {{nodes}} (entities)
Edges: {{edges}} (relationships or flows between entities)
Key question: {{question}}

1. Chart type selection:

 Sankey diagram:
 - Shows flow volumes between stages or categories
 - Best for: conversion funnels, budget allocation, material flows
 - Read: width of each flow proportional to volume
 - Limit: < 20 nodes; > 20 becomes unreadable without interaction
 - Tool: Plotly, D3.js, Google Charts

 Alluvial diagram:
 - A Sankey variant showing how categories change over time or across dimensions
 - Best for: before-after category changes, cohort migration
 - Example: how customers moved between subscription tiers from Q1 to Q4

 Network graph:
 - Nodes and edges showing relationships
 - Best for: social networks, dependency graphs, knowledge graphs
 - Layouts:
 - Force-directed: natural clustering, no hierarchy
 - Hierarchical: for tree structures (org chart, taxonomy)
 - Circular: for dense networks where crossing edges are unavoidable
 - Color nodes by: category, cluster membership, or a metric
 - Size nodes by: degree centrality, importance, volume
 - Edge width: proportional to relationship strength

 Chord diagram:
 - Circular diagram showing flows between all pairs of groups
 - Best for: mutual flows (trade between countries, team collaboration)
 - Harder to read than Sankey — use only when bidirectional flows are both important

 Arc diagram:
 - Nodes on a line with arcs above showing connections
 - Best for: temporal networks where order matters

2. Managing complexity:
 - > 50 nodes: aggregate less important nodes into 'Other' category
 - Filter controls: allow users to filter to relevant subgraphs
 - Highlight on hover: fade all non-connected nodes and edges when hovering
 - Community detection: use clustering algorithm to group related nodes; color by cluster

3. Performance for large networks:
 - > 500 nodes: use WebGL-based rendering (Sigma.js, GPU.js)
 - Static alternative: aggregate to a summary view with interactive drill-down

Return: chart type recommendation, layout specification, node and edge encoding, complexity management approach, and tool recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin advanced visualization types work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Advanced Visualization Types or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Chart type selection:, Shows flow volumes between stages or categories, Best for: conversion funnels, budget allocation, material flows. The final answer should stay clear, actionable, and easy to review inside a advanced visualization types workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Advanced Visualization Types.
