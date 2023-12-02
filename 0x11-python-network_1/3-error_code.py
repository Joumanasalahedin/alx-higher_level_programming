#!/usr/bin/python3
"""sends a request to URL and displays body"""
from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
