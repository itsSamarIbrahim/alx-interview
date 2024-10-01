#!/usr/bin/python3
"""
A function determines the fewest number of coins needed to meet a given
amount total, given a pile of coins of different values.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount
    using a list of coin denominations. If the total cannot be met, returns -1.

    Parameters:
    coins (list): A list of positive integers representing coin denominations.
    total (int): The target amount to be achieved with the coins.

    Returns:
        int: The minimum number of coins needed to make the total, or -1 if the
             total cannot be met with the given denominations.

    Example:
    >>> makeChange([1, 2, 25], 37)
    7
    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1

    Explanation:
    - For the first example, the fewest number of coins is 7 (25 + 10 + 2 = 37)
    - For the second example, it's not possible to make 1453 with the given
      coins, so the result is -1.
    """
    if total == 0:
        return 0

    # Initialize a dp array where dp[i] represents the minimum coins
    #   to make amount i
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Loop through all amounts from 1 to total
    for n in range(1, total + 1):
        # Check for every coin
        for coin in coins:
            if n - coin >= 0:
                # Update dp[n] to the minimum number of coins needed
                dp[n] = min(dp[n], dp[n - coin] + 1)

    # If dp[total] is still greater than total, it means it's not possible to
    #   form the amount
    return dp[total] if dp[total] <= total else -1
