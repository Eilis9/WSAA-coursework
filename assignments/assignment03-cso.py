# Assignment 3
# Name: Eilis Donohue

import requests
import json

# Exchequer account (historical series) from the CSO
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Get the data
response = requests.get(url)
dataset = response.json()

# https://www.geeksforgeeks.org/json-dump-in-python/
with open("assignments/cso.json", "wt") as fp:
  json.dump(dataset, fp, indent=4)

