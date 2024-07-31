# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 8b Problem 12
# Date:         10/30/2022
#
n = int(input("Please enter the number of Key pairs the dictionary should have:"))
#input 5
my_dict1 = {}
for i in range(n):
    i+=1
    my_dict2 = {i:i*i}
    my_dict1.update(my_dict2)
print(my_dict1)

#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)