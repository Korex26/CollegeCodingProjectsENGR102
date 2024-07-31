# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 40
# Date:         10/30/2022
#
x = int(input("Please enter an integer:"))
#input 42
list = []
for i in range (x):
    if (x % (i+1) == 0):
        list.append(i+1)
print(list[0])

#Python Program to Find the Smallest Divisor of an Integer

#Every integers smallest divisor will always be 1 so this doesnt really make much sense