#!/usr/bin/python3
'''This is a module'''


def island_perimeter(grid):
    '''
    returns the perimeter of the island described in grid
    '''
    row = len(grid)
    col = len(grid[0])
    p = 0
    connected = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                p = p + 4
                if i > 0 and grid[i-1][j]:
                    connected = connected + 1
                if j > 0 and grid[i][j-1]:
                    connected = connected + 1
                    print(i, j)

    return p - (connected * 2)


# grid = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]
