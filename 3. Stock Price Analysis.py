import streamlit as st
import pandas as pd
import plotly.express as px


st.title(" Stock Price Analysis")


df = pd.read_csv("master_df.csv")


# Price trend

fig = px.line(
    df,
    x="Date",
    y="Close",
    title="Closing Price Trend"
)

st.plotly_chart(fig)


# Volume Analysis

fig2 = px.bar(
    df.head(20),
    x="Ticker",
    y="Vol.",
    title="Stock Volume"
)

st.plotly_chart(fig2)