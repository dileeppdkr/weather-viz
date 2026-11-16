from weather_viz.clean import to_daily_dataframe


def test_to_daily_dataframe_builds_expected_columns():
    api_response = {
        "daily": {
            "time": ["2026-11-10", "2026-11-11"],
            "temperature_2m_max": [18.2, 19.5],
            "temperature_2m_min": [10.1, 11.0],
        }
    }

    df = to_daily_dataframe(api_response)

    assert list(df.columns) == ["date", "max_temperature", "min_temperature"]
    assert len(df) == 2
    assert df["date"].dtype.kind == "M"  # real datetime, not text
    assert df["max_temperature"].iloc[1] == 19.5
