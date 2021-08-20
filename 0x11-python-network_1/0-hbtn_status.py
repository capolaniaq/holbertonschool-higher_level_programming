#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    """function to print the content body to responde"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        content = response.read()
        print(" - type: {}".format(type(content)))
        print(" - content: {}".format(content))
        print(" - utf8 content: {}".format(content.decode('utf-8')))