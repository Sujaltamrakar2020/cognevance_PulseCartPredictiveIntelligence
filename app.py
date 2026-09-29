import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "pulsecart_clean.csv"

st.set_page_config(
    page_title="PulseCart Intelligence",
    page_icon="📦",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(DATA)

df = load_data()

st.title("📦 PulseCart Intelligence")
st.caption("A beginner-friendly customer behavior & repeat-purchase analytics lab")

# Sidebar filters
st.sidebar.header("Explore the customer base")
region = st.sidebar.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
membership = st.sidebar.multiselect("Membership", sorted(df["membership"].unique()), default=sorted(df["membership"].unique()))

filtered = df[df["region"].isin(region) & df["membership"].isin(membership)].copy()

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Customers", f"{len(filtered):,}")
c2.metric("90d Revenue", f"₹{filtered['revenue_90d'].sum():,.0f}")
c3.metric("Repeat Rate", f"{filtered['repeat_purchase_30d'].mean()*100:.1f}%")
c4.metric("Avg Order Value", f"₹{filtered['avg_order_value'].mean():.2f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Revenue by Region")
    region_rev = filtered.groupby("region", as_index=False)["revenue_90d"].sum()
    fig = px.bar(region_rev, x="region", y="revenue_90d", title="90-day revenue")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Repeat Purchase by Membership")
    repeat = filtered.groupby("membership", as_index=False)["repeat_purchase_30d"].mean()
    repeat["repeat_rate"] = repeat["repeat_purchase_30d"] * 100
    fig2 = px.bar(repeat, x="membership", y="repeat_rate", title="Repeat rate (%)")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Customer Value Map")
fig3 = px.scatter(
    filtered,
    x="days_since_last_purchase",
    y="revenue_90d",
    size="orders_90d",
    color="membership",
    hover_data=["customer_id", "region", "repeat_label"],
    title="Recency vs 90-day revenue"
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Simple Customer Segments")
segment = filtered.groupby("customer_value_band", observed=True).agg(
    customers=("customer_id", "count"),
    revenue=("revenue_90d", "sum"),
    repeat_rate=("repeat_purchase_30d", "mean")
).reset_index()
segment["repeat_rate"] = (segment["repeat_rate"] * 100).round(1)
st.dataframe(segment, use_container_width=True)

st.subheader("Business Notes")
st.info(
    "Use this dashboard to spot customers with high revenue but long recency, "
    "compare acquisition channels, and test simple retention ideas. "
    "The dataset is synthetic and is intended for learning/demo purposes."
)

st.caption("PulseCart • Built with Python, pandas, scikit-learn, Plotly and Streamlit")
