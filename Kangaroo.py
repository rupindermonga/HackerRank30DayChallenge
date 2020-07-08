#https://www.hackerrank.com/challenges/kangaroo/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v1 == v2 and x1 != x2):
        print("NO")
        exit
    elif (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or (x2 - x1) % (v1 - v2) != 0:
        print("NO") # this istance from its tree of origin along the -axis. A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right.

Given the value of for apples and orangesis for local
        # return "NO" # this is for hackerrank
    else:
        print("YES") # this is for local
        # return "YES" # this is for hackerrank

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    # fptr.write(result + '\n')

    # fptr.close()
