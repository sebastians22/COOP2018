# U04_Ex11_5_Click_House.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 08 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# In five clicks this program will create a house
# The first two clicks is the outside, the third is the top center of the door
# The fourth is the window and the fifth is the top of the roof
#
# Algorithm (pseudocode)
# Get the window up
# Get p1 and p2 with mouse clicks and make a rectangle with them
# Get p3 with mouse clicks and make a door with it. The click should be the top mid of the door
# Get p4 for the window, get the middle
# Get p5 is the roof (polygon), find a way to get three points from one click, use p1 and p2

from graphics import *
import math

def main():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()

    rect = Rectangle(p1, p2)
    rect.draw(win)

    p3 = win.getMouse()

    arect = Rectangle(p3, p3)
    p3.draw(win)
    centerPoint = arect.getCenter()
    centerPoint.draw(win)

    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    p5 = win.getMouse()
    roof = Polygon(Point(x1, y2), Point(x2, y2), p5)
    roof.draw(win)


    input("Press ENTER to continue")


main()