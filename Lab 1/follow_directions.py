# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kyle Rex
# Section:      516
# Assignment:   Lab 1b
# Date:         08/31/2022
#
print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")
print("My guess is 3")
x = 1.1
f = (x**2 - 1)/(x - 1)# I repeat this 8 time but add one more zero
print(f)
x = 1.01
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.001
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.0001
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.00001
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.000001
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.0000001
f = (x**2 - 1)/(x - 1)
print(f)
x = 1.00000001
f = (x**2 - 1)/(x - 1)
print(f)
print()
print("My guess was a little off")