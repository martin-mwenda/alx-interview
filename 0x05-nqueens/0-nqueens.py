#!/usr/bin/python3
import sys


def solve_nqueens(n):
    """Solve the N-Queens problem using backtracking."""
    solutions = [[]]
    for row in range(n):
        solutions = place_queen(row, n, solutions)
    return solutions


def place_queen(row, n, previous_solutions):
    """Place a queen on the board, ensuring no attacks with other queens."""
    new_solutions = []
    for solution in previous_solutions:
        for col in range(n):
            if is_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_safe(row, col, solution):
    """Check if a queen can be safely placed at the given position."""
    if col in solution:
        return False
    return all(abs(solution[i] - col) != row - i for i in range(row))


def parse_input():
    """Parse and validate the input argument."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        formatted_solution = [[row, col] for row, col in enumerate(solution)]
        print(formatted_solution)


def nqueens():
    """Main function to solve the N-Queens problem."""
    n = parse_input()
    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == '__main__':
    nqueens()
