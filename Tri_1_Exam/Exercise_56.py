# Exercise_56.py.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 14 Nov 2018
#   IDE: PyCharm
#
# Assignment Info
#
#   Trimester 1 exam
#
# Program Description
#
# This program will check the lengths of the sides of triangles and see if they can form a triangle or not
#
#
# Algorithm (pseudocode)
# Write the def main()
# Print what the program is about (use program description)
# Ask the user for sides a, b and, c of the triangle using eval(input(prompt  )
# Use the is_triangle function and have it use a, b, and c variables
# (go to is_triangle)
# it = is_triangle(a, b, c)
# print that true means that the length of that line is good, and false means that the line needs to be shorter
# print the three sides of the triangle (s1, s2 ,s3) with a message "Side (one/two/three)"
# print "This triangle is", it"
# main()

# is_triangle function:
# use the name is_triangle(a, b, c)
# If b + c >= a return True  After this line have a return false
# If c + a >= b return True  After this line have a return false
# If a + b >= c return True  After this line have a return false
# return the information to the main()
#


def main():
    print("This program you will input 3 values to form a triangle.")
    print("It will check the lengths of the sides of the triangle and see if they can form a triangle or not")
    a = eval(input("Enter the first sides length  "))
    b = eval(input("Enter the seconds sides length  "))
    c = eval(input("Enter the thirds sides length  "))
    print("True means that the sides are good, false means that you need to make that side smaller")
    it = is_triangle(a, b, c)
    print("Side one is", a)
    print("Side two is", b)
    print("Side three is", c)
    print("This triangle is", it)


def is_triangle(a, b, c):
    if b + c >= a:
        return True

    return False

    if c + a >= b:
        return True

    return False

    if a + b >= c:
        return True

    return False

    # s1 = b + c >= a
    # s2 = c + a >= b
    # s3 = a + b >= c
    # return True
    # return False


if __name__ == '__main__':
    main()
