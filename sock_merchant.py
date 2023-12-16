import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    pairs = 0
    set_of_socks = set(ar)
    for s in set_of_socks:
        pairs += (ar.count(s) // 2)
    return pairs

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)