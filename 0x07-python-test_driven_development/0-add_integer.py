#!/usr/bin/python3
"""
add integer function to test
"""


def add_integer(a, b=98):
    """
    adds 2 integers
    Parameters
    a: int or float convert to int
    b: int or float convert to int
    Returns result of add the two integers
    """
    # isinstance check an object, verify the classinfo
    # returns true or false
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (a + b)
