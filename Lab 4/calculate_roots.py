# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 4a - individual
# Date:         09/22/2022
#
from math import *

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

if (a != 0 and (4*a*c) <= (b**2)):
    y = ((-b -(sqrt((b**2 - 4*a*c))))// 2*a)
    x = ((-b +(sqrt((b**2 - 4*a*c))))// 2*a) #quadratic formula (had to separate it because +- isnt in python)
    if (x> y):
        print(f"The roots are x = {x:.1f} and x = {y:.1f}") # used these type of variable statements to round it to the first decimal place
    if (y> x):
        print(f"The roots are x = {y:.1f} and x = {x:.1f}")
    if (y == x):
        print(f"The root is x = {y:.1f}")
if (a != 0 and (4*a*c) > (b**2)): #this is for the complex solution
    c = (b**2)-(4*a*c)  
    d = sqrt(-c)/(2* a)
    e = -b/(2*a)
    print(f"The roots are x = {e:.1f} + {d:.1f}i and x = {e:.1f} - {d:.1f}i") 

if (a == 0) and (b != 0) and (c != 0): 
    t= -c/b # given the equation I just switched the values to make it equal to x
    print(f"The root is x = {t:.1f}")
if (a == b == 0 and c != 0):
    print("You entered an invalid combination of coefficients!")

