# U04_Ex09_Rectangle_By_User.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 31 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# This program will get two points by the user x1, y1, and x2, y2, (via click) and it will draw a rectangle with it.
#
#
#
# Algorithm (pseudocode)
# Print what the program is about
# Get the window up
# Ask the user for two points and that it will draw a rectangle.
# Once the user has clicked twice then take the coordinates and make a square
# Use p1 and p2 for the points that the user clicked
# Make sure to not use point (p1), but to just use p1
# Press RETURN to continue

from graphics import *

def main():
    print("This program will draw a rectangle where ever you click the mouse")
    win = GraphWin("Click Me!")
    p1 = win.getMouse()
    p2 = win.getMouse()
    rect1 = Rectangle(p1, p2)
    rect1.setFill("blue")
    rect1.draw(win)

    input("Press RETURN to continue")


main()
