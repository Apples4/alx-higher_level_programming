#!/usr/bin/python3
'''
This module '4-print_square.py'
The module has one function, print_square(size)
'''


def print_square(size):
    '''
    Args:
        size is an int

    Returns:
         prints a square with the character #

    Raises:
        TypeError: size must be an integer
        TypeError: size must be an integer
        ValueError: size must be >= 0
        '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
