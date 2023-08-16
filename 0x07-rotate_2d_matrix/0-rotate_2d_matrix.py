#!/usr/bin/python3
'''This is a module'''


def rotate_2d_matrix(matrix):
    '''rotates a nxn 2D matrix in place
    '''
    row = len(matrix)

    # Transpose the matrix
    for i in range(row):
        for j in range(i, row):
            # swap values
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row in matrix
    for i in matrix:
        i.reverse()
