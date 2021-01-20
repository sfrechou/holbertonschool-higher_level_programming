#!/usr/bin/python3
"""Module for task 2 - Append to a file"""


def append_write(filename="", text=""):
    """Function to append string to file"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
