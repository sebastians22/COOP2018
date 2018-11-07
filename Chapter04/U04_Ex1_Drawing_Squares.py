# U04_Ex1_Drawing_Squares.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 23 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# This program will make a red square, it will make a square where ever you click on the window,
# and it will say to quit from the user
#
#
#
# Algorithm (pseudocode)
# Make a red square
# for loop for if you click with the mouse, it will quit the program
# A click can also draw a new square on the screen
# Press Enter to continue
#

from graphics import *

def main():
    win = GraphWin()
    shape = \
        Rectangle(Point(0, 0), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()


        shape = Rectangle(Point(p.getX() - 50, p.getY() - 50), Point(p.getX() + 50, p.getY() + 50))
        shape.draw(win)
        shape.setFill("red")
        shape.setOutline("red")

        #dx = p.getX() - c.getX()
        #dy =p.getY() - c.getY()
        #shape.move(dx, dy)

    input("press ENTER to continue")

    win.close()


main()
