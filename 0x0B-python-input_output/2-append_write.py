#!/usr/bin/python3
'''
This function is for appending a file
at the end of the file
'''


def append_write(filename="", text=""):
    '''
    Args:
        filename- file that will be appended
        text- string to be appended onto the file

    Return:
        the number of characters added
    '''
    with open(filename, "a") as f:
        return f.write(text)
