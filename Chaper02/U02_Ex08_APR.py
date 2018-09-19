# U02_Ex08_APR.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#

def main():
    print("This program calculates the future value of investments")
    periods = eval(input("Enter the amount of periods"))
    interest = eval(input("Enter the initial interest: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        interest = interest * (1 + apr)

    print("The value in periods is:", interest)

main()