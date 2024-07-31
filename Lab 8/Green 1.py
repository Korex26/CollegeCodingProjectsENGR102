# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 1
# Date:         10/30/2022
#
String = str(input("Please type a word:"))
#input Animal
String = String.split()
Dictionary = {"a":"$", "A":"$"}
for i in String:
    for x in i:
        if x not in Dictionary:
            print(x,end="")
        if x in Dictionary:
            x= Dictionary[x]
            print(x,end="")
    print(" ", end="")
    
#Python Program to Replace all Occurrences of ‘a’ with $ in a String
