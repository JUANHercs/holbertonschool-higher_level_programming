#!/usr/bin/python3
'''
A class that inherits
'''


class MyList(list):
    '''
    list: superclass or parent class
    My_list: subclass inheriting from list
    '''
    def print_sorted(self):
        '''
        function that returns a sorted list
        '''
        list = []
        print(sorted(self))
