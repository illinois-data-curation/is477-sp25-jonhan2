import pandas as pd
import requests
import json
import hashlib

with open("fred.apikey.txt", "r") as f:
    apikey = f.readline().strip()

series = "SP500"
start = "2019-01-01"
end = "2024-01-01"
url = (f"https://api.stlouisfed.org/fred/series/observations?"
      f"series_id={series}&api_key={apikey}"
      f"&observation_start={start}&observation_end={end}&file_type=json")

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

with open("assignment1/sp500.json", "w") as f:
    f.write(json.dumps(json_data, indent=4))

df = pd.json_normalize(json_data, 'observations')

df = df.drop(["realtime_start", "realtime_end"], axis=1)

df = df[df.value != "."]

df["date"] = pd.to_datetime(df["date"])
df["value"] = pd.to_numeric(df["value"])

print(df.head())

print(df.dtypes)

df = df.set_index(["date"])
plt = df.plot(title="SP500 (2019-2024)", legend=False)
plt.set_xlabel("Date")
plt.set_ylabel("Index Value")
plt.get_figure().savefig("assignment1/sp500.png")

df.to_csv("assignment1/sp500.csv", lineterminator='\n')

with open("assignment1/sp500.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("assignment1/sp500.sha", "w") as f:
    f.write(sha256hash)