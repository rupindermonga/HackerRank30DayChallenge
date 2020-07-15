#https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

def arrays(arr):
    new_array = numpy.array(arr, int)
    final_array = numpy.reshape(new_array,(3,3))
    return final_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)