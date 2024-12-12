#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """
    Determines the overall winner after x rounds of the game.

    Args:
        x (int): Number of rounds to be played.
        nums (list of int): List of numbers defining the range for each round.

    Returns:
        str or None: The name of the winner ("Maria" or "Ben"),
        or None if it's a tie.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_win = 0
    maria_win = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben_win += 1
        else:
            maria_win += 1
    if ben_win > maria_win:
        return "Ben"
    if maria_win > ben_win:
        return "Maria_win"
    return None


def rm_multiples(ls, x):
    """removes multiple of prime numbers
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
