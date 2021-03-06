# U06_Ex09_Exam_Scores.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 06 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
# This program will put the students grade into different buckets of A,B,C,D, and F using functions
#
# Algorithm (pseudocode)
# Ask the user for what they got (stugrade)
# call calc(stugrade)
# print what the student got (stugrade)
#
# Function calc
# subtract one from stugrade so the computed can read it
# make a grade string that says if they got an A,B,C,D, or F
# Return stugrade


def main():

    stugrade = eval(input("What grade did the student get? "))

    new_stugrade = calc(stugrade)

    print("The student got a", new_stugrade)

def calc(stugrade):

    gradesStr = 'F' * 59 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11
    new_stugrade = gradesStr[int(stugrade) - 1]
    return new_stugrade


main()
