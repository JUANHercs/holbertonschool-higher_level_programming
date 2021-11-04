#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    try:
        for elements in range(x):
            print("{}".format(my_list[elements]), end="")
        return x
    except IndexError:
        return elements
    finally:
        print(" ")
