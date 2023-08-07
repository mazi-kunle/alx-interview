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
            if (bin(i >> 7) == '0b0'):
                remainder = 0
            elif (bin(i >> 5) == '0b110'):
                remainder = 1
            elif (i >> 4 == 1110):
                remainder = 2
            elif (bin(i >> 3) == '0b11110'):
                remainder = 3
            else:
                return False
        else:
            if (bin(i >> 6) == '0b10'):
                remainder = remainder - 1
            else:
                return False

    return (remainder == 0)

# data = [65]
# print(validUTF8(data)) # True

# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print(validUTF8(data)) # True
# data = [229, 65, 127, 256]
# print(validUTF8(data)) # False
