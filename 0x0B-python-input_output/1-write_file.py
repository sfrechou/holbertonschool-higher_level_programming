#!/usr/bin/python3
""" Module for task 1 - Write to a file"""


def write_file(filename="", text=""):
    """Function to write string to text file"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
