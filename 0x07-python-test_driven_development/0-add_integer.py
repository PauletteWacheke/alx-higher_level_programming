#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Adds two integers
    
    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integrs
    """


    if type(a) in [int, float]:
        try:
            a = int(a)
        except:
            raise TypeError('a must be an integer')
    else:
        raise TypeError('a must be an integer')

    if type(b) in [int, float]:
        try:
            b = int(b)
        except:
            raise TypeError("b must be an integr")
    else:
        raise TypeError('b must be an integer')

    return a + b
