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
# Helper function to get matrix dimensions from the user's input
def read_dims(name):
    """Ask for rows and columns, and keep asking until both are positive."""
    while True:
        dims = input(f"Enter number of rows and columns for {name} separated by space: ").split()
        if len(dims) != 2:
            print("Please enter exactly two numbers separated by a space.")
            continue

        try:
            rows, cols = int(dims[0]), int(dims[1])
        except ValueError:
            print("Please enter valid integers for rows and columns.")
            continue

        if rows <= 0 or cols <= 0:
            print("Please enter positive integer values for rows and columns.")
            continue

        return rows, cols

#Defining the functions for rows and columns of the matrix and performing operations on them
def read_matrix(rows, cols):
    """Ask the user for one value at a time and build a matrix (list of lists)."""
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            value = int(input(f"Enter value for row {r + 1}, column {c + 1}: "))
            row.append(value)
        matrix.append(row)
    return matrix


def format_matrix(mat):
    """Turn a matrix into a printable string, one row per line."""
    lines = []
    for row in mat:
        line = ""
        for value in row:
            line += str(value) + " "
        lines.append(line)
    return "\n".join(lines)

#defining part A- Matrix operations:Transpose
def transpose_matrix(mat):
    """Flip rows and columns: new_row c, column r = old row r, column c."""
    rows = len(mat)
    cols = len(mat[0])

    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(mat[r][c])
        result.append(new_row)
    return result

#defining part B- Matrix operations:Addition
def add_matrices(a, b):
    """Add two same-sized matrices, position by position."""
    rows = len(a)
    cols = len(a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)
    return result


#defining part C- Matrix operations:Multiplication
def multiply_matrices(a, b):
    """
    Multiply matrix a (rows_a x cols_a) by matrix b (cols_a x cols_b).
    Each result cell is the sum of (row from a) times (column from b).
    """
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result




while True:
    print("\nChoose operation:\n1) Transpose\n2) Add two matrices\n3) Multiply two matrices\nQ) Quit")
    choice = input("Enter choice: ").strip().lower()

    if choice == "1":
        rows, cols = read_dims("matrix")
        mat = read_matrix(rows, cols)
        print("\nOriginal Matrix:")
        print(format_matrix(mat))
        print("\nTransposed Matrix:")
        print(format_matrix(transpose_matrix(mat)))

    elif choice == "2":
        rows, cols = read_dims("matrices")
        print("Enter values for matrix A:")
        a = read_matrix(rows, cols)
        print("Enter values for matrix B:")
        b = read_matrix(rows, cols)
        print("\nMatrix A:")
        print(format_matrix(a))
        print("\nMatrix B:")
        print(format_matrix(b))
        print("\nSum (A + B):")
        print(format_matrix(add_matrices(a, b)))

    elif choice == "3":
        rows_a, cols_a = read_dims("matrix A")
        print("Enter values for matrix A:")
        a = read_matrix(rows_a, cols_a)

        rows_b, cols_b = read_dims("matrix B")
        if rows_b != cols_a:
            print("\nError: Number of rows in B must equal number of columns in A.")
            continue

        print("Enter values for matrix B:")
        b = read_matrix(rows_b, cols_b)
        print("\nMatrix A:")
        print(format_matrix(a))
        print("\nMatrix B:")
        print(format_matrix(b))
        print("\nProduct (A x B):")
        print(format_matrix(multiply_matrices(a, b)))

    elif choice == "q":
        break

    else:
        print("Invalid choice.")
