#!/usr/bin/python3
"""
use json bult in package
to transform python to jason syntax
json text writting in javascript object notation
"""


import json
def to_json_string(my_obj):
    """ Args:
        my_obj - recieve object from python
                stye syntax
    """
    json_style = json.dumps(my_obj)
    return json_style