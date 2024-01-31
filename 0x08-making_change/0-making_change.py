#!/usr/bin/python3

"""
Module: 0-making_change.py
"""


def makeChange(coins, total):
    """
    Determines fewest number of coins needed to meet a given total
    """
    if total <= 0:
        return 0

    # Sort the coins in desc order
    coins.sort(reverse=True)

    # Initialize number of coins
    count = 0

    # Iterrate through the list of coins
    for coin in coins:
        if total <= 0:
            break

        remainder = total // coin
        count += remainder
        total -= (remainder * coin)
    if total != 0:
        return -1
    return count
