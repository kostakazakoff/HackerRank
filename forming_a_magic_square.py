#!/bin/python3

import math
import os
import random
import re
import sys


def formingMagicSquare(s):
    all_vars = []

    magic_sequence = [8, 1, 6, 7, 2, 9, 4, 3]
    magic_sequence_mirror = [4, 9, 2, 7, 6, 1, 8, 3]
    matrix_sequence = [s[0][0], s[0][1], s[0][2], s[1][2], s[2][2], s[2][1], s[2][0], s[1][0]]

    for _ in range(4):
        cost_1 = 0
        cost_2 = 0
        [magic_sequence.append(magic_sequence.pop(0)) for _ in range(2)]
        [magic_sequence_mirror.append(magic_sequence_mirror.pop(0)) for _ in range(2)]

        for i in range(8):
            cost_1 += abs(matrix_sequence[i] - magic_sequence[i])
            cost_2 += abs(matrix_sequence[i] - magic_sequence_mirror[i])

        cost = min(cost_1, cost_2)
        cost += abs(s[1][1] - 5)

        all_vars.append(cost)

    cost = min(all_vars)

    return cost


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
