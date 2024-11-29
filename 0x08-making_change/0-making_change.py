#!/usr/bin/python3

""" 
Module for the makeChange function.

The makeChange function returns the fewest number of coins needed to make up a given total.
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
    if total <= 0:
        return 0

    # Initialize dp array where dp[i] is the minimum number of coins needed for i amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed for total 0

    # Loop through each coin in coins and update dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 (total can't be made)
    return dp[total] if dp[total] != float('inf') else -1
