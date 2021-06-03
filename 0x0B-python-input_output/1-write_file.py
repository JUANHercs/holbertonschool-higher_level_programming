#!/usr/bin/python3
"""
Text file write function
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as file_to_write:
        file_to_write.write(text)

    count = 0
    for words in text:
        count += 1
    return(count)
