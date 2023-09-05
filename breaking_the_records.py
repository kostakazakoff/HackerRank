import math
import os
import random
import re
import sys


def breakingRecords(scores):
    min_points = max_points = scores[0]
    scores = scores[1::]
    min_points_record = 0
    max_points_record = 0

    for s in scores:
        if s > max_points:
            max_points = s
            max_points_record += 1
        elif s < min_points:
            min_points = s
            min_points_record += 1

    return [max_points_record, min_points_record]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
