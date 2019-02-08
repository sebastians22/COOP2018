# U06_Ex09_Exam_Scores.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 06 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#



def main():

    def scores(stugrade):
        gradesStr = 'F' * 59 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11

        return stugrade


    print("This program will put grades into the A, B, C, D, and F buckets")

    stugrade = eval(input("What grade did the student get? "))
    #new_stugrade = stugrade - 1
    stugrade = gradesStr[int(stugrade) - 1]

    print("The student got a", stugrade)


main()
