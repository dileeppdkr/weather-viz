# weather-viz

Fetch daily temperatures from the free [Open-Meteo](https://open-meteo.com/) API and chart them.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
python -m weather_viz.main   # or just: weather-viz
```

Outputs:
- `data/raw/<city>.json` — API response as-is
- `data/processed/<city>_daily.csv` — cleaned table
- `outputs/charts/<city>_daily_temperatures.png` — chart

## Test

```bash
pytest
```

## Layout

```
src/weather_viz/
  config.py   settings: paths, API URL, default city
  fetch.py    API calls only
  clean.py    JSON -> DataFrame
  plot.py     charts
  main.py     wires it together
tests/        pytest tests
notebooks/    scratch exploration
```
