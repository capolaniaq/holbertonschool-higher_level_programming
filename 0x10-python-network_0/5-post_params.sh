#!/bin/bash
# GET request to the URL
curl -sX POST "$1" -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
