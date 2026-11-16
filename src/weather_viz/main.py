"""Entry point: fetch -> clean -> save -> plot."""

import json

import matplotlib.pyplot as plt

from weather_viz.clean import to_daily_dataframe
from weather_viz.config import (
    CHARTS_DIR,
    DEFAULT_CITY,
    DEFAULT_LATITUDE,
    DEFAULT_LONGITUDE,
    PROCESSED_DIR,
    RAW_DIR,
    CITIES,
)
from weather_viz.fetch import fetch_daily_temperatures
from weather_viz.plot import plot_daily_temperatures


def main() -> None:
    city_slug = DEFAULT_CITY.lower().replace(" ", "_")  # "San Francisco" -> "san_francisco"

    # 1. Fetch and keep the raw response
    raw = fetch_daily_temperatures(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / f"{city_slug}.json").write_text(json.dumps(raw, indent=2))

    # 2. Clean and save as CSV
    df = to_daily_dataframe(raw)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / f"{city_slug}_daily.csv", index=False)
    print(df)

    # 3. Plot
    chart_path = CHARTS_DIR / f"{city_slug}_daily_temperatures.png"
    plot_daily_temperatures(df, DEFAULT_CITY, chart_path)
    print(f"Saved chart to {chart_path}")
    plt.show()


if __name__ == "__main__":
    for city_name, (lat, lon) in CITIES.items():
        print(f"Processing city: {city_name}")
        DEFAULT_CITY = city_name
        DEFAULT_LATITUDE = lat
        DEFAULT_LONGITUDE = lon
        main()
