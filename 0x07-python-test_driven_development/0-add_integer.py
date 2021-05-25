#!/usr/bin/python3
"""Module that contain the fucntion add_integer"""


def add_integer(a, b=98):
    """function that add two numbers"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer or b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
