#!/bin/bash
# makes a request that responds witha specific message
curl -sLX PUT -H "Origin: HolbertonSchool" --data "user_id=98" 0.0.0.0:5000/catch_me
