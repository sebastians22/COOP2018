# U07_Ex13_dayNum.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 26 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
# This program will calculate how many days into the year a date is
#
#
#
# Algorithm (pseudocode)
# import calculation and cal from u7 ex12 and ex13
# print the program into
# make a string of dates to test called dates
# make a for loop which is for date in dates
# make day = days(date)
# make an if statement which says if day == -1, then pring that it is not a valid date
# else print the how many days into the year the date is
#
# def days
# call calculation from ex 12, and if it does not follow it return "not a date"
# split the date into month, day, year
# make month, day, year into variables and turn them into integers
# make dayNum = 31 * (month-1) + day
# if month is bigger then 2, then make dayNum -= (4*month+23)//10
# if cal(year) from ex 11 and month are bigger then 2, then have dayNum += 1
# return dayNum


from Chapter07.U07_Ex12_Date import calculation
from Chapter07.U07_Ex11_Leap_Year import cal

def main():

    print('This program will tell whether the date entered is a valid date, use this format(month/day/year).')

    dates = ['2/7/1860', '3/24/1976', '5/19/1995', '2/28/2000', '2/29/2000', '12/32/2019', '12/31/2019']


    for date in dates:
        day = days(date)
        if day == -1:
            print(day, 'is not a valid date.'.format(date))
        else:

            print('The day number for {0} is {1}'.format(date, days(date)))


def days(date):

    if not calculation(date):

        return "not a date"

    month, day, year = date.split('/')

    month = int(month)
    day = int(day)
    year = int(year)

    dayNum = 31 * (month - 1) + day

    if month > 2:
        dayNum -= (4 * month + 23) // 10

    if cal(year) and month > 2:
        dayNum += 1

    return dayNum


if __name__ == '__main__':

    main()

"""
RESULTS:
========
days("2/7/1860")    -->    38 |    38 | [ Pass ]
days("3/24/1976")   -->    84 |    84 | [ Pass ]
days("5/19/1995")   -->   139 |   139 | [ Pass ]
days("2/28/2000")   -->    59 |    59 | [ Pass ]
days("2/29/2000")   -->    60 |    60 | [ Pass ]
========
"""