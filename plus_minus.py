#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    global n
    negatives = len([x for x in arr if x < 0])
    positives = len([x for x in arr if x > 0])
    zeros = arr.count(0)

    print(f'{positives/n:6f}')
    print(f'{negatives/n:6f}')
    print(f'{zeros/n:6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
