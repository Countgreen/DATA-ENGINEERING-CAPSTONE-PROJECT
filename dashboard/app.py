import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/stream_data.csv")

st.set_page_config(page_title="Data Engineering Dashboard", layout="wide")

st.title("📊 Advanced Data Engineering Dashboard")

# =========================
# 🔹 KPIs
# =========================
st.subheader("📌 Key Metrics")

avg_price = df["price"].mean()
max_price = df["price"].max()
min_price = df["price"].min()

col1, col2, col3 = st.columns(3)

col1.metric("Average Price", round(avg_price, 2))
col2.metric("Max Price", max_price)
col3.metric("Min Price", min_price)

# =========================
# 🔹 Trend Detection
# =========================
st.subheader("📈 Trend Analysis")

trend = "Increasing 📈" if df["price"].iloc[-1] > df["price"].iloc[0] else "Decreasing 📉"
st.write(f"Overall Trend: **{trend}**")

# =========================
# 🔹 Simple Prediction
# =========================
st.subheader("🔮 Next Value Prediction")

# Simple prediction (last difference method)
if len(df) > 1:
    last_diff = df["price"].iloc[-1] - df["price"].iloc[-2]
    predicted = df["price"].iloc[-1] + last_diff
else:
    predicted = df["price"].iloc[-1]

st.success(f"Predicted Next Price: {round(predicted, 2)}")

# =========================
# 🔹 Charts
# =========================
st.subheader("📊 Price Trend")
st.line_chart(df["price"])

st.subheader("📊 Price Distribution")
st.bar_chart(df["price"])

# =========================
# 🔹 Stats Table
# =========================
st.subheader("📋 Statistical Summary")
st.write(df.describe())