# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kyle Rex
#               Ethan Nguyen
#               Jesse Garcia
#               Lilly Woodward
# Section:      516
# Assignment:   Lab 2a - team
# Date:         09/21/2022
#input numbers for  a,b,c
a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))
#find out what a,b,c fit into
equation = ''
if a != 0:
    if a == 1:
        equation += 'x^2'
    elif a == -1:
        equation += '- x^2 '
    else:
        equation += f'{a}x^2 '
if b != 0:
    if b == 1:
        equation += '+ x'
    elif b == -1:
        equation += ' - x'
    elif (b > 0) and (a==0):
        equation += f'{b}x'
    elif b > 0:
        equation += f' + {b}x'
    else:
        equation += f'- {abs(b)}x'
if c != 0:
    if c > 0:
        equation += f' + {c}'
    elif c == 0:
        equation = ''
    else:
        equation += f' - {abs(c)}'

print('The quadratic equation is', equation, "= 0")