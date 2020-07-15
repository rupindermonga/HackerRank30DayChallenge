#https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

arr = input().strip().split(' ')

n = int(arr[0])
m = int(arr[1])
p = int(arr[2])

final_list = []
for i in range(n + m):
    new_list = input().strip().split(' ')
    final_list.append(new_list)

final_array = np.array(final_list, int)
print(final_list)
print(final_array)