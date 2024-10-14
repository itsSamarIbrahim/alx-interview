#!/usr/bin/python3
"""
Prime Game - Competitive Game Simulation

This module simulates a competitive game between two players, Maria and Ben,
who take turns choosing prime numbers from a set of consecutive integers
ranging from 1 to n. The chosen prime number and its multiples are removed
from the set, and the game continues until no prime numbers are left. The
player who cannot make a move loses the game. Maria always starts first, and
both players play optimally.

Functions:
    - sieve_of_eratosthenes(max_num): Generates a list indicating prime numbers
      up to a given limit using the Sieve of Eratosthenes algorithm.
    - calculate_winner(n, primes): Determines the winner for a given round
      based on the optimal moves made by the players.
    - isWinner(x, nums): Determines the overall winner after x rounds of the
      game, given an array of integers representing the set size for each
      round.

Assumptions:
    - 1 <= n <= 10000 for all rounds.
    - Maria always starts the game.
    - Both players play optimally.

Usage:
    This module can be used to determine the winner of multiple rounds of the
    game by calling the isWinner function with the number of rounds (x) and
    an array (nums) containing the upper limits for each round.

Example:
    >>> isWinner(3, [4, 5, 1])
    'Ben'
"""


def sieve_of_eratosthenes(max_num):
    """Helper function to generate prime numbers up to max_num."""
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime


def calculate_winner(n, primes):
    """Determine the winner for a given n based on optimal moves."""
    removed = [False] * (n + 1)
    turn = 0  # 0 for Maria, 1 for Ben

    for i in range(2, n + 1):
        if primes[i] and not removed[i]:
            # Remove the prime and its multiples
            for j in range(i, n + 1, i):
                removed[j] = True
            # Switch turns
            turn = 1 - turn

    # If Maria was the last to make a valid move, Ben loses
    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """Determine who won the most rounds given x rounds."""
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
