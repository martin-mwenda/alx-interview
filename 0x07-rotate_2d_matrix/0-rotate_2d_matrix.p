#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a square matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The square matrix to rotate.

    Raises:
        ValueError: If the input is not a square matrix.
    """
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Input must be a square matrix")

    n = len(matrix)
    for i in range(n // 2):  # Loop through layers
        last = n - i - 1  # Index of the last element in the current layer
        for j in range(i, last):  # Loop through elements in the layer
            opposite = n - 1 - j  # Calculate the opposite index
            # Perform the 4-way swap
            tmp = matrix[i][j]
            matrix[i][j] = matrix[opposite][i]
            matrix[opposite][i] = matrix[last][opposite]
            matrix[last][opposite] = matrix[j][last]
            matrix[j][last] = tmp
