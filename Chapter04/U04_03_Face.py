# U04_03_Face.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 23 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 04
#
# Program Description
# Write a program that draws some sort of face
#
#
#
# Algorithm (pseudocode)
# Draw the first circle and have it tan
# Draw the two eyes and have them blue
# Draw the nose
# Draw a neutral smile
#

from graphics import *

def main():
    win1 = GraphWin()

    Face = Circle(Point(100, 100), 50)
    Face.setFill("tan")
    Face.setWidth(0)

    Face.draw(win1)

    Right_eye = Circle(Point(83, 95), 5)
    Right_eye.setFill("blue")
    Right_eye.setWidth(0)

    Right_eye.draw(win1)

    Left_eye = Circle(Point(117, 95), 5)
    Left_eye.setFill("blue")
    Left_eye.setWidth(0)

    Left_eye.draw(win1)

    Nose = Polygon(Point(105, 115), Point(100, 105), Point(95, 115))
    Nose.setFill("tan")
    Nose.setWidth(1)

    Nose.draw(win1)

    Mouth = Line(Point(90, 130), (Point(110, 130)))
    Mouth.setFill("black")
    Mouth.setWidth(1)

    Mouth.draw(win1)

    input("Press ENTER to continue")

main()