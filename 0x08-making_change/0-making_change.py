#!/usr/bin/python3

"""
Module for the makeChange function using a greedy algorithm.

The makeChange function returns the fewest number of coins
needed to make up a given total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The total amount for which we need to make change.

    Returns:
        int: The fewest number of coins required to meet the total, or
             -1 if it's not possible to form the total with the given coins.

    If total is 0 or less, returns 0, as no coins are needed.
    If the total cannot be made with any combination of the available coins,
    returns -1.
    """
    if not coins or total <= 0:
        return 0 if total <= 0 else -1

    # Sort coins in descending order for greedy approach
    coins.sort(reverse=True)

    change = 0
    for coin in coins:
        # Use as many of the current coin as possible
        while total >= coin:
            total -= coin
            change += 1
        # If we have exactly matched the total, return the number of coins used
        if total == 0:
            return change

    return -1
