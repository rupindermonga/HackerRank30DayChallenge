#https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    if s[-2:] == "PM":
        if int(s[0:2]) == 12:
            print(str(int(s[0:2])) + s[2:-2])
        else:
            print(str(int(s[0:2])+12) + s[2:-2]) #use return for Hackerrank website
    else:
        if int(s[0:2]) == 12:
            print("00" + s[2:-2])
        else:
            print(s[:-2])

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # f.write(result + '\n')

    # f.close()
