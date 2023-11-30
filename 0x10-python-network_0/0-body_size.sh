#!/bin/bash
# sends a request to an URL and displays size of response
curl -s "$1" | wc -c
