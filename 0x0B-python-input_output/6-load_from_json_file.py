#!/usr/bin/python3
"""
function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    write in filename the object and
    return number of characters written
    """
    with open(filename, 'r', encoding='utf-8') as file_from_json:
        return json.load(file_from_json)
