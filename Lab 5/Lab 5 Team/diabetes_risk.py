# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lilly Woodward
#               Kyle Rex
#               Jesse Garcia
#               Ethan Nugyen
# Section:      516
# Assignment:   Lab 5
# Date:         9 28 2022
from math import*


sex = input('Enter your sex (M/F):')
if sex == ('M') or sex == ('m'): #male
    sex = float(0)
elif sex == ('F') or sex == ('f'): #female
    sex = float(0.879)
else: #Edge case moment
    sex = float(0)

age = float(input('Enter your age (years):'))

BMI = float(input('Enter your BMI:'))
if BMI < 25:
    BMI = 0
elif BMI < 27.49:
    BMI = 0.699
elif BMI <= 29.99:
    BMI = 1.97
elif BMI >= 30:
    BMI = 2.518 #edge case!!

hypertension = input('Are you on medication for hypertension (Y/N)?')
if hypertension == ('Y') or hypertension == ('y'): #yes i am
    hypertension = float(1.222)
elif hypertension == ('N') or hypertension == ('n'): #no i am not
    hypertension = float(0)
else: #Edge case again
    hypertension = 0.0

steroids = input('Are you on steroids (Y/N)?')
if steroids == ('Y') or steroids == ('y'): #yes i do
    steroids = float(2.191)
elif steroids == ('N') or steroids == ('n'): #no i don't
    steroids = float(0)
else:
    hypertension = 0.0 #edge case moment

smoker = input('Do you smoke cigarettes (Y/N)?')
if smoker == ('Y') or smoker == ('y'): #yes i do
    smoker = float(0.855)
elif smoker == ('N') or smoker == ('n'): #no i don't
    smoker = input('Did you used to smoke (Y/N)?')
    if smoker == ('Y') or smoker == ('y'): #yes i used too
        smoker = float(-0.218)
    elif smoker == ('N') or smoker == ('n'): #no i didn't
        smoker = float(0)
    else:
        smoker = float(0) #edge case moment
else:
    smoker = float(0.855) #edge case moment

history = input('Do you have a family history of diabetes (Y/N)?')
if history == ('N') or history == ('n'): #no family history
    history = float(0)
elif history == ('Y') or history == ('y'): #yes family history
    history = input('Both parent and sibling (Y/N)?')
    if history == ('N') or history == ('n'): #no not both but one of them
        history = float(0.728)
    elif history == ('Y') or history == ('y'): #yes both
        history = float(0.753)
    else: #edge case moment
      history = float(0.728)
else: #edge case moment
  history = 0.0
n = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history

risk = 100 / (1 + e**n)

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')