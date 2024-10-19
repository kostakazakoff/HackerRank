import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    player_positions = []
    ranked = set(ranked)

    for result in player:
        ranklist = ranked.copy()
        ranklist.add(result)
        ranklist = sorted(list(ranklist), reverse=True)
        player_positions.append(ranklist.index(result) + 1)

    return player_positions


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print (result)