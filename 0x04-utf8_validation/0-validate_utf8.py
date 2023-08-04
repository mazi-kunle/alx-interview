#!/usr/bin/python3
'''This is a module'''


def validUTF8(data):
    '''
    A function that determines if a given data set represents
    a valid UTF-8 encoding

    Return: True if data is valid UTF-8 encoding else False
    '''
    remainder = 0

    for i in data:
        i = int(i)
        if remainder == 0:
            if (i >> 7 == 0):
                remainder = 0
            elif (i >> 5 == 110):
                remainder = 1
            elif (i >> 4 == 1110):
                remainder = 2
            elif (i >> 3 == 11110):
                remainder = 3
            else:
                return False
        else:
            if (i >> 6 == 10):
                remainder = remainder - 1

    return (remainder == 0)
