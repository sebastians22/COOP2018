# U06_Ex6_Redo_Triangle.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 6
#

# Program Description
# Calculate the area of a triangle using the area formula a = lw
#
#
#
# Algorithm (pseudocode)
# Print what program is about
# Get all three sides of triangle using eval(input), use a b c
# Calculate with the formula with a+v+c/2
# Calculate again with A = math.sqrt(s(s-a)(s-b)(s-c))
# Print answer
#



import math


def main():
    print("This program will calculate the area of a triangle")
    a = eval(input("What is your first length?  "))
    b = eval(input("What is your second length?  "))
    c = eval(input("What is your third length?  "))
    print(A, " is the area of your triangle")


def area(a, b, c):
    s = a + b + c / 2
    A = math.sqrt(s(s - a)(s - b)(s - c))

main()
