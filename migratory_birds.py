import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    nums = sorted(list(set(arr)), reverse=True)
    birds_dict = {arr.count(k): k for k in nums}
    birds_dict = dict(sorted(birds_dict.items(), key=lambda x: -x[0]))
    return next(iter(birds_dict.values()))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
