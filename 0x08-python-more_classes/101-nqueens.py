#!/usr/bin/python3
"""
N Queens solver

This script solves the N Queens problem and prints
all possible solutions.
Usage: ./101-nqueens.py N
Where N is an integer greater than or equal to 4.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
    board (list): The current state of the board
    row (int): The row to check
    col (int): The column to check

    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board, col, n):
    """
    Utility function to solve N Queens problem using backtracking

    Args:
    board (list): The current state of the board
    col (int): The current column being processed
    n (int): The size of the board

    Yields:
    list: A valid solution to the N Queens problem
    """
    if col == n:
        yield [[i, board[i]] for i in range(n)]
    else:
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                yield from solve_nqueens_util(board, col + 1, n)


def solve_nqueens(n):
    """
    Solve the N Queens problem and
    print all solutions

    Args:
    n (int): The size of the board
    and number of queens
    """
    board = [-1] * n
    for solution in solve_nqueens_util(board, 0, n):
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
