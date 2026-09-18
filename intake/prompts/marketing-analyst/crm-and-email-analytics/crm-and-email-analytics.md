# CRM and Email Analytics *AI Prompts *

4 Marketing Analyst prompts in CRM and Email Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in CRM and Email Analytics 
4 prompts Intermediate Single prompt 01 
### Customer Lifecycle Email Analysis 

Analyze the effectiveness of lifecycle email sequences and identify gaps in the program. Lifecycle data: {{lifecycle_data}} (email type, trigger event, send date, open, click, c... 
Prompt text Analyze the effectiveness of lifecycle email sequences and identify gaps in the program.

Lifecycle data: {{lifecycle_data}} (email type, trigger event, send date, open, click, conversion)
Customer journey stages: {{stages}} (onboarding, activation, engagement, expansion, retention, win-back)

1. Lifecycle email inventory:
 Map every automated email to the customer journey stage:
 - Trigger: what event sends this email?
 - Goal: what action should the recipient take?
 - Metric: how is success measured?

2. Coverage gaps:
 - Which stages have no automated email coverage?
 - Are there high-value moments in the customer journey with no triggered email?
 - Common gaps: post-onboarding engagement, pre-renewal reminder, post-cancellation win-back

3. Sequence performance:
 For each lifecycle sequence:
 - Open rate by email position (Email 1, 2, 3...): how quickly does engagement decay?
 - Click rate by position
 - Completion rate: what % of recipients receive all emails in the sequence?
 - Conversion rate: what % take the desired action?

4. Time-to-convert analysis:
 - From lifecycle email send to conversion: how long does it take?
 - Is there an optimal timing window? (Some emails may be sent too early or too late)

5. Optimization opportunities:
 - Sequences with lowest conversion rate: content or timing issue?
 - High open but low click sequences: strong subject line but weak email body
 - Low open sequences: timing, subject line, or sender name issue

6. Recommended additions:
 Based on the gap analysis, propose 3 new lifecycle automations:
 - Trigger event
 - Goal
 - Message approach
 - Expected impact on activation/retention/revenue metric

Return: lifecycle email inventory, coverage gap analysis, sequence performance table, and 3 recommended new automations. Copy prompt Open prompt details Advanced Single prompt 02 
### Customer LTV Calculation 

Calculate Customer Lifetime Value (LTV) using multiple methods and apply it to marketing decisions. Customer data: {{customer_data}} (cohort, revenue history, churn events) Busi... 
Prompt text Calculate Customer Lifetime Value (LTV) using multiple methods and apply it to marketing decisions.

Customer data: {{customer_data}} (cohort, revenue history, churn events)
Business model: {{business_model}}
Discount rate: {{discount_rate}} (cost of capital, typically 10-15%)

1. Simple LTV (for early-stage / approximate use):
 LTV = Average Purchase Value x Purchase Frequency x Customer Lifespan
 - Average Purchase Value: total revenue / total orders
 - Purchase Frequency: total orders / total unique customers per period
 - Customer Lifespan: 1 / Monthly Churn Rate (in months)
 - Gross Profit LTV: multiply by gross margin %

2. Cohort-based LTV (most accurate for historical data):
 - For each acquisition cohort: cumulative revenue per customer through each month of life
 - Plot the cumulative LTV curve: how does LTV grow as cohort ages?
 - LTV at 12 months, 24 months, and steady state
 - Are newer cohorts trending above or below older cohorts? (Improving or declining customer quality)

3. Discounted LTV (for financial decisions):
 Discounted LTV = sum over t: (Expected Cash Flow_t / (1 + r)^t)
 - Where r = monthly discount rate = (1 + annual rate)^(1/12) - 1
 - Cash flow_t = monthly gross profit from the cohort in month t
 - Captures the time value of money: a dollar of LTV received in year 3 is worth less than in year 1

4. LTV by segment:
 - LTV for different acquisition channels, customer segments, product categories, geographies
 - Which segments have 2x or higher LTV than average?
 - This should drive differential CAC targets by segment

5. LTV / CAC framework for marketing decisions:
 - Healthy: LTV / CAC > 3
 - Acceptable: LTV / CAC 1-3 (with path to improvement)
 - Unsustainable: LTV / CAC < 1
 - Maximum CAC by segment = LTV x maximum acceptable CAC ratio

6. LTV improvement levers:
 - Increase average order value (cross-sell, upsell)
 - Increase purchase frequency (engagement, reminder programs)
 - Reduce churn (retention programs)
 - For each lever: estimated impact on LTV

Return: LTV calculation by method, cohort LTV curves, segment LTV comparison, LTV/CAC framework, and LTV improvement lever analysis. Copy prompt Open prompt details Beginner Single prompt 03 
### Email Campaign Analysis 

Analyze the performance of this email campaign and identify optimization opportunities. Email data: {{email_data}} Campaign type: {{type}} (newsletter, promotional, lifecycle, t... 
Prompt text Analyze the performance of this email campaign and identify optimization opportunities.

Email data: {{email_data}}
Campaign type: {{type}} (newsletter, promotional, lifecycle, transactional)
Audience: {{audience_size}} recipients

1. Deliverability metrics:
 - Delivery rate: delivered / sent (target > 98%)
 - Bounce rate: hard + soft bounces / sent
 - Spam complaint rate: spam reports / delivered (target < 0.1%)
 - List health: what % of the list is engaged (opened at least once in 90 days)?

2. Engagement metrics:
 - Open rate: unique opens / delivered (benchmark varies by industry, typically 20-40%)
 - Click-to-open rate (CTOR): clicks / opens (measures email content quality, target > 10%)
 - Click rate: clicks / delivered
 - Unsubscribe rate: unsubscribes / delivered (target < 0.2%)

3. Conversion metrics:
 - Conversion rate: desired action completions / delivered
 - Revenue per email: total revenue attributed / emails delivered
 - Compare to target and prior campaigns

4. Timing analysis:
 - What day of week and time of day were emails sent?
 - Compare open rate and click rate at different send times (if A/B tested)
 - Industry best practice send times for this audience segment

5. Subject line analysis:
 - If A/B tested: winning subject line and the open rate lift
 - Characteristics of high-performing subject lines: length, personalization, urgency, question vs statement
 - Recommendation for next campaign

6. Segment performance:
 - Break engagement metrics by: customer segment, tenure, geography, prior engagement level
 - Which segment has the highest CTOR? Should receive more targeted sends.
 - Which segment has the lowest open rate? Review frequency, relevance, send time.

7. Optimization recommendations:
 - Top 3 actions to improve performance in the next send

Return: deliverability metrics, engagement analysis, conversion results, segment breakdown, and optimization recommendations. Copy prompt Open prompt details Intermediate Single prompt 04 
### Email List Health Audit 

Audit the health of this email list and build a re-engagement and list hygiene plan. List data: {{list_data}} (subscriber_id, subscribe_date, last_open_date, last_click_date, em... 
Prompt text Audit the health of this email list and build a re-engagement and list hygiene plan.

List data: {{list_data}} (subscriber_id, subscribe_date, last_open_date, last_click_date, email_type)
List size: {{list_size}}
Current engagement rate: {{engagement_rate}}

1. Engagement segmentation:
 Classify every subscriber into engagement tiers:
 - Active: opened or clicked in the last 90 days
 - Warming: opened or clicked 90-180 days ago
 - At-risk: last engaged 180-365 days ago
 - Inactive: no engagement in > 365 days
 - Never engaged: subscribed but never opened a single email

 Size and % of list in each tier.

2. List decay rate:
 - How quickly is the active tier shrinking as a % of total?
 - Monthly new subscribers vs monthly subscribers moving to inactive
 - If inactive subscribers > 30% of list: email deliverability is at risk

3. Impact on deliverability:
 - High inactive rates signal to ISPs that your emails are unwanted
 - Gmail, Outlook, and Apple Mail track engagement heavily
 - Estimated deliverability risk: at current inactive %, what is the projected impact on inbox placement?

4. Re-engagement campaign design:
 For the 'At-risk' tier:
 - Trigger: 180 days since last open
 - Sequence: 3-email re-engagement series
 - Email 1: 'We miss you' + best recent content
 - Email 2: Incentive offer or value reminder
 - Email 3: 'Last chance' + explicit opt-down/unsubscribe option
 - Success criteria: any open or click = move back to 'Warming' tier

5. Sunset policy:
 - After the re-engagement sequence: move non-responders to suppression list
 - Do NOT delete: keep suppressed for compliance (unsubscribe proof)
 - Expected list size reduction and engagement rate improvement from sunset

6. List growth quality:
 - Which acquisition sources are producing the highest-engagement subscribers?
 - Which sources produce low-engagement (likely purchased or low-intent) subscribers?
 - Stop acquiring from low-quality sources even if it slows list growth

Return: engagement tier breakdown, list decay analysis, re-engagement sequence, sunset policy, and acquisition source quality assessment. Copy prompt Open prompt details 
## Recommended CRM and Email Analytics workflow 
1 
### Customer Lifecycle Email Analysis 

Start with a focused prompt in CRM and Email Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Customer LTV Calculation 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Email Campaign Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Email List Health Audit 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
