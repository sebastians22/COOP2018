# U03_07_Distance.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 26 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 07
#     Source: Python Programming
#    Chapter: 03
#
# Program Description
# This program will calculate distance
#
#
#
# Algorithm (pseudocode)
# Print opening message
# Get all four coordinates
# Show the formula
# Print the answer
#

def main():
    print("This program will calculate the distance formula for you if you put in 4 coordinates")
    x1 = eval(input("Please put in the first coordinate"))
    x2 = eval(input("Please put in the second coordinate"))
    y1 = eval(input("Please put in the third coordinate"))
    y2 = eval(input("Please put in the fourth coordinate"))
    print("Your distance is" (x2 - x1)**2 + (y2 - y1)**2)


main()
