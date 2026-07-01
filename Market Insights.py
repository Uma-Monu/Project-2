import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "master_df.csv"

df = pd.read_csv(CSV_PATH)

df["date"]=pd.to_datetime(df["date"])

df=df.sort_values(["Ticker","date"])

returns=(
    df.groupby("Ticker")
      .agg(
          First_Close=("close","first"),
          Last_Close=("close","last")
      )
)

returns["Yearly Return (%)"]=(
    (returns["Last_Close"]-returns["First_Close"])
    /returns["First_Close"]
)*100

returns=returns.reset_index()

top_green=returns.sort_values(
    "Yearly Return (%)",
    ascending=False
).head(10)

top_loss=returns.sort_values(
    "Yearly Return (%)"
).head(10)

green=(returns["Yearly Return (%)"]>0).sum()
red=(returns["Yearly Return (%)"]<0).sum()

avg_price=df["close"].mean()
avg_volume=df["volume"].mean()

st.title("📊 Market Insights")

c1,c2,c3,c4=st.columns(4)

c1.metric(" Green Stocks",green)
c2.metric(" Red Stocks",red)
c3.metric(" Avg Price",f"{avg_price:.2f}")
c4.metric(" Avg Volume",f"{avg_volume:,.0f}")

st.divider()

col1,col2=st.columns(2)

with col1:

    fig=px.bar(
        top_green,
        x="Yearly Return (%)",
        y="Ticker",
        orientation="h",
        title="Top 10 Green Stocks",
        text="Yearly Return (%)"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig=px.bar(
        top_loss,
        x="Yearly Return (%)",
        y="Ticker",
        orientation="h",
        title="Top 10 Loss Stocks",
        text="Yearly Return (%)"
    )

    st.plotly_chart(fig,use_container_width=True)

st.divider()

col3,col4=st.columns(2)

with col3:

    summary=pd.DataFrame({
        "Category":["Green Stocks","Red Stocks"],
        "Count":[green,red]
    })

    fig=px.pie(
        summary,
        names="Category",
        values="Count",
        hole=0.5,
        title="Market Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with col4:

    metrics=pd.DataFrame({
        "Metric":["Average Price","Average Volume"],
        "Value":[avg_price,avg_volume]
    })

    fig=px.bar(
        metrics,
        x="Metric",
        y="Value",
        text="Value",
        title="Average Market Metrics"
    )

    st.plotly_chart(fig,use_container_width=True)
