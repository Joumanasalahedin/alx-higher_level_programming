#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep -i allow | cut -d' ' -f2-
