import streamlit as st
import pandas as pd


st.title("📊 Stock Data Overview")

df = pd.read_csv("master_df.csv")


st.subheader("Dataset Preview")

st.dataframe(df.head())


st.subheader("Dataset Information")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])


st.subheader("Summary Statistics")

st.write(df.describe())