# Inventory Analytics *AI Prompt *

Analyze inventory performance and identify stock-out and overstock risks. Inventory data: {{inventory_data}} (SKU, units_on_hand, daily_sales_rate, lead_time_days, reorder_point... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze inventory performance and identify stock-out and overstock risks.

Inventory data: {{inventory_data}} (SKU, units_on_hand, daily_sales_rate, lead_time_days, reorder_point)
Sales data: {{sales_data}}

1. Inventory coverage analysis:
 - Days of Inventory Outstanding (DIO): units_on_hand / average_daily_sales_rate
 - Flag: DIO > 90 days = likely overstock
 - Flag: DIO < 14 days = reorder urgently (below safety stock for most lead times)
 - Distribution of DIO across the catalog

2. Stock-out risk assessment:
 - Products with DIO < lead_time_days: will stock out before reorder arrives
 - Products currently at zero inventory: lost sales occurring now
 - Lost revenue estimate from out-of-stocks:
 Out-of-stock loss = (days_out_of_stock x average_daily_revenue_when_in_stock)

3. Overstock identification:
 - Products with DIO > 90 days: cash and storage tied up unproductively
 - Total overstock value: units_excess x unit_cost (units_excess = inventory - 90 days supply)
 - Products with declining sales trend: overstock risk is growing over time

4. Reorder point calculation:
 Reorder Point = (Average Daily Sales x Lead Time) + Safety Stock
 Safety Stock = Z x Standard Deviation of Demand x sqrt(Lead Time)
 - Z = 1.65 for 95% service level, 2.05 for 98%
 - Compare current reorder points to calculated optimal reorder points

5. ABC classification:
 - A items: top 20% of products by revenue (80% of revenue) - high control
 - B items: next 30% of products (15% of revenue) - moderate control
 - C items: bottom 50% of products (5% of revenue) - minimal control
 - A items should never stock out; C items can have lower service levels

6. Inventory optimization actions:
 - Immediate: order products in stock-out risk category
 - Short term: markdown or bundle overstock items to release cash
 - Medium term: revise reorder points and safety stock levels for top-50 SKUs

Return: DIO distribution, stock-out risk list with lost revenue, overstock list with excess value, optimized reorder points, ABC classification, and action priorities. 
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

The AI should return a structured result that covers the main requested outputs, such as Inventory coverage analysis:, Days of Inventory Outstanding (DIO): units_on_hand / average_daily_sales_rate, Flag: DIO > 90 days = likely overstock. The final answer should stay clear, actionable, and easy to review inside a merchandising analytics workflow for ecommerce analyst work. 

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
