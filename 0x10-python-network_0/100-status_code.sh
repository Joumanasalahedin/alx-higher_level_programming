#!/bin/bash
# sends a request and displays only the status code
curl -s -w "%{http_code}\n" "$1"
