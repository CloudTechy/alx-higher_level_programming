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


    # solve matrix multiplication using numpy
    A = np.array(m_a)
    B = np.array(m_b)
    result_matrix = np.dot(A, B)
    return result_matrix
