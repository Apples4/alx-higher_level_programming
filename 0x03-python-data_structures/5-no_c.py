#!/usr/bin/python3
def no_c(my_string):
    no_c_string = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(no_c_string))
