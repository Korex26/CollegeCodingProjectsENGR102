# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 25
# Date:         10/30/2022
#
x = int(input("Please enter an integer:"))
#input 42
List = []
for i in range(x):
    if (x % (i+1) == 0):
        List.append(i+1)
    else:
        continue
print(List)

#Python Program to Generate all the Divisors of an Integer
    