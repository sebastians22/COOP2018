# U03_Ex15_pi.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 27 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program prints pi
#
# Algorithm (pseudocode)
# Print what program is about
# Get the input
# Calculate the problem with 4/1 - 4/3 + 4/7 - 4/9...
# for loop
# print y
# z = y - pi
# print (z)



def main():

    print("This program will approximate pi and subtract it from the real pi, and shows the difference between the two")
    x = eval(input("How many times would you like to approximate pi?  "))
    y = 4/1 - 4/3 + 4/5 - 4/7 + 4/9
    for x in range(1, x + 1):
        print(y)


main()
