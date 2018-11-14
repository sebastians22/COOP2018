# Exercise_56.py.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 14 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 56
#     Source: Python Programming
#    Chapter: Tri 1 exam
#
# Program Description
#
# This program will check the lengths of the sides of triangles and see if they can form a triangle or not
#
#
# Algorithm (pseudocode)
# Write the def main()
# Print what the program is about
# Ask the user for sides a, b and, c of the triangle
# Use the is_triangle function
# Return the function
# is_triangle function:
# use the name is_triange(a, b, c)
# (add a + b < c
# add b + c < a
# add a + c < b)
# This is the equation to use to see if the triangle will work
# Return

def main():
    print("This program you will input 3 values to form a triangle.")
    print("It will check the lengths of the sides of the triangle and see if they can form a triangle or not")
    a = eval(input("Enter the first sides length  "))
    b = eval(input("Enter the seconds sides length  "))
    c = eval(input("Enter the thirds sides length  "))
    print("True means that the sides are good, false means that you need to make that side smaller")
    triangle(a, b, c)


def triangle(a, b, c):
    s1 = b + c >= a
    s2 = c + a >= b
    s3 = a + b >= c
    print("Side one is", s1)
    print("Side two is", s2)
    print("Side three is", s3)


main()
