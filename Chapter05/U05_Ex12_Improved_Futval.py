# U04_Ex6_APR.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 09 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
# This program will print a table of the yearly balance account after entering principle, balance, and how many years of investing
#
#
#
# Algorithm (pseudocode)
# print the intro to the program
# have the user enter the principle
# have the user enter the apr
# have the user enter how many years they would be investing into the bank
# print a table
# have a for loop years in range (years)
# have principle = principle * apr + 1
# print the total of how much they will get

def main():

    print("This program will calculate the future value over 10 years ")
    print()

    principle = eval(input("Enter the initial principle "))
    print()

    apr = eval(input("Enter the annul interest rate "))
    print()

    years = eval(input("Enter the number of years you will be investing "))
    print()

    print("Year Value")
    print("==========")

    for years in range(years):
        principle = principle * (1 + apr)

        print('{0:4}\t${1:.2f}'.format(years + 1, principle))

main()
