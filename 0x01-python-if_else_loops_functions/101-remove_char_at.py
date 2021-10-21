#!/usr/bin/python3


def remove_char_at(str, n):
    str2 = ""
    if n <= len(str) and n >= 0:
        for i in range(0, len(str)):
            if str[i] == str[n]:
                continue
            else:
                str2 += str[i]
    else:
        str2 = str
    return str2
