# U03_Ex01_Calculate_Surface_Area.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 25 Sep 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
# This program will write a program that will calculate the volume and surface area of a sphere
#
# Algorithm (pseudocode)
# Print what the program is about
# Input V
# Input r
# Input A
# Calculate

def main():
    print("This program will calculate the volume and surface are of a sphere using pi")
    R = eval(input("What is your radius value?"))
    V = 4 / 3 * 3.1415 * R ** 3
    A = 4 * 3.1415 * R**2
    print(R, "The volume is",V)
    print(R, "Surface area is",A)


main()
