# Power BI Quick Guide

The project includes `data/processed/pulsecart_clean.csv`, which is Power BI-ready.

### Beginner steps
1. Open Power BI Desktop.
2. Choose **Get Data → Text/CSV**.
3. Select `pulsecart_clean.csv`.
4. Load the data.
5. Create these visuals:
   - Card: total `revenue_90d`
   - Card: average `avg_order_value`
   - Card: average `repeat_purchase_30d` formatted as %
   - Clustered column: `region` vs `revenue_90d`
   - Column chart: `membership` vs average `repeat_purchase_30d`
   - Scatter: `days_since_last_purchase` vs `revenue_90d`
6. Add slicers for `region`, `membership`, and `device`.
7. Save as `PulseCart_Dashboard.pbix`.

The `.pbix` file is not generated automatically because it must be created in Power BI Desktop.
