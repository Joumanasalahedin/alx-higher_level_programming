#!/usr/bin/python3
""" Module with function that divides numbers in a matrix """


def matrix_divided(matrix, div):
    """
    Function that divides integers/floats of a matrix

    Args:
    matrix: list of a lists of integers/floats
    div: number which divides the matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
