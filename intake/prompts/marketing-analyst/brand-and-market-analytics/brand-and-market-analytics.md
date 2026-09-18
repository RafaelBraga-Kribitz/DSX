# Brand and Market Analytics *AI Prompts *

4 Marketing Analyst prompts in Brand and Market Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate levels and 4 single prompts. 

## AI prompts in Brand and Market Analytics 
4 prompts Intermediate Single prompt 01 
### Brand Sentiment Analysis 

Analyze brand sentiment from customer reviews, social mentions, and survey data. Data sources: {{data_sources}} (reviews, social listening, NPS survey, support tickets) Time per... 
Prompt text Analyze brand sentiment from customer reviews, social mentions, and survey data.

Data sources: {{data_sources}} (reviews, social listening, NPS survey, support tickets)
Time period: {{period}}
Competitors to compare: {{competitors}}

1. Sentiment scoring:
 For each text data source:
 - Classify each item as: Positive, Neutral, Negative
 - Sentiment score: (Positive - Negative) / Total
 - Track sentiment score over time
 - Volume by sentiment category per period

2. Theme extraction:
 - Use topic modeling or keyword clustering to identify the main themes in reviews/mentions
 - For each theme: count of mentions, sentiment split, trend over time
 - Positive themes: what do customers love most? (Product quality, service, value, ease of use)
 - Negative themes: what are the biggest complaints? (Price, reliability, support, missing features)

3. NPS driver analysis:
 - Promoters (9-10): what do they consistently praise?
 - Passives (7-8): what would convert them to promoters?
 - Detractors (0-6): what are the primary complaint themes?
 - For each NPS segment: top 3 verbatim themes

4. Competitive sentiment comparison:
 - Overall sentiment score vs competitors
 - Which themes does our brand win on vs competitors?
 - Which themes do competitors win on? (Areas to improve)

5. Sentiment anomalies:
 - Any spikes in negative sentiment? What triggered them? (Product issue, PR event, policy change)
 - Any unexpected positive spikes? What can we replicate?

6. Marketing implications:
 - Which proven positive themes should be amplified in marketing messages?
 - Which negative themes represent reputation risks that marketing must address?

Return: sentiment score trends, theme analysis, NPS driver breakdown, competitive comparison, and marketing implications. Copy prompt Open prompt details Intermediate Single prompt 02 
### Competitor Analysis Framework 

Build a competitive marketing intelligence framework for {{company}}. Competitors: {{competitor_list}} Analysis dimensions: {{dimensions}} 1. Digital presence benchmarking: For... 
Prompt text Build a competitive marketing intelligence framework for {{company}}.

Competitors: {{competitor_list}}
Analysis dimensions: {{dimensions}}

1. Digital presence benchmarking:
 For each competitor:
 - Website traffic estimate (SimilarWeb, SEMrush)
 - Organic keyword ranking count and estimated traffic
 - Paid search spend estimate (SEMrush, SpyFu)
 - Social media followers and engagement rate by platform
 - App store ratings and review count (if applicable)

2. SEO competitive analysis:
 - Keyword gap: keywords competitors rank for that we do not
 - Content gap: topics competitors have content on that we do not
 - Backlink comparison: domain authority and linking root domains
 - Top content by traffic for each competitor

3. Paid advertising analysis:
 - Estimated monthly paid search spend per competitor
 - Ad copy analysis: what messages and value propositions are they using?
 - Landing page analysis: what does their conversion experience look like?
 - Facebook Ad Library: active social ad creative and messaging

4. Messaging and positioning:
 - For each competitor: primary value proposition (from homepage)
 - Target audience stated or implied
 - Key differentiators claimed
 - Pricing tier and model (if visible)
 - Create a positioning map: plot competitors on 2 axes (e.g. price vs feature depth)

5. Share of voice:
 - Estimated organic search share of voice for target keyword set
 - Social mention volume comparison
 - PR and news coverage volume

6. Competitive threats and opportunities:
 - Where are competitors investing heavily? (Threat)
 - Where are competitors weak? (Opportunity)
 - What positioning gaps exist that no competitor is occupying?

Return: competitor benchmarking table, SEO gap analysis, paid ad insights, positioning map, share of voice, and threat/opportunity matrix. Copy prompt Open prompt details Intermediate Single prompt 03 
### Market Sizing Analysis 

Estimate the Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for this business. Business: {{business_description}}... 
Prompt text Estimate the Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for this business.

Business: {{business_description}}
Product/service: {{product}}
Geography: {{geography}}

1. TAM (Total Addressable Market):
 The total market demand if the product captured 100% of the market.

 Top-down approach:
 - Start with a published industry market size (from Gartner, IDC, IBISWorld, etc.)
 - Narrow to the specific segment relevant to this product
 - Adjust for the geographic scope

 Bottom-up approach:
 - Count the number of potential customers (from public data, census, industry directories)
 - Estimate average annual spend per customer
 - TAM = customer count x average spend
 - Use both approaches and triangulate

2. SAM (Serviceable Addressable Market):
 The portion of TAM that can realistically be served given product scope, geography, and channel.
 - Exclude segments the product is not designed for
 - Exclude geographies where the company does not or cannot operate
 - Exclude customer sizes that do not match the go-to-market motion

3. SOM (Serviceable Obtainable Market):
 The realistic market share the business can capture in 3-5 years.
 - Benchmark against comparable companies at similar stages
 - Consider: competitive intensity, sales capacity, brand awareness, capital available
 - Typical SOM = 1-10% of SAM in year 3-5 for venture-stage companies

4. Market growth rate:
 - Historical CAGR of the market
 - Forward-looking drivers: what is accelerating or decelerating market growth?
 - TAM in 5 years at current growth rate

5. Sanity check:
 - Revenue target / SOM: what market share does the business plan imply?
 - Is that market share realistic given competitors and market dynamics?

Return: TAM, SAM, and SOM estimates with both top-down and bottom-up methodology, market growth rate, and sanity check on business plan assumptions. Copy prompt Open prompt details Intermediate Single prompt 04 
### Survey Analysis for Marketing Insights 

Analyze this marketing survey and extract actionable insights. Survey data: {{survey_data}} Survey type: {{survey_type}} (NPS, CSAT, brand awareness, customer effort, market res... 
Prompt text Analyze this marketing survey and extract actionable insights.

Survey data: {{survey_data}}
Survey type: {{survey_type}} (NPS, CSAT, brand awareness, customer effort, market research)
Respondents: {{n_respondents}}

1. Response quality check:
 - Response rate and completion rate
 - Speeders: respondents who completed the survey in < 30% of median time (unreliable data)
 - Straightliners: respondents who gave the same answer to every scale question
 - Recommend excluding speeders and straightliners from analysis

2. Quantitative analysis:
 - For each closed-ended question: frequency distribution (count and % per response option)
 - For scale questions (1-10 NPS, 1-5 satisfaction): mean, median, standard deviation
 - Cross-tabulation: how do responses differ by key demographic or segment?

3. NPS analysis (if applicable):
 - Promoters (9-10), Passives (7-8), Detractors (0-6): count and %
 - NPS = % Promoters - % Detractors
 - NPS by segment: which customer group has the highest / lowest NPS?
 - NPS trend vs prior survey wave

4. Open-text analysis:
 - Theme extraction: top 10 themes from open-ended responses
 - Sentiment per theme: positive, neutral, negative
 - Volume and sentiment for: Promoters vs Detractors vs Passives
 - Most actionable verbatims: select 5 representative quotes per theme

5. Correlation with behavior:
 - Match survey respondents to CRM/behavioral data
 - Do high-NPS customers actually have higher retention rates?
 - Do customers who cite price as a concern have higher churn rates?

6. Marketing implications:
 - Promoter themes to amplify in marketing messaging
 - Detractor themes that are reputation risks to address
 - Awareness and perception gaps revealed by the survey

Return: response quality check, quantitative summary, NPS calculation, theme analysis, behavioral correlation, and marketing implications. Copy prompt Open prompt details 
## Recommended Brand and Market Analytics workflow 
1 
### Brand Sentiment Analysis 

Start with a focused prompt in Brand and Market Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Competitor Analysis Framework 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Market Sizing Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Survey Analysis for Marketing Insights 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
