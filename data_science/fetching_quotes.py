import requests
import urllib.request
import json

main_url = "https://zenquotes.io/api/"

modes = [
    "quotes/",
    "today/",
    "author/",
    "random/"
]

def get_random_quote():
    response = requests.get(main_url + modes[3])
    if response.status_code == 200:
        data = response.json()
        return data[0]['q']
    else:
        return "API error"

print(get_random_quote())