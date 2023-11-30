#!/bin/bash
# sends a POST request and displays response
curl -s --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
