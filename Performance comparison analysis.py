import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "master_df.csv"

df = pd.read_csv(CSV_PATH)
df["date"] = pd.to_datetime(df["date"])


stock1 = st.selectbox("Select First Stock", sorted(df["Ticker"].unique()))
stock2 = st.selectbox("Select Second Stock", sorted(df["Ticker"].unique()))

compare = df[df["Ticker"].isin([stock1, stock2])]

fig = px.line(
    compare,
    x="date",
    y="close",
    color="Ticker",
    title="Stock Price Comparison"
)

st.plotly_chart(fig, use_container_width=True)

avg_close = (
    df.groupby("Ticker")["close"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    avg_close,
    x="Ticker",
    y="close",
    title="Top 10 Average Closing Prices"
)

st.plotly_chart(fig, use_container_width=True)

import plotly.express as px

corr = df[["open", "high", "low", "close"]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Between Stock Prices"
)

st.plotly_chart(fig, use_container_width=True)