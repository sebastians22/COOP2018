# U02_Ex08_APR.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 08
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#
# Apr program
#
#
# Algorithm (pseudocode)
#   Get number of periods
#   Get number of interest
#   Get number of interest rate
#   Use formula
#   print answer


def main():
    print("This program calculates the future value of investments")
    periods = eval(input("Enter how many periods"))
    interest = eval(input("Enter the initial interest: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        interest = interest * (1 + apr) ** periods

    print("The value in periods is:", interest)


main()
