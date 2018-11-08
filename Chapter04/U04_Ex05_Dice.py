# U04_Ex05_Dice.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# This program will make 5 dice with different numbers on each one of them. The background is red, and you can quit
# by pressing ENTER
#
# Algorithm (pseudocode)
# Make a window 500 by 100
# Make the first dice at 50, 50
# Make the second dice at 150, 50
# Make the third dice at 250, 50
# Make the 4th dice at 350, 50
# Make the 5th dice at 450, 50
# Make the background red
# Draw the points on every die, the points will be 1, 2 ,3 ,4 ,5
#

from graphics import *


def main():
    win = GraphWin("Dice", 500, 100)
    win.setBackground("red")

    rect1 = Rectangle(Point(25, 25), Point(75, 75))
    rect1.setFill("white")
    rect1.draw(win)

    rect2 = Rectangle(Point(125, 25), Point(175, 75))
    rect2.setFill("white")
    rect2.draw(win)

    rect3 = Rectangle(Point(225, 25), Point(275, 75))
    rect3.setFill("white")
    rect3.draw(win)

    rect4 = Rectangle(Point(325, 25), Point(375, 75))
    rect4.setFill("white")
    rect4.draw(win)

    rect5 = Rectangle(Point(425, 25), Point(475, 75))
    rect5.setFill("white")
    rect5.draw(win)

    circ11 = Circle(Point(50, 50), 2)
    circ11.setFill("black")
    circ11.draw(win)

    circ21 = Circle(Point(135, 35), 2)
    circ21.setFill("black")
    circ21.draw(win)

    circ22 = Circle(Point(165, 65), 2)
    circ22.setFill("black")
    circ22.draw(win)

    circ31 = Circle(Point(235, 35), 2)
    circ31.setFill("black")
    circ31.draw(win)

    circ32 = Circle(Point(250, 50), 2)
    circ32.setFill("black")
    circ32.draw(win)

    circ33 = Circle(Point(265, 65), 2)
    circ33.setFill("black")
    circ33.draw(win)

    circ41 = Circle(Point(365, 35), 2)
    circ41.setFill("black")
    circ41.draw(win)

    circ42 = Circle(Point(335, 35), 2)
    circ42.setFill("black")
    circ42.draw(win)

    circ43 = Circle(Point(365, 65), 2)
    circ43.setFill("black")
    circ43.draw(win)

    circ44 = Circle(Point(335, 65), 2)
    circ44.setFill("black")
    circ44.draw(win)

    circ51 = Circle(Point(465, 35), 2)
    circ51.setFill("black")
    circ51.draw(win)

    circ52 = Circle(Point(435, 35), 2)
    circ52.setFill("black")
    circ52.draw(win)

    circ53 = Circle(Point(465, 65), 2)
    circ53.setFill("black")
    circ53.draw(win)

    circ54 = Circle(Point(435, 65), 2)
    circ54.setFill("black")
    circ54.draw(win)

    circ55 = Circle(Point(450, 50), 2)
    circ55.setFill("black")
    circ55.draw(win)


    input("Press ENTER to continue")


main()
