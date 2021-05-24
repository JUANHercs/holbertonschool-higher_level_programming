#!/usr/bin/python3
''' Better way to do it '''


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort()
    return my_list[-1]

''' first attempt 

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    max = -10000
    for element in my_list:
        if element > max:
            max = element
    return (max)
    '''
