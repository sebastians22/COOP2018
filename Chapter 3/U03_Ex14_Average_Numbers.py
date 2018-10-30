# U03_Ex14_Average_Numbers.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 26 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program will average an amount of numbers entered by the user
#
#
#
# Algorithm (pseudocode)
# Print what program is about
# Ask how many numbers there are (use x)
# Set up a loop to ask as many numbers there are with x
# Have user enter each number
# Make average a float
# Use the equation sum = sum + n in the loop
# Print the response, average the score with sum/i

def main():

    print("This program will average out any amount of numbers")
    amount = eval(input("How many number's are you going to average"))
    i = amount
    sum = 0
    for amount in range(i):
        n = eval(input("What is your number?"))
        sum = sum + n

    print("Your averages score is", sum / i)


main()

