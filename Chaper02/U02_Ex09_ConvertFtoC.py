# U02_Ex09_ConvertFtoC.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 04 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 08
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#
#   This program converts F to C
#
#
#
# Algorithm (pseudocode)
#   Print program introduction
#   Get C from user and assign to fahrenheitption
#   Calculate formula
#   Print F
#

def main():
    print("Click on the bottom box, and input a fahrenheit degrees. After you input a number press enter, and the celsius degress will appear")

    #   Print program introduction
    print("This program converts temperature from fahrenheit to celsius")

    #   Get °C from user and assign to fahrenheit
    fahrenheit = eval(input("Enter °F to convert: "))
    celsius = (fahrenheit - 32) * 5/9

    #   Calculate °F using 9/5 * °C + 32 and assign to fahrenheit  main()

    #   Print °F
    print(fahrenheit, "°F is equivalent to ", celsius, "°C")

    print("re run the program do use it again")


main()
