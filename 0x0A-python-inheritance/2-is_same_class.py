#!/usr/bin/python3
"""Module that check if a object is a respectixc type"""


def is_same_class(obj, a_class):
    """Function that check type of object"""

    if type(obj) is a_class:
        return True
    else:
        return False
