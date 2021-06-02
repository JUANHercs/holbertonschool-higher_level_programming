#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str) - 1):
        if n < 0:
            n = len(str) + n
        if i != n:
            print(str[i], end='')