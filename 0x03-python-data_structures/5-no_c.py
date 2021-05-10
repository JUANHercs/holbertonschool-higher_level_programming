#!/usr/bin/python3
def no_c(my_string):
    new2 = ""
    new = list(my_string)
    if 'c' in new:
        new.remove('c')
    if 'C' in new:
        new.remove('C')
    for i in new:
        new2 += i
    return new2
