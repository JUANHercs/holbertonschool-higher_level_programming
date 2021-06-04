#!/usr/bin/python3
"""
Write a function that writes an Object to a text
file, using a JSON representation
"""


import json

def save_to_json_file(my_obj, filename):
    """
    write in filename the object and
    return number of characters written
    """
    with open(filename, 'w', encoding='utf8') as file_with_json:
        #file_with_json.write(json.dumps(my_obj))
        json.dump(my_obj, file_with_json)