# U07_Ex17_Bouncing_ball.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 28 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
# This program will create a window with a bouncing ball and it will count how many times it hits the side and it
# will also say what side it hits every time it hits a side
#
#
# Algorithm (pseudocode)
# import graphics
# make top, right, bottom, left = to 0
# print the intro to the program
# make a window called bouncing ball
# make right and top = win.getWidth()/2
# make bottom and left = top * -1
# make a small red ball that starts in the top left corner
# Input ENTER to continue

from graphics import *

top = 0
right = 0
bottom = 0
left = 0

def main():
    print("This program is a bouncing ball")

    win = GraphWin('Bouncing Ball', 600, 600)
    right = win.getWidth() / 2
    left = right * -1
    top = win.getHeight() / 2
    bottom = top * -1

    ball = Circle(Point(0, 0), 10)
    ball.setFill('red')
    ball.draw(win)

    input("Press ENTER to continue")


main()
