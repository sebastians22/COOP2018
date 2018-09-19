# U02_Ex06_Value_of_Investment.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 06
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
# A program to compute the value of an investment
# Carried 10 years in the future
#
#
# Algorithm (pseudocode)
#   Explain what it does
#   Input the time of the investment
#   Input Principle
#    Input apr
#   Loop

def main():
    print("This program calculates the future value of investments")
    years = eval(input("Enter the amount of years"))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in years is:", principal)


main()
