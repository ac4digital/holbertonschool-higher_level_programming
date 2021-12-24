#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    functions = [add, sub, mul, div]
    operators = ["+", "-", "*", "/"]
    a = int(argv[1])
    b = int(argv[3])
    for i, s in enumerate(operators):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, functions[i](a, b)))
            exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
