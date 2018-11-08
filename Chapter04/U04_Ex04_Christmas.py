# U04_Ex04_Christmas.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 24 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
# This program will make a christmas scene with a snowman and a tree
#
#
#
# Algorithm (pseudocode)
# Make the window 500 by 500
# Make the big circle for the snowman 25
# Make the middle circle for the snowman 20
# Make the small circle for the snowman 15
# Christmas Tree (6 green points, 4 brown points
# 3 Circles for a Snowman
# Nose, Mouth, Eyes, Arms (brown)
#

from graphics import *

def main():

    win = GraphWin("Christmas", 500, 500)

    smb = Circle(Point(450, 475), 25)
    smb.draw(win)

    smm = Circle(Point(450, 430), 20)
    smm.draw(win)

    smt = Circle(Point(450, 395), 15)
    smt.draw(win)

    smrh = Line(Point(470, 430), Point(500, 430))
    smrh.setOutline("brown")
    smrh.draw(win)

    smlh = Line(Point(430, 430), Point(400, 430))
    smlh.setOutline("brown")
    smlh.draw(win)

    smle = Circle(Point(445, 390), 2)
    smle.setFill("blue")
    smle.draw(win)

    smre = Circle(Point(455, 390), 2)
    smre.setFill("blue")
    smre.draw(win)

    tree_s = Polygon(Point(150, 500), Point(150, 470), Point(190, 470), Point(190, 500))
    tree_s.setFill("brown")
    tree_s.draw(win)

    tree_l = Polygon(Point(120, 470), Point(220, 470), Point(170, 400))
    tree_l.setFill("green")
    tree_l.draw(win)

    input("Press ENTER to continue")


main()
