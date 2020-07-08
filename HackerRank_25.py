#https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem


def prime_number():
    no_of_tests = int(input())
    final_list = []
    for i in range(no_of_tests):
        new_number = int(input())
        if new_number == 2:
            final_list.append("Prime")
        elif new_number % 2 == 0 or new_number == 1:
            final_list.append("Not prime")
        else:
            count = 0
            for j in range(3, int(new_number**0.5) + 1, 2):
                if new_number % j == 0:
                    count += 1
                    break
            if count == 0:
                final_list.append("Prime")
            else:
                final_list.append("Not prime")
    return final_list

f = prime_number()

for eachResult in f:
    print(eachResult)