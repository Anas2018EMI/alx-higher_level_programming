#!/usr/bin/python3
"""
N Queens solver

This script solves the N Queens problem and prints
all possible solutions.
Usage: ./101-nqueens.py N
Where N is an integer greater than or equal to 4.
"""

import sys


class NQueens:
    """
    A class to solve the N Queens problem.
    """

    def __init__(self, n):
        """
        Initialize the NQueens solver.

        Args:
        n (int): The size of the board and number of queens
        """
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        """
        Check if it's safe to place a queen at board[row][col]

        Args:
        row (int): The row to check
        col (int): The column to check

        Returns:
        bool: True if it's safe to place a queen, False otherwise
        """
        for i in range(col):
            if self.board[i] == row or \
               self.board[i] - i == row - col or \
               self.board[i] + i == row + col:
                return False
        return True

    def solve_util(self, col):
        """
        Utility function to solve N Queens problem
        using backtracking

        Args:
        col (int): The current column being processed

        Yields:
        list: A valid solution to the N Queens problem
        """
        if col == self.n:
            yield [[i, self.board[i]] for i in range(self.n)]
        else:
            for row in range(self.n):
                if self.is_safe(row, col):
                    self.board[col] = row
                    yield from self.solve_util(col + 1)

    def solve(self):
        """
        Solve the N Queens problem and print all solutions
        """
        for solution in self.solve_util(0):
            print(solution)


def main():
    """
    Main function to handle input and solve the N Queens problem
    """
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

    nqueens = NQueens(n)
    nqueens.solve()


if __name__ == "__main__":
    main()
