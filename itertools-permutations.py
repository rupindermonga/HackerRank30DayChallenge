#https://www.hackerrank.com/challenges/itertools-permutations/problem


import itertools


a = input().split()

k = int(a[1]) #permutation length

word = a[0]

f = list(itertools.permutations(word, k))

f = sorted([''.join(i) for i in f])

for eachElement in f:
    print(eachElement)