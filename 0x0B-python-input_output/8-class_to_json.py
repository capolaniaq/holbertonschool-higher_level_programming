#!/usr/bin/python3
"""Module that Convert to instance class to json dict"""

def class_to_json(obj):
    """Function that convert to Instance class to json"""

    obj = obj.__dict__
    return obj
