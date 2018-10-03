# practice01.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 01 Oct 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: Practice 01
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#  This program will calculate the amount of Joules to Calories
#
# Algorithm (pseudocode)
# Print what program is about
# Joules = 0
#   while True statement
#   Text for exit condition (break if True)
#   Get input: Joules
#   Calculate using (1 J = .239 Calories)
#   calories = J * .239
#   Print the amount of calories
#

def main():

    # Print what program is about\
    print("\nThis program will calculate the amount of Joules to Calories")

    J = 0

    # Loop until exit requested
    while True:
        # Get input: Joules
        J = float(input("\nHow many Joules are there?(0 to quit)  "))

        if J == 0:
            break

        # Calculate using (1 J = .239 Calories)
        #   calories = J * .239
        calories = J* .239

        # Print the amount of calories
        print(J, "\n" "Joules is equivalent to", calories, "Calories.")


main()
