#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    max = -10000
    for element in my_list:
        if element > max:
            max = element
    return (max)
