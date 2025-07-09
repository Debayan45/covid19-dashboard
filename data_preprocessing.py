# data_preprocessing.py
import pandas as pd

@st.cache_data

def load_data():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    
    # Basic cleanup
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['continent'].notna()]  # Filter out continents only
    return df
