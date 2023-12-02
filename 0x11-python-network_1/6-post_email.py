#!/usr/bin/python3
"""sends a POST request to URL with an email as a parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    r = requests.post(argv[1], data={'email': email})
    print(r.text)
