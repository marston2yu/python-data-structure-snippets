# Dynamic programming solution for change calculation problems.
# Problem: calculate minimum coins needed for given changes.

import numpy as np


def minCoins(coinValues, change):
    ''' Calculate minimum coins needed for change from 1 to `change`.
    To calculate coins needed for each change, find the minimum coins needed for change of `change - coin value`,
    in which coin value is fetched from `coinValues`.
    In order to calculate the specific coins for change, we trace the minimum-optimization path by maintaining a list
    of last coin added to reach the change index.
    :param coinValues: List of coin values.
    :param change: Total change.
    :return: Minimum coins needed for change and list of coins for the given change.
    '''
    changeList = [0] * change  # Initialize min coins look-up list with zero.
    coinsList = [0] * change  # Last coins needed to reach the change values.

    for currentChange in range(1, change + 1):
        minCoins = np.inf  # Initialize minimum coins needed with positive infinity.

        # Initialize last coin with any value because the first time the following inner loop is executed,
        # the `coins` must be smaller than `minCoins` witch is infinity, therefore lastCoin will be reassigned.
        lastCoin = 0
        for v in [v for v in coinValues if v <= currentChange]:
            # Find the minimum coins needed for change of `change - coin value`, then add one, meaning counting the
            # coin of value `v`.
            coins = changeList[currentChange - v - 1] + 1
            if coins < minCoins:
                minCoins = coins
                lastCoin = v
        coinsList[currentChange - 1] = lastCoin
        changeList[currentChange - 1] = minCoins  # Index is smaller than change by 1.

    # Trace back coins flows to collect the coins for change.
    coins = []
    remainChange = change
    while remainChange != 0:
        lastCoin = coinsList[remainChange - 1]
        remainChange = remainChange - lastCoin
        coins.append(lastCoin)

    return changeList[change - 1], coins


if __name__ == '__main__':
    coinValues = [1, 5, 10, 25]
    print(minCoins(coinValues, 63))
