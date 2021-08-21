#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
use the request"""

import requests
import sys


if __name__ == '__main__':
    """request with the module request
    use the Post request type"""
    if len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        value = ""

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': value})
        js = r.json()

        if js:
            print("[{}] {}".format(js.get('id'), js.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
