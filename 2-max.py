#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


arr = list(arr)
max_value = max(arr)

while max_value in arr:
    arr.remove(max_value)


print(max(arr))