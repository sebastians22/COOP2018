# U05_Ex08_Ceaser_Cipher.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 14 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
# This program will encode a message entered by the user by shifting the letters
# also entered by the user
#
#
# Algorithm (pseudocode)
# Print the program description
# have the user input their message, have it = message
# have the user input how much they would like to code it, have it = code
# make a variable named letters and have "Xabcdefghijklmnopqrstuvwxyz"
# lowercase the message, have it = message_lower
# split message_lower, have it = message_split

def main():

    print("This program you will input a message and it will shift the letters by how many you input.")
    message = input("Please enter a message. ")
    code = input("How many letters would you like to shift it by? ")
    letters = {'zzzz': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
               'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18',
               's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    message_lower = message.lower()
    message_split = message_lower.split()
    cipher = code + message_split
    final = message_split + code
    print("Your original message is", message, "and the coded message by", code, "would be", final, ".")


main()
