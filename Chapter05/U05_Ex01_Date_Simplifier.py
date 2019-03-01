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
# ask the user to input a date in mm/dd/yyyy format
# split it with ("/")
# make a string with all the months
# makes monthStr = moths[int(monthStr)-1]
# print a blank like so it's easier to read
# print the outro

def main():
    print("This program will take your birthday and put it into simpler terms, then it will convert it into a nice form")

    dateStr = input("Enter a date mm/dd/yyyy ")

    monthStr, dayStr, yearStr = dateStr.split("/")

    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")

    monthStr = months[int(monthStr)-1]
    print("")
    print("The date you entered was", dateStr, "The converted date is", monthStr, dayStr, yearStr)

main()
