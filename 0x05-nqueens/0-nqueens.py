#!/usr/bin/python3

"""
Module: 0-nqueens
"""

import sys


def is_safe(board, row, col, N):
    """
    Function to check if Queen can be placed
    """
    # Check if there's a queen in the same col
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N):
    """
    Implement the backtracking algorithim
    """
    if row == N:
        print([[i, j] for i in range(N)
              for j in range(N) if board[i][j] == 1])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N)
            board[row][col] = 0


def main():
    """
    Initaialize the chessboard and call the solver
    """
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize empty chessboard
    board = [[0] * N for _ in range(N)]

    # Call the solver
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
