import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    res = []

    for g in grades:
        if g > 37 and g % 5 >= 3:
            g = (g // 5 + 1) * 5
        res.append(g)

    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print()
    [print(x) for x in result]

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
