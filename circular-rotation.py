#https://www.hackerrank.com/challenges/circular-array-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    new_list = [1]*len(a)
    for i in range(len(a)):
        j = (i + k) % len(a)
        new_list[j] = a[i]
    for eachQuery in queries:
        print(new_list[eachQuery])
    
    #for hackerrank
    # new_list = [1]*len(a)
    # result_list = []
    # for i in range(len(a)):
    #     j = (i + k) % len(a)
    #     new_list[j] = a[i]
    # for eachQuery in queries:
    #     result_list.append(new_list[eachQuery])
    # return result_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
