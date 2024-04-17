import math
import os
import random
import re
import sys


def pickingNumbers(a):
    length = len(a)
    max_len = 1

    for i in range(length):
        upper = [a[i]]
        lower = [a[i]]

        for j in range(length):
            if i == j:
                continue
            target = a[i]
            num = a[j]

            if 0 <= num - target <= 1:
                upper.append(num)
            elif 0 <= target - num <= 1:
                lower.append(num)

        if len(upper) > len(lower):
            if len(upper) > max_len:
                max_len = len(upper)
        else:
            if len(lower) > max_len:
                max_len = len(lower)

        print (upper, lower)

    return (max_len)


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
