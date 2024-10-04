#!/usr/bin/python3
""" This module contain the pascal_triangle function"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to the nth row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return [] # Return an empty list if n is less than or equal to 0

    triangle = []

    for i in range(n):
        row = [1] * (i + 1) # Create a row with 'i + 1' ones
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

for row in pascal_triangle(5):
    print(row)
