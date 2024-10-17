#!/usr/bin/python3
"""
Function that calculates the minimum number of operations
to achieve exactly n 'H' characters using Copy All and Paste.
"""


def minOperations(n):
    # Return 0 for impossible cases
    if n < 2:
        return 0

    total_operations = 0  # Total number of operations needed
    factor = 2  # Start checking from the smallest prime factor

    while n > 1:
        # While n is divisible by the current factor
        while n % factor == 0:
            total_operations += factor  # Increment operation byfactor(Cp+Pst)
            n //= factor  # Reduce n by dividing it by the factor
        factor += 1  # Move to the next potential factor

    return total_operations
