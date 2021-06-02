#!/usr/bin/python3
'''
checkif the object its exactly an instance
of specific class
'''


def is_same_class(obj, a_class):
    '''
    method check if is same  class
    '''
    if type(obj) == a_class:
        '''proper way isinstance(obj, a_class)'''
        return True
    else:
        return False
