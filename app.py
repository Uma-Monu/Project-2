import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Stock Analysis Dashboard",
                   page_icon="📈",
                   layout="wide")

# Load Data
df = pd.read_csv("data/master_df.csv")
df["date"] = pd.to_datetime(df["date"])

st.title("Data-Driven Stock Analysis Dashboard")
st.markdown("### Nifty 50 Stock Performance Analysis")

#performance metrics

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Stocks", df["Ticker"].nunique())
col2.metric("Total Records", len(df))
col3.metric("Avg Close Price", round(df["close"].mean(),2))
col4.metric("Avg Volume", f"{df['volume'].mean():,.0f}")

st.divider()

#Marketing prices over time

market = df.groupby("date")["close"].mean().reset_index()

fig = px.line(
    market,
    x="date",
    y="close",
    title="Average Market Closing Price",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

#Avg Volume by Ticker

top_volume = (
    df.groupby("Ticker")["volume"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig2 = px.bar(
    top_volume,
    x="Ticker",
    y="volume",
    color="volume",
    title="Top 10 Stocks by Average Volume"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)