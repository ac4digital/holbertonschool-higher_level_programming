#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        module = number % 10
    else:
        module = (number % -10) * -1

    print("{:d}".format(module), end="")

    return(module)
