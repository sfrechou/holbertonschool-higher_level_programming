#!/usr/bin/python3
"""
Module to define function that multiplies 2 matrices
by using the module NumPy
The columns of m_a should be the same as rows in m_b
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication
        m_a and m_b must be an list of lists of integers or floats
    """

    return numpy.matmul(m_a, m_b)
