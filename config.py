import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENWEATHER_API_KEY environment variable (in the .env file).")

# Set the working directory to the parent directory of this file
working_directory = Path(__file__).resolve().parent

# Set the DuckDB database path
db_path = working_directory / "data" / "openweather.duckdb"