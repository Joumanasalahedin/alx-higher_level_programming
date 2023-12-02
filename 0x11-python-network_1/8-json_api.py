#!/usr/bin/python3
"""takes in a letter and sends a POST request"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1]:
        q = argv[1]
    else:
        q = ""

    r = requests.post(url, data={'q': q})

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
