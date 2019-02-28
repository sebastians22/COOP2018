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
# print the intro to the program
# have the user enter a sentence that will be averages
# split the sentence and have it into words
# make average = adding all of the words by letters and divide it by how many words there are
# print the answer

def main():

    print("This program will determine the average word length of a sentence, paragraph, or paper")
    sentence = input("Please enter words to be averaged ")

    words = sentence.split()

    average = sum(len(word) for word in words) / len(words)

    print("In the sentence", sentence, "there are", average, "letters per word.")




main()
