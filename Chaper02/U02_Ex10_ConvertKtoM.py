# U02_Ex10_ConvertKtoM.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 04 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise:
#     Source: Python Programming
#    Chapter:
#
# Program Description
# This will convert kilos into miles
#
# Algorithm (pseudocode)
#   Print hello
#   Formula (.6 k = 1 mile)
#   Print the answer

def main():
    print("Press the box bellow. Enter in a kilometer number and it will turn it into miles.")
    mile = eval(input("Enter Miles to convert: "))
    kilo = (mile - .4)
    print(mile, "is equivalent to ", kilo, "kilos")


main()
