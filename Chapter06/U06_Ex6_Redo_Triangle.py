# U06_Ex6_Redo_Triangle.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 6
#

# Program Description
# Calculate the area of a triangle using the area formula a = lw
#
#
#
# Algorithm (pseudocode)
# Get the window up
# Print the intro statement
# Ask the user to click on three places on the screen
# The point variables are p1, p2, p3
# Use the triangle formula wit p1, p2, and p3 to make a triangle
# Print all the sides, then print the area using the function
# Make the triangle what ever colour you want
# get each distance of the sides by getting the distance of every side, use a, b, c
# make s = a, b, c, /2
# print the outro
#
# Make a get function
# Get all the points from the triangle
# make a distance formula that averages the triangle


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

    dist = distance(p1, p2)

    print("The area of your triangle is", dist)

    input("Press ENTER to continue")



def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return dist

main()






