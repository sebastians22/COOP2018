# U07_Ex06_Speeding_Ticket.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
# This program will do the math for the speeding ticket in podunksville
#
#
#
# Algorithm (pseudocode)
# print the program description
# get limit
# get the speed
# call fine
# print fine

# def cal
# see if speed is over 90
# Make an if statement that says if the speed is over 90, subtract speed from limit, *5 the mph over, + 250
# Make an if statement that says if the speed is under 90, subtract speed from limit, *5 the mph over, and only ad 50
# return fine


def main():

    print("This program does math")
    limit = eval(input("What is the limit? "))
    speed = eval(input("How fast where you going? "))
    fine = cal(limit, speed)
    print(fine)


def cal(limit, speed):
    fine = 0

    if speed > 90:
        over = speed - limit
        fine = over * 5 + 250
        return fine


    if speed > limit:
        over = speed - limit
        fine = over * 5 + 50
    return fine

if __name__ == '__main__':

    main()
    print(cal(20, 20))

"""
RESULTS:
========
cal(20, 10)   -->     0 |     0 | [ Pass ]
cal(20, 20)   -->     0 |     0 | [ Pass ]
cal(20, 21)   -->    55 |    55 | [ Pass ]
cal(20, 50)   -->   200 |   200 | [ Pass ]
cal(20, 91)   -->   605 |   605 | [ Pass ]
========"""