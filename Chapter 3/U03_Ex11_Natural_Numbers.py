# U03_Ex11_Natural_Numbers.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 05 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   This program will find the sum of natural numbers with natural numbers be a user input
#
# Algorithm (pseudocode)
#   Print Intro
#   Eval Input how many times the user wants to print a natural number
#   Eval Input a natural number
#   Print all the natural numbers
#   Print the sum of all the natural numbers
#

def main():
    #   Print Intro
    print("This program will find the sum of natural numbers with natural numbers  ")

    #   Eval Input how many times the user wants to print a natural number
    x = eval(input("How many times would you like to print the program?  "))

    #   Eval Input a natural number
    y = eval(input("What natural number would you like to print?  "))

    #   Print all the natural numbers
    for x in range(x):
        y = (y + 1)

    #   Print the sum of all the natural numbers
    print("The natural numbers that you have are")
    for x in range(x):
        print(y + 1)

    print("The sum of all of your natural number's is", y)


main()
