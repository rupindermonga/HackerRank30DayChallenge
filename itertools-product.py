#https://www.hackerrank.com/challenges/itertools-product/problem

import itertools


a = map(int,input().split())
b = map(int,input().split())


f = itertools.product(a, b,repeat=1)


for eachItem in f:
    print(eachItem,end = ' ')

