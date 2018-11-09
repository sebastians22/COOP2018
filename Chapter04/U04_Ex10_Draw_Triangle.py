# U04_Ex10_Draw_Triangle.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 08 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# The user will click on three places on the screen, and it will make a triangle and print the formula
#
#
#
# Algorithm (pseudocode)
# Get the window up
# Ask the user to click on three places on the screen
# The point variables are p1, p2, p3
# Use the triangle formula wit p1, p2, and p3 to make a triangle
# Print all the sides, then print the area using the function
# Make a get function
# p1.getX()...
#

from graphics import *
import math

def main():
    win = GraphWin("Triangle")
    print("Press on three points of the screen to make a triangle")
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    Triangle = Polygon(p1, p2, p3)
    Triangle.setFill("red")
    Triangle.draw(win)

    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)


    s = a+b+c/2

    print("Side one is", p1)
    print("Side two is", p2)
    print("Side three is", p3)

    print("The area of your triangle is", math.sqrt(s * (s - a) * (s - b) * (s - c)))

    input("Press ENTER to continue")



def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return dist

main()