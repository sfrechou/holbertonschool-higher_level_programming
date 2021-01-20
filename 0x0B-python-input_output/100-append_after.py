#!/usr/bin/python3
"""Task 13 - Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """insert line after text"""
    with open(filename, mode='r') as my_file:
        lines = my_file.readlines()
    with open(filename, mode='w') as new_file:
        for line in lines:
            if search_string in line:
                new_file.write(line + new_string)
            else:
                new_file.write(line)
