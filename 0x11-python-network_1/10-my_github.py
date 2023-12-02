#!/usr/bin/python3
"""takes Github credentials and uses API to display id"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get('id'))
