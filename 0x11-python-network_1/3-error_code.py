#!/usr/bin/python3
"""Python script that takes in a URL, sends a
request to the URL and displays the body"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """You have to manage urllib.error.HTTPError
    exceptions and print: Error code"""

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
