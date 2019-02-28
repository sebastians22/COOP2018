# U07_Ex12_Date.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
# This program will determine whether a date is a valid date or not
#
#
#
# Algorithm (pseudocode)
# import cal for u7 ex 11
# print the into
# make a list of dates to test with, make it dates
# for date in dates, print the answer in a if else statement using the function
#
# def calculation
# split month, day, and year
# make month, day, and year into variables and turn them into integers
# make a list of dayranges that ranges how many days are in each month (february has 29)
# make answer = False
# make an if statement that says month - 1 in range(12):
# make another if statement that says (day-1) in range(dayranges[month - 1])
# another if statement that says if not( month == 2) and day == 29 and not cal(year)), make answer true
#   this is for leap years (february 29)
# then return answer


from Chapter07.U07_Ex11_Leap_Year import cal


def main():

    print('This program will determine whether a date is a valid date or not')
    dates = ['4/8/1973', '11/23/2005', '2/29/2017', '2/28/2017', '2/29/2002', '2/28/2002']

    for date in dates:

        print('{0} {1} valid date'.format(date, 'is' if calculation(date) else 'is not'))


def calculation(dates):

    month, day, year = dates.split('/')

    month = int(month)
    day = int(day)
    year = int(year)

    dayranges = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = False

    if (month - 1) in range(12):

        if (day - 1) in range(dayranges[month - 1]):

            if not (month == 2 and day == 29 and not cal(year)):
                answer = True

    return answer

if __name__ == '__main__':

    main()

"""
RESULTS:
========
cal(4/8/1973)     -->   0 |       0 | [ Pass ]
cal(11/23/2005)   -->   0 |       0 | [ Pass ]
cal(2/29/2017)    -->   0 |       0 | [ Pass ]
cal(2/28/2017)    -->   0 |       0 | [ Pass ]
cal(2/29/2002)    -->   0 |       0 | [ Pass ]
cal(2/28/2002)    -->   0 |       0 | [ Pass ]
========
"""