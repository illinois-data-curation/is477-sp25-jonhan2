import pandas as pd
import numpy as np
from datetime import datetime , timedelta
import hmac
import hashlib

seed = 123

df = pd.read_csv('lab2/private_data.csv', sep='|')
df.to_csv('lab2/deidentified_data.csv')
# print(df.head())

df.drop(columns=["name","phone"], inplace=True)

# print(df.head())

print("Generalize address to 5-digit ZIP Code and drop the address field")
df["zip"] = df["address"].str[-5:]
# df["zip"] = df["address"].str.split(' ').str[-1]
df.drop(columns="address", inplace=True)

# print(df.head())

study_date = datetime(2024, 1, 1)
np.random.seed(seed)
random_years = np.random.randint(low=1, high=4, size=100)

print (df.head())

with open("lab2/secret.txt") as f:
    secret_key = f.readline().strip()

df["id"] = df["ssn"].apply(
    lambda x: 
        hmac.new(
            bytes(secret_key, 'latin-1'), 
            msg=bytes(x, 'latin-1'), 
            digestmod=hashlib.sha256
        ).hexdigest())

df.drop(columns="ssn", inplace=True)

print(df.head())

df.to_csv("lab2/deidentified_data.csv")