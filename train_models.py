import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error, r2_score
import joblib

ROOT = Path(__file__).resolve().parents[1]

df = pd.read_csv(ROOT / "data" / "processed" / "pulsecart_clean.csv")

# -------- Repeat-purchase model --------
features = [
    "age", "region", "device", "acquisition_channel", "membership",
    "days_since_last_purchase", "sessions_30d", "orders_90d", "items_90d",
    "avg_order_value", "discount_pct", "support_tickets", "returns_90d",
    "review_score"
]
target = "repeat_purchase_30d"

X = df[features]
y = df[target]

cat = ["region", "device", "acquisition_channel", "membership"]
num = [c for c in features if c not in cat]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
    ("num", StandardScaler(), num)
])

classifier = Pipeline([
    ("prep", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)

print("Repeat-purchase accuracy:", round(accuracy_score(y_test, pred), 3))
print(classification_report(y_test, pred, zero_division=0))

joblib.dump(classifier, ROOT / "reports" / "repeat_purchase_model.joblib")

# -------- Revenue model --------
rev_features = [
    "orders_90d", "items_90d", "avg_order_value",
    "discount_pct", "sessions_30d", "review_score"
]
Xr = df[rev_features]
yr = df["revenue_90d"]

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    Xr, yr, test_size=0.2, random_state=42
)

reg = LinearRegression()
reg.fit(Xr_train, yr_train)
rev_pred = reg.predict(Xr_test)

print("Revenue MAE:", round(mean_absolute_error(yr_test, rev_pred), 2))
print("Revenue R2:", round(r2_score(yr_test, rev_pred), 3))

joblib.dump(reg, ROOT / "reports" / "revenue_model.joblib")
