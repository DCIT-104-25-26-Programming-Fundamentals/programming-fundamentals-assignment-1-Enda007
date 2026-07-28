# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
#Defining a function to validate if the input is a positive integer
def validate_positive_integer(value):
    try:
        number = int(value)
    except ValueError:
        return None

    if number > 0:
        return number
    return None

# Defining a function to print the multiplication table for a single number
def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:>2}  =  {number * i:>2}")

# Defining a function to print multiplication tables for numbers from 1 to n
def print_full_tables(n):
    for number in range(1, n + 1):
        print(f"Multiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number}  x  {i:>2}  =  {number * i:>2}")
        if number != n:
            print("-" * 27)

#Defining the main function to handle user input and call the appropriate functions
def main():
    part_a_input = input("Enter a number for Part A: ")
    part_a = validate_positive_integer(part_a_input)
    if part_a is None:
        print("Error: Please enter a positive integer.")
        return

    print_single_table(part_a)

    part_b_input = input("Enter a number N for Part B: ")
    part_b = validate_positive_integer(part_b_input)
    if part_b is None:
        print("Error: Please enter a positive integer.")
        return

    print_full_tables(part_b)


if __name__ == "__main__":
    main()

