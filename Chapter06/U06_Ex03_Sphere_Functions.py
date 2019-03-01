# U06_Ex03_Sphere_Functions.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 17 Jan 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
# This program will write a program that will calculate the volume and surface area of a sphere
#
# Algorithm (pseudocode)
# Print what the program is about
# Input radius
# Calculate using 4 * c.1415 * R**2 and 4/3 * 3.1415 * R ** 3
# Print the answer
#
# shpereArea(radius)
# have area = to 4 * math.pi * radius**2
# return volume
#
# sphereVolume(radius)
# have volume = 4/3 * math.pi*radius**3
# return volume

import math

def main():

    print("This program will calculate the volume and surface are of a sphere using pi")
    radius = eval(input("What is your radius value?"))
    print(radius, "The volume of the sphere is", sphereVolume(radius))
    print(radius, "Surface area of the sphere is", sphereArea(radius))


def sphereArea(radius):

    area = 4 * math.pi * radius**2
    return area


def sphereVolume(radius):

    volume = 4 / 3 * math.pi * radius ** 3

    return volume


main()
