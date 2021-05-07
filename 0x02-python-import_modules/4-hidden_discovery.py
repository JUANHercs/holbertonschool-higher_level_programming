#!/usr/bin/python3.4
import hidden_4
if __name__ == "__main__":
    x = dir(hidden_4)
    for i in x:
        if "__" in i:
            pass
        else:
            print(i)
