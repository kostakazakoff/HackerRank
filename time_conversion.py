#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    h, min, sec = list(map(lambda x: int(x), re.findall(r'\d{2}', s)))
    pm = s[-2:] == 'PM'

    if pm and h != 12:
        h += 12

    if not pm and h == 12:
        h = 0
    
    return ':'.join(list(map(lambda x: f'{x:02}', (h, min, sec))))

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
