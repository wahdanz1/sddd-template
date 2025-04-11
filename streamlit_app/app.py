import streamlit as st
import plotly.express as px
import pandas as pd
import sys
import os
import requests

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dlt_pipeline.db import DuckDBConnection
from dlt_pipeline.pipeline import run_pipeline
from config import db_path

# --- Dashboard components ---
st.title("🌦️ OpenWeatherMap Dashboard")

# --- Select a city for current weather data ---
st.markdown("## Current Weather Data")
cities = st.multiselect("Select a city:", ["New York", "London", "Tokyo", "Uddevalla", "San Pedro Sula", "Visby"])

# --- Trigger the data fetching when cities are selected --- 
if cities:
    # Call the pipeline to fetch data if necessary
    with st.spinner('Fetching weather data...'):
        run_pipeline(cities, "current_weather")
        st.success('Data fetched successfully!')

    # --- Query weather data from DuckDB based on selected cities --- 
    with DuckDBConnection(db_path) as conn:
        city_query = f"""
            SELECT * FROM staging.current_weather
            WHERE city IN ({', '.join([f"'{city}'" for city in cities])})
            """
        
        # Execute the query and fetch the data
        weather_data = conn.query(city_query)

        # --- Display the data in a table ---
        st.write("### Current Weather Data", weather_data)

        # --- Plot the data using Plotly ---
        if not weather_data.empty:
            fig = px.bar(
                weather_data,
                x="city",
                y="temperature",
                color="city",
                title="Current Temperature by City",
                )
            st.plotly_chart(fig, use_container_width=True)

        else: 
            st.write("Please select a city to view the current weather data.")

