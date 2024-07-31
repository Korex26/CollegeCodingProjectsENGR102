# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Ethan Nguyen
#               Jesse Garcia
# Section:      516
# UIN:          932007222
# Assignment:   Lab 8
# Date:         10 23 2022
from math import*

### Creating ASCII Clock
## get user input 
var = input("Enter the time: ")

## define the function 
def asciiClock(var):
# create variables for each row
    a1 = ""
    a2 = ""
    a3 = ""
    a4 = ""
    a5 = ""
    for i in var:
# make the output the correct format for each number
        if i == ":":
            a1 += " "
            a2 += ":"
            a3 += " "
            a4 += ":"
            a5 += " "
        if i == "0":
            a1 += "000"
            a2 += "0 0"
            a3 += "0 0"
            a4 += "0 0"
            a5 += "000"
        if i == "1":
            a1 += " 1 "
            a2 += "11 "
            a3 += " 1 "
            a4 += " 1 "
            a5 += "111"
        if i == "2":
            a1 += "222"
            a2 += "  2"
            a3 += "222"
            a4 += "2  "
            a5 += "222"
        if i == "3":
            a1 += "333"
            a2 += "  3"
            a3 += "333"
            a4 += "  3"
            a5 += "333"
        if i == "4":
            a1 += "4 4"
            a2 += "4 4"
            a3 += "444"
            a4 += "  4"
            a5 += "  4"
        if i == "5":
            a1 += "555"
            a2 += "5  "
            a3 += "555"
            a4 += "  5"
            a5 += "555"        
        if i == "6":
            a1 += "666"
            a2 += "6  "
            a3 += "666"
            a4 += "6 6"
            a5 += "666"
        if i == "7":
            a1 += "777"
            a2 += "  7"
            a3 += "  7"
            a4 += "  7"
            a5 += "  7"
        if i == "8":
            a1 += "888"
            a2 += "8 8"
            a3 += "888"
            a4 += "8 8"
            a5 += "888"
        if i == "9":
            a1 += "999"
            a2 += "9 9"
            a3 += "999"
            a4 += "  9"
            a5 += "999"
        a1 += " "
        a2 += " "
        a3 += " "
        a4 += " "
        a5 += " "
# make sure there is no bugs and the code can be followed
# print the ASCII art
    print()
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
asciiClock(var)