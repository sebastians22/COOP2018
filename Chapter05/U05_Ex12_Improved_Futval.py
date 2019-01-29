# U04_Ex6_APR.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 09 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# This program will modify the graphical future value program to add graphics
#
#
#
# Algorithm (pseudocode)
# print the intro to the program
# have the user enter the principle
# have the user enter the apr
# have the user enter how many years they would be investing into the bank
# print a table
# have a for loop years = to years
# have principle = principle * apr + 1

def main():

    print("This program will calculate the future value over 10 years ")
    print()

    principle = eval(input("Enter the annul interest rate "))
    print()

    apr = eval(input("Enter the annul interest rate "))
    print()

    years = eval(input("Enter the number of years you will be investing "))
    print()

    print("Year Value")
    print("==========")

    for years in range(years):
        principle = principle * (1 + apr)

    print("Over", years + 1, "you will have", principle, "dollars.")


main()
