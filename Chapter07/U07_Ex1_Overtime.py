# U07_Ex1_Overtime.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 21 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
# This program will calculate the pay + overtime in a week
#
#
#
# Algorithm (pseudocode)
# Print the intro
# Get how much you get paid per hour
# Get hours
# call cal with money, extra_pay, and extra_hours
# if state is over 40, print the extra pay, else print their pay
#
# cal (pay,hours)
# make extra_hours = hours - 40 (this is the overtime amount)
# make money = pay times hour
# make extra pay = money * .5 (this is the overtime that they got)
# return money, extra_pay, and extra_hours

def main():

    print("This program will see how much you make after 40 hours")
    pay = eval(input("How much do you get paid per hour "))
    hours = eval(input("How many hours did you work this week? "))

    money, extra_pay, extra_hours = calc(pay, hours)

    if hours > 40:
        print("You worked", hours, "hours and you got", extra_hours, "of overtime and you earned", money+extra_pay, "dollars.")
    else:
        print("You worked", hours, "hours and you earned", money, "dollars.")


def calc(pay, hours):

    extra_hours = hours - 40
    money = pay * hours
    extra_pay = money * .5

    return money, extra_pay, extra_hours


if __name__ == '__main__':
    main()

"""
RESULTS:
========
calc(10, 0)    -->       (0, 0, -40) |       (0, 0.0, -40) | [ Pass ]
calc(10, 1)    -->      (10, 5, -39) |      (10, 5.0, -39) | [ Pass ]
calc(10, 5)    -->     (50, 25, -35) |     (50, 25.0, -35) | [ Pass ]
calc(10, 10)   -->    (100, 50, -30) |    (100, 50.0, -30) | [ Pass ]
calc(10, 30)   -->   (300, 150, -10) |   (300, 150.0, -10) | [ Pass ]
calc(10, 39)   -->    (390, 195, -1) |    (390, 195.0, -1) | [ Pass ]
calc(10, 40)   -->     (400, 200, 0) |     (400, 200.0, 0) | [ Pass ]
calc(10, 41)   -->     (410, 205, 1) |     (410, 205.0, 1) | [ Pass ]
calc(10, 50)   -->    (500, 250, 10) |    (500, 250.0, 10) | [ Pass ]
========
"""