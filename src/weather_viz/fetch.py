"""Call the weather API. Only network code lives here."""

from datetime import date, timedelta

import requests

from weather_viz.config import BASE_URL, DAYS_BACK


def fetch_daily_temperatures(latitude: float, longitude: float, days_back: int = DAYS_BACK) -> dict:
    """Return Open-Meteo's JSON with daily max/min temps for the past `days_back` days."""
    end_date = date.today()
    start_date = end_date - timedelta(days=days_back)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date.isoformat(),  # YYYY-MM-DD
        "end_date": end_date.isoformat(),
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",  # use the city's local time zone
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()  # stop with a clear error on 4xx/5xx
    return response.json()
