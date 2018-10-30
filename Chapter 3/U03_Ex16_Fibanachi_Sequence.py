# U03_Ex16_Fibanachi_Sequence.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 03 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 03
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
    z = eval(input("What number would you like to see in the sequence"))
    for i in range(z - 1):
        x = x + y
        y = x - y

    print("The", z, "term is the last number", x)



main()
