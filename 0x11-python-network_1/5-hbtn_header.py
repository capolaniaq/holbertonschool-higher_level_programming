#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
use the request"""

import requests
import sys


if __name__ == '__main__':
    """request with the module request"""
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
