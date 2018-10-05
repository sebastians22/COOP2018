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
    x = 0
    y = 0
    print("This program will print the fibonacci sequence")
    x = eval(input("What number would you like to put into the fibonacci sequence?"))
    for i in range(8):
        x = x + y
        y = x - y
        print(x)



main()
