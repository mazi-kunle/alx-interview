#!/usr/bin/python3
'''This is a module'''


def canUnlockAll(boxes):
    '''
    A function that solves a lockbox problem
    '''
    unlocked = [0]
    for index, box in enumerate(boxes):
        for i in box:
            if i < len(boxes) and i not in unlocked and i != index:
                unlocked.append(i)

    return len(boxes) == len(unlocked)
