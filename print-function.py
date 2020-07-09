#https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
initial_string = ""
for i in range(1, n+1):
    initial_string += str(i)

print(initial_string)