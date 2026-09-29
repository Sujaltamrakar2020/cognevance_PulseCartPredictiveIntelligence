import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_and_prepare():
    path = ROOT / "data" / "raw" / "pulsecart_customers.csv"
    df = pd.read_csv(path)

    # Beginner-friendly cleaning
    df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])
    numeric_cols = [
        "age", "days_since_last_purchase", "sessions_30d", "orders_90d",
        "items_90d", "avg_order_value", "discount_pct", "support_tickets",
        "returns_90d", "review_score", "revenue_90d", "repeat_purchase_30d"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    df["customer_value_band"] = pd.cut(
        df["revenue_90d"],
        bins=[-1, 50, 150, 300, float("inf")],
        labels=["Starter", "Growing", "Valued", "VIP"]
    )

    df["engagement_score"] = (
        df["sessions_30d"] * 2
        + df["orders_90d"] * 3
        + df["review_score"] * 2
        - df["support_tickets"]
        - df["returns_90d"]
    ).round(2)

    return df

if __name__ == "__main__":
    clean = load_and_prepare()
    out = ROOT / "data" / "processed" / "pulsecart_clean.csv"
    clean.to_csv(out, index=False)
    print(f"Saved {len(clean):,} rows to {out}")
