#!/usr/bin/python3
"""Module to print a content in a respect file"""


def read_file(filename=""):
    """Function that print the content of the my_file_0.txt"""

    with open("my_file_0.txt", "r") as myfile:
        print(myfile.read())
