#!/usr/bin/python3
"""responde to header at the https://intranet.hbtn.io/status"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """function to print the value of the X-Request-Id
    variable found in the header of the response."""
    data_email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data_email).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
    print(content.decode('utf-8'))
