# U02_Ex03_Average_Scores.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 05 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 03
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#
# This will average three scores
#
#
# Algorithm (pseudocode)
#
#   Print what program does
#   Have user put in three scores
#   Average scores
#   Print the final score

def main():
    score_1 = eval(input("Enter first score: "))
    score_2 = eval(input("Enter second score: "))
    score_3 = eval(input("Enter thrid score: "))
    score = (score_1 + score_2 + score_3 / 3)
    print("Your score is")


main()
