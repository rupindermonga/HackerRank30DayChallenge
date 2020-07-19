#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/

import itertools


a = input().split()

k = int(a[1]) #permutation length

word = a[0]

f = list(itertools.combinations_with_replacement(word, k))

f = sorted([''.join(sorted(i)) for i in f])

for eachElement in f:
    print(eachElement)