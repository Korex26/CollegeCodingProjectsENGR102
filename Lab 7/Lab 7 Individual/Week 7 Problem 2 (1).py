# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#
a = str(input("Please enter any word you would like to be added to your list: "))
old_list = [a]
print("Here is your current list:", old_list)
b = int(input("Would you like to repeat the list? (If so enter number of times. If not enter 0):"))
if b>0:
    print(old_list[0]*b)
else:
    print()