#!/usr/bin/python3
"""Module that return a JSON object as string"""
import json


def to_json_string(my_obj):
    """Function that return a JSON object as string"""

    return json.dumps(my_obj)
