# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 28
# Date:         10/30/2022
#
List = [-6,3,4,-5,8,7,9,-3,6] # example list, can be any length or values
List_odd = []
List_even = []
for i in range(len(List)):
    if (List[i] % 2 == 0):
        List_even.append(List[i])
    if (List[i] % 2 != 0):
        List_odd.append(List[i])
List_odd.sort()
List_even.sort()
print("The largest even value is:", List_even[len(List_even)-1])
print("The largest odd value is:", List_odd[len(List_odd)-1])

#Python Program to Print Largest Even and Largest Odd Number in a List
