import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("data/customers.csv", parse_dates=["signup_date", "churn_date"])
usage = pd.read_csv("data/product_usage.csv", parse_dates=["month"])

# Basic quality checks
print("Customers:", customers.shape)
print("Duplicate customer IDs:", customers["customer_id"].duplicated().sum())
print("Missing values:\n", customers.isna().sum())

active = customers[customers["status"].eq("Active")]
mrr = active["monthly_fee"].sum()
churn_rate = customers["status"].eq("Churned").mean()

print(f"Snapshot active customers: {len(active):,}")
print(f"Snapshot MRR: ${mrr:,.2f}")
print(f"Snapshot customer churn share: {churn_rate:.1%}")

print("\nCustomers by plan and status:")
print(pd.crosstab(customers["plan"], customers["status"]))

usage_monthly = usage.groupby("month", as_index=False).agg(
    sessions=("sessions", "sum"),
    key_actions=("key_actions", "sum"),
    support_tickets=("support_tickets", "sum")
)
print("\nMonthly product usage:")
print(usage_monthly.tail())

plan_summary = customers.groupby("plan", as_index=False).agg(
    customers=("customer_id", "count"),
    active_customers=("status", lambda s: (s == "Active").sum()),
    monthly_fee=("monthly_fee", "first")
)
plan_summary["snapshot_mrr"] = customers[customers.status.eq("Active")].groupby("plan")["monthly_fee"].sum().reindex(plan_summary["plan"]).values
print("\nPlan summary:")
print(plan_summary)

usage.to_csv("usage_monthly_source.csv", index=False)
