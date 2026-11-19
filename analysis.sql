-- Replace table names if your SQL platform uses a different naming convention.

-- 1. Customer status and plan mix
SELECT plan, status, COUNT(*) AS customers
FROM customers
GROUP BY plan, status
ORDER BY plan, status;

-- 2. Snapshot MRR by plan (active subscriptions only)
SELECT plan, SUM(monthly_fee) AS snapshot_mrr
FROM customers
WHERE status = 'Active'
GROUP BY plan
ORDER BY snapshot_mrr DESC;

-- 3. Snapshot churn share by plan
SELECT
    plan,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) AS churned_customers,
    1.0 * SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) / COUNT(*) AS churn_share
FROM customers
GROUP BY plan
ORDER BY churn_share DESC;

-- 4. Average product engagement by customer status
SELECT
    c.status,
    AVG(u.sessions * 1.0) AS avg_sessions_per_customer_month,
    AVG(u.key_actions * 1.0) AS avg_key_actions_per_customer_month
FROM customers c
JOIN product_usage u ON c.customer_id = u.customer_id
GROUP BY c.status;

-- 5. Monthly product usage
SELECT
    month,
    SUM(sessions) AS total_sessions,
    SUM(key_actions) AS total_key_actions
FROM product_usage
GROUP BY month
ORDER BY month;
