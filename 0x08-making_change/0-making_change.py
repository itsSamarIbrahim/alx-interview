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

    # Initialize the dp array to store the minimum number of coins
    #   for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    # Loop through each coin
    for coin in coins:
        # Update the dp array for amounts that can be made with this coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total is achievable, return the number of coins,
    #   otherwise return -1
    return dp[total] if dp[total] != float('inf') else -1
