import pandas as pd
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]
MODEL = joblib.load(ROOT / "reports" / "repeat_purchase_model.joblib")

def predict_customer(customer_row: dict) -> float:
    sample = pd.DataFrame([customer_row])
    probability = MODEL.predict_proba(sample)[0, 1]
    return round(float(probability), 3)

if __name__ == "__main__":
    example = {
        "age": 29, "region": "Central", "device": "Mobile",
        "acquisition_channel": "Referral", "membership": "Regular",
        "days_since_last_purchase": 18, "sessions_30d": 7,
        "orders_90d": 3, "items_90d": 7, "avg_order_value": 55,
        "discount_pct": 10, "support_tickets": 0, "returns_90d": 0,
        "review_score": 4.5
    }
    print("Example repeat-purchase probability:", predict_customer(example))
