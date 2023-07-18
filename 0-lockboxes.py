#!/usr/bin/python3


def canUnlockAll(boxes):
    '''
    A function that solves a lockbox problem
    '''
    unlocked = [0]
    for index, box in enumerate(boxes):
        for i in box:
            print(i)
            if i < len(boxes) and i not in unlocked and i != index:
                unlocked.append(i)

    return len(boxes) == len(unlocked)
