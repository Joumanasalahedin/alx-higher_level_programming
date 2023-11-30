#!/bin/bash
# sends a JSON POST request and displays response
curl -sX POST -H 'Content-Type: application/json' -d "$2" "$1"
