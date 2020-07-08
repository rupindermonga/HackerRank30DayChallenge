#https://www.hackerrank.com/challenges/compare-the-triplets/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    for i, j in zip(a, b):
        if i > j:
            alice_points += 1
        elif i < j:
            bob_points += 1
    print(alice_points, bob_points)
    # return alice_points, bob_points  # for hackerrank


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
