# U06_Ex01_Mcdonald's_Farm.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 16 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
# This program will print Old Mcdonalds Farm using functions. It will print different animals and different sounds
#
#
#
# Algorithm (pseudocode)
# def main():
# have mcdonald(animal, sound) for the function, type this 5 times
# put a different animal and different sound for each mcdonald()
#
# def mcdonald(animal, sound):
# print the full version of Old Mcdonalds Farm, and every time there is a part with an animal, put animal for animal
#   and sound for animal sound
# print a line after the last line to make it easier to read for the user



def main():

    mcdonald("pig", "oink")

    mcdonald("cow", "moo")

    mcdonald("Llama", "Yeet")

    mcdonald("Lion", "Roar")

    mcdonald("Dog", "Bark")


def mcdonald(animal, sound):

    print()
    print()
    print()
    print("Old mcdonald had a farm Ee-igh, Ee-igh, Oh!")
    print()
    print("And on that farm he had a", animal + ".")
    print()
    print("With a", sound, sound, "here and a", sound, sound, "there")
    print()
    print("Here a", sound, "there a", sound, "everywhere a", sound, sound + ".")
    print()
    print("Old mcdonald had a farm Ee-igh, Ee-igh, Oh!")
    print()
    print()
    print()


main()
