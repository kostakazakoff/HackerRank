#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_in_house = [x for x in apples if s <= x + a <= t]
    oranges_in_house = [x for x in oranges if s <= x + b <= t]
    print(len(apples_in_house))
    print(len(oranges_in_house))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
