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
# This program will show the numeric value of your full name, numerologists claim that they
# can determine a persons character traits based on the numeric value of a persons name
#
#
#
# Algorithm (pseudocode)
# Have the user enter a name, use name as a variable
# Make all the letters of what the user entered to lowercase, use lower_name as a variable
# get rid of the spaces
# split the lower_name, use new_name as a variable
# write out the alphabet and make a capital X before the start to account for -1, name that letters (Xabcd....)
# Make word_value worth 0
# Make char worth 0
# Join the new_name, have it named new_new_name
# Make a loop for char in new_name
# Make a letter_value worth 0
# Find the new_new_name
# Make word_value = to word_value + letter_value
# Print the value of your name is (new_new_name)

def main():
    name = input("Please enter a name ")
    lower_name = name.lower().replace(" ", "")
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