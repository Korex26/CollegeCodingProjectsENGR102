# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 4a - individual
# Date:         09/22/2022
#
a = int(input("Please enter a positive value for day: "))

if (0 < a < 11):
    print("The total number of gadgets produced on day ", a, " is ", a * 5) # each day it goes up 5

elif (10 < a < 61):
    print("The total number of gadgets produced on day ", a, " is ", 50 + (a-10) * 50) # each day past 10 pays it goes up 50
    
elif (60 < a < 100):
    print("The total number of gadgets produced on day ", a, " is ", 2550 + (((50) + (50-(a-59)))//2)* (a-60)) 

elif (a < 0):
    print("You entered an invalid number!") # days cant be negative in this situation

elif (a > 100):
    print("The total number of gadgets produced on day ", a, " is ", 3730) # after day 100 producting stops and at day 100 production = 3730
