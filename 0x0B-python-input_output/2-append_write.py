#!/usr/bin/python3
"""
Text file append function
"""


def append_write(filename="", text=""):
    """
    write in filename the text and
    return number of characters written
    """
    with open(filename, 'a') as file_to_write_append:
        file_to_write_append.write(text)

    count = 0
    for words in text:
        count += 1
    return(count)
