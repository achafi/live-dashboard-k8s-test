import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

# Title of the dashboard
st.title("Streamlit Dashboard Example")

# Line chart
st.write("### Data Over Time")
st.line_chart(data=df, x="date", y="value")

# Display raw data
st.write("### Raw Data")
st.dataframe(df)
