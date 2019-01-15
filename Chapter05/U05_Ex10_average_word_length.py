# U05_Ex10_average_word_length.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 15 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
# This program will accept any kind of word, sentence, or paragraph and it will determine the average word length
#
#
#
# Algorithm (pseudocode)
# Print the program introduction
# Have the user input words to average, use words for a variable
# assign each letter to a number, use zzzz for 0, use letters for a variable
# split words to find out how many words their are
# average out the letters to words

def main():

    print("This program will determine the average word length of a sentence, paragraph, or paper")
    words = input("Please enter words to be averaged ")
    letters = {'zzzz': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
               'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18',
               's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    new_words = words.split()
    final = words/letters
    print("The average word length of each word is", final, ".")


main()
