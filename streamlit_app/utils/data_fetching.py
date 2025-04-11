from datetime import datetime, timedelta
from dlt_pipeline.db import DuckDBConnection
from config import db_path
import pandas as pd

# --- Function for checking if data is recently fetched ---
def is_data_fresh(city: str):
    """Check if the weather data for the given city is fresh (within 1 hour)."""
    with DuckDBConnection(db_path) as conn:
        query = f"""
            SELECT MAX(timestamp) AS last_update
            FROM staging.current_weather
            WHERE city = '{city}'
            """
        result = conn.query(query)
        if not result.empty:
            last_update = result['last_update'].iloc[0]
            if last_update:
                now = datetime.now(last_update.tzinfo)  # Match timezone
                if (now - last_update) < timedelta(hours=1):
                    return True
    return False

# --- Function for fetching current weather data for selected cities ---
def get_weather_data_for_cities(cities: list[str]) -> pd.DataFrame:
    if not cities:
        return pd.DataFrame()
    
    placeholders = ', '.join(['?'] * len(cities))
    query = f"""
        SELECT * FROM staging.current_weather
        WHERE city IN ({placeholders})
    """

    with DuckDBConnection(db_path) as conn:
        return conn.query(query, cities)