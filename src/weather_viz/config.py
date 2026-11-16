"""Settings in one place: paths, API URL, default city."""

from pathlib import Path

# Folders (project root is two levels up from this file: src/weather_viz/config.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CHARTS_DIR = PROJECT_ROOT / "outputs" / "charts"

# Open-Meteo API (free, no key needed)
BASE_URL = "https://api.open-meteo.com/v1/forecast"
DAYS_BACK = 7

# Default city
DEFAULT_CITY = "San Francisco"
DEFAULT_LATITUDE = 37.7749
DEFAULT_LONGITUDE = -122.4194
CITIES = {
    "San Francisco": (37.7749, -122.4194),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6895, 139.6917),
    "India": (20.5937, 78.9629),
}