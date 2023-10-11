#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    sum_set = set(my_list)
    for i in sum_set:
        summation += i
    return summation
