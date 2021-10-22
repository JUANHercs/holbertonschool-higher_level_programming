#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operator = {'+': add, '-': sub, '*': mul, '/': div}
    if len(sys.argv) != 4:
        print("Usage: ./{} <a> <operator> <b>".format("100-my_calulator.py"))
        sys.exit(1)
    elif sys.argv[2] not in list(operator.keys()):
        print("Uknown operator, Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b,
                                     operator[sys.argv[2]](a, b)))
