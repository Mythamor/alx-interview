#!/usr/bin/python3

"""
Module: 0-prime_game
"""


# Helper function to find prime nums upto n
def is_prime(n):
    """
    finds prime numbers upto a given value
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Helper function to find number of primes in a given range
def prime_numbers(start, end):
    """"
    Finds number of primes in a given range
    """
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determines winner using prime numbers
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        divisible_nums = list(range(1, n + 1))
        primes = prime_numbers(1, n)

        if not primes:
            ben_wins += 1
            continue

        maria_turn = True

        while (True):
            if not primes:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes.pop(0)
            divisible_nums.remove(smallest_prime)

            divisible_nums = [x for x in divisible_nums if x %
                              smallest_prime != 0]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
