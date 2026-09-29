# PulseCart Predictive Intelligence — Project Report

## 1. Executive Summary
PulseCart is a beginner-friendly analytics project for an e-commerce business.
It studies customer behavior, revenue, and repeat-purchase likelihood using a
synthetic dataset of 5,000 customer records.

## 2. Business Questions
- Which regions generate the most 90-day revenue?
- How does membership relate to repeat purchase behavior?
- Which customers have high value but long purchase gaps?
- Can a simple machine-learning model estimate repeat-purchase probability?

## 3. Data
The dataset is synthetic and reproducible. It contains customer attributes,
engagement signals, purchase history, service signals, and outcomes.

Important fields include:
- `sessions_30d`
- `orders_90d`
- `avg_order_value`
- `days_since_last_purchase`
- `membership`
- `revenue_90d`
- `repeat_purchase_30d`

## 4. Preprocessing
1. Read CSV with pandas.
2. Convert the purchase date to a date type.
3. Convert numeric fields safely.
4. Fill numeric missing values with the median.
5. Create `customer_value_band`.
6. Create a simple `engagement_score`.

## 5. SQL
The project includes a SQLite database and beginner SQL queries for:
- regional revenue
- repeat rate by membership
- acquisition-channel revenue
- high-value customers with long recency

## 6. Machine Learning
A Logistic Regression model predicts `repeat_purchase_30d`.
A Linear Regression model provides a simple revenue benchmark.

The models are intentionally simple and explainable so a beginner can understand
the workflow instead of using a black-box algorithm.

## 7. Dashboard
The Streamlit dashboard includes:
- KPI cards
- revenue by region
- repeat rate by membership
- recency vs revenue scatter plot
- customer value segmentation
- region and membership filters

## 8. Business Recommendations
These are learning-oriented recommendations rather than real customer decisions:
1. Review high-value customers with long purchase gaps.
2. Compare repeat rates across membership groups.
3. Investigate channels that produce both revenue and repeat customers.
4. Use the model as a prioritization aid, not as a final business decision.

## 9. Limitations
- Data is synthetic.
- It does not represent a real company's customers.
- Model quality may not transfer to real-world data.
- No claim should be made that the model is production-ready.

## 10. Reproducibility
Random seed = 42.
Run the preprocessing and model scripts from the project root.

## 11. Reproducible baseline metrics
- Rows: 5,000
- Repeat-purchase accuracy on the holdout set: 0.672
- Revenue MAE: ₹26.40
- Revenue R²: 0.800
- Dataset repeat-purchase rate: 65.28%
- Synthetic 90-day revenue: ₹509,492.13

These numbers are only baseline results on the synthetic dataset.
