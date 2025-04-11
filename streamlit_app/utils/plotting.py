import plotly.express as px
import pandas as pd

def create_temperature_bar_chart(weather_data: pd.DataFrame):
    """
    Returns a Plotly bar chart showing the latest temperature per city.
    """
    # Ensure we only get the latest entry per city
    latest_data = (
        weather_data.sort_values("timestamp", ascending=False)
        .drop_duplicates(subset="city", keep="first")
    )

    fig = px.bar(
        latest_data,
        x="city",
        y="temperature",
        color="city",
        title="Current Temperature by City",
        labels={"city": "City", "temperature": "Temperature (°C)"},
    )
    return fig


def create_temperature_line_chart(weather_data: pd.DataFrame):
    """
    Returns a Plotly line chart showing temperature trends over time per city.
    """
    # Convert timestamp to datetime if it's not already
    weather_data["timestamp"] = pd.to_datetime(weather_data["timestamp"])

    # Sort for consistent plotting
    weather_data = weather_data.sort_values(by=["city", "timestamp"])

    fig = px.line(
        weather_data,
        x="timestamp",
        y="temperature",
        color="city",
        markers=True,
        title="Temperature Trends by City Over Time",
        labels={
            "timestamp": "Time",
            "temperature": "Temperature (°C)",
            "city": "City"
        },
    )
    return fig

