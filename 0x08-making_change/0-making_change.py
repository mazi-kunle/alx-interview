#!/usr/bin/python3
'''This is a module
'''


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''

    if total <= 0:
        return 0

    cache = [total + 1] * (total + 1)

    cache[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                cache[i] = min(cache[i], cache[i - coin] + 1)

    return cache[total] if cache[total] < total else -1

# print(makeChange([1, 2, 25], 37))

# print(makeChange([1256, 54, 48, 16, 102], 1453))
