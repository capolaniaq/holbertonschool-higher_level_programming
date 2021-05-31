#!/usr/bin/python3
"""Module that load data from a string"""
import json


def from_json_string(my_str):
    """function that load from a string"""

    return json.loads(my_str)
