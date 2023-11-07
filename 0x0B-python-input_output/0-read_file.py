#!/usr/bin/python3
'''
Function that reads a file
'''


def read_file(filename=""):
    '''
    Args:
        filename: name of he file

    Return:
        prints file to STDOUT
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end='')
