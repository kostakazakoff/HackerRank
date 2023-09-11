import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    # arr = sorted(arr, reverse=True)
    # birds_dict = {arr.count(k): k for k in arr}
    # print(birds_dict)
    # birds_dict = dict(sorted(birds_dict.items(), key=lambda x: -x[0]))
    # return list(birds_dict.values())[0]

    arr = sorted(arr, reverse=True)
    nums = set(arr)
    birds_dict = {k: arr.count(k) for k in nums}
    return max(birds_dict, key=birds_dict.get)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
