# U07_Ex15_Target.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 28 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#Create a GraphWin
# The center of the circle at 100, 100
# Draw the inner circle yellow (10 pixel width)
# The second circle will be red (20 pixel width)
# The third circle will be blue (30 pixel width)
# The fourth circle will be black (40 pixel width)
# The fifth circle will be white (50 pixel width)
# Make all circles full of their color
# Each outer ring has a radius than previous, in increments equal to center circle radius
#
# def click
# have the user click on the target 5 times
# get all the cooridnates of where the user clicked
# make a small white dot where the user clicked by making a circle
# do this 5 times

from graphics import *

def main():
    win = GraphWin("archery", 200, 200)

    circ5 = Circle(Point(100, 100), 50)
    circ5.setFill("white")
    circ5.setWidth(1)

    circ5.draw(win)

    circ4 = Circle(Point(100, 100), 40)
    circ4.setFill("black")
    circ4.setWidth(1)

    circ4.draw(win)

    circ3 = Circle(Point(100, 100), 30)
    circ3.setFill("blue")
    circ3.setWidth(1)

    circ3.draw(win)

    circ2 = Circle(Point(100, 100), 20)
    circ2.setFill("red")
    circ2.setWidth(1)

    circ2.draw(win)

    circ = Circle(Point(100, 100), 10)
    circ.setFill("yellow")
    circ.setWidth(1)

    circ.draw(win)

    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = click(win)

    center = Point(0, 0)
    points = [5, 4, 3, 2, 1]


    #print(circles)




    input("Press Return to continue")




    win.close()

def click(win):

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    p4 = win.getMouse()
    p5 = win.getMouse()

    x1 = p1.getX()
    y1 = p1.getY()

    dot1 = Circle(Point(x1, y1), 1)
    dot1.setFill("white")

    dot1.draw(win)

    x2 = p2.getX()
    y2 = p2.getY()

    dot2 = Circle(Point(x2, y2), 1)
    dot2.setFill("white")

    dot2.draw(win)

    x3 = p3.getX()
    y3 = p3.getY()

    dot3 = Circle(Point(x3, y3), 1)
    dot3.setFill("white")

    dot3.draw(win)

    x4 = p4.getX()
    y4 = p4.getY()

    dot4 = Circle(Point(x4, y4), 1)
    dot4.setFill("white")

    dot4.draw(win)

    x5 = p5.getX()
    y5 = p5.getY()

    dot5 = Circle(Point(x5, y5), 1)
    dot5.setFill("white")

    dot5.draw(win)

    return x1, y1, x2, y2, x3, y3, x4, y4, x5, y5


main()
