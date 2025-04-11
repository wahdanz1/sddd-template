import os
import sys
import pandas as pd
import streamlit as st
import plotly.express as px

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dlt_pipeline.pipeline import run_pipeline
from utils.data_fetching import is_data_fresh, get_weather_data_for_cities
from utils.constants import cities
import utils.plotting as plotting

# --- Dashboard components ---
st.title("🌦️ OpenWeatherMap Dashboard")

# --- Select a city for current weather data ---
st.markdown("## Current Weather Data")

selected_cities = st.multiselect("Select a city:", cities)
force_refresh = st.button("🔄 Force-fetch data")

# --- Trigger the data fetching when cities are selected ---
for city in selected_cities:
    needs_update = not is_data_fresh(city) or force_refresh
    # Check if the weather data is fresh
    if needs_update:
        with st.spinner(f'Fetching weather data for {city}...'):
            # If the data is not fresh, run the pipeline to fetch the latest data
            run_pipeline([city], "current_weather")
            st.success(f'Data for {city} fetched successfully!')

# --- Query weather data from DuckDB based on selected cities ---
if selected_cities:
    weather_data = get_weather_data_for_cities(selected_cities)

    # --- Display the data in a table ---
    st.dataframe(weather_data, use_container_width=True)

    # --- Plot the data using Plotly ---
    if not weather_data.empty:
        fig_bar = plotting.create_temperature_bar_chart(weather_data)
        st.plotly_chart(fig_bar, use_container_width=True)
        fig_line = plotting.create_temperature_line_chart(weather_data)
        st.plotly_chart(fig_line, use_container_width=True)

    else:
        st.info("Please select at least one city to view weather data.")

