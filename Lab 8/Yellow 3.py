# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 18
# Date:         10/30/2022
#
List1 = [1,10,5,7,4]
List2 = [2,9,6,8,3]
List1 = [int(i) for i in List1]
List2 = [int(i) for i in List2]
for i in range(len(List2)):
    List1.append(List2[i])
List1.sort()
print(List1)

#Python Program to Merge Two Lists and Sort it