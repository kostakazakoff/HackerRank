import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards = sorted(list(set([x for x in keyboards if x < b])))
    drives = sorted(list(set([x for x in drives if x < b])))

    if len(keyboards) < 0 or len(drives) < 0:
        return -1
    
    max_sum = -1
    
    for keyboard in keyboards:
        for drive in drives:
            current_sum = keyboard + drive
            if current_sum > b:
                break
            if current_sum > max_sum:
                max_sum = current_sum
            
    return (max_sum)


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print (moneySpent)