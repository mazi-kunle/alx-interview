#!/usr/bin/python3
'''This is a module'''


def isPrime(num):
    '''check for prime number
    '''
    if num in [0, 1]:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def getFirstPrime(arr):
    '''gets the first prime num in an arr
    '''
    for i in arr:
        if (isPrime(i)):
            return i
    return None


def getMultiple(num, arr):
    '''remove multiples of <num> from <arr>
    '''
    new_arr = []
    for i in arr:
        if i % num != 0:
            new_arr.append(i)

    return new_arr


def isWinner(x, nums):
    '''check for winner
    '''
    data = {'Maria': 0, 'Ben': 0}

    for i in nums:

        playing = True
        available = [i for i in range(1, i+1)]
        while playing:
            # maria plays
            maria_picks = getFirstPrime(available)
            if (maria_picks is not None):
                # data['Maria'] = data['Maria'] + 1
                available = getMultiple(maria_picks, available)
            else:
                data['Ben'] = data['Ben'] + 1
                playing = False
                break

            # Ben plays
            ben_picks = getFirstPrime(available)
            if (ben_picks is not None):
                # data['Ben'] = data['Ben'] + 1
                available = getMultiple(ben_picks, available)
            else:
                data['Maria'] = data['Maria'] + 1
                playing = False
                break

    if (data['Maria'] == data['Ben']):
        return None
    if (data['Maria'] > data['Ben']):
        winner = 'Maria'
    else:
        winner = 'Ben'

    return f'Winner: {winner}'
