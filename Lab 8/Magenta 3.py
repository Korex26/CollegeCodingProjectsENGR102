# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 27
# Date:         10/30/2022
#
List = [-6,3,4,-5,8,7,9,-3,6] # example list, can be any length or values
Sum_neg = 0
Sum_pos_even = 0
Sum_pos_odd = 0
for i in range(len(List)):
    if (List[i] < 0):
        Sum_neg += List[i]
    if (List[i]> 0) and (List[i] % 2 == 0):
        Sum_pos_even += List[i]
    if (List[i]> 0) and (List[i] % 2 != 0):
        Sum_pos_odd += List[i]
print("Sum of Negative numbers:", Sum_neg )
print("Sum of Positive Even numbers:", Sum_pos_even)
print("Sum of Positive Odd numbers:", Sum_pos_odd)

#Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List