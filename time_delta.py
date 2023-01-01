import os
from datetime import datetime


def time_delta(t1, t2):
    date1_obj = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2_obj = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = date2_obj - date1_obj
    seconds_diff = diff.total_seconds()
    return str(int(abs(seconds_diff)))


if __name__ == '__main__':
    
    # with open(os.environ['OUTPUT_PATH'], 'w') as f:
    with open('./timedelta.txt', 'w') as f:

        t = int(input())

        for _ in range(t):
            t1 = input()
            t2 = input()
            delta = time_delta(t1, t2)
            f.write(delta + '\n')
