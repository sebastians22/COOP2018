# U04_Ex08_Line_Segmants.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 09 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
#  This program gives the area and perimeter of a rectangle
#
#
#
# Algorithm (pseudocode)
# Get p1 and p2 from the user to make a rectangle, draw the rectangle
# get x and y of p1 and p2
# calculate the area with area = length * width
# calculate the perimeter with perimeter 2 * (area + perimeter
#

from graphics import *

def main():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()

    rect = Rectangle(p1, p2)
    rect.draw(win)

    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    length = x1 + x2
    width = y1 + y2

    area = length * width
    print("The area of your rectangle is", area, "pixels")

    perimeter = 2 * (length + width)
    print("The perimeter of your rectangle is", perimeter, "pixels")

    input("Press ENTER to continue")

main()