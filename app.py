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

# Sidebar - Searchable Country Dropdown
st.sidebar.subheader("🌍 Search & Select a Country")

country_list = sorted(df['location'].unique())
default_country = "India" if "India" in country_list else country_list[0]

# This dropdown lets users type and filter countries
country = st.sidebar.selectbox(
    "Type to search a country",
    options=country_list,
    index=country_list.index(default_country)
)




# Filtered data
country_df = df[df['location'] == country]

# Summary metrics
# Summary metrics
latest = country_df.sort_values('date').iloc[-1]

total_cases = int(latest['total_cases']) if pd.notna(latest['total_cases']) else 0
total_deaths = int(latest['total_deaths']) if pd.notna(latest['total_deaths']) else 0
total_vacc = int(latest['total_vaccinations']) if pd.notna(latest['total_vaccinations']) else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", f"{total_cases:,}")
col2.metric("Total Deaths", f"{total_deaths:,}")
col3.metric("Total Vaccinations", f"{total_vacc:,}")


# Chart: Cases over time
cases_chart = alt.Chart(country_df).mark_line().encode(
    x='date:T',
    y='total_cases:Q'
).properties(width=700, height=400, title="Total Cases Over Time")

st.altair_chart(cases_chart, use_container_width=True)
