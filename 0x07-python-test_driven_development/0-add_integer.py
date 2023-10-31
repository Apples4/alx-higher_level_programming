#!/usr/bin/python3
'''
     a function that returns the sum of two ints or floats.

    Args:
        a(int or float): input value by user
        b(int or float): inpit value by user
'''


def add_integer(a, b=98):
    '''
    Returns: sum of a + b

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    '''
    if ((not isinstance(a, int) and isinstance(a, float))):
        raise TypeError("a must be an integer")
    else:
        a = int(a)

    if ((not isinstance(b, int) and isinstance(b, float))):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return a + b
