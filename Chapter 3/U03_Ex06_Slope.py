# U03_Ex06_Slope.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 26 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program will calculate slops with the slope formula
#
#
#
# Algorithm (pseudocode)
# Print what program is about
# Get x1 value
# Get x2 value
# Get x3 value
# Get x4 value
# Calculate
# Print the answer

def main():
    print("This program will take four coordinates, and it will calculate the slope")
    x1 = eval(input("What is your first coordinate?"))
    x2 = eval(input("What is your second coordinate?"))
    print("Now that you have put in x1 and x2, it is time to input the y coordinates")
    y1 = eval(input("What is your third coordinate?"))
    y2 = eval(input("What is your fourth coordinate?"))
    print("Now that you have put in all of your coordinates, it will calculate it for you")
    print("Your answer is", y2 - y1 / x2 - x1)


main()
