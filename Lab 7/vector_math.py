# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 7b
# Date:         10/14/2022
#
from math import *
import math

#gets inputs and translates inputs into lists
Vec_a_input = input("Enter the elements for vector A:")
Vec_b_input = input("Enter the elements for vector B:")
Vec_a_list = Vec_a_input.split()
Vec_b_list = Vec_b_input.split()

#makes elements in the list all floats
Vec_a_list = [float(element) for element in Vec_a_list]
Vec_b_list = [float(element) for element in Vec_b_list]

#finds magnitude of a and b
mag_a = 0
mag_b = 0
for element in Vec_a_list:
    mag_a += (element)**2
    mag_a1 = sqrt(mag_a)
for element in Vec_b_list:
    mag_b += (element)**2
    mag_b1 = sqrt(mag_b)

#finds the addition and subtraction models     
addition = []
subtraction = []
x = 0
for element in Vec_a_list:
    addition.append(float(Vec_a_list[x] + Vec_b_list[x]))
    x += 1
x = 0
for element in Vec_a_list:
    subtraction.append(float(Vec_a_list[x] - Vec_b_list[x]))
    x += 1

#finds the dot product
dotprod_str = []
x = 0
for element in Vec_a_list:
    dotprod_str.append(float(Vec_a_list[x] * Vec_b_list[x]))
    x += 1
x = 0
dotprod = 0
for element in dotprod_str:
    dotprod += dotprod_str[x]
    x+=1

# prints out the values with the correct formating
print(f'The magnitude of vector A is {mag_a1:.5f}')
print(f'The magnitude of vector B is {mag_b1:.5f}')
print(f"A + B is {addition}")
print(f"A - B is {subtraction}")
print(f'The dot product is {dotprod:.2f}')













