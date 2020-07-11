#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem


def wrapper(f):
    def fun(l):
        # complete the function
        new_list = []
        for eachNumber in l:
            new_list.append(int(eachNumber[-10:]))
        new_list = sorted(new_list)
        for eachNumber in new_list:
            new_number = "+91" + " " + str(eachNumber)[0:5] +" " + str(eachNumber)[5:]
            print(new_number)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


