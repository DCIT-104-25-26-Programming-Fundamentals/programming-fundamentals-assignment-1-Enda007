# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in


def calculate_sum(numbers):
    """Calculate the sum of all numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculate the average of all numbers in the list."""
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Find the maximum value in the list."""
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    """Find the minimum value in the list."""
    if len(numbers) == 0:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main():
    """Main program that reads numbers and displays statistics."""
    # Get the number of values from the user
    while True:
        try:
            n = int(input("How many numbers? "))
            if n <= 0:
                print("Error: Number of values must be positive.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    while True:
        try:
            n = int(input("How many numbers? "))
            if n <= 0:
                print("Error: Number of values must be positive.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
        return
    
    # Validate that n is positive
    if n <= 0:
        print("Error: Number of values must be positive.")
        return
    
    # Read the numbers from the user
    numbers = []
    for i in range(1, n + 1):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Enter a valid number.")
    
    # Calculate statistics
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    max_val = find_maximum(numbers)
    min_val = find_minimum(numbers)
    
    # Display results
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")


if __name__ == "__main__":
    main()

