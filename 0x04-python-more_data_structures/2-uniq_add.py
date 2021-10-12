#!/usr/bin/python3
def uniq_add(my_list=[]):
    """add all unique items in a list."""
    result = 0
    unique_list = set(my_list)
    for elements in unique_list:
        result += elements
    return (result)
