#!/usr/bin/env python3
"""
Prime Number Checker

A simple Python script that checks if a given integer is prime using trial division.
The script implements robust input validation and follows best practices for code quality.
"""

import math
import sys


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division algorithm.

    Parameters
    ----------
    n : int
        The integer to check for primality.

    Returns
    -------
    bool
        True if n is prime, False otherwise.

    Notes
    -----
    - Uses trial division up to and including sqrt(n)
    - Handles edge cases: n < 2 returns False, n == 2 returns True
    - Even numbers (except 2) are immediately rejected
    """
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only need to check odd divisors up to sqrt(n)
    # math.isqrt() returns the integer square root
    limit = math.isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False

    return True


def get_validated_input() -> int:
    """
    Prompt the user for a positive integer and validate the input.

    Returns
    -------
    int
        A valid positive integer entered by the user.

    Notes
    -----
    - Reprompts on invalid input (negative numbers, zero, non-integers)
    - Provides clear error messages for different failure modes
    - Strips whitespace from input
    """
    while True:
        try:
            # Get input and strip whitespace
            user_input = input("Enter a positive integer: ").strip()

            # Convert to integer
            number = int(user_input)

            # Validate positivity
            if number <= 0:
                print("Error: Please enter a positive integer (greater than 0).")
                continue

            return number

        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")


def main() -> None:
    """
    Main function that orchestrates the prime number checking workflow.

    Gets validated input from user, checks if it's prime, and prints the result.
    """
    # Get validated input from user
    number = get_validated_input()

    # Check if the number is prime
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


if __name__ == "__main__":
    main()