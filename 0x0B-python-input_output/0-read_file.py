#!/usr/bin/python3
""" Module for task 0 - Read File"""


def read_file(filename=""):
    """Function to read a text file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
