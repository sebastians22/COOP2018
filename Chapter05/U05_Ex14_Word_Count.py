# U05_Ex14_Word_Count.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 24 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#
# This program tells you the amount of words you input from a file
#
#
# Algorithm (pseudocode)
# Print the intro to the program
# Get the file name
# Open the file so the computer can read it
# Read file
# Close the file
# Make words and chars = 0
# Make a for loop lines for lines
# split the lines
# len the words
# make another for loop for words in words
# make char += len(words)
# Print the answer


def main():

    print("This program tells you the amount of words you input from a file")

    file = input("Please input the file name to the program")
    words = open(file)
    lines = words.readlines()
    words.close()

    word = 0
    char = 0

    for lines in lines:
        lines_split = lines.split
        lines_split += len(words)

    for words in words:
        char += len(words)

    print("There are", word, "words and", char, "characters in your file")


main()
