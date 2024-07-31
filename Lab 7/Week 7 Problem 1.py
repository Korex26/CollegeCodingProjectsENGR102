# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#

a = str(input("Would you like to create a list (yes or no):"))
while a == "yes":
    b = int(input("Please enter the maximum value of your list:"))
    c = int(input("Please enter the minimum value of your list:"))
    d = int(input("Please enter the step value of your list:"))
    print("Here is your list with maximum", b, end=",")
    print(" minimum", c, end=",")
    print(" and step", d, end=":")
    for i in range(b-c):
        print("(", end="")
        while c<b:
            print(c, end=", ")
            c+=d    
        else:
            break 
    print(b, end="")
    print(")")
    a = str(input("Would you like to create a list (yes or no):"))
else:
    print()