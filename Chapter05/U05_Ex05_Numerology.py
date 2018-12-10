# U05_Ex05_Numerology.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 04 Dec 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
# This program will assign numbers to every letter, and the user will enter a word and it will output
# how much the word is worth
#
#
# Algorithm (pseudocode)
# Print in intro to the program
# Make a list with every letter of the alphabet = to a number. a = 1, b = 2, c = 3...
# have the user input their name, tell them to only enter in one name
# create an algorithm to make each letter go with a name, then add all the letters up
# Print the numeric value of the name


def main():
    name = input("Please enter a name ")
    lower_name = name.lower()
    letters = "Xabcdefghijklmnopqrstuvwxyz"
    letter_value = 0
    word_value = 0
    char = 0
    for char in lower_name:
        name.find(lower_name)
        letter_value = letters.index(char)
        word_value = word_value + letter_value

    print("The value of your name is", word_value)


main()
