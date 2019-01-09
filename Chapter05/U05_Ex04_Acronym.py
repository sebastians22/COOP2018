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
# Make all the words uppercase all of the words
# Make a final variable with quotations
# Make a for loop with for chunks in chunks
# Have first_char = to 0
# first_char_string is = to the first letter of all the words
# Make final += to the first_char_string
# print the original words and the final acronym


def main():


    words = input("Please enter a phrase to become an acronym: ")

    words_upper = words.upper()
    chunk = words_upper.split()

    final = ""
    for chunk in chunk:
        first_char = (chunk[0])
        first_char_str = str(first_char)
        final += first_char_str

    print("The acronym of", words, "is", final)


main()
