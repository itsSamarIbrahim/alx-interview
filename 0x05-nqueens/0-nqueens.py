#!/usr/bin/python3
"""A program that solves the N queens problem"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check column conflict
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check diagonal conflict (upper-left)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check diagonal conflict (upper-right)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    """Use backtracking to find all solutions to the N Queens problem."""
    if row == N:
        # Found a valid solution, extract it as a list of positions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack


def print_solutions(solutions):
    """Print each solution."""
    for solution in solutions:
        print(solution)


def main():
    # Handle command-line arguments
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

    # Initialize board
    board = [[0] * N for _ in range(N)]
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(board, 0, N, solutions)

    # Print the solutions
    print_solutions(solutions)


if __name__ == "__main__":
    main()
