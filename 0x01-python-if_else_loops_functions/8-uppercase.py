def uppercase(str):
    for i in str:
        if 97 <= ord(i) < 122:
            i = chr(ord(i) - (97 - 65))
        print("{}".format(i), end='')
    print('')
