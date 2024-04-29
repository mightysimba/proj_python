import requests
import json


url = "http://api.giphy.com/v1/gifs/search"
api_key = "8EcMAl9U5q3fY9ghYyTqOJyppeIc0a8X"
keyword = input("Enter your keyword: ")

params = {
    "q": keyword,
    "api_key": api_key,
    "limit": 2
}

response = requests.get(url, params=params)
if response.status_code == 200:
    images = response.json()['data']
    for image in images:
        print(f"URL: {image['embed_url']}, Title: {image['title']}")
else:
    print("Error:", response.status_code)
