import streamlit as st
import pandas as pd
import altair as alt
from data_preprocessing import load_data

# Set page config
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Load data
df = load_data()

# Title
st.title("🌍 COVID-19 Global Impact Dashboard")

# Sidebar - Country selector
country = st.sidebar.selectbox("Select a country", sorted(df['location'].unique()))

# Filtered data
country_df = df[df['location'] == country]

# Summary metrics
latest = country_df.sort_values('date').iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", f"{int(latest['total_cases']):,}")
col2.metric("Total Deaths", f"{int(latest['total_deaths']):,}")
col3.metric("Total Vaccinations", f"{int(latest.get('total_vaccinations', 0)):,}")

# Chart: Cases over time
cases_chart = alt.Chart(country_df).mark_line().encode(
    x='date:T',
    y='total_cases:Q'
).properties(width=700, height=400, title="Total Cases Over Time")

st.altair_chart(cases_chart, use_container_width=True)
