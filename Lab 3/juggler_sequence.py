# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 3b
# Date:         10/3/2022
#

import math
from math import *
n = int(input("Enter a positive integer: "))
print("The Juggler sequence starting at ", n, " is: ")
c = 0
while (n>1):
    if n % 2 == 0 and n != 1: #if n is an even number and not equal to 1
        print(n, end=", ") #makes the output go into a sequence instead of its own line
        n = int(math.floor(n**(1/2))) 
        c+= 1 # adds to the amount of iterations
    if n % 2 != 0 and n != 1: #if n is an odd number and not equal to 1
        print(n, end=", ") #makes the output go into a sequence instead of its own line
        n = int(math.floor(n**(3/2)))
        c+= 1 # adds to the amount of iterations
print(1)
print("It took", (c), "iterations to reach 1")