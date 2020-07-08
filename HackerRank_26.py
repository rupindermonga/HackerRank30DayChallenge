#https://www.hackerrank.com/challenges/30-nested-logic/problem

import datetime

def fine_library():
    return_date_input = input()
    expected_date_input = input()

    return_day, return_month, return_year = return_date_input.split()
    expected_day, expected_month, expected_year = expected_date_input.split()

    return_day, return_month, return_year = int(return_day), int(return_month), int(return_year)
    expected_day, expected_month, expected_year = int(expected_day), int(expected_month), int(expected_year)

    return_date = datetime.date(return_year, return_month, return_day)
    expected_date = datetime.date(expected_year, expected_month, expected_day)

    if return_date <= expected_date:
        fine = 0
    elif return_year == expected_year and return_month == expected_month:
        fine = 15 * (return_day - expected_day)
    elif return_year == expected_year:
        fine = 500 * (return_month - expected_month)
    else:
        fine = 10000
    return fine

f = fine_library()
print(f)