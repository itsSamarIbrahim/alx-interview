#!/usr/bin/python3
"""
This script contains a function to calculate the minimum number of operations
needed to result in exactly n 'H' characters in a text editor, where the only
operations allowed are "Copy All" and "Paste".
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in
    exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required.
            If n is less than or equal to 1, returns 0.
    """
    if n <= 1:
        return 0  # If n is less than or equal to 1, no operations are needed

    operations = 0
    factor = 2  # Start with the smallest factor

    while n > 1:
        while n % factor == 0:  # While n is divisible by the factor
            operations += factor  # Add the factor to operations
            n /= factor  # Reduce n by dividing it by the factor
        factor += 1  # Move to the next factor

    return operations
