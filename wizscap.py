import requests
import config
import argparse
from bs4 import BeautifulSoup

def print_banner():
    print('''
    ▄█░ ▀████▄     ▄████▄   ▄▄▄       ██░ ██ ▓█████ 
   ░██░   █░░██   ██▀ ▀█  ▒████▄    ▓██░ ██▒▓█   ▀ 
   ░██░   ░░░██▄  ██   ██ ▒██  ▀█▄  ▒██▀▀██░▒███   
   ░██░    ░░██  ██▄▄███ ░██▄▄▄▄██ ░▓█ ░██ ▒▓█  ▄ 
   ░▓█░    ░░██ ▓█   ▀  ▓█   ▓██▒░▓█▒░██▓░▒████▒
   ░▒█░     ░░▓ █░░░░░░░░░░░░░░░░░░▒█░░ ▓█░░░░░
    ▒█░       ░ ░░ ░░░ ░░░░░░░░░░░░▒█░  ▒█░░░░░
    ▓█░         ░░░░░░░░░░░░░░░░░░░░▒█   ▓█░░░░
    ██░          ░░░░░░░░░░░░░░░░░░░░█▒  ░█░░░░
   ▒██░             ░░░░░░░░░░░░░░░░░░░  ░█░░░░
  ▒███▒                                 ▓█░░░░
 ░▓███▒                                 ██░░░
░▒████░                                 ██░░
░▒███▓░    https://github.com/Wizaad/wizscrap░░░░░░░░░░░░
 ░▓██▓░        https://wizaad.com      ░░░░░░░░
   ░▓█░                                        ░░░░░░░░
    ▒█░  A POWERFUL BUSINESS SEARCH TOOL!      ░░░░░░░░
     ▓█░                                      ░░░░░░░░
      ▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       ▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
         ░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
          ░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
           ░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
             ░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░
              ░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░░░
               ░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░░░
                 ░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░░
                  ░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░
                   ░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░▀█░░░░░░░░░░░░░
                     ░░░░░░░░░░░░░░▀█░░░░░░░░░░░
                      ░░░░░░░░░░░░░░░▀█░░░░░░░░░
                       ░░░░░░░░░░░░░░░░▀█░░░░░░░
                        ░░░░░░░░░░░░░░░░░▀█░░░░
                         ░░░░░░░░░░░░░░░░░░░▀█░
                          ░░░░░░░░░░░░░░░░░░░░░▀
    ''')

def search_businesses(term, location):
    url = "https://api.yelp.com/v3/businesses/search"

    headers = {
        "Authorization": "Bearer " + config.api_key
    }

    params = {
        "term": term,
        "location": location
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        businesses = response.json()["businesses"]
        names = [business["name"]
                for business in businesses if business["rating"] > 4.5]
        return names
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data:")
        print("Error:", e)
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        return []


def search_google(term, location):
    search_url = f"https://www.google.com/search?q={term}+{location}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all("h3")
        names = [result.get_text() for result in results]
        return names
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching Google data:")
        print("Error:", e)
        return []

def search_bing(term, location):
    search_url = f"https://www.bing.com/search?q={term}+{location}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all("h2")
        names = [result.get_text() for result in results]
        return names
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching Bing data:")
        print("Error:", e)
        return []

def search_duckduckgo(term, location):
    search_url = f"https://duckduckgo.com/html/?q={term}+{location}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all("a", class_="result__url")
        names = [result.get_text() for result in results]
        return names
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching DuckDuckGo data:")
        print("Error:", e)
        return []

def search_yahoo(term, location):
    search_url = f"https://search.yahoo.com/search?p={term}+{location}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all("h3")
        names = [result.get_text() for result in results]
        return names
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching Yahoo data:")
        print("Error:", e)
        return []


def main():
    print_banner()

    parser = argparse.ArgumentParser(description='A powerful program to search for highly-rated businesses.')
    parser.print_help()

    term = input("What type of business are you looking for? ")
    location = input("In which city? ")

    print("\nYelp Search Results:")
    yelp_names = search_businesses(term, location)
    print_results(yelp_names)

    print("\nGoogle Search Results:")
    google_names = search_google(term, location)
    print_results(google_names)

    print("\nBing Search Results:")
    bing_names = search_bing(term, location)
    print_results(bing_names)

    print("\nDuckDuckGo Search Results:")
    duckduckgo_names = search_duckduckgo(term, location)
    print_results(duckduckgo_names)

    print("\nYahoo Search Results:")
    yahoo_names = search_yahoo(term, location)
    print_results(yahoo_names)

def print_results(names):
    if names:
        for idx, name in enumerate(names, start=1):
            print(f"{idx}. {name}")
    else:
        print("No results found or an error occurred.")

if __name__ == "__main__":
    main()
