#!/usr/bin/python3
"""
Module that contain the fucntion add_integer
"""


def print_square(size):
    """Function that print the size of the square
    with the # simbol
    if size is not integer typeerror "size must be an integer"
    if size is less 0, typeerror "size must be >= 0"
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
