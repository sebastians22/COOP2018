# practice02.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 01 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
#   This program is an interactive calculator that accepts mathematical expressions.
#
# Algorithm (pseudocode)
#  Print intro
#  Make while loop
#   Get input (mathematical expression; 0 to quit)
#   Test for exit
#   Evaluate mathematical expression
#   Print Result
#

def main():

    # Print intro
    print("\nThis program is an interactive calculator that accepts mathematical expressions.")
    #  Make while loop

    while True:
        #   Get input (mathematical expression; 0 to quit)
        expr = eval(input("\nPlease enter a mathematical expression to evaluate(0 to quit):  "))

        #   Test for exit
        if expr == 0:
            break

        #   Evaluate mathematical expression

        #   Print Result
        print("\n Your answer is", expr)

main()
