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
# This program will calculate slopes with the slope formula
#
#
#
# Algorithm (pseudocode)
# Print what program is about
# Get x1 value with eval(input)
# Get x2 value with eval(input)
# Get y1 value with eval(input)
# Get y2 value with eval(input)
# Calculate using y2 - y1 / x2 - x1
# Print the answer "Your Slope is" (then the calculation)

def main():
    print("This program will take four coordinates, and it will calculate the slope")
    x1 = eval(input("What is your first coordinate?"))
    x2 = eval(input("What is your second coordinate?"))
    print("Now that you have put in x1 and x2 (horizontal), it is time to input the y coordinates")
    y1 = eval(input("What is your third coordinate?"))
    y2 = eval(input("What is your fourth coordinate?"))
    print("Now that you have put in all of your coordinates, it will calculate it for you")
    print("Your slope is", y2 - y1 / x2 - x1)


main()
