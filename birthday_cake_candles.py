#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    result = {}

    for c in candles:
        if c not in result:
            result[c] = 0
        result[c] += 1
    
    key = next(filter(lambda x: x[1] > 1, sorted(result.items(),reverse=True)))[1]

    return key

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
