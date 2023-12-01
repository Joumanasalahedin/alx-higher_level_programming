#!/usr/bin/python3
"""Sends a request to URL and displays the value of the X-Request-Id"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.getheader('X-Request-Id'))
