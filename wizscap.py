import requests
import config

import argparse

print('''
 __      __.__                           .___
/  \    /  \__|____________  _____     __| _/
\   \/\/   /  \___   /\__  \ \__  \   / __ | 
 \        /|  |/    /  / __ \_/ __ \_/ /_/ | 
  \__/\  / |__/_____ \(____  (____  /\____ | 
       \/           \/     \/     \/      \/ 
        https://github.com/Wizaad/wizscrap
           https://twitter.com/MrWizaad
''')

parser = argparse.ArgumentParser(description='A simple program to help search businesses with high rating.')
parser.print_help()

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": input("What business are you looking for?  "),
    "location": input("What city do you want? ")
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
