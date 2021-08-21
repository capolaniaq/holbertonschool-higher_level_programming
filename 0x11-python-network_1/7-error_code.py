#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
use the request"""

import requests
import sys


if __name__ == '__main__':
    """request with the module request
    use the Post request type"""
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
