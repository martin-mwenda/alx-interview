#!/usr/bin/python3
import sys


def find_solutions(n):
    """Find all solutions to the N-Queens problem using backtracking."""
    solutions = [[]]
    for row in range(n):
        solutions = try_placing_queen(row, n, solutions)
    return solutions


def try_placing_queen(row, n, current_solutions):
    """Try placing a queen on the board, ensuring no attacks with others."""
    new_solutions = []
    for solution in current_solutions:
        for col in range(n):
            if is_valid_position(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_valid_position(row, col, solution):
    """Check if placing a queen at (row, col) is safe."""
    if col in solution:
        return False
    return all(abs(solution[i] - col) != row - i for i in range(row))


def parse_input_args():
    """Parse and validate the input argument for N."""
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


def display_solutions(solutions):
    """Print the N-Queens solutions in the required format."""
    for solution in solutions:
        formatted_solution = [[row, col] for row, col in enumerate(solution)]
        print(formatted_solution)


def main():
    """Main function to solve the N-Queens problem."""
    n = parse_input_args()
    solutions = find_solutions(n)
    display_solutions(solutions)


if __name__ == '__main__':
    main()
