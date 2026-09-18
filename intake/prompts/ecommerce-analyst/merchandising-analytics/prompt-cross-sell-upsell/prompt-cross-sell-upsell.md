# Cross-Sell and Upsell Analysis *AI Prompt *

Analyze cross-sell and upsell opportunities to increase average order value and customer LTV. Order data: {{order_data}} (order_id, customer_id, product_ids, quantities, values)... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze cross-sell and upsell opportunities to increase average order value and customer LTV.

Order data: {{order_data}} (order_id, customer_id, product_ids, quantities, values)
Product catalog: {{catalog}}

1. Market basket analysis:
 Compute product affinity using association rules:
 - Support: % of orders containing both product A and product B
 - Confidence: given product A, what % of those orders also contain product B?
 - Lift: how much more likely is product B in the basket given product A (vs random chance)?
 Lift > 1: products are bought together more than by chance

 Find the top 20 product pairs by lift score (minimum support = 1% of orders, minimum confidence = 20%)

2. Category cross-sell patterns:
 - Which pairs of product categories are most frequently purchased together?
 - Which categories are under-crosssold? (Frequently ordered independently but rarely together)
 - Are there natural product bundles the data suggests?

3. Sequential purchase analysis:
 - After purchasing product A, what does the customer buy in their next order?
 - Time between purchase A and related purchase B: how long do we have to suggest the cross-sell?
 - This drives post-purchase email timing and content

4. Upsell opportunities:
 - Products where customers frequently upgrade to a higher-priced variant after initial purchase
 - Product categories where the second purchase is at a higher price point than the first
 - Which products serve as 'entry points' that lead to higher-value subsequent purchases?

5. Bundle creation recommendations:
 - Based on affinity analysis: top 5 product bundle opportunities
 - For each bundle: expected AOV lift, current % of customers who buy both individually
 - Bundle pricing strategy: slight discount vs individual sum (3-7% discount typical)

6. Implementation recommendations:
 - Product page 'Frequently Bought Together': use top affinity pairs
 - Cart page 'Add to your order': show the highest-confidence cross-sell for items in cart
 - Post-purchase email: trigger with the sequential purchase insight (timing and product)
 - Bundle listings: create bundles for top affinity pairs

Return: top association rules table, category cross-sell matrix, sequential purchase analysis, upsell patterns, bundle recommendations, and implementation priorities. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin merchandising analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Merchandising Analytics or the wider Ecommerce Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Market basket analysis:, Support: % of orders containing both product A and product B, Confidence: given product A, what % of those orders also contain product B?. The final answer should stay clear, actionable, and easy to review inside a merchandising analytics workflow for ecommerce analyst work. 

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

Once you have the first result, continue deeper with related prompts in Merchandising Analytics.
