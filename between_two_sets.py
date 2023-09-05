#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    factors = set()
    max_a = max(a)
    min_b = min(b)

    for i in range(max_a, min_b + 1):
        factor = all([True if i % num == 0 else False for num in a])\
        and all([True if num % i == 0 else False for num in b])
        if factor:
            factors.add(i)

    return len(factors)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    # fptr.write(str(total) + '\n')

    # fptr.close()
