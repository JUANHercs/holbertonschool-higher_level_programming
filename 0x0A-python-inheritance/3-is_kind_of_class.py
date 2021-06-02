#!/usr/bin/python3
'''
Function that returns True if object is an instance
of, or if object is an instance of a class that
inherited from, the specified class
otherwise False.
'''


def is_kind_of_class(obj, a_class):
    '''
    method check if obj is instance of a class
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
