#!/usr/bin/python3

"""
Module: 0-rotate_2d_matrix.py
        Given an n x n 2D matrix, rotate it 90 degrees clockwise.
            - Do not return anything.
            - The matrix must be edited in-place.
            - Assume the matrix will have 2 dimensions & will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D Matrix
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
