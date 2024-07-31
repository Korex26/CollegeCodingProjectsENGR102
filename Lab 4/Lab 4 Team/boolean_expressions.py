# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kyle Rex
#               Ethan Nguyen
#               Jesse Garcia
#               Lilly Woodward
# Section:      516
# Assignment:   Lab 4a - team
# Date:         09/21/2022
from math import*
############ Part A ############
a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')
if (a =='t') or (a =='T') or (a =='True'):
    a = True
else:
    a = False
if (b =='t') or (b =='T') or (b =='True'):
    b = True
else:
    b = False
if (c =='t') or (c =='T') or (c =='True'):
    c = True
else:
    c = False
############ Part B ############
exp1 = a and b and c
exp2 = a or b or c
############ Part C ############
XOR = (a and not b) or (b and not c) or (not a and b)
odd_num = a and not (b or c) or b and not (a or c) or c and not (a or b) or (a and b and c)

print('a and b and c:',exp1)
print('a or b or c: ', exp2)
print('XOR:', XOR)
print('Odd number:', odd_num)

############ Part D ############
complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b))))

print(complex1)
print(complex2)