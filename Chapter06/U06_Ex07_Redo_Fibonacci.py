# U06_Ex07_Redo_Fibonacci.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
# This program will print the fibonacci sequence with 1, 1, 2, 3, 5, 8, 13
#
#
#
# Algorithm (pseudocode)
#   Print intro
#   n = number
#   eval original number
#   Start printing sequence
#
#

def main():
    x = 1
    y = 0
    print("This program will print what number you want from the fibonacci sequence")
    num = eval(input("What number would you like to see in the sequence"))
    for i in range(num - 1):
        x = x + y
        y = x - y

    print("The", num, "term is the last number", x)



main()