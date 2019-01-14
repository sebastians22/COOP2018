# U05_Ex09_Word_Counter.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 14 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
# This program will count the number of words in a sentence entered by the user.
#
#
# Algorithm (pseudocode)
# Print the program description
# Have the user input words using variable words
# use len(variable.split()) and have it = to final
# print final
#

def main():

    print("This program will count the number of words that you input")
    words = input("Please input words. ")
    final = len(words.split())
    print("You entered", final, "words.")


main()
