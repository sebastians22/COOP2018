# U05_Ex04_Acronym.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 28 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
# This program will take the first letter of every word and make an acronym
#
#
# Algorithm (pseudocode)
# Print what the program does
# Have the user enter in words using input, use words as the variable
#
#
#


def main():

    words = input("What words would you like to acronym? ")
    words_upper = words.upper()
    chunk = words_upper.split()

    space = words.find("")

    for chunk in words_upper:
        char = (chunk[0])
        char_str = str(char)
        acronym = char_str
        final = acronym

    print("The acronym of", words, "is", final)







    # program is just printing what is inputed. I have to just take the first letter.
main()