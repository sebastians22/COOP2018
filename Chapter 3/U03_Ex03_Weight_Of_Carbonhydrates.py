# U03_Ex03_Weight_Of_Carbonhydrates.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program will compute the molecular weight of a carbohydrate
# in grams per mole based on the number of hydrogen, carbon, and oxygen atoms in the molecule
#
#
# Algorithm (pseudocode)
# print what program is about
# get the number of hydrogen with eval(input) use H
# get the number of carbon with eval(input) use C
# get the number of oxygen with eval(input) use O
# print answer with H C O

def main():
    print("This program will compute the molecular weight of carbohydrates in grams")
    H = eval(input("What is your Hydrogen value?"))
    C = eval(input("What is your Carbohydrates value?"))
    O = eval(input("What is your oxygen value?"))
    print("Your hydrogen is  ", H, "Your carbon is  ", C, "Your oxygen is  ", O)

main()
