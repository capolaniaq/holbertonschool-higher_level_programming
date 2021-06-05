#!/usr/bin/python3
"""Module that check if obj is a instance"""


def is_kind_of_class(obj, a_class):
    """Function that check if obj is a instance"""

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
