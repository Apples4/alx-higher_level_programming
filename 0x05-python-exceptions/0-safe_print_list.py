#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(0, x):
        try:
            print(my_list[i], end='')
            i = i + 1
        except IndexError:
            break
    print()
    return (i)
