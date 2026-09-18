# Correlation Structure Analysis *AI Prompt *

Analyze the correlation structure of this multi-asset portfolio and identify instabilities. Assets: {{asset_list}} Return frequency: {{frequency}} Period: {{period}} 1. Static c... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the correlation structure of this multi-asset portfolio and identify instabilities.

Assets: {{asset_list}}
Return frequency: {{frequency}}
Period: {{period}}

1. Static correlation matrix:
 - Compute Pearson correlation matrix
 - Visualize as heatmap with hierarchical clustering (assets with similar correlations grouped together)
 - Report the range: minimum and maximum pairwise correlations
 - Flag pairs with correlation > 0.9 (potential redundancy) and < -0.5 (potential hedge)

2. Robust correlation estimation:
 Pearson correlation is sensitive to outliers. Apply:
 - Spearman rank correlation: robust to outliers, captures monotonic relationships
 - Ledoit-Wolf shrinkage: regularized covariance matrix — critical for portfolio optimization with many assets
 - Minimum covariance determinant (MCD): downweights outliers automatically
 Compare: how much do robust estimates differ from Pearson for each pair?

3. Rolling correlation analysis:
 - 63-day rolling pairwise correlations for all pairs
 - Plot selected pairs over time
 - Identify correlation regime changes: periods when correlations were notably higher or lower
 - Crisis correlation: do correlations spike during market stress? (Diversification typically fails when needed most)

4. Principal Component Analysis (PCA):
 - Apply PCA to the correlation matrix
 - Report: variance explained by each PC (scree plot)
 - How many PCs explain 80% of variance? (Indicates effective dimensionality of the portfolio)
 - PC1 loadings: usually the 'market factor' — uniform positive loadings on all assets
 - PC2 onward: often sector or style tilts
 - Track PC1 explained variance over time: rising explained variance indicates increasing co-movement (correlation risk)

5. Instability metrics:
 - Correlation instability index: average change in pairwise correlations across rolling windows
 - Lowest-correlation period vs highest-correlation period: what drove the change?
 - Correlation between asset pairs during down markets vs up markets (asymmetric correlation)

6. Implications for portfolio construction:
 - Which correlations are most unstable? (Least reliable for diversification)
 - What is the maximum theoretical diversification benefit given current correlations?

Return: correlation matrix heatmap, Ledoit-Wolf estimate, rolling correlation plots, PCA results, instability metrics, and portfolio construction implications. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial data analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Data Analysis or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Static correlation matrix:, Compute Pearson correlation matrix, Visualize as heatmap with hierarchical clustering (assets with similar correlations grouped together). The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Data Analysis.
