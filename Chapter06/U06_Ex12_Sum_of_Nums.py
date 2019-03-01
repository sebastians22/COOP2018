# U06_Ex12_Sum_of_Nums.py
#
#  Author: Sebastian Schaefer
#  Course: Coding for OOP
# Section: A2
#   Date: 19 Feb 2019
#   IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
# This program will take a list of numbers and print the sum of the lis
#
# Algorithm (pseudocode)
# main()
# make a list called numbers
# call cal and get list
# print the answer (list)
#
# cal(nums)
# make list = 0
# make a for loop num in nums
# have list += num
# return list


def main():

    numbers = [1, 2, 3, 4]
    list = cal(numbers)
    print("the added up numbers in your list is", list)


def cal(nums):

    list = 0

    for num in nums:
            list += num

    return list

if __name__ == '__main__':

    main()
