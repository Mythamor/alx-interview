#!/usr/bin/python3

def pascal_triangle(n):
    """
    first diagonal contains all 1s
    outer edges are all 1s
    each interior no. is the sum of the 2 no.s directly above it
    """
    # Check if list is empty
    if n <= 0:
        return []

    # Initialize the triangle
    triangle = []

    for i in range(n):
        # First element of the row is always 1
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Last element of the row is always 1
        if i > 0:
            row.append(1)

        # Append each row to the triangle
        triangle.append(row)

    return triangle
