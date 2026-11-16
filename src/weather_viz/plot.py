"""Charts. Takes a DataFrame in, writes a PNG out."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_daily_temperatures(df: pd.DataFrame, city: str, save_path: Path) -> None:
    """Line chart of daily max and min temperatures, saved to `save_path`."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["max_temperature"], label="Max Temperature", color="red")
    ax.plot(df["date"], df["min_temperature"], label="Min Temperature", color="blue")

    ax.set_title(f"Daily Max and Min Temperatures - {city}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path)
