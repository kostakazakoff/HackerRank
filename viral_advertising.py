#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    liked = 2
    comulative = 2
    
    for _ in range(1, n):
        liked = int(liked * 3 / 2)
        comulative += liked
    
    return comulative

if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
