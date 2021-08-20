#!/usr/bin/python3
"""responde to header at the https://intranet.hbtn.io/status"""

import urllib.request
import sys

if __name__ == "__main__":
    """function to print the value of the X-Request-Id
    variable found in the header of the response."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.headers
    print("{}".format(content.get('X-Request-Id')))
