#!/usr/bin/python3
"""
Module to define function that multiplies 2 matrices
m_a and m_b must be an list of lists of integers or floats
The columns of m_a should be the same as rows in m_b
"""


def matrix_mul(m_a, m_b):
    """ Matrix multiplication
        m_a and m_b must be an list of lists of integers or floats
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if not all(isinstance(lists, list) for lists in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(lists, list) for lists in m_b):
        raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for lists in m_a:
        if not all(isinstance(elems, (int, float)) for elems in lists):
            raise TypeError('m_a should contain only integers or floats')
    for lists in m_b:
        if not all(isinstance(elems, (int, float)) for elems in lists):
            raise TypeError('m_b should contain only integers or floats')
    if not all(len(l) == len(m_a[0]) for l in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(l) == len(m_b[0]) for l in m_b):
        raise TypeError('each row of m_b must be of the same size')
    m_a_col = len(m_a[0])
    m_b_row = len(m_b)
    if m_a_col != m_b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[sum(a*b for a, b in zip(
                    X_row, Y_col)) for Y_col in zip(*m_b)] for X_row in m_a]
    return new_matrix
