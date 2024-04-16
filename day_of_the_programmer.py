import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    Julian = year < 1918
    Gregorian = year > 1918
    
    if Gregorian:
        leap_day = int(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
    elif Julian:
        leap_day = int(year % 4 == 0)
    else:
        leap_day, month = -13, 8

    day, month = 13 - leap_day, 9
    
    return (f'{str(day).zfill(2)}.{str(month).zfill(2)}.{year}')

if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)