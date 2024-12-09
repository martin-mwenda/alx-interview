#!/usr/bin/python3
"""Function to find the perimeter of an island."""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (list of list of int): The grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four neighbors (top, left, right, bottom)
                neighbors = [
                    (i - 1, j),  # Top
                    (i, j - 1),  # Left
                    (i, j + 1),  # Right
                    (i + 1, j)   # Bottom
                ]

                for x, y in neighbors:
                    # Increment perimeter if out of bounds or water
                    if (
                        x < 0 or x >= rows or
                        y < 0 or y >= cols or
                        grid[x][y] == 0
                    ):
                        perimeter += 1

    return perimeter
