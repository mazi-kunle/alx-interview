#!/usr/bin/python3
'''This is a module'''

import datetime
import time
import sys

def checkFormat(lst):
    '''
    check format for string
    '''
    lst = lst.split(' ')
    # print(lst)
    checks = 0
    if len(lst) != 9:
        return checks
    
    # ip check
    ip = lst[0].split('.')
    if len(ip) == 4:
        if len([i for i in ip if 
                int(i) >= 0 and int(i) <= 255]) == 4:
            checks = checks + 1
    
    if lst[1] == '-':
        checks += 1
    
    # date check
    date = lst[2] + ' ' + lst[3]
    if date[0] == '[' and date[-1] == ']':
        date = date[1:-1]
        format = "%Y-%m-%d %H:%M:%S.%f"
        try:
            date = datetime.datetime.strptime(date, format)
        except ValueError:
            return
        else:
            checks += 1

    req = lst[4] + ' ' + lst[5] + ' ' + lst[6]
    if req == '"GET /projects/260 HTTP/1.1"':
        checks += 1
    
    statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
    if (type(eval(lst[7])) == int
         and int(lst[7]) in statusCodes):
        checks += 1
    
    filesize = lst[8].rstrip()
    if type(eval(filesize)) == int:
        checks += 1

    return checks

read = True
statusCodes = {'200': 0, '301': 0, '400': 0, '401':0,
              '403':0, '404': 0, '405':0, '500':0}
count = 0

while read:
    start = 0
    while start < 10:
        # user = input()
        try:
            user = input()
        
            if (checkFormat(user) == 6):
                status = user.split(' ')[-2].rstrip()
                filesize = int(user.split(' ')[-1])
                count = count + filesize

                if (status in statusCodes.keys()):
                    statusCodes[status] += 1
        
        except (KeyboardInterrupt):
            start = 10
            print(f'File size: {count}')
            for (key, value) in statusCodes.items():
                if value != 0:
                    print(f'{key}: {value}')
            time.sleep(0.01)
        
        if start == 9:
            print(f'File size: {count}')
            for (key, value) in statusCodes.items():
                if value != 0:
                    print(f'{key}: {value}')
        
        start += 1
