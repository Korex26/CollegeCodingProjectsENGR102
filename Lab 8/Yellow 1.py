# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 15
# Date:         10/30/2022
#
List_num = input("Please enter a list of numbers with spaces in between:")
#input 1 8 4 9 3 6
List_num = List_num.split()
List_num = [int(i) for i in List_num]
List_num.sort()
print(List_num[len(List_num)-1])

#Python Program to Find the Largest Number in a List