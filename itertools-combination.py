#https://www.hackerrank.com/challenges/itertools-combinations/problem



import itertools


a = input().split()

k = int(a[1]) #permutation length

word = a[0]

for i in range(1, k+1):
    f = list(itertools.combinations(word, i))
    f = sorted([''.join(sorted(j)) for j in f])
    for eachElement in f:
        print(eachElement)