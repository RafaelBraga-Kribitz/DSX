# Multi-Touch Attribution for Product *AI Prompt *

Analyze which in-product touchpoints and features most contribute to conversion or activation. User journey data: {{journey_data}} (user_id, touchpoint_type, touchpoint_timestam... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze which in-product touchpoints and features most contribute to conversion or activation.

User journey data: {{journey_data}} (user_id, touchpoint_type, touchpoint_timestamp, converted: Y/N)
Conversion event: {{conversion_event}} (e.g. first purchase, plan upgrade, feature activation)

1. Touchpoint inventory:
 - List all unique touchpoints users encounter before the conversion event
 - Count how often each appears in converting vs non-converting journeys
 - What % of converters touched each touchpoint?

2. Attribution models - compare all three:

 First touch:
 - 100% credit to the first touchpoint the user interacted with
 - Best for: understanding what initiates the conversion journey

 Last touch:
 - 100% credit to the touchpoint immediately before conversion
 - Best for: understanding what closes the conversion

 Linear:
 - Equal credit to all touchpoints in the path
 - Best for: understanding overall touchpoint contribution

3. Path analysis:
 - What are the top 10 most common touchpoint sequences for converters?
 - What sequences do non-converters follow? Where do they diverge?
 - Is there a specific touchpoint combination that strongly predicts conversion?

4. Time-to-conversion by path:
 - Do users with certain touchpoint paths convert faster?
 - Is there a touchpoint that accelerates conversion when added to the path?

5. Recommendations:
 - Which touchpoints should be promoted (high attribution, currently under-used)?
 - Which touchpoints appear to delay or interrupt conversion?
 - What is the optimal path to guide new users through?

Return: touchpoint attribution table (all three models), top conversion paths, path divergence analysis, and recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin funnel analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Funnel Analysis or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Touchpoint inventory:, List all unique touchpoints users encounter before the conversion event, Count how often each appears in converting vs non-converting journeys. The final answer should stay clear, actionable, and easy to review inside a funnel analysis workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Funnel Analysis.
