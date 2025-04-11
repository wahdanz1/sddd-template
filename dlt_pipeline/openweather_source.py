import dlt
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime
import pandas as pd
import duckdb as ddb

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENWEATHER_API_KEY environment variable (in the .env file).")

# Set the working directory to the parent directory of this file
working_directory = Path(__file__).resolve().parent.parent

# Set the DuckDB database path
db_path = working_directory / "data" / "openweather.duckdb"

# --- Current weather resource ---
@dlt.resource(write_disposition="append")
def current_weather(cities: list):
    """Fetch current weather data from OpenWeatherMap API for a list of cities."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    for city in cities:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric",
        }
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Yield data for the pipeline
            yield {
                "city": data["name"],
                "timestamp": timestamp,
                "temperature": data["main"].get("temp"),
                "humidity": data["main"].get("humidity"),
                "pressure": data["main"].get("pressure"),
                "wind_speed": data["wind"].get("speed"),
                "cloudiness": data["clouds"].get("all"),
                "description": data["weather"][0]["description"]
            }
        else:
            print(f"Request failed for {city}, Status code: {response.status_code}")

# --- Historical weather resource (placeholder for future implementation) ---
@dlt.resource(write_disposition="append")
def historical_weather(cities: list, start_date: str, end_date: str):
    """Placeholder function to fetch historical weather data (to be implemented)."""
    # You will need to adjust this function with an actual API for historical weather
    pass

# --- Source definition ---
@dlt.source
def openweather_source(cities: list, table_name: str):
    """OpenWeatherMap source for fetching weather data."""
    if table_name == "current_weather":
        yield current_weather(cities)
    elif table_name == "historical_weather":
        # Start and end dates for historical weather - not yet sure if that's what I'm after
        start_date = "2021-01-01"  # placeholder start date
        end_date = "2021-01-02"    # placeholder end date
        yield historical_weather(cities, start_date, end_date)
    else:
        raise ValueError(f"Unsupported table name: {table_name}")

# --- Pipeline runner ---
def run_pipeline(cities: list, table_name: str):
    """Run the data pipeline and load data into DuckDB."""
    pipeline = dlt.pipeline(
        pipeline_name="openweather_pipeline",
        destination=dlt.destinations.duckdb(str(db_path)),
        dataset_name="staging",
    )

    load_info = pipeline.run(openweather_source(cities, table_name=table_name))
    print(load_info)

# --- Database connection class ---
class DuckDBConnection:
    """Context manager for DuckDB connection."""

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = ddb.connect(str(self.db_path))
        return self
    
    def query(self, query):
        """Execute a query and return the result."""
        try:
            return self.conn.execute(query).df()
        except Exception as e:
            print(f"Error executing query: {e}")
            return pd.DataFrame()  # Return an empty DataFrame if there's an error

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()


# -------------------------------------------------------------------------------------------------------
# Run if this file is executed directly
if __name__ == "__main__":
    cities = ["London", "New York", "Tokyo"]  # Example cities
    table_name = "current_weather"
    run_pipeline(cities, table_name)
    print("Pipeline executed successfully.")

with DuckDBConnection(db_path) as conn:
    # Check if the table exists in DuckDB
    query = """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'staging' 
            AND table_name = 'current_weather';
            """
    result = conn.query(query)

    if result.empty:
        print("Table does not exist yet.")
    else:
        df = conn.query("SELECT * FROM staging.current_weather")
        print(type(df))
        print(df)