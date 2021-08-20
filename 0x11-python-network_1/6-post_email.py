#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
use the request"""

import requests
import sys


if __name__ == '__main__':
    """request with the module request
    use the Post request type"""
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
