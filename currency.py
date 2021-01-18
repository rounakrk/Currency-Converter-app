import requests
import json
import numpy as np
import pandas as pd

url = "https://free.currconv.com/api/v7/currencies?apiKey=<apikey>"
response = requests.get(url)
status_get = response.content
status_get = status_get.decode('utf-8')
status_json = json.loads(status_get)

all_currencies = []
for i in status_json["results"]:
    all_currencies.append(i)

# print(all_currencies)