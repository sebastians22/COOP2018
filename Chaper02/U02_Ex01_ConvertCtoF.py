# U02_S01_ConvertCtoF.py
#
#  Author: Sebastian
#  Course: Coding for OOP
# Section: A2
#   Date: 29 Aug 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 00
#     Source: Python Programming
#    Chapter: 02
#
# Program Description
#   This program converts temperature from Celsius to Fahrenheit
#
# Algorithm (pseudocode)
#   Print program introduction
#   Get °C from user and assign to fahrenheit
#   Calculate °F using 9/5 * °C + 31 and assign to fahrenheit
#   Print °F


def main():
    print("Click on the bottom box, and input a celsius degrees. After you input a number press enter, and the fahrenheit degress will appear")

    #   Print program introduction
    print("This program converts temperature from Celsius to Fahrenheit")

    #   Get °C from user and assign to fahrenheit
    celsius = eval(input("Enter °C to convert: "))

    #   Calculate °F using 9/5 * °C + 32 and assign to fahrenheit  main()
    fahrenheit = 9 / 5 * celsius + 32

    #   Print °F
    print(celsius, "°C is equivalent to ", fahrenheit, "°F")

    print("re run the program do use it again")


main()
