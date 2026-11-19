# Power BI dashboard specification

## Page 1 — Executive overview
- KPI cards: Active Customers, Snapshot MRR, Snapshot Churn Share, Average Monthly Sessions.
- Line chart: monthly sessions and key actions.
- Bar chart: snapshot MRR by plan.
- Donut/bar chart: customer status distribution.

## Page 2 — Customer health
- Churn share by plan and country.
- Average sessions and key actions by customer status.
- Customer table with plan, country, status, and signup date.

## Suggested model
`customers[customer_id]` (one) → `product_usage[customer_id]` (many).

Use a proper date table for time intelligence. Clearly label MRR as a snapshot estimate because this sample does not contain subscription billing history.
