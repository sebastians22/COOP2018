# U07_Ex11_Leap_Year.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#
# This program determines whether a year is a leap year or not
#
#
# Algorithm (pseudocode)
# print what the program does
# have a list of years to test
# make a loop of for years in leap_years
# print the answer

# cal
# make an equation that determines whether a year is a leap year or not
# return true if it's a leap year
# return false if it's not a leap year


def main():

    print("This program determines whether a year is a leap year or not")

    leap_years = [1800, 1804, 1808, 1810]

    for years in leap_years:

        print('{0} {1} a leap year'.format(years, 'is' if cal(years) else 'is not'))


def cal(years):

        if years % 4 == 0 and not (years % 100 == 0 and not years % 400 == 0):
            return True

        return False

if __name__ == '__main__':

    main()

"""
RESULTS:
========
cal(1800)   -->       0 |       0 | [ Pass ]
cal(1804)   -->       1 |       1 | [ Pass ]
cal(1808)   -->       1 |       1 | [ Pass ]
cal(1810)   -->       0 |       0 | [ Pass ]
========"""