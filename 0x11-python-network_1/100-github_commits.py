#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()

    for i in range(10):
        print(
            f"{commits[i].get('sha')}: {commits[i].get('commit').get('author').get('name')}")
