#!/usr/bin/python3
"""N queens solution finder module."""
import sys


def parse_arguments():
    """Parses and validates the program's argument."""
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
    return n


def queens_conflict(pos0, pos1):
    """Checks if two queens are in an attacking position."""
    return (
        pos0[0] == pos1[0] or
        pos0[1] == pos1[1] or
        abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])
    )


def find_nqueens_solutions(n):
    """Uses backtracking to find all solutions for the N queens problem."""
    def backtrack(row, current_solution):
        if row == n:
            solutions.append(current_solution[:])
            return
        for col in range(n):
            candidate = (row, col)
            if all(
                not queens_conflict(candidate, q)
                for q in current_solution
            ):
                current_solution.append(candidate)
                backtrack(row + 1, current_solution)
                current_solution.pop()

    solutions = []
    backtrack(0, [])
    return solutions


# Main execution
n = parse_arguments()
solutions = find_nqueens_solutions(n)
for solution in solutions:
    print(solution)
