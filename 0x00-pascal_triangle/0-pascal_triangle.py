#!/usr/bin/python3
'''This is a module'''

from math import factorial


def combination(n):
    '''
    returns a list of n combination n-1
    '''
    rows = []
    for r in range(n):
        ans = int((factorial(n - 1) / (factorial(n - 1 - r) * factorial(r))))
        rows.append(ans)

    return rows


def pascal_triangle(n):
    '''
    returns the n pascal triangle
    '''
    res = []
    for i in range(1, n+1):
        res.append(combination(i))
    return res
