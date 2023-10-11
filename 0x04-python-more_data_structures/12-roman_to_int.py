#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}
    int_val = 0
    p = 0
    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if roman_num[roman_string[c]] >= p:
                int_val += roman_num[roman_string[c]]
            else:
                int_val -= roman_num[roman_string[c]]
            p = roman_num[roman_string[c]]
    return int_val
