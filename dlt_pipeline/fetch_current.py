import requests
from datetime import datetime
from config import api_key
import dlt

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
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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