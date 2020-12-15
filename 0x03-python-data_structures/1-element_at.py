#!/usr/bin/python3
def element_at(my_list, idx):
    if (my_list):
        if idx >= len(my_list) or idx < 0:
            return
        else:
            return my_list[idx]
    else:
        return
