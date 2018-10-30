# U04_Ex02_Target.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 23 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
# This program will draw an archery target. Each ring will have different colors, and they will all of the same width
#
#
#
# Algorithm (pseudocode)
# Create a GraphWin
# Draw the inner circle yellow
# The second circle will be red
# The third circle will be blue
# The fourth circle will be black
# The fifth circle will be white
# Make all circles full of their color
# Each outer ring has a radius than previous, in increments equal to center circle radius
#

from graphics import *

def main():
    win1 = GraphWin()

    circ5 = Circle(Point(100, 100), 50)
    circ5.setFill("white")
    circ5.setWidth(1)

    circ5.draw(win1)

    circ4 = Circle(Point(100, 100), 40)
    circ4.setFill("black")
    circ4.setWidth(1)

    circ4.draw(win1)

    circ3 = Circle(Point(100, 100), 30)
    circ3.setFill("blue")
    circ3.setWidth(1)

    circ3.draw(win1)

    circ2 = Circle(Point(100, 100), 20)
    circ2.setFill("red")
    circ2.setWidth(1)

    circ2.draw(win1)

    circ = Circle(Point(100, 100), 10)
    circ.setFill("yellow")
    circ.setWidth(1)

    circ.draw(win1)

    input("Press ENTER to continue")

    win1.close()


main()
