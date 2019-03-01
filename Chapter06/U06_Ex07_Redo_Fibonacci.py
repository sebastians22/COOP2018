# U06_Ex07_Redo_Fibonacci.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
# This program will print the fibonacci sequence with 1, 1, 2, 3, 5, 8, 13. It will then ask the user for what
# number they want from the sequence and it will print that number
#
#
# Algorithm (pseudocode)
#   Print intro
#   make num and eval input to see what number they want from the sequence
#   call x from pi(num)
#   Print the answer
#
# def pi(num)
# make x = 1 and y = 0
# make a for loop with a range of num - 1
# Use the equations x = x + y and y = x - y
# return x

def main():

    print("This program will print what number you want from the fibonacci sequence")
    num = eval(input("What number would you like to see in the sequence  "))

    x = pi(num)

    print("The", num, "term of Fibonacci is number", x)


def pi(num):

    x = 1
    y = 0

    for i in range(num - 1):
        x = x + y
        y = x - y

    return x


main()

