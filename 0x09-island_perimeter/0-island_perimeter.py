#!/usr/bin/python3

"""
Module: 0. Island Perimeter
"""


def island_perimeter(grid):
    """
    It returns the perimeter of the isalnd described in the grid
    """
    # Check if grid is empty or exceeds size liomit
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    if not grid or rows > 100 or cols > 100:
        return 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
