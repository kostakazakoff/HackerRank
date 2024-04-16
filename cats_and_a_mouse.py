import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a_distance = abs(x - z)
    cat_b_distance = abs(y - z)


    result = cat_a_distance - cat_b_distance

    if result > 0:
        return 'Cat B'
    elif result < 0:
        return 'Cat A'
    else:
        return 'Mouse C'

    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)