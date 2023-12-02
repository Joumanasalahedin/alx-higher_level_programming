#!/usr/bin/python3
"""sends a POST request to URL with an email as a parameeter"""
from sys import argv
import urllib.request
import urllib.parse

url = argv[1]
email = argv[2]

data = urllib.parse.urlencode({'email': email}).encode('ascii')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode('utf-8'))
