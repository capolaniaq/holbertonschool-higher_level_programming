#!/usr/bin/python3
"""Module that write a string in the file exist or don't exist"""


def write_file(filename="", text=""):
    """Function that write a string in the file exist or don't exist"""

    text = str(text)
    lenght = len(text)
    with open(filename, "w") as myfile:
        myfile.write(text)
    return lenght
