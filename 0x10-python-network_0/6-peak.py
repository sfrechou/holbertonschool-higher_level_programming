#!/usr/bin/python3
"""
Write a function that finds a peak
in a list of unsorted integers
"""


def find_peak(lst):
    """function that finds a peak in a list of unsorted integers"""
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)
    else:
        mid_ind = int(len(lst) / 2)
        if lst[mid_ind] > lst[mid_ind + 1]:
            if lst[mid_ind] > lst[mid_ind - 1]:
                return lst[mid_ind]
            else:
                return find_peak(lst[:mid_ind])
        else:
            return find_peak(lst[mid_ind + 1:])
