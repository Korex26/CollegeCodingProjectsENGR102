# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 3b
# Date:         10/3/2022
#
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))
for x in range (1,101): # creates a list from 1 to 100
    if(x%a == 0 and x%b != 0): #evenly divisible by a but not b
        print("Howdy")
    if(x%b == 0 and x%a != 0):#evenly divisible by b but not a
        print("Whoop")
    if(x%a == 0 and x%b == 0):#evenly divisible by a and b
        print("Howdy Whoop")
    if(x%a != 0 and x%b != 0):#not evenly divisible by a or b
        print(x)

