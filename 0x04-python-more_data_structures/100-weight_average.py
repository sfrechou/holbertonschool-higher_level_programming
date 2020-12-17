#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multsum = 0
    div = 0
    for element in my_list:
        multsum += element[0] * element[1]
        div += element[1]
    return multsum / div
