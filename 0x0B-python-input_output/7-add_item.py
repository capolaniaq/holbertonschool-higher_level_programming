#!/usr/bin/python3
"""Module that save and load data json of the add_item.json"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    dict_json = load_from_json_file("add_item.json")
except:
    dict_json = []

for args in (sys.argv[1:]):
    dict_json.append(args)

save_to_json_file(dict_json, "add_item.json")
