#!/usr/bin/python3
'''This is a module'''


def factorial(n):
    '''
    returns factorial of n
    '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combination(n):
    '''
    returns a list of n combination n-1
    '''
    rows = []
    for r in range(n):
        ans = factorial(n - 1) // (factorial(n - 1 - r) * factorial(r))
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
