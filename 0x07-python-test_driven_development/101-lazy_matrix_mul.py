#!/usr/bin/python3

""" This module solves numpy matrix multiplication """

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrix

    args:
        m_a (list): matrix a
        m_b (list): matrix b

    Returns
        m_C (list): product of matrix a and b
    """

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # check if m_a and m_b is list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check for valid list in list
    row_len = set()
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("m_a should contain only integers or floats")
        row_len.add(len(row))

    # check if the rows are equal length
    if len(row_len) != 1:
        raise TypeError("each row of m_a must be of the same size")

    row_len = set()
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("m_b should contain only integers or floats")
        row_len.add(len(row))

    # check if the rows are equal length
    if len(row_len) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # check for valid matrix

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # solve matrix multiplication using numpy
    A = np.array(m_a)
    B = np.array(m_b)
    result_matrix = np.dot(A, B)
    return result_matrix
