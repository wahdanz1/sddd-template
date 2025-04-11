import dlt
from dlt_pipeline import fetch_current as fc
from dlt_pipeline import fetch_historical as fh
from config import db_path

# --- Source definition ---
@dlt.source
def openweather_source(cities: list, table_name: str):
    """OpenWeatherMap source for fetching weather data."""
    if table_name == "current_weather":
        yield fc.current_weather(cities)
    elif table_name == "historical_weather":
        # Start and end dates for historical weather - not yet sure if that's what I'm after
        start_date = "2021-01-01"  # placeholder start date
        end_date = "2021-01-02"    # placeholder end date
        yield fh.historical_weather(cities, start_date, end_date)
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