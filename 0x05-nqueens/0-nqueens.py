#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Checks if a queen can be placed safely at the given position.
    """
    # Check for queens in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for queens in diagonals (upward and downward)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """
    Solves the N queens problem recursively using backtracking.
    """
    if col >= len(board):
        # Print the solution when all queens are placed
        solution = [[i, j] for i in range(len(board))
                    for j in range(len(board)) if board[i][j] == 1]
        print(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            board[i][col] = 0  # Backtrack


def main():
    """
    Main function for handling arguments and solving N queens problem.
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

    board = [[0] * n for _ in range(n)]  # Initialize empty board
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()
