"""Turn raw API JSON into a pandas DataFrame. No network, no charts."""

import pandas as pd


def to_daily_dataframe(api_response: dict) -> pd.DataFrame:
    """Build a DataFrame with date, max_temperature, min_temperature."""
    daily = api_response["daily"]
    return pd.DataFrame(
        {
            "date": pd.to_datetime(daily["time"]),
            "max_temperature": daily["temperature_2m_max"],
            "min_temperature": daily["temperature_2m_min"],
        }
    )
