# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 39
# Date:         10/30/2022
#
a = int(input("Please enter side length 1:"))
#input 5
b = int(input("Please enter side length 2:"))
#input 4
c = int(input("Please enter side length 3:"))
#input 3
p = (a+b+c)//2
Area = (p*(p-a)*(p-b)*(p-c))**(1/2)
print(Area)

#Python Program to Find the Area of a Triangle Given All Three Sides