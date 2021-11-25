#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print dictionary bt ordered keys."""
    sorted_items = sorted(a_dictionary)
    for k in sorted_items:
        print("{}: {}".format(k, a_dictionary[k]))
