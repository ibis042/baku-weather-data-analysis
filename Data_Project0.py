import pandas as pd
import requests

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 40.4093,
    "longitude": 49.8671,
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "Asia/Baku",
}

cavab = requests.get(url, params=params)
melumat = cavab.json()


gundelik = melumat["daily"]

cedvel = pd.DataFrame({
    "tarix": gundelik["time"],
    "maks_temp": gundelik["temperature_2m_max"],
    "min_temp": gundelik["temperature_2m_min"],
    "yagis": gundelik["precipitation_sum"],
})

cedvel.to_csv("baki_2025.csv", index=False)

print("Hazırdır! İlk 5 sətir:")
print(cedvel.head())