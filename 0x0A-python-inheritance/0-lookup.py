#!/usr/bin/python3
"""
Module that return list of available
attributes and methods of an objec
"""


def lookup(obj):
    """Function that return alist of available attributes and methods
    of an object"""

    return dir(obj)
