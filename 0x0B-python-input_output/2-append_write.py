#!/usr/bin/python3
"""Module that insert a text in end file"""


def append_write(filename="", text=""):
    """Function that insert a text in the end file"""

    text = str(text)
    with open(filename, "a") as myfile:
        myfile.write(text)
    return len(text)
