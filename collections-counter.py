#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

no_of_shoes = int(input())

size_of_shoes = list(map(int,input().split()))

no_of_sales = int(input())

size_desirable = []
amount_paid = []
for i in range(no_of_sales):
    a = list(map(int,input().split()))
    size_desirable.append(a[0])
    amount_paid.append(a[1])

size_of_shoes_counter = Counter(size_of_shoes)

amount = 0

for i, eachShoe in enumerate(size_desirable):
    if eachShoe in size_of_shoes_counter.keys():
        if size_of_shoes_counter[eachShoe] != 0:
            amount += amount_paid[i]
            size_of_shoes_counter[eachShoe] -= 1
print(amount)
