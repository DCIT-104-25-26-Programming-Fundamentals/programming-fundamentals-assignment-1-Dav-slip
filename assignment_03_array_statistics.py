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
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the largest value in the list (no built-in max())."""
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def find_minimum(numbers):
    """Return the smallest value in the list (no built-in min())."""
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def main():
    count_input = input("How many numbers? ")

    try:
        count = int(count_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if count <= 0:
        print("Error: The count must be a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        value_input = input(f"Enter number {i}: ")
        try:
            value = float(value_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    print()
    print("Results:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()