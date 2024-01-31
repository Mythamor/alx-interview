#!/usr/bin/python3

"""
Module: 0-making_change.py
"""


def makeChange(coins, total):
    """
    Determines fewest number of coins needed to meet a given total
    """
    number_of_coins = [float('inf')] * (total + 1)

    # Base case
    number_of_coins[0] = 0

    # Iterate throught the coins
    for coin in coins:
        for i in range(coin, total + 1):
            number_of_coins[i] = min(number_of_coins[i],
                                     number_of_coins[i - coin] + 1)

    # Return the fewest no. of coins needed to meet the total
    return number_of_coins[total] if \
        number_of_coins[total] != float('inf') else -1
