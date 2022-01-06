#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(roman_string)-1, -1, -1):
            num = roman[roman_string[i]]
            if 3 * num < sum:
                sum = sum - num
            else:
                sum = sum + num
        return (sum)
    else:
        return (0)
