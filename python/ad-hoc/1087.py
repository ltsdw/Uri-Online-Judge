'''
title: Dama
number of the problem: 1087
date: 15/04/2018
author: ltsdw
'''

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0:
        break
    else:
        if x1 == x2 and y1 == y2:
            print('0')
        elif x2 - x1 == -(y2 - y1) or -(x2 - x1) == -(y2 - y1) or -(x2 - x1) == y2 - y1 or x2 - x1 == y2 - y1:
            print('1')
        elif x1 == x2 or y1 == y2:
            print('1')
        else:
            print('2')

