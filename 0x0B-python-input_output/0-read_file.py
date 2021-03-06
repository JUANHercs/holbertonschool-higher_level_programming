#!/usr/bin/python3
"""
Text file reading function
"""


def read_file(filename=""):
    """ Prints a UTF8 file content to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
