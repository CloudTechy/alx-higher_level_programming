#!/usr/bin/python3

""" Divides all element of a matrix with a given number """


def matrix_divided(matrix, div):
    """
    Divides a matrix by div argument

    args:
        matrix (nested list): a matrix
        div (int): divisible operand
    Returns:
        matrix: returns a nested list of the divided matrix
    """
    row_length = set(len(row) for row in matrix)
    if len(row_length) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)
    return new_matrix
