import requests
import config

import argparse

parser = argparse.ArgumentParser(description='A simple program to help search businesses with high rating.')
parser.print_help()

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "AirBnB",
    "location": "Nairobi"
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
        for business in businesses if business["rating"] > 4.5]
print(names)
