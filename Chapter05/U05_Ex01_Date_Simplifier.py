# U05_Ex01_Date_Simplifier.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 27 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
# This program will take the day, month, and year and put it into a simplifier and simplify it to month/day/year,
# then it will give you the actual month, day, and year
#
# Algorithm (pseudocode)
# Print what the program is about, use a shorter version of the program description
# Use a string to get monthStr, dayStr, and year Str = dateStr
# print a blank line to make the code easier to read
# print month/day/year
# print a blank line to make the code easier to read
# Make a list with every month in order
# Subtract the value by 1 to make the months and what the user input to line up
# Print the date using a string

def main():
    print("This program will take your birthday and put it into simpler terms, then it will convert it into a nice form")

    dateStr = input("Enter a date mm/dd/yyyy ")

    monthStr, dayStr, yearStr = dateStr.split("/")

    print("")

    print("You where born on", monthStr, "/", dayStr, "/", yearStr)

    print("")

    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")

    monthStr = months[int(monthStr)-1]

    print("The converted date is", monthStr, dayStr, yearStr)


main()
