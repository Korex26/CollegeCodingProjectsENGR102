# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 4a - individual
# Date:         09/22/2022
#
a = float(input("Enter number 1: "))# Recieves number from input, initializes it, and converts it to a float
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
if (b < a > c): # if a is largest
    print("The largest number is ", float(a) )
elif (c < b > a): # if b is largest
    print("The largest number is ", float(b) )
else: # if c is largest
    print("The largest number is ", float(c) )
            