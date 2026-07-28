# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(name):
    """Prompt the user for dimensions and rows, and return a 2D list."""
    while True:
        try:
            rows = int(input(f"Enter number of rows{name}: "))
            cols = int(input(f"Enter number of columns{name}: "))
            if rows <= 0 or cols <= 0:
                print("Error: Rows and columns must be positive integers.")
                continue
            break
        except ValueError:
            print("Error: Please enter valid whole numbers.")

    matrix = []
    for r in range(1, rows + 1):
        while True:
            row_input = input(f"Enter row {r}: ").split()
            try:
                row = [float(value) for value in row_input]
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
                continue
            if len(row) != cols:
                print(f"Error: Expected {cols} values, got {len(row)}.")
                continue
            break
        matrix.append(row)

    return matrix


def display_matrix(matrix, title="Matrix"):
    """Print a matrix in a neat, aligned grid format."""
    print(f"{title}:")
    for row in matrix:
        formatted = "  ".join(f"{value:g}" for value in row)
        print(formatted)
    print()


def transpose_matrix(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-size matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product of A (MxN) and B (NxP)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    matrix = read_matrix("")
    display_matrix(matrix, "Original Matrix")
    display_matrix(transpose_matrix(matrix), "Transposed Matrix")


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    print("Matrix A:")
    matrix_a = read_matrix(" for Matrix A")
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    print("Matrix B (must be the same size as Matrix A):")
    while True:
        matrix_b = read_matrix(" for Matrix B")
        if len(matrix_b) != rows_a or len(matrix_b[0]) != cols_a:
            print(f"Error: Matrix B must be {rows_a}x{cols_a} to match Matrix A.")
            continue
        break

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(add_matrices(matrix_a, matrix_b), "A + B")


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    print("Matrix A (M x N):")
    matrix_a = read_matrix(" for Matrix A")
    cols_a = len(matrix_a[0])

    print("Matrix B (N x P) — rows of B must equal columns of A:")
    while True:
        matrix_b = read_matrix(" for Matrix B")
        if len(matrix_b) != cols_a:
            print(f"Error: Matrix B must have {cols_a} rows to match Matrix A's columns.")
            continue
        break

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(multiply_matrices(matrix_a, matrix_b), "A x B")


def main():
    part_a_transpose()
    part_b_add()
    part_c_multiply()


if __name__ == "__main__":
    main()