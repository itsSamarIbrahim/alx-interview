""" 0. Change comes from within """


# Given a pile of coins of different values,
# determine the fewest number of coins needed to
# meet a given amount total
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total
    """
    # create the 'array of ways'
    matrix = [total + 1] * (total + 1)
    matrix[0] = 0

    # for each step of the matrix, l -> r
    for n in range(1, total + 1):
        # look at each coin in matrix
        for coin in coins:
            # if n (index of matrix) minus coin is greater than 0
            if n - coin >= 0:
                # Then we must be able to remove a coin
                # Thus making the count of coins necessary less
                # we'll check the min to set the new lower value
                matrix[n] = min(matrix[n], 1 + matrix[n - coin])

    return matrix[total] if matrix[total] < total + 1 else -1
