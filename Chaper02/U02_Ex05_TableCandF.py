# U02_Ex05_TableCandF.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 31 Aug 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 05
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
# This program will display a table of celsius to fahrenheit
#
#
#
# Algorithm (pseudocode)
#   Function name
#   Description of the function
#   List every celsius with its fahrenheit until 100 using a for loop
#   Use the formula (9/5) * celsius + 32
#   Make the answer be in a full sentence

def main():
    print("This program lists every multiple of 10 from celsius to fahrenheit until 100")
    fahrenheit = (9 / 5)
    celsius = (+32)
    n = 0


    for i in range(10):
        n = n + 10
        print("The amount", n, "° celsius is equivalent to", (9 / 5) * n + 32, "degrees")


main()
