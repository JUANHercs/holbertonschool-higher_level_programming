#!/usr/bin/python3
"""
Defines a text file insertion function
"""


def append_after(filename="", search_string="", new_string=""):
    """ Insert text after each line containing a given string in file

    Args:
    filename (str): name of file
    search_string (str): the string to search within the file
    new_string (str): The string to insert
    """
    text = ""
    with open(filename) as k:
        for line in k:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
