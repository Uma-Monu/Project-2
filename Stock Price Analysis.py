import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "master_df.csv"

df = pd.read_csv(CSV_PATH)
df["date"]=pd.to_datetime(df["date"])

st.title(" Stock Analysis")

company=st.selectbox(
    "Select Stock",
    sorted(df["Ticker"].unique())
)

stock=df[df["Ticker"]==company]

col1,col2=st.columns(2)

with col1:

    fig=px.line(
        stock,
        x="date",
        y="close",
        title="Closing Price Trend"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig=px.bar(
        stock,
        x="date",
        y="volume",
        title="Volume Trend"
    )

    st.plotly_chart(fig,use_container_width=True)

st.subheader("Stock Data")

st.dataframe(stock)
