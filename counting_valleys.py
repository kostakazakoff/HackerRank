import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    path = [1 if x == "U" else -1 for x in path]

    start = False
    end = False
    level = 0
    valleys = 0

    for i in range(steps):
        level += path[i]
        if level < 0:
            start = True
        elif start and level == 0:
            end = True
        if all([start, end]):
            valleys += 1
            start = False
            end = False
    
    return valleys

        

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)