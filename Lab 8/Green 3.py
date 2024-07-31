# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 6
# Date:         10/30/2022
#
String = str(input("Please type a word:"))
#input Animal Animal
String = list(String)
for i in range(len(String)-1):
    if (String[i] == " "):
        String[i] = "-"
    else:
        continue
String = "".join(String)
print(String)

#Python Program to Take in a String and Replace Every Blank Space with Hyphen