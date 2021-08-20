#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    """function to print the content body to responde"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        content = response.read()
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
