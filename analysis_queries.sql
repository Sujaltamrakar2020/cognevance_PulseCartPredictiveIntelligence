-- PulseCart beginner-friendly SQL examples

-- 1. Revenue by region
SELECT region, ROUND(SUM(revenue_90d), 2) AS revenue
FROM customers
GROUP BY region
ORDER BY revenue DESC;

-- 2. Repeat purchase rate by membership
SELECT membership,
       ROUND(AVG(repeat_purchase_30d) * 100, 2) AS repeat_rate_pct
FROM customers
GROUP BY membership
ORDER BY repeat_rate_pct DESC;

-- 3. Top acquisition channels by revenue
SELECT acquisition_channel,
       ROUND(SUM(revenue_90d), 2) AS revenue,
       COUNT(*) AS customers
FROM customers
GROUP BY acquisition_channel
ORDER BY revenue DESC;

-- 4. High-value customers who have not purchased recently
SELECT customer_id, region, membership, revenue_90d,
       days_since_last_purchase
FROM customers
WHERE revenue_90d >= 300
  AND days_since_last_purchase >= 60
ORDER BY revenue_90d DESC;
