import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    start_difference = x2 - x1
    jump_difference = v1 - v2
    return 'YES' if v1 > v2 and start_difference % jump_difference == 0 else 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
