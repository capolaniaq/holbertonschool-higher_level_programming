#!/bin/bash
# GET request to the URL
curl -sI "$1" | grep Allow | cut -d " " -f2-
