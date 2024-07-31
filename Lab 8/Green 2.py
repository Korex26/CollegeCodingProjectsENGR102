# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 4
# Date:         10/30/2022
#
String = str(input("Please type a word:"))
#input Animal
String = list(String)
a = String[0]
String[0] = String[len(String)-1]
String[len(String)-1] = a
String = "".join(String)
print(String)

#Python Program to Form a New String where the First Character and the Last Character have been Exchanged