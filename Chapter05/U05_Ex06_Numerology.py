# U05_Ex06_Numerology.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 06 Dec 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
# This program will assign numbers to every letter, and the user will enter a word and it will output
# # how much the word is worth. Make spaces worth 0
#
#
#
# Algorithm (pseudocode)
# Print the intro to the program
# Make a list with every letter of the alphabet = to a number. a = 1, b = 2, c = 3...
# Make spaces worth 0
# have the user input their name, tell them it can take their full name
# create an algorithm to make each letter go with a name, then add all the letters up
# Print the numeric value of the name

def main():
    name = input("Please enter a name ")
    lower_name = name.lower()
    new_name = lower_name.split()
    letters = "Xabcdefghijklmnopqrstuvwxyz"
    word_value = 0
    char = 0
    # int_name = new_name.int
    """new_name has to be a string, not a list, only thing that's wrong"""

    new_new_name = (''.join(new_name))

    for char in new_name:
        letter_value = 0
        name.find(new_new_name)
        #letter_values = letters.index(char)
        word_value = word_value + letter_value
        #str_value = word_value.join()

    print("The value of your name is", new_new_name)


main()
