import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stock Analysis Dashboard",
                   page_icon="📊",
                   layout="wide")

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "master_df.csv"

df = pd.read_csv(CSV_PATH)

df["date"] = pd.to_datetime(df["date"])

st.title("📊 Stock Analysis Dashboard")

st.markdown("""
### Welcome

This dashboard analyzes stock market performance using
- Python
- Pandas
- SQL
- Plotly
- Streamlit
""")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Companies", df["Ticker"].nunique())
col3.metric("Start Date", df["date"].min().strftime("%Y-%m-%d"))
col4.metric("End Date", df["date"].max().strftime("%Y-%m-%d"))

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head())