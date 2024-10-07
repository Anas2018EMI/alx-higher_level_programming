#!/usr/bin/python3

"""
N Queens solver

This script solves the N Queens problem and prints
all possible solutions.
Usage: ./101-nqueens.py N
Where N is an integer greater than or equal to 4.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
    board (list): The current state of the board
    row (int): The row to check
    col (int): The column to check
    n (int): The size of the board

    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Utility function to solve N Queens problem using backtracking

    Args:
    board (list): The current state of the board
    col (int): The current column being processed
    n (int): The size of the board
    solutions (list): List to store all solutions

    Returns:
    bool: True if a solution is found, False otherwise
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions

    Args:
    n (int): The size of the board and number of queens
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
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
