import matplotlib.pyplot as plt
import pandas as pd
import requests


def make_temperature_df(hours: list, temps: list) -> pd.DataFrame:
    """Создаёт DataFrame из времени и температур."""
    df = pd.DataFrame({
        "time": pd.to_datetime(hours),
        "temperature_c": temps,
    })
    return df.sort_values("time").reset_index(drop=True)


def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.75,
        "longitude": 37.61,
        "hourly": "temperature_2m",
        "forecast_days": 2,
        "timezone": "Europe/Moscow",
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    hours = data["hourly"]["time"][:24]
    temps = data["hourly"]["temperature_2m"][:24]

    df = make_temperature_df(hours, temps)
    df.to_csv("temperature_24h.csv", index=False)
    print("Сохранено в temperature_24h.csv")

    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["temperature_c"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Температура в Москве (24 часа)")
    plt.xlabel("Время")
    plt.ylabel("Температура, °C")
    plt.tight_layout()
    plt.savefig("temperature_24h.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()