#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

arr = input().strip().split(' ')
n_rows = int(arr[0])
m_columns = int(arr[1])
final_list = []
for i in range(n_rows):
    new_list = input().strip().split(' ')
    final_list.append(new_list)
new_array = numpy.array(final_list,int)
inter_array = numpy.transpose(new_array)
final_array = new_array.flatten()
print(inter_array)
print(final_array)